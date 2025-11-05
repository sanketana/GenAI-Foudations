# Week 07: RAG Part 2 - Advanced Techniques - Instructor Notes


- LCEL
- Langsmith
- Langchain Architectural changes
- ConversationalChain --> Deprecated
- RetrievalQA --> Deprecated
=======
- Whats Deprecated
- Why?
- What's new
- Packages - langchain, langchain-core, langchain-community, langchain-classic
- Agent abstraction
- Key new architectural components like LCEL, runnable, new package structure, langgraph as foundational runtime, lightweight core
- New Langchain concepts - Agent abstraction
- New RAG architecture
- Langsmith
- Modern Conversational RAG Application
- Key Migration aspects
    - Pipe for chaining
    - Runnable object (retriever, prompt, LLM), agent.invoke

- Agent Chat UI
======
Ver 1 changes
Creating Agent in Version 1
Decorator pattern 
Runnables and Chain 
Memory and context
Invoke vs batch
RAG
Langchain case studies


Runnables
- types of runnables
- decorator pattern
- | operator
- invoke or batch




## Learning Objectives
- Advanced RAG optimization techniques
- Multi-modal and complex retrieval patterns
- Production deployment and scaling
- RAG system evaluation and monitoring

## Key Topics to Cover
1. Advanced retrieval strategies (hierarchical, multi-hop)
2. Query expansion and reformulation
3. Multi-modal RAG (text, images, structured data)
4. Context compression and summarization
5. Production monitoring and optimization

## Advanced Techniques
- Hypothetical Document Embeddings (HyDE)
- Multi-query retrieval and fusion
- Retrieval with metadata filtering
- Re-ranking and relevance scoring
- Context-aware chunking strategies

## Hands-on Activities
- Implementing query expansion techniques
- Building multi-hop reasoning systems
- Creating evaluation frameworks
- Deploying production RAG systems
- Performance monitoring and alerting

## Production Considerations
- Latency optimization strategies
- Cost management and API usage
- Error handling and fallback mechanisms
- A/B testing for RAG improvements
- User feedback integration

## Evaluation and Monitoring
- Automated evaluation pipelines
- User satisfaction metrics
- Retrieval quality assessment
- Generation factualness checking
- System performance monitoring 