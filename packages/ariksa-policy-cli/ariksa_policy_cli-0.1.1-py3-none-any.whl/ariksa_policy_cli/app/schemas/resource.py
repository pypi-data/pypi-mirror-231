import enum
from datetime import datetime
from types import GenericAlias
from typing import Any
from uuid import UUID

import aiohttp  # type: ignore
from loguru import logger
from pydantic import BaseModel, parse_obj_as
from sqlmodel import SQLModel

from ariksa_policy_cli.app.core.settings import settings


class HTTPMethods(enum.Enum):
    GET: str = 'GET'
    POST: str = 'POST'
    PUT: str = 'PUT'
    PATCH: str = 'PATCH'
    DELETE: str = 'DELETE'


class APIResources(str, enum.Enum):
    START_DISCOVERY: str = 'cloud-account/code-repository/discover/'
    VALIDATE_TOKEN = 'cloud-account/code-repository/validate-token'