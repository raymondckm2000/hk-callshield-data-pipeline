"""Application configuration settings."""

from dotenv import load_dotenv
import os


# Load environment variables from a .env file if present
load_dotenv()

# Database connection URL
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://callshield:callshield@localhost:5432/callshield",
)

# FastAPI host and port configuration
API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", "8080"))

# Directory for published artifacts
PUBLISH_DIR = os.getenv("PUBLISH_DIR", "app/public")

# Miscellaneous ETL settings
IOS_CHUNK_SIZE = int(os.getenv("IOS_CHUNK_SIZE", "50000"))
DELTA_MAX_LOOKBACK_DAYS = int(os.getenv("DELTA_MAX_LOOKBACK_DAYS", "7"))

