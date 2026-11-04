from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry import trace
import time
from open_telemetry.metrics import init_metrics, init_instruments

tracer = trace.get_tracer(__name__)


def init_tracer(worker : int):
    resource = Resource.create(attributes={
        "service.name": "enterprise-rag-app",
        "process.pid" : worker
        })

    provider = TracerProvider(resource=resource)
    trace.set_tracer_provider(provider)

    # otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4318/v1/traces")
    provider.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))

    return provider


def node_trace(function):
    def inner(*args, **kwargs):
        
        with tracer.start_as_current_span(function.__name__) as span:
            start_time = time.perf_counter()
            
            value = function(*args, **kwargs)
            # span.set_attributes({})
            
            end_time = time.perf_counter()
            # self.histogram.record(round((end_time-start_time), 2))
            
            return value
    
    return inner

class NodeTracer:
    def __init__(self, counter, error_counter, histogram):
        self.counter = counter
        self.error_counter = error_counter
        self.histogram = histogram

    def node_trace(self, function):
        def inner(*args, **kwargs):
            self.counter.add(1)
            with tracer.start_as_current_span(function.__name__) as span:
                start_time = time.perf_counter()
                try:
                    value = function(*args, **kwargs)
                    # span.set_attributes({})
                except:
                    self.error_counter.add(1)
                end_time = time.perf_counter()

                self.histogram.record(round((end_time-start_time), 2))
                
                return value
        
        return inner
