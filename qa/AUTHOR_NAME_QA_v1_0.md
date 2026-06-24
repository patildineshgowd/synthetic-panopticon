# Author-name normalization QA - Version 1.0

Visible recommended citations were normalized to the full author name:

- Dinesh Gowd Patil (2026). The Synthetic Panopticon: AI-Enabled Identity Fraud, PII Degradation, and Multi-Layered Identity Defense. Version 1.0, June 2026.
- Dinesh Gowd Patil (2026). SP-SEC-50 Evidence Corpus v1.0: Structured Evidence on AI-Enabled Identity Fraud and PII Degradation. Version 1.0, June 2026.

QA checks performed:

- Scanned PDF text extraction.
- Scanned DOCX XML.
- Scanned XLSX XML.
- Scanned Markdown, README, CFF, BibTeX, CSV, JSONL, and script files.
- Confirmed no abbreviated visible author strings remain.
- Re-rendered DOCX and PDF title page for visual verification.

Structured CFF fields still use `family-names: Patil` and `given-names: Dinesh Gowd`, because that is the schema-correct way to encode the same full person name.
