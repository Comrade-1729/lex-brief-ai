from django.shortcuts import render
from documents.services.analyze_document import analyze
from documents.models import Document
from documents.ai.summarizer_impl import DummySummarizer

def upload_view(request):
    if request.method == "POST":
        file = request.FILES["document"]
        doc = Document.objects.create(
            title=file.name,
            file=file
        )

        summarizer = DummySummarizer()
        result = analyze(doc.file.path, summarizer)

        doc.summary = result["summary"]
        doc.analysis = result
        doc.save()

        return render(
            request,
            "ui/result.html",
            {"result": result, "title": doc.title}
        )

    return render(request, "ui/upload.html")


def history_view(request):
    docs = Document.objects.order_by("-created_at")[:20]
    return render(request, "ui/history.html", {"documents": docs})
