from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from documents.ai.summarizer import Summarizer


class LegalT5Summarizer(Summarizer):
    """
    Production-safe LegalT5 summarizer.
    - Deterministic
    - No sampling
    - Length controlled
    """

    def __init__(self, model_name="nsi319/legal-t5-base"):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name,
            use_fast=True,
            local_files_only=False
        )
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        self.model.to(self.device)
        self.model.eval()

    def summarize(self, text: str) -> str:
        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            max_length=1024
        ).to(self.device)

        with torch.inference_mode():
            summary_ids = self.model.generate(
                **inputs,
                max_length=250,
                min_length=80,
                do_sample=False,
                num_beams=4,
                early_stopping=True
            )

        return self.tokenizer.decode(
            summary_ids[0],
            skip_special_tokens=True
        )
