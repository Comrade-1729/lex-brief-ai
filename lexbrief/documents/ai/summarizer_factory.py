from django.conf import settings

_summarizer = None

def get_summarizer():
    global _summarizer

    if _summarizer is not None:
        return _summarizer

    if settings.USE_DUMMY_SUMMARIZER:
        # 🚨 HARD SAFETY: never load transformers in prod
        from documents.ai.dummy_summarizer import DummySummarizer
        _summarizer = DummySummarizer()
    else:
        # LegalT5 is allowed ONLY when explicitly enabled
        from documents.ai.legal_t5_summarizer import LegalT5Summarizer
        _summarizer = LegalT5Summarizer()

    return _summarizer
