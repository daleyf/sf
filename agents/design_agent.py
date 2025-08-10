from typing import Dict, List


class DesignAgent:
    """Design Agent handles UI/UX and asset generation tasks."""

    def produce_mockups(self, components: List[str]) -> Dict[str, str]:
        """Return simple mockup representation for each component."""
        return {component: f"mockup for {component}" for component in components}

    def generate_assets(self, assets: List[str]) -> List[str]:
        """Return asset file names for provided asset types."""
        return [f"{asset}.png" for asset in assets]

    def maintain_design_system(self, guidelines: Dict[str, str]) -> Dict[str, str]:
        """Return guidelines to simulate maintaining design system."""
        return guidelines
