from pydantic_extra_types.color import Color

def handler(event, context):
    # The redirect above turns /badge/John into ?name=John
    params = event.get("queryStringParameters", {})
    
    # Required param: name
    name = params.get("name", "User")
    
    # Optional params with defaults
    try:
        text_color = Color(params.get("textColor", "#ffffff")).as_hex()
        bg_color = Color(params.get("backgroundColor", "#000000")).as_hex()
    except Exception:
        text_color = "#ffffff"
        bg_color = "#000000"

    no_logo = params.get("no_logo", "false").lower() == "true"
    rounded = params.get("rounded", "false").lower() == "true"
    image_url = params.get("image", "")

    # Layout Logic
    # 12px per char is a safe estimate for Courier New
    text_width = (len(name) * 10) 
    text_offset = 35 if not no_logo else 10
    svg_width = text_width + text_offset + 10 # Adding some right-side padding
    
    svg_template = f'''
        <svg width="{svg_width}" height="30" xmlns="http://www.w3.org/2000/svg">
            <rect width="100%" height="100%" fill="{bg_color}" rx="{10 if rounded else 0}" ry="{10 if rounded else 0}" />
            {'' if no_logo else f'<image href="{image_url}" x="10" y="7.5" width="15" height="15" />'}
            <text x="{text_offset}" y="50%" font-family="Courier New" font-size="15" fill="{text_color}" dominant-baseline="middle">{name}</text>
        </svg>'''

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "image/svg+xml",
            "Cache-Control": "public, max-age=3600"
        },
        "body": svg_template,
        "isBase64Encoded": False
    }