import numpy as np
from pathlib import Path
import re

def testing(n=5):
    return np.random.randint(1, 11, n)

def report_count(word):
    word = str(word).lower()
    root = Path(__file__).resolve().parents[1]
    allowed = {".md", ".txt", ".py", ".ipynb"}
    text = []

    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in allowed:
            try:
                text.append(path.read_text(encoding="utf-8", errors="ignore"))
            except Exception:
                pass

    corpus = " ".join(text).lower()
    tokens = re.findall(r"[a-z']+", corpus)
    return sum(1 for token in tokens if token == word)
