"""Agent classes implementing core tasks for a solo AI-first company."""

from .engineering import EngineeringAgent
from .design import DesignAgent
from .marketing import MarketingAgent
from .sales import SalesAgent
from .support import SupportAgent

__all__ = [
    "EngineeringAgent",
    "DesignAgent",
    "MarketingAgent",
    "SalesAgent",
    "SupportAgent",
]
