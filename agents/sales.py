"""Sales agent for qualifying leads and running outreach."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class SalesAgent:
    """Automates sales tasks."""

    name: str = "Sales Agent"

    def qualify_lead(self, lead: str) -> str:
        """Simulate lead qualification."""
        return f"Qualified lead {lead}."

    def run_sequence(self, prospect: str) -> str:
        """Simulate running an email sequence."""
        return f"Ran outreach sequence for {prospect}."

    def track_pipeline(self, deal: str) -> str:
        """Simulate tracking a deal in the pipeline."""
        return f"Tracked deal {deal}."
