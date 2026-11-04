# Enterprise RAG Synthetic Corpus

Synthetic enterprise knowledge base for the `Production Agentic RAG Knowledge Assistant` project.

## Corpus
13 Markdown policy documents across HR, Engineering, Finance, Product, and Security.

Every document contains YAML frontmatter with:
- document_id
- department
- category
- version
- effective_date
- access_level
- title

The policies intentionally cross-reference one another. This creates realistic retrieval cases where the best answer requires metadata-aware retrieval, hybrid search, reranking, and multi-document synthesis.

## Evaluation
`evaluation/questions.json` contains 45 questions:
- 15 direct
- 10 paraphrased
- 8 multi-document
- 6 ambiguous
- 6 unanswerable

Each question includes a ground-truth answer and source document IDs where applicable.

## Suggested retrieval experiments
Run the same 45 questions against:
1. Dense vector retrieval
2. BM25
3. Hybrid retrieval
4. Hybrid + Reciprocal Rank Fusion
5. Hybrid + RRF + reranker
6. Query rewriting + the above
7. Agentic retry/grade loop + the above

Measure retrieval separately from generation. In particular, track whether the expected source document is present in top-K before judging the LLM answer.

## Suggested metadata filters
Try filters for:
- department
- category
- access_level
- effective_date
- document_id
- version

## Intended use
This corpus is fictional and created for engineering practice and RAG evaluation. It contains no real company policy.
