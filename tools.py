PACKAGES = {
    "mini": {"price": 250, "includes": "30 minutes, 15 edited photos"},
    "standard": {"price": 600, "includes": "2 hours, 60 edited photos"},
    "full-day": {"price": 2400, "includes": "8 hours, 400 edited photos, second shooter"},
}


def get_package_price(package_name):
    package = PACKAGES.get(package_name.lower())
    if package is None:
        return f"No package called '{package_name}'. Options: {', '.join(PACKAGES)}"
    return f"{package_name}: ${package['price']} CAD, includes {package['includes']}"


tools = [
    {
        "name": "get_package_price",
        "description": "Look up the price and what is included for a photography package. Use this whenever the user asks what a package costs or contains.",
        "input_schema": {
            "type": "object",
            "properties": {
                "package_name": {
                    "type": "string",
                    "description": "The package to look up: mini, standard, or full-day.",
                }
            },
            "required": ["package_name"],
        },
    }
]

SCHEDULE = {
    "weekday": ["Anytime after 5pm"],
    "weekend": ["In the mornings is the best for no rush"]
    }

def check_shoot_availability(date):
    
    return