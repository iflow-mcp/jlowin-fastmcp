"""FastMCP - An ergonomic MCP interface."""

import warnings
from importlib.metadata import version as _version
from fastmcp.settings import Settings
from fastmcp.utilities.logging import configure_logging as _configure_logging

settings = Settings()
if settings.log_enabled:
    _configure_logging(
        level=settings.log_level,
        enable_rich_tracebacks=settings.enable_rich_tracebacks,
    )

from fastmcp.server.server import FastMCP
from fastmcp.server.context import Context
import fastmcp.server

from fastmcp.client import Client
from . import client

try:
    __version__ = _version("iflow-mcp_jlowin-fastmcp")
except Exception:
    __version__ = "3.0.0"


# ensure deprecation warnings are displayed by default
if settings.deprecation_warnings:
    warnings.simplefilter("default", DeprecationWarning)


__all__ = [
    "Client",
    "Context",
    "FastMCP",
    "settings",
]