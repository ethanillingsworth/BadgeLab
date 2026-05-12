from enum import Enum

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

class IconName(str, Enum):
     # Languages
    HTML = "html"
    CSS = "css"
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
    KHAN = "khan"
    CODECADEMY = "codecademy"
    MDN = "mdn"
    GEEKSFORGEEKS = "geeksforgeeks"

    # Socials
    FACEBOOK = "facebook"
    LINKEDIN = "linkedin"
    INSTAGRAM = "instagram"
    YOUTUBE = "youtube"
    WEB = "web"
    PORTFOLIO = "portfolio"
    EMAIL = "email"
    GMAIL = "gmail"
    BEHANCE = "behance"
    X = "x"
    TWITTER = "twitter"

    # Hosting
    FIREBASE = "firebase"
    NETLIFY = "netlify"
    
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

class IconStyle(str, Enum):
    COLOR = "color"
    WHITE = "white"
    BLACK = "black"