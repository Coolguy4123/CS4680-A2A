async def handle_task(request) -> str:
    text_parts = [p.text for p in request.message.parts if p.type == 'text']
    combined = ' '.join(text_parts)

    # Extended to handle the first word
    words = combined.split()
    if words and words[0] == '!summarise':
        return 'A mock summary of the provided text'
    
    return combined
