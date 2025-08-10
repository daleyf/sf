from typing import Dict, List


class SalesAgent:
    """Sales Agent converts leads into customers."""

    def qualify_lead(self, lead_info: Dict[str, int]) -> bool:
        """Return True if lead has budget and interest."""
        return bool(lead_info.get("budget")) and bool(lead_info.get("interest"))

    def run_outbound_sequence(self, prospect: str) -> List[str]:
        """Return a simple three-step outreach sequence for prospect."""
        return [
            f"Introductory email to {prospect}",
            f"Follow-up email to {prospect}",
            f"Closing email to {prospect}",
        ]

    def track_pipeline(self, leads: List[str]) -> List[str]:
        """Return the list of leads to simulate tracking pipeline."""
        return leads
