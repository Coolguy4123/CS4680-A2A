AGENT_CARD = {
    "id": "echo-agent-v1",
    "name": "Echo Agent",
    "version": "1.0.0",
    "description": "A simple agent that echoes back any text it receives.",
    "url": "http://localhost:8000", # updated at deploy time
    "contact": {
        "email": "fyiu@cpp.edu",
    },
    "capabilities": {
        "streaming": False,
        "pushNotifications": False
    },
    "defaultInputModes": ["text/plain"],
    "defaultOutputModes": ["text/plain"],
    "skills": [
        {
            "id": "echo",
            "name": "Echo",
            "description": "Returns the user message verbatim.",
            "inputModes": ["text/plain"],
            "outputModes": ["text/plain"]
        },
        {
            "id": "summarize",
            "name": "Summarize",
            "description": "Summarize the user message verbatim.",
            "inputModes": ["text/plain"],
            "outputModes": ["text/plain"]
        }
    ]
}

# Method that checks all required fields are present
def validate_card(card: dict) -> bool:
    main_fields = (
        "id",
        "name",
        "version",
        "description",
        "url",
        "contact",
        "capabilities",
        "defaultInputModes",
        "defaultOutputModes",
        "skills",
    )

    for key in main_fields:
        if key not in card:
            return False

    contact = card.get("contact")
    if not isinstance(contact, dict) or "email" not in contact:
        return False

    capabilities = card.get("capabilities")
    if not isinstance(capabilities, dict):
        return False
    if "streaming" not in capabilities or "pushNotifications" not in capabilities:
        return False

    if not isinstance(card.get("defaultInputModes"), list):
        return False
    if not isinstance(card.get("defaultOutputModes"), list):
        return False
    if not isinstance(card.get("skills"), list):
        return False

    return True
