"""
Analytics Made Simple (analyticsmadesimple.com)
Tutorial: Cosine search over vectors stored in SQLite
License: MIT

The vectors below are hand-written teaching numbers, not the output of an embedding model.
SQLite stores them. Python ranks them. Run: python3 03_vector_search_sqlite.py
"""

import json
import math
import sqlite3


def cosine_similarity(v1: list[float], v2: list[float]) -> float:
    dot_product = sum(a * b for a, b in zip(v1, v2))
    norm_a = math.sqrt(sum(a * a for a in v1))
    norm_b = math.sqrt(sum(b * b for b in v2))
    if norm_a == 0.0 or norm_b == 0.0:
        return 0.0
    return dot_product / (norm_a * norm_b)


documents = [
    ("SQL Joins and Entity Relationships", [0.92, 0.15, 0.05]),
    ("Pandas DataFrame Aggregations", [0.85, 0.35, 0.12]),
    ("Customer Retention Rate Analysis", [0.10, 0.88, 0.45]),
    ("Churn Prevention with Machine Learning", [0.15, 0.82, 0.52]),
]
query_vector = [0.95, 0.20, 0.02]

connection = sqlite3.connect(":memory:")
connection.execute("CREATE TABLE documents (id INTEGER PRIMARY KEY, title TEXT NOT NULL, vector TEXT NOT NULL)")
connection.executemany(
    "INSERT INTO documents (title, vector) VALUES (?, ?)",
    [(title, json.dumps(vector)) for title, vector in documents],
)

ranked = []
for title, raw_vector in connection.execute("SELECT title, vector FROM documents"):
    score = cosine_similarity(query_vector, json.loads(raw_vector))
    ranked.append((score, title))
ranked.sort(reverse=True)

print("Search intent: database queries and table merging")
print("Vectors are hand-written teaching numbers stored in SQLite.")
for rank, (score, title) in enumerate(ranked, 1):
    print(f"  {rank}. [{score:.4f}] {title}")
