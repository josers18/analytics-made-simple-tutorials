"""
Analytics Made Simple (analyticsmadesimple.com)
Tutorial: Vector Databases and Semantic Search from Scratch
Canonical Article: https://analyticsmadesimple.com/tutorials/
License: MIT
"""

import math
import sqlite3

def cosine_similarity(v1: list[float], v2: list[float]) -> float:
    """Compute cosine similarity between two float vectors without external dependencies."""
    dot_product = sum(a * b for a, b in zip(v1, v2))
    norm_a = math.sqrt(sum(a * a for a in v1))
    norm_b = math.sqrt(sum(b * b for b in v2))
    if norm_a == 0.0 or norm_b == 0.0:
        return 0.0
    return dot_product / (norm_a * norm_b)

# Toy knowledge base with mock 3-dimensional semantic embeddings
documents = [
    {"id": 1, "title": "SQL Joins and Entity Relationships", "vector": [0.92, 0.15, 0.05]},
    {"id": 2, "title": "Pandas DataFrame Aggregations", "vector": [0.85, 0.35, 0.12]},
    {"id": 3, "title": "Customer Retention Rate Analysis", "vector": [0.10, 0.88, 0.45]},
    {"id": 4, "title": "Churn Prevention with Machine Learning", "vector": [0.15, 0.82, 0.52]}
]

# Query vector representing "database queries and table merging"
query_vector = [0.95, 0.20, 0.02]

# Calculate similarity scores
ranked = []
for doc in documents:
    score = cosine_similarity(query_vector, doc["vector"])
    ranked.append((score, doc["title"]))

ranked.sort(reverse=True, key=lambda x: x[0])

print("=== Semantic Vector Search Results ===")
print("Search Intent: 'Database queries and table merging'")
for rank, (score, title) in enumerate(ranked, 1):
    print(f"  {rank}. [{score:.4f}] {title}")
