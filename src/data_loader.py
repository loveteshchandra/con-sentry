"""
Data loader for test interactions dataset.
"""

import json
from pathlib import Path
from dataclasses import dataclass
from typing import List, Tuple, Optional


@dataclass
class TestInteraction:
    """Represents a single test interaction with metadata."""
    prompt: str
    response: str
    category: str = "general"
    expected_compliant: bool = True
    
    def as_tuple(self) -> Tuple[str, str]:
        """Return as simple (prompt, response) tuple for backward compatibility."""
        return (self.prompt, self.response)


def load_interactions(
    file_path: Optional[str] = None,
    category: Optional[str] = None
) -> List[TestInteraction]:
    """
    Load test interactions from a JSON file.
    
    Args:
        file_path: Path to JSON file. Defaults to data/test_interactions.json
        category: Optional filter by category
        
    Returns:
        List of TestInteraction objects
    """
    if file_path is None:
        # Default to data/test_interactions.json relative to project root
        project_root = Path(__file__).parent.parent
        file_path = project_root / "data" / "test_interactions.json"
    else:
        file_path = Path(file_path)
    
    if not file_path.exists():
        raise FileNotFoundError(f"Interactions file not found: {file_path}")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    interactions = [
        TestInteraction(
            prompt=item["prompt"],
            response=item["response"],
            category=item.get("category", "general"),
            expected_compliant=item.get("expected_compliant", True)
        )
        for item in data
    ]
    
    # Filter by category if specified
    if category:
        interactions = [i for i in interactions if i.category == category]
    
    return interactions


def load_interactions_as_tuples(
    file_path: Optional[str] = None,
    category: Optional[str] = None
) -> List[Tuple[str, str]]:
    """
    Load interactions and return as simple (prompt, response) tuples.
    
    This provides backward compatibility with the original main.py format.
    """
    interactions = load_interactions(file_path, category)
    return [i.as_tuple() for i in interactions]
