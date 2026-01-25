from django.conf import settings
from documents.ai.summarizer_factory import get_summarizer
from documents.ai.dummy_summarizer import DummySummarizer

def test_dummy_summarizer_used_by_default():
    settings.USE_DUMMY_SUMMARIZER = True
    summarizer = get_summarizer()
    assert isinstance(summarizer, DummySummarizer)
