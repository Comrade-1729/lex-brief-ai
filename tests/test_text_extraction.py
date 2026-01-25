from documents.pipelines.extract_text import extract_text
import tempfile
import os

def test_extract_text_from_txt():
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".txt", delete=False) as f:
        f.write("Hello contract world")
        path = f.name

    try:
        text = extract_text(path)
        assert "Hello contract world" in text
    finally:
        os.remove(path)
