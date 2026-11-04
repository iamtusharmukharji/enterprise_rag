from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from contextlib import asynccontextmanager
from fastapi.responses import RedirectResponse, JSONResponse
from app.graph import graph
from app.api.routes import chat
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from open_telemetry import open_t_tracer, metrics
from langfuse.langchain import CallbackHandler
import os

@asynccontextmanager
async def app_lifespan(app: FastAPI):
    try:
        spanner = open_t_tracer.init_tracer(worker= os.getpid())
        # provider = metrics.init_metrics()
        # counter, error_counter, histogram = metrics.init_instruments()
        # node_tracer = open_t_tracer.NodeTracer(counter, error_counter, histogram)

        app.state.graph = graph.build_support_graph()
        app.state.langfuse_trace = CallbackHandler()

        yield
    finally:
        spanner.shutdown()
        # provider.shutdown()


app = FastAPI(
    lifespan=app_lifespan,
    title="Enterprise RAG",
    version="1.0.1"
)

FastAPIInstrumentor.instrument_app(app=app)


@app.get('/', include_in_schema=False)
async def root():
    return RedirectResponse('/docs')

@app.get('/status')
async def server_status():
    return JSONResponse(status_code=200, content={"status":"ok"})


app.include_router(chat.router)