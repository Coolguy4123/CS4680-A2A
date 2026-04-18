AGENT_CARD = {
    "id": "reverse-agent-v1",
    "name": "Reverse Agent",
    "version": "1.0.0",
    "description": "An agent that returns the user's words in reverse",
    "url": "http://localhost:8000",
    "contact": {
        "email": "fyiu@cpp.edu",
    },
    "capabilities": {
        "streaming": False,
        "pushNotifications": False,
    },
    "defaultInputModes": ["text/plain"],
    "defaultOutputModes": ["text/plain"],
    "skills": [
        {
            "id": "reverse",
            "name": "Reverse",
            "description": "Returns the user message in reverse order",
            "inputModes": ["text/plain"],
            "outputModes": ["text/plain"],
        }
    ],
}
