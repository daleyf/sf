"""Marketing agent to generate content and analyze campaigns."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class MarketingAgent:
    """Automates marketing tasks."""

    name: str = "Marketing Agent"

    def write_content(self, topic: str) -> str:
        """Simulate writing a piece of content."""
        return f"Wrote content about {topic}."

    def perform_seo_research(self, keyword: str) -> str:
        """Simulate SEO research."""
        return f"Researched SEO for {keyword}."

    def analyze_campaign(self, campaign: str) -> str:
        """Simulate campaign analytics."""
        return f"Analyzed campaign {campaign}."
