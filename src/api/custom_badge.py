import base64
import httpx
from pathlib import Path
from typing import Optional
from pydantic_extra_types.color import Color
from fastapi import APIRouter, Response, HTTPException
router = APIRouter(prefix="/api", tags=["badges"])

async def get_image_as_base64(image_source: str) -> Optional[str]:
    """
    Fetches an image from a URL or local path and returns a base64 data URI.
    """
    try:
        content = b""
        
        # Case 1: Web URL
        if image_source.startswith(("http://", "https://")):
            async with httpx.AsyncClient() as client:
                response = await client.get(image_source, timeout=5.0)
                response.raise_for_status()
                content = response.content
        
        # Case 2: Local Path
        else:
            path = Path(str(Path.cwd()) + "/src" + image_source)
            print(path)
            if path.is_file():
                content = path.read_bytes()
            else:
                return None

        # Encode to Base64
        base64_data = base64.b64encode(content).decode("utf-8")
        return f"data:image/svg+xml;base64,{base64_data}"
    
    except Exception as e:
        print(f"Error processing image: {e}")
        return None

@router.get(
    "/customBadge/{name}",
    responses={
        200: {
            "content": {
                "image/svg+xml": {
                    "schema": {"type": "string", "format": "binary"}
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
    # 1. Handle Image Logic
    img_data_uri = ""
    if not no_logo and image:
        resolved_img = await get_image_as_base64(image)
        if resolved_img:
            img_data_uri = resolved_img

    text_width = len(name) * 9 
    text_offset = 35 if not no_logo else 15
    svg_width = text_width + text_offset + 10

    # 3. Build Template
    rx = 10 if rounded else 0
    
    logo_tag = f'<image href="{img_data_uri}" x="10" y="7.5" width="15" height="15" />' if not no_logo else ""

    svg_template = f'''
    <svg width="{svg_width}" height="30" xmlns="http://www.w3.org/2000/svg">
        <rect width="100%" height="100%" fill="{bg_color.as_hex()}" rx="{rx}" ry="{rx}" />
        {logo_tag}
        <text x="{text_offset}" y="50%" 
            font-family="'Courier New', monospace" 
            font-size="15" 
            font-weight="700"
            fill="{text_color.as_hex()}" 
            dominant-baseline="middle">
                {name}
        </text>
    </svg>'''.strip()

    return Response(
        content=svg_template,
        media_type="image/svg+xml",
        # headers={
        #     "Cache-Control": "public, max-age=3600"
        # }
    )