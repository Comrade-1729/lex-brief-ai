# documents/config/limits.py

# -------- File handling --------
MAX_UPLOAD_MB = 5
ALLOWED_EXTENSIONS = {".pdf", ".docx", ".txt"}
AUTO_DELETE_HOURS = 24

# -------- Text processing --------
CHUNK_WORDS = 400
CHUNK_OVERLAP_WORDS = 50

# -------- Summarization --------
SUMMARY_MIN_TOKENS = 80
SUMMARY_MAX_TOKENS = 250
MODEL_MAX_INPUT_TOKENS = 1024

# -------- Performance --------
MAX_DOCUMENT_WORDS = 20_000
