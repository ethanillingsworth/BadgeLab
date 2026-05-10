import json
from pydantic_extra_types import Color
from src.api.custom_badge import custom_badge
from fastapi import APIRouter, Response
from pydantic import BaseModel, Field
from enum import Enum

badge_list = {}
with open("src/badgeList.json", "r") as f:
    badge_list = json.load(f)

class BadgeNotFound(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

def deep_get(dictionary, target_key):
    if target_key in dictionary:
        return dictionary[target_key]
    
    for _, value in dictionary.items():
        for key2, value2 in value.items():
            if key2 == target_key:
                return value2
    
    raise BadgeNotFound(f"Could not find badge with name {target_key}")

router = APIRouter(prefix="/api", tags=["badges"])

from enum import Enum

class BadgeName(str, Enum):
    # Langs
    HTML5 = "html5"
    CSS3 = "css3"
    JAVASCRIPT = "javascript"
    PYTHON = "python"
    SWIFT = "swift"
    JAVA = "java"
    MARKDOWN = "markdown"
    ARDUINO = "arduino"
    C = "c"
    CPP = "cpp"

    # Frameworks
    JQUERY = "jquery"
    TAILWINDCSS = "tailwindcss"

    # Learning
    W3SCHOOLS = "w3schools"
    KHAN_ACADEMY = "khan-academy"
    CODECADEMY = "codecademy"
    MDN = "mdn"

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
    VSCODE_WHITE = "vscode-white"

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
                    "example": {"detail": "Could not find badge with name {name}"}
                }
            },
        }
    }
)
async def badge(
        name:       BadgeName,
        style:      BadgeStyle  = BadgeStyle.COLOR,
        no_logo:    bool        = False,
        rounded:    bool        = False
    ):


    try:
        badge_info = deep_get(badge_list[style], name)
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
    
