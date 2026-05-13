from typing import Optional

from fastapi import APIRouter, Query, Response

from src.api.shared import get_badge_list

router = APIRouter(prefix="/api", tags=["Badges"])
badge_list = get_badge_list()


def _build_badge_url(base_url: str, badge_id: str, style: Optional[str] = None) -> str:
    if style:
        return f"{base_url}/api/badge/{badge_id}?style={style}"
    return f"{base_url}/api/badge/{badge_id}"


def _build_badge_row_html(base_url: str, badge_id: str) -> str:
    color_url = _build_badge_url(base_url, badge_id)
    alt_url = _build_badge_url(base_url, badge_id, "alt")
    mono_url = _build_badge_url(base_url, badge_id, "mono")

    return (
        "<tr>"
        f"<td><strong>{badge_id}</strong></td>"
        f"<td><img src=\"{color_url}\" alt=\"{badge_id}\"></td>"
        f"<td><img src=\"{alt_url}\" alt=\"{badge_id}\"></td>"
        f"<td><img src=\"{mono_url}\" alt=\"{badge_id}\"></td>"
        "</tr>"
    )


def _render_section_html(section_key: str, badges: dict, base_url: str) -> str:
    rows = "".join(_build_badge_row_html(base_url, badge_id) for badge_id in badges.keys())
    return (
        f"<section>"
        f"<h2>{section_key}</h2>"
        f"<table>"
        "<thead>"
        "<tr><th>ID</th><th>Color</th><th>Alt</th><th>Mono</th></tr>"
        "</thead>"
        "<tbody>"
        f"{rows}"
        "</tbody>"
        "</table>"
        "</section>"
    )


@router.get("/badgeTable")
async def badge_table(
    sections: Optional[str] = Query(
        None,
        description="Comma-separated section keys to include. Defaults to all available badge sections."
    ),
) -> str:
    """Generate an HTML badge table from badgeList.json."""
    base_url = ""
    selected_sections = None

    if sections:
        selected_sections = {section.strip() for section in sections.split(",") if section.strip()}

    color_sections = badge_list.get("color", {})
    section_html = []

    for section_key, badges in color_sections.items():
        if selected_sections and section_key not in selected_sections:
            continue

        section_html.append(_render_section_html(section_key, badges, base_url))

    if not section_html:
        available = ", ".join(color_sections.keys())
        body = f"<p>No badge sections found. Available sections: {available}.</p>"
    else:
        body = "".join(section_html)

    return Response(content=(
        "<html>"
        "<head>"
        "<meta charset=\"utf-8\">"
        "<title>BadgeLab Badge Table</title>"
        "<style>"
        "body{font-family:Arial,Helvetica,sans-serif;margin:24px;}"
        "table{border-collapse:collapse;width:100%;margin-bottom:24px;}"
        "th,td{border:1px solid #ddd;padding:12px;text-align:left;vertical-align:middle;}"
        "th{background:#f3f4f6;color:#111;font-weight:600;}"
        "img{max-height:32px;display:block;}"
        "section{margin-bottom:32px;}"
        "h2{margin-bottom:12px;text-transform:capitalize;}"
        "</style>"
        "</head>"
        "<body>"
        "<h1>BadgeLab Badge Table</h1>"
        f"{body}"
        "</body>"
        "</html>"
        ), 
        media_type="text/html",
        status_code=200
    )
