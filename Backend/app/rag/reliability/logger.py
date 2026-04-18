import json 
from pathlib import Path
from datetime import datetime


BASE_DIR = Path(__file__).resolve().parents[3]
LOG_FILE = BASE_DIR / "data" / "logs" / "failed_queries.json"

def log_failed_query(question: str):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

    record = {
        "question": question,
        "timestamp": datetime.now().isoformat()
    }

    if LOG_FILE.exists():
        try:
            data = json.loads(LOG_FILE.read_text(encoding="utf-8"))
            if not isinstance(data, list):
                data = []
        except (json.JSONDecodeError, OSError):
            data = []
    else:
        data = []

    data.append(record)

    LOG_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")