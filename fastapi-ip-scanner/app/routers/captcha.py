from fastapi import HTTPException

def validate_captcha(captcha_value: str):
    # Dummy captcha validation
    if not captcha_value or captcha_value.strip() == "":
        raise HTTPException(status_code=400, detail="Captcha required")
    return True
