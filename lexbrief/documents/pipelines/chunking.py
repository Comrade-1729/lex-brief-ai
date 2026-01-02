from documents.config.limits import CHUNK_WORDS

def chunk_text(text: str, max_words=CHUNK_WORDS) -> list[str]:
    words = text.split()
    chunks = []

    for i in range(0, len(words), max_words):
        chunk = " ".join(words[i:i + max_words])
        chunks.append(chunk)

    return chunks
