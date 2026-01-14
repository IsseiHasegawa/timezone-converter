from typing import List, Dict

def convert_times(from_tz: str, to_tz: str, time: List[str]) -> List[Dict]:
    """
    Temporary implementation (dummy).
    This will be replaced with real timezone conversion logic.
    """
    results = []
    for t in time:
        results.append({
            "input": t,
            "output": f"[{from_tz} -> {to_tz}] {t}",
            "status": "ok"
        })
    return results
