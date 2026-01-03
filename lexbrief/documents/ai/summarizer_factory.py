from django.conf import settings
from documents.ai.dummy_summarizer import DummySummarizer
from documents.ai.legal_t5_summarizer import LegalT5Summarizer

_summarizer = None

def get_summarizer():
    global _summarizer

    if _summarizer is not None:
        return _summarizer

    if settings.USE_DUMMY_SUMMARIZER:
        _summarizer = DummySummarizer()
    else:
        _summarizer = LegalT5Summarizer()

    return _summarizer
