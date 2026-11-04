                    ingestion/
                         │
              ┌──────────┴──────────┐
              ↓                     ↓
           loader                metadata
              │                     │
              └──────────┬──────────┘
                         ↓
                      cleaner
                         ↓
                      chunker
                         ↓
                    Chunk objects
                         ↓
                  inspect/debug
                         ↓
                     embeddings
                         ↓
                      Qdrant