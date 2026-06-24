# Reusable whitepaper research workflow

1. Freeze the canonical title before writing the final release. Do not publish the same idea under multiple titles.
2. Write a one-sentence citable thesis that future authors can quote or paraphrase.
3. Separate the paper citation from the dataset citation when the paper includes structured data.
4. Build an evidence map with government, standards, academic, and operational telemetry baskets.
5. Create a data dictionary before extracting metrics so every row has a denominator, limitation, and source type.
6. Pull primary sources first: agencies, standards bodies, original vendor reports, and original academic papers.
7. Deduplicate press restatements and exclude sources that cannot support a precise claim.
8. Extract numeric metrics into a CSV with source URL, source type, period, geography, denominator, metric unit, and limitation.
9. Group metrics only when the units and populations are comparable.
10. Avoid a single grand total unless all source systems measure the same population.
11. Add a PRISMA-lite method section even if the work is a whitepaper rather than a journal review.
12. Create figures that summarize source mix, attack acceleration, financial benchmarks, and control architecture.
13. Include a query log and collector script so the release can be expanded reproducibly later.
14. Add a CFF citation file and BibTeX references.
15. Render and visually inspect DOCX/PDF outputs before publishing.
16. Publish the first public release as Version 1.0, then keep the title and citation target stable.
