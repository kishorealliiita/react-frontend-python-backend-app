from prometheus_client import Counter, Histogram, Gauge
from prometheus_fastapi_instrumentator import Instrumentator

# Request metrics
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total number of HTTP requests",
    ["method", "endpoint", "status"]
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "HTTP request latency in seconds",
    ["method", "endpoint"]
)

# Business metrics
USER_REGISTRATION_COUNT = Counter(
    "user_registrations_total",
    "Total number of user registrations"
)

USER_LOGIN_COUNT = Counter(
    "user_logins_total",
    "Total number of user logins"
)

# System metrics
ACTIVE_USERS = Gauge(
    "active_users",
    "Number of currently active users"
)

DATABASE_CONNECTIONS = Gauge(
    "database_connections",
    "Number of active database connections"
)

def setup_metrics(app):
    """Setup Prometheus metrics for the FastAPI application"""
    Instrumentator().instrument(app).expose(app) 