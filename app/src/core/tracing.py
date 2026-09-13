import logging
from os import environ
from os import getpid

from fastapi import FastAPI
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.psycopg import PsycopgInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.resources import SERVICE_INSTANCE_ID
from opentelemetry.sdk.resources import SERVICE_NAME
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

from src.core.config import Environment
from src.core.config import settings

logger = logging.getLogger(__name__)

span_exporters = {
    Environment.LOCAL: OTLPSpanExporter,
    Environment.DEVELOPMENT: OTLPSpanExporter,
    Environment.PRODUCTION: OTLPSpanExporter,
}


def setup_tracing(app: FastAPI):
    is_otel_env_vars_defined = any(env_var.startswith("OTEL") for env_var in environ)
    if not is_otel_env_vars_defined:
        logger.warning("No OpenTelemetry configured, no traces will be sent")
        return

    resource = Resource(
        attributes={
            SERVICE_NAME: settings.PROJECT_NAME,
            SERVICE_INSTANCE_ID: f"worker-{getpid()}",
        },
    )

    span_exporter = span_exporters[settings.ENVIRONMENT]
    logger.info(f"Using {span_exporter!r}")
    processor = BatchSpanProcessor(span_exporter())

    trace_provider = TracerProvider(resource=resource)
    trace_provider.add_span_processor(processor)
    trace.set_tracer_provider(trace_provider)

    FastAPIInstrumentor.instrument_app(app)
    PsycopgInstrumentor().instrument()
