def filter_response(detection: dict) -> dict:
    category = detection.get("category", "safe")
    risk = detection.get("risk_level", "low")

    if category == "self_harm" and risk in ["medium", "high"]:
        return {
            "action": "block",
            "crisis": True,
            "replacement": (
                "I'm really concerned about your safety. "
                "Please reach out for help right away. "
                "Find local crisis resources: https://www.iasp.info/suicidalthoughts/"
            ),
            "message_to_user": "This content was blocked for safety reasons."
        }

    if category == "violence" and risk == "high":
        return {
            "action": "block",
            "crisis": True,
            "replacement": (
                "This conversation involves serious harm to others. "
                "If you or someone else is in danger, contact local emergency services immediately."
            ),
            "message_to_user": "Content blocked due to violence risk."
        }

    if category == "dangerous_instructions" and risk in ["medium", "high"]:
        return {
            "action": "block",
            "crisis": False,
            "replacement": "I can't help with that request. Let's talk about something else.",
            "message_to_user": "Request blocked for safety."
        }

    if category == "ai_dependency" and risk in ["medium", "high"]:
        return {
            "action": "modify",
            "crisis": False,
            "replacement": None,
            "message_to_user": (
                "It seems like you're relying a lot on AI right now. "
                "Real conversations with people who care about you matter too."
            )
        }

    if risk == "medium":
        return {
            "action": "modify",
            "crisis": False,
            "replacement": None,
            "message_to_user": "Please keep the conversation safe and respectful."
        }

    return {
        "action": "allow",
        "crisis": False,
        "replacement": None,
        "message_to_user": None
    }
