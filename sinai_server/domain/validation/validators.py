from fastapi import HTTPException

def validate_prompt(prompt: str):
    if prompt is None:
        raise HTTPException(status_code=400, detail="Prompt cannot be null")
    if not isinstance(prompt, str):
        raise HTTPException(status_code=400, detail="Prompt must be a string")
    prompt = prompt.strip()
    if len(prompt) == 0:
        raise HTTPException(status_code=400, detail="Prompt cannot be empty")
    if len(prompt) > 5000:
        raise HTTPException(status_code=400, detail="Prompt too long")
    return True
