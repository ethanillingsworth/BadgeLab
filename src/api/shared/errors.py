from src.api.shared.enums import BadgeName, BadgeStyle


class BadgeNotFound(Exception):
    def __init__(self, key: BadgeName, style: BadgeStyle):
        super().__init__()
        self.message = f"Could not find badge with name {key} with style {style}"

