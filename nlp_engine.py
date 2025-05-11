def get_intent(query):
    query = query.lower()
    if "weather" in query:
        return "weather"
    elif "time" in query:
        return "time"
    elif "exit" in query or "stop" in query:
        return "exit"
    else:
        return "unknown"