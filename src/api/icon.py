
from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from src.api.shared import IconStyle, IconName


router = APIRouter(prefix = "/api", tags=["Icons"])

@router.get("/icon/{id}")
async def icon(
    id: IconName,
    style: IconStyle = IconStyle.COLOR
):
    return RedirectResponse(
        f"/static/icons/{style.value}/{id.value}.svg",
        status_code=200,
        headers={
            "Cache-Control": "public, max-age=3600"
        }
    )