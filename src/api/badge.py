import json
from pydantic_extra_types import Color
from src.api.custom_badge import custom_badge
from fastapi import APIRouter, Path, Query, Response
from enum import Enum

badge_list = {}
with open("src/badgeList.json", "r") as f:
    badge_list = json.load(f)

router = APIRouter(prefix="/api", tags=["badges"])

def deep_get(target_style, dictionary, target_key, fallback_flag):

    styles = list(BadgeStyle)

    if fallback_flag and target_style in styles:
        styles.remove(target_style) # Removes the first occurrence
        styles.insert(0, target_style) # Places it at the very start
    else:
        styles = [target_style]
    
    
    for style in styles:

        style_dict = dictionary[style]
        
        for _, value in style_dict.items():
            for key2, value2 in value.items():
                if key2 == target_key:
                    return value2
    
    raise BadgeNotFound(f"Could not find badge with name {target_key} with style {target_style}")

class BadgeNotFound(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class BadgeName(str, Enum):
    # Languages
    HTML5 = "html5"
    CSS3 = "css3"
    JAVASCRIPT = "javascript"
    PYTHON = "python"
    SWIFT = "swift"
    JAVA = "java"
    JSON = "json"
    MARKDOWN = "markdown"
    ARDUINO = "arduino"
    C = "c"
    CPP = "cpp"

    # Frameworks
    REACT = "react"
    JQUERY = "jquery"
    TAILWINDCSS = "tailwindcss"

    # Learning
    W3SCHOOLS = "w3schools"
    KHAN_ACADEMY = "khan-academy"
    CODECADEMY = "codecademy"
    MDN = "mdn"
    GEEKSFORGEEKS = "geeksforgeeks"

    # Socials
    FACEBOOK = "facebook"
    LINKEDIN = "linkedin"
    INSTAGRAM = "instagram"
    YOUTUBE = "youtube"
    WEBSITE = "website"
    PORTFOLIO = "portfolio"
    EMAIL = "email"
    GMAIL = "gmail"
    BEHANCE = "behance"
    X = "x"
    TWITTER = "twitter"

    # Hosting
    FIREBASE = "firebase"
    NETLIFY = "netlify"
    GITHUB_PAGES = "github-pages"

    # Tools
    GITHUB = "github"
    VSCODE = "vscode"

    # Browsers
    FIREFOX = "firefox"
    CHROME = "chrome"
    SAFARI = "safari"
    EDGE = "edge"
    OPERA = "opera"
    BRAVE = "brave"
    TOR = "tor"

    # Systems
    DEBIAN = "debian"
    UBUNTU = "ubuntu"
    WINDOWS = "windows"

class BadgeStyle(str, Enum):
    COLOR = "color"
    MONO = "mono"
    ALT = "alt"

@router.get(
    "/badge/{name}", 
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
        name:       BadgeName   = Path(..., description="Name the badge you want to fetch."),
        style:      BadgeStyle  = Query(BadgeStyle.COLOR, description="Style for the badge."),
        no_logo:    bool        = Query(False, description="Don't show the logo if one is provided."),
        rounded:    bool        = Query(False, description="Round the corners of the badge."),
        fallback:   bool        = Query(True, description="Fallback to another style if the badge is not available in the given style.")
    ):


    try:
        badge_info = deep_get(style, badge_list, name, fallback)
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
    
