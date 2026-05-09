import json
from pydantic_extra_types import Color
from netlify.functions.custom_badge import custom_badge

badge_list = {}
with open("badgeList.json", "r") as f:
    badge_list = json.load(f)

def deep_get(dictionary, target_key):
    if target_key in dictionary:
        return dictionary[target_key]
    
    for _, value in dictionary.items():
        for key2, value2 in value.items():
            if key2 == target_key:
                return value2

    return {}

async def badge(
        name: str,
        no_logo: bool = False,
        rounded: bool = False
    ):

    badge_info = deep_get(badge_list, name)

    return await custom_badge(
        name=badge_info.get("name"),
        textColor=Color(badge_info.get("textColor", "#FFFFFF")),
        backgroundColor=Color(badge_info.get("bgColor", "#000000")),
        image=f'/static{badge_info.get("image")}',
        no_logo=no_logo,
        rounded=rounded
    )
    