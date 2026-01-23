import re

SECTION_PATTERN = re.compile(
    r"^\s*(\d+[\.\)]?\s+[A-Za-z][A-Za-z\s\-]{2,})$",
    re.MULTILINE
)

def split_sections(text: str):
    matches = list(SECTION_PATTERN.finditer(text))
    sections = []

    for i, match in enumerate(matches):
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)

        title = match.group(1).strip()
        content = text[start:end].strip()

        sections.append((title, content))

    return sections
