EMERGENCY_KEYWORDS = [
    "chest pain",
    "can't breathe",
    "stroke",
    "unconscious",
    "severe bleeding",
    "heart attack"
]


def triage_check(query: str) -> dict:
    query_lower = query.lower()

    for keyword in EMERGENCY_KEYWORDS:
        if keyword in query_lower:
            return {
                "level": "🚨 EMERGENCY",
                "message": "CALL 911 IMMEDIATELY. This is a medical emergency.",
                "proceed": False
            }

    return {
        "level": "✅ Non-emergency",
        "proceed": True
    }