def answer(question, docs):
    if not docs:
        return "I couldn't find anything about that in your documents."
    return "Based on your documents: " + " / ".join(docs)
