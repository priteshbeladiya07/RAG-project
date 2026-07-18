# RAG-project

## Summary
A simple Retrieval-Augmented Generation (RAG) project focused on producing concise summaries and context-aware answers from your own documents and websites—not on building new ML models.

## What this project does
- PDF summaries (single or batch)
- Plain text summaries
- Website / URL summaries (HTML content)
- Short Q&A and context-grounded answers using retrieved document excerpts
- Exportable outputs (plain text / markdown)

## Who this is for
Anyone who wants quick, accurate summaries or answers from their private corpus (reports, manuals, web pages) without dealing with model training.

## How to use (high-level)
1. Place input files in the `data/` folder or provide URLs.
2. Run the ingestion/processing script to extract and chunk text.
3. Build or update the vector store.
4. Use the UI or API to request summaries or ask questions.

## Notes
- Uses preconfigured LLM and embedding providers.
- Focuses on retrieval + summarization/Q&A, not model training.
- Tune chunk sizes and retrieval settings for better results.

