#!/usr/bin/env python3
    """Reproducible literature collector for future SP-SEC releases.

    Usage examples:
      export SEMANTIC_SCHOLAR_API_KEY="..."   # optional but recommended
      export NCBI_API_KEY="..."               # optional for higher rate limits
      python collect_literature_open_sources.py --out literature_candidates.jsonl

    This script queries Semantic Scholar, OpenAlex, Crossref, and PubMed/NCBI E-utilities.
    It intentionally saves raw candidate metadata only; human review is required before any
    metric enters the evidence corpus.
    """
    from __future__ import annotations
    import argparse, json, os, time, urllib.parse, urllib.request

    QUERIES = [
        "synthetic identity fraud",
        "AI identity fraud detection",
        "deepfake liveness verification identity",
        "face swap attack remote identity verification",
        "digital injection attack biometrics",
        "voice cloning fraud vishing",
        "LLM voice phishing detection",
        "knowledge based authentication breached PII",
        "passkeys phishing resistant authentication",
        "account opening fraud machine learning",
    ]

    def fetch_json(url, headers=None, timeout=30):
        req = urllib.request.Request(url, headers=headers or {})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8"))

    def semantic_scholar(query):
        key = os.getenv("SEMANTIC_SCHOLAR_API_KEY")
        headers = {"x-api-key": key} if key else {}
        params = urllib.parse.urlencode({
            "query": query,
            "limit": 20,
            "fields": "title,authors,year,venue,citationCount,externalIds,url,abstract"
        })
        return fetch_json(f"https://api.semanticscholar.org/graph/v1/paper/search?{params}", headers=headers)

    def openalex(query):
        params = urllib.parse.urlencode({"search": query, "per-page": 20})
        return fetch_json(f"https://api.openalex.org/works?{params}")

    def crossref(query):
        params = urllib.parse.urlencode({"query.title": query, "rows": 20})
        return fetch_json(f"https://api.crossref.org/works?{params}")

    def pubmed(query):
        api_key = os.getenv("NCBI_API_KEY")
        base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        params = {"db": "pubmed", "term": query, "retmode": "json", "retmax": 20}
        if api_key: params["api_key"] = api_key
        return fetch_json(base + "?" + urllib.parse.urlencode(params))

    def main():
        ap = argparse.ArgumentParser()
        ap.add_argument("--out", default="literature_candidates.jsonl")
        args = ap.parse_args()
        funcs = [("semantic_scholar", semantic_scholar), ("openalex", openalex), ("crossref", crossref), ("pubmed", pubmed)]
        with open(args.out, "w", encoding="utf-8") as f:
            for q in QUERIES:
                for name, func in funcs:
                    try:
                        data = func(q)
                        f.write(json.dumps({"source": name, "query": q, "data": data}, ensure_ascii=False) + "
")
                    except Exception as e:
                        f.write(json.dumps({"source": name, "query": q, "error": repr(e)}) + "
")
                    time.sleep(1.0)
    if __name__ == "__main__":
        main()
