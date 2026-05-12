import json
from pydantic_extra_types import Color
from src.api.custom_badge import custom_badge
from fastapi import APIRouter, Path, Query, Response
from src.api.shared import get_badge_list, BadgeNotFound, BadgeStyle, BadgeName

router = APIRouter(prefix="/api", tags=["Badges"])

badge_list = get_badge_list()

def deep_get(target_style, target_key, fallback_flag):

    styles = list(BadgeStyle)

    if fallback_flag and target_style in styles:
        styles.remove(target_style) # Removes the first occurrence
        styles.insert(0, target_style) # Places it at the very start
    else:
        styles = [target_style]
    
    
    for style in styles:

        style_dict = badge_list[style]
        
        for _, value in style_dict.items():
            for key2, value2 in value.items():
                if key2 == target_key:
                    return value2
    
    raise BadgeNotFound(target_key, target_style)

@router.get(
    "/badge/{id}", 
    responses={
        200: {
            "content": {
                "application/json": None,
                "image/svg+xml": {
                    "schema": {
                        "description": "Raw SVG XML string",
                        "xml": {"name": "svg"},
                        "format": "binary"
                    }
                }
            }
        },
        404: {
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "detail": {
                                "type": "string",
                                "description": "A message explaining why the badge was not found."
                            }
                        }
                    },
                    "example": {"detail": "Could not find badge with name {target_key} with style {target_style}"}
                }
            },
        }
    }
)
async def badge(
        id:       BadgeName   = Path(..., description="ID of the badge you want to fetch."),
        style:      BadgeStyle  = Query(BadgeStyle.COLOR, description="Style for the badge."),
        no_logo:    bool        = Query(False, description="Don't show the logo if one is provided."),
        rounded:    bool        = Query(False, description="Round the corners of the badge."),
        fallback:   bool        = Query(True, description="Fallback to another style if the badge is not available in the given style.")
    ):


    try:
        badge_info = deep_get(style, id, fallback)
    except BadgeNotFound as e:
        return Response(
            json.dumps(
                {
                    "detail": e.message,
                }
            ),
            status_code=404,
            headers={"Content-Type": "application/json"}
        )

    return await custom_badge(
        name=badge_info.get("name"),
        text_color=Color(badge_info.get("textColor", "#FFFFFF")),
        bg_color=Color(badge_info.get("bgColor", "#000000")),
        image=f'/static{badge_info.get("image")}',
        no_logo=no_logo,
        rounded=rounded
    )
    
