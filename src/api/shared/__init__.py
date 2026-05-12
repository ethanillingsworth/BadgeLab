import json
from src.api.shared.enums import *
from src.api.shared.errors import *

def get_badge_list() -> dict:
    badge_list = {}
    with open("src/badgeList.json", "r") as f:
        
        badge_list = json.load(f)

    return badge_list