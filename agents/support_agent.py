from typing import Dict


class SupportAgent:
    """Support Agent resolves tickets and maintains a knowledge base."""

    def __init__(self) -> None:
        self.knowledge_base: Dict[str, str] = {
            "How do I reset my password?": "Click 'Forgot password' on the login page and follow the instructions."
        }

    def resolve_ticket(self, question: str) -> str:
        """Answer a support question using the knowledge base."""
        return self.knowledge_base.get(question, "Please provide more details.")

    def update_knowledge_base(self, question: str, answer: str) -> None:
        """Update the knowledge base with a new Q&A pair."""
        self.knowledge_base[question] = answer

    def escalate_issue(self, issue: str) -> str:
        """Return a message indicating the issue has been escalated."""
        return f"Escalated: {issue}"
