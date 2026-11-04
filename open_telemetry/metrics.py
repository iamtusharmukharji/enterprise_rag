from opentelemetry import metrics
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import (
    ConsoleMetricExporter,
    PeriodicExportingMetricReader,
)

def init_metrics():
    resource = Resource.create({
        "service.name" : "enterprise-rag-app"
    })

    exporter = ConsoleMetricExporter()

    reader = PeriodicExportingMetricReader(
        exporter= exporter,
        export_interval_millis=5000
    )

    provider = MeterProvider(
        resource= resource,
        metric_readers=[reader]
    )
    
    metrics.set_meter_provider(provider)

    
    return provider

def init_instruments():
    meter = metrics.get_meter(__name__)
    
    counter = meter.create_counter(
        name="rag_node_executions_total",
        description="Total node executions",
        unit="1"
    )

    error_counter = meter.create_counter(
            name="rag_node_errors_total",
            description="Total node execution failure",
            unit="1"
        )

    histogram = meter.create_histogram(
        name="rag_node_duration_seconds",
        description="Node execution duration",
        unit="s"
    )

    return counter, error_counter, histogram