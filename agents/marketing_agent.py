from typing import Dict, List


class MarketingAgent:
    """Marketing Agent creates content and analyzes campaigns."""

    def write_blog_post(self, topic: str) -> str:
        """Return a simple blog post draft for a given topic."""
        return f"Blog post about {topic}"

    def perform_seo_research(self, keyword: str) -> List[str]:
        """Return a list of related keywords to simulate SEO research."""
        return [keyword, f"{keyword} tips", f"{keyword} tutorial"]

    def analyze_campaign(self, views: int, clicks: int) -> Dict[str, float]:
        """Return campaign metrics including click-through rate (CTR)."""
        ctr = (clicks / views) if views else 0
        return {"views": views, "clicks": clicks, "ctr": ctr}
