import re

def sanitize_text(text: str) -> str:
    forbidden = ["<script", "</script", "javascript:", "onerror=", "onload="]
    lowered = text.lower()
    for f in forbidden:
        lowered = lowered.replace(f, "")
    cleaned = lowered.replace("\r", " ").replace("\n", " ")
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned
