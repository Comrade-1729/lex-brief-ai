from documents.ai.summarizer import Summarizer

class DummySummarizer(Summarizer):
    def summarize(self, text: str) -> str:
        return text[:500] + "..."
