import json
import os

CONFIG_FILE = os.path.expanduser("~/.oto-debug-config.json")

def get_api_key() -> str:
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("api_key")
        except json.JSONDecodeError:
            return None
    return None

def save_api_key(api_key: str):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump({"api_key": api_key}, f, indent=4)
    
    if os.name != 'nt':
        os.chmod(CONFIG_FILE, 0o600)