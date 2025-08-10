"""Agent implementations for the solo unicorn playbook."""

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
