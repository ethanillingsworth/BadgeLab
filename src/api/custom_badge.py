from pydantic_extra_types.color import Color
from fastapi import APIRouter, Response
from typing import Optional

router = APIRouter(prefix="/api", tags=["badges"])

@router.get(
    "/customBadge/{name}",
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
        }
    }
)
async def custom_badge(
    name:       str,
    text_color: Color           = Color("#ffffff"),
    bg_color:   Color           = Color("#000000"),
    image:      Optional[str]   = None,
    no_logo:    bool            = False,
    rounded:    bool            = False,
):
    text_width = (len(name) * 10) 
    text_offset = 35 if not no_logo else 10
    svg_width = text_width + text_offset
    
    svg_template = f'''
        <svg width="{svg_width}" height="30" xmlns="http://www.w3.org/2000/svg">

            <rect width="100%" height="100%" fill="{bg_color}" rx="{10 if rounded else 0}" ry="{10 if rounded else 0}" />

            {'' if no_logo else f'<image href="{image}" x="10" y="7.5" width="15" height="15" />'}

            <text x="{text_offset}" y="50%" font-family="Courier New" font-size="15" fill="{text_color}" dominant-baseline="middle">{name}</text>

        </svg>'''

    return Response(
            content=svg_template,
            status_code=200,
            headers={
                "Content-Type": "image/svg+xml",
                "Cache-Control": "public, max-age=3600"
            }
        )
