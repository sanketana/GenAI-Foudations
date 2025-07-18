# Week 04: Homework Assignment

## Assignment: Building with Embeddings

### Part 1: Embedding Exploration (30 points)
**Deadline:** Before Week 05 class

1. **Generate and Analyze Embeddings** (15 points)
   - Create embeddings for 20+ text samples
   - Analyze embedding dimensions and properties
   - Compute pairwise similarities
   - Document interesting patterns found

2. **Similarity Analysis** (15 points)
   - Test different distance metrics (cosine, euclidean)
   - Compare results with human judgment
   - Identify edge cases and limitations
   - Create visualizations of similarity relationships

### Part 2: Semantic Search Implementation (40 points)
**Build a functional semantic search system**

1. **Data Preparation** (15 points)
   - Collect or use provided dataset (100+ documents)
   - Clean and preprocess text
   - Generate embeddings for all documents
   - Store embeddings efficiently

2. **Search Functionality** (25 points)
   - Implement query processing
   - Rank results by similarity
   - Return top-k most relevant documents
   - Handle edge cases (empty queries, no results)

**Technical Requirements:**
- Use OpenAI embeddings API
- Implement efficient similarity search
- Add query time optimization
- Include relevance scoring

### Part 3: Application Development (30 points)
**Create a user-friendly interface for your search system**

1. **Streamlit Interface** (20 points)
   - Search input with real-time results
   - Display ranked results with similarity scores
   - Allow filtering and sorting options
   - Show embedding visualizations

2. **Advanced Features** (10 points)
   - Query expansion suggestions
   - Result clustering or categorization
   - Performance metrics display
   - Export functionality

## Bonus Challenges (5 points each)
- Compare different embedding models
- Implement hybrid search (keyword + semantic)
- Add multi-language support
- Create embedding-based recommendation system
- Implement active learning for relevance feedback

## Deliverables
1. **Jupyter Notebook** with analysis and experiments
2. **Python application** with search functionality
3. **Streamlit interface** for user interaction
4. **Report** (500-750 words) covering:
   - Methodology and approach
   - Results and findings
   - Challenges encountered
   - Performance analysis
   - Future improvements

## Evaluation Criteria
- **Technical Implementation (40%):** Correctness and efficiency
- **Analysis Quality (30%):** Depth of exploration and insights
- **Interface Design (20%):** Usability and functionality
- **Documentation (10%):** Code quality and explanations

## Dataset Options
- Course-provided document collection
- Wikipedia articles on specific topics
- News articles or blog posts
- Scientific paper abstracts
- Product descriptions
- Custom dataset (requires approval)

## Resources
- OpenAI embeddings documentation
- NumPy and scikit-learn tutorials
- Streamlit embedding examples
- Office hours for technical support
- Discussion forum for questions

## Tips for Success
1. Start with small datasets for testing
2. Cache embeddings to avoid repeated API calls
3. Optimize for both accuracy and speed
4. Test with diverse query types
5. Consider user experience in interface design 