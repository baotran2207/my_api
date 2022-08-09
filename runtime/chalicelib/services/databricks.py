from typing import Protocol
from pydantic import HttpUrl, BaseModel
from dataclasses import dataclass
from chalicelib.config import settings

@dataclass
class DataBricksService():
    DATABRICKS_WORKSPACE_URL: HttpUrl
    DATABRICKS_TOKEN: str
    DATABRICKS_JOB_API_VERSION: str


databricks_service = DataBricksService(
    DATABRICKS_WORKSPACE_URL=settings.DATABRICKS_WORKSPACE_URL,
    DATABRICKS_TOKEN=settings.DATABRICKS_TOKEN,
    DATABRICKS_JOB_API_VERSION=settings.DATABRICKS_JOB_API_VERSION,
)