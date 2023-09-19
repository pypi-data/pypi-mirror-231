"""REST API for CADA using FastAPI."""
from contextlib import asynccontextmanager
import os
import typing

from dotenv import load_dotenv
from fastapi import FastAPI, Query
from pydantic import BaseModel
from starlette.responses import Response

import cada_prio
from cada_prio import predict

# Load environment
env = os.environ
load_dotenv()

#: Debug mode
DEBUG = env.get("CADA_DEBUG", "false").lower() in ("true", "1")
#: Path to data / model
PATH_DATA = env.get("CADA_PATH_DATA", "/data/cada")
#: Optional path to legacy model from CADA
PATH_LEGACY = env.get("CADA_PATH_LEGACY", None)

#: The CADA models, to be loaded on startup.
GLOBAL_STATIC = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the models
    all_to_hgnc, hgnc_info_by_id = predict.load_hgnc_info(
        os.path.join(PATH_DATA, "hgnc_info.jsonl")
    )
    GLOBAL_STATIC["all_to_hgnc"] = all_to_hgnc
    GLOBAL_STATIC["hgnc_info_by_id"] = hgnc_info_by_id
    graph, model = predict.load_graph_model(PATH_DATA, PATH_LEGACY)
    GLOBAL_STATIC["graph"] = graph
    GLOBAL_STATIC["model"] = model

    yield

    GLOBAL_STATIC.clear()


app = FastAPI(lifespan=lifespan)


# Register endpoint for returning CADA version.
@app.get("/version")
async def version():
    return Response(content=cada_prio.__version__)


class PredictionResult(BaseModel):
    rank: int
    score: float
    gene_symbol: str
    ncbi_gene_id: str
    hgnc_id: str


# Register endpoint for the prediction
@app.get("/predict")
async def handle_predict(
    hpo_terms: typing.Annotated[str, Query()],
    genes: typing.Annotated[typing.Optional[str], Query()] = None,
):
    hpo_terms_list = hpo_terms.split(",")
    genes_list = genes.split(",") if genes else None
    _, sorted_scores = predict.run_prediction(
        hpo_terms_list,
        genes_list,
        GLOBAL_STATIC["all_to_hgnc"],
        GLOBAL_STATIC["graph"],
        GLOBAL_STATIC["model"],
        PATH_LEGACY is not None,
    )
    hgnc_info_by_id = GLOBAL_STATIC["hgnc_info_by_id"]
    return [
        PredictionResult(
            rank=rank,
            score=score,
            gene_symbol=hgnc_info_by_id[hgnc_id].symbol,
            ncbi_gene_id=hgnc_info_by_id[hgnc_id].ncbi_gene_id,
            hgnc_id=hgnc_info_by_id[hgnc_id].hgnc_id,
        )
        for rank, (hgnc_id, score) in enumerate(sorted_scores.items(), start=1)
    ]
