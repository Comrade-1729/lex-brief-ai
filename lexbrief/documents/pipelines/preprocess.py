def clean_text(text: str) -> str:
    text = text.replace("\x00", "")
    text = "\n".join(line.strip() for line in text.splitlines() if line.strip())
    return text
