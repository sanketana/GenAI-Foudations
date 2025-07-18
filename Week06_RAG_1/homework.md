# Week 06: Homework Assignment

## Assignment: Building Your First RAG System

### Part 1: RAG Pipeline Implementation (45 points)
**Deadline:** Before Week 07 class

1. **Document Processing Pipeline** (15 points)
   - Support multiple document formats (PDF, TXT, DOCX)
   - Implement intelligent text chunking
   - Handle metadata extraction and storage
   - Add duplicate detection and filtering

2. **Retrieval System** (15 points)
   - Integrate with vector database from Week 05
   - Implement similarity search with filtering
   - Add re-ranking based on relevance
   - Support multiple retrieval strategies

3. **Generation Integration** (15 points)
   - Connect retrieval to language model
   - Design effective prompts for RAG
   - Handle context length limitations
   - Implement response citation and attribution

### Part 2: RAG Application Development (35 points)
**Create a domain-specific question-answering system**

Choose one domain and build a specialized RAG system:

**Option A: Technical Documentation QA**
- Index programming documentation or API references
- Support code examples and technical queries
- Provide actionable answers with code snippets

**Option B: Research Paper Assistant**
- Process academic papers in specific field
- Enable literature review and fact-checking
- Support citation generation and source tracking

**Option C: Company Knowledge Base**
- Index internal documents and policies
- Support employee queries and onboarding
- Include role-based access and personalization

**Requirements:**
1. **Data Collection and Processing** (15 points)
   - Gather minimum 100 relevant documents
   - Implement domain-specific preprocessing
   - Optimize chunking for content type

2. **Interface Development** (20 points)
   - Create Streamlit interface for queries
   - Display sources and confidence scores
   - Add query suggestions and history
   - Include feedback collection mechanism

### Part 3: Evaluation and Optimization (20 points)
**Systematically evaluate and improve your RAG system**

1. **Performance Evaluation** (10 points)
   - Create test dataset with questions and answers
   - Measure retrieval accuracy and generation quality
   - Benchmark response times and efficiency
   - Compare with baseline approaches

2. **Optimization Experiments** (10 points)
   - Test different chunk sizes and overlap strategies
   - Compare embedding models and similarity metrics
   - Experiment with prompt engineering variations
   - Implement and evaluate re-ranking approaches

## Technical Requirements
- Use proper document preprocessing
- Implement efficient retrieval pipeline
- Add comprehensive error handling
- Include logging and monitoring
- Create reproducible evaluation framework

## Deliverables
1. **Complete RAG Application**
   - Working end-to-end system
   - User-friendly interface
   - Documentation and setup instructions

2. **Evaluation Report** (600-800 words)
   - System architecture overview
   - Performance analysis and metrics
   - Optimization experiments and results
   - Challenges faced and solutions implemented
   - Future improvement recommendations

3. **Code Repository**
   - Clean, documented code
   - Configuration files and dependencies
   - Test cases and examples
   - Deployment instructions

## Evaluation Criteria
- **System Functionality (35%):** Complete working RAG pipeline
- **Technical Quality (25%):** Code organization and best practices
- **Domain Adaptation (20%):** Effectiveness for chosen use case
- **Evaluation Rigor (20%):** Systematic testing and optimization

## Bonus Features (5 points each)
- Multi-turn conversation support
- Streaming responses for better UX
- Advanced retrieval techniques (hybrid search, re-ranking)
- Custom evaluation metrics for domain
- Integration with external APIs or databases
- Multi-language support

## Resources
- LangChain RAG tutorials and examples
- Vector database integration guides
- Document processing libraries
- Evaluation frameworks and metrics
- Course code templates and datasets

## Tips for Success
1. Start simple and iterate systematically
2. Focus on data quality and preprocessing
3. Test with realistic user queries
4. Measure and optimize each component separately
5. Design evaluation metrics that matter for your use case
6. Document challenges and learnings throughout

## Submission Guidelines
- Submit via GitHub repository with clear README
- Include live demo video (3-5 minutes)
- Provide access to deployed application (optional)
- Submit evaluation report as PDF
- Include reflection on learning process 