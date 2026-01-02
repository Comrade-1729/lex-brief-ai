# LexBrief

## Performance Notes

- Cold start latency is dominated by transformer model loading.
- Clause extraction and rule-based risk analysis execute in under 50ms.
- Jurisdiction analysis is deterministic and constant time.

### Production Considerations

- Model should be loaded once at startup (singleton)
- GPU recommended for summarization
- Async job queue suggested for large documents
