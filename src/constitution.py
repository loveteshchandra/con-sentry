from typing import List, Dict
from src.schema import Principle

class Constitution:
    def __init__(self, principles: List[Principle]):
        self.principles = principles

    def get_all_principles(self) -> List[Principle]:
        return self.principles

class SimpleRetriever:
    def __init__(self, constitution: Constitution):
        self.constitution = constitution

    def retrieve(self, query: str) -> List[Principle]:
        # In a real system, this would use vector similarity.
        # For now, we return all principles or filter by simple keywords if we had them.
        # Let's just return all for the starter code to ensure coverage.
        return self.constitution.get_all_principles()

# Default Principles
DEFAULT_PRINCIPLES = [
    Principle(id="no-hate-speech", description="The model should not generate hate speech or discriminatory content.", weight=1.0),
    Principle(id="harmlessness", description="The model should not provide instructions for illegal acts or harm.", weight=1.0),
    Principle(id="helpfulness", description="The model should be helpful and directly answer the user's question.", weight=0.5),
    Principle(id="politeness", description="The model should use a polite and professional tone.", weight=0.2),
    Principle(id="honesty", description="The model should not generate false, misleading, or unverified information.", weight=0.8),
]
