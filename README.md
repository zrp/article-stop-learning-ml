# Stop Learning ML - Start Building AI Systems

This repository contains three practical AI applications that demonstrate how to build real-world AI systems using modern tools and frameworks. These projects are designed to help you move from theoretical ML concepts to building functional AI applications.

## 📚 Article

This repository supports the article: **[Stop Learning ML - Start Building AI Systems](https://techblog.zrp.com.br/p/e3372ba1-caae-414f-8d53-4bd6c778be6e/)**

## 🚀 Projects Overview

### 1. **AI Code Reviewer** 
A code analysis tool that uses GPT-4 to review code for bugs, performance issues, style improvements, and security concerns. Supports multiple programming languages including Python, JavaScript, Java, Go, and Rust.

**Features:**
- Real-time code analysis with streaming responses
- Multi-language support
- Structured JSON output with detailed feedback
- Security and performance recommendations

### 2. **Document Q&A System**
A conversational AI system that allows you to upload PDF documents and ask questions about their content. Built with LangChain and FAISS for efficient document processing and retrieval.

**Features:**
- PDF document processing and text extraction
- Intelligent text chunking and embedding
- Conversational chat interface
- Streaming responses for better UX
- Persistent chat history

### 3. **AI Content Moderator**
A content moderation tool that uses Hugging Face's toxic-bert model to detect and flag inappropriate content in real-time.

**Features:**
- Toxicity detection and scoring
- Real-time content analysis
- Configurable blocking thresholds
- Clean, intuitive interface

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.11 or higher
- OpenAI API key (for Code Reviewer and Document Q&A)
- Internet connection (for model downloads)

### Installation

#### Option 1: Using Conda (Recommended)
```bash
# Clone the repository
git clone <repository-url>
cd document-qa

# Create and activate conda environment
conda env create -f environment.yaml
conda activate demo
```

#### Option 2: Using pip
```bash
# Clone the repository
git clone <repository-url>
cd document-qa

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Environment Setup

1. **Get your OpenAI API key:**
   - Visit [OpenAI Platform](https://platform.openai.com/api-keys)
   - Create a new API key
   - Copy the key for use in the applications

2. **Set your API key:**
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```

## 🎯 Running the Applications

### Code Reviewer
```bash
streamlit run code-reviewer.py
```
- Upload or paste your code
- Select the programming language
- Get instant feedback on bugs, performance, style, and security

### Document Q&A
```bash
streamlit run document-qa.py
```
- Upload a PDF document
- Start a conversation about the document content
- Ask questions and get AI-powered answers

### Content Moderator
```bash
streamlit run content-moderator.py
```
- Enter text to check for inappropriate content
- Get toxicity scores and moderation recommendations
- **Note:** First run will download the toxic-bert model (~500MB)

## 🔧 Technical Details

### Dependencies
- **Streamlit**: Web application framework
- **OpenAI**: GPT-4 API for code review and document Q&A
- **LangChain**: Framework for building LLM applications
- **FAISS**: Vector database for document similarity search
- **PyPDF2**: PDF text extraction
- **Transformers**: Hugging Face models for content moderation

### Architecture
- **Frontend**: Streamlit web interface
- **Backend**: Python with async processing
- **AI Models**: 
  - OpenAI GPT-4 for code review and Q&A
  - Hugging Face toxic-bert for content moderation
- **Vector Database**: FAISS for document embeddings

## 🎨 Features

### Code Reviewer
- Multi-language support (Python, JavaScript, Java, Go, Rust)
- Streaming responses for real-time feedback
- Structured JSON output with categorized feedback
- Security vulnerability detection
- Performance optimization suggestions

### Document Q&A
- PDF document processing
- Intelligent text chunking (1000 chars with 200 char overlap)
- OpenAI embeddings for semantic search
- Conversational chat interface
- Persistent session state

### Content Moderator
- Real-time toxicity detection
- Configurable blocking thresholds
- Clean, intuitive interface
- Fast inference with optimized models

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests to improve these applications.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- OpenAI for providing the GPT-4 API
- Hugging Face for the toxic-bert model
- Streamlit for the web framework
- LangChain for the LLM orchestration framework

---

**If you found this repository helpful, please give it a ⭐ star!**
