# University Policy Assistant 🎓

A modern AI-powered conversational assistant that helps students, faculty, and staff get instant answers to questions about university policies. Built with **Retrieval Augmented Generation (RAG)**, this system retrieves accurate information from university documents and uses a local LLM to provide contextual, grounded responses.

---

## 📋 Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Key Modules](#key-modules)
- [Development](#development)
- [Contributing](#contributing)

---

## ✨ Features

### User Interface
- **Interactive Chat Interface**: Real-time conversation with AI assistant
- **Citation Support**: Every answer includes sources from university documents
- **Session Management**: Persistent conversation history per user
- **Typing Indicators**: Visual feedback while AI is processing
- **Responsive Design**: Works on desktop and mobile devices

### AI Capabilities
- **RAG Pipeline**: Combines document retrieval with LLM generation for accurate answers
- **Conversational Memory**: Remembers context across multiple messages in a session
- **Safety Checks**: Escalation mechanism for out-of-scope queries
- **Confidence Scoring**: Indicates reliability of each answer
- **Question Rewriting**: Improves query understanding through semantic analysis

### Administrative Features
- **Policy Upload Panel**: Easy bulk upload of university policy documents
- **Failed Query Tracking**: Monitor and review queries the system couldn't answer
- **Metrics Dashboard**: Real-time statistics on chat volume and performance
- **Ticket Management**: Track escalated queries requiring human review

---

## 🏗️ Architecture

### System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        FRONTEND (React)                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐           │
│  │ Chat Page    │  │ Admin Page   │  │  Sidebar     │           │
│  └──────────────┘  └──────────────┘  └──────────────┘           │
│  Components: ChatWindow, MessageBubble, AdminWindow             │
│  Tech: React 19, Vite, Tailwind CSS, Framer Motion             │
└─────────────────────────────────────────────────────────────────┘
                              ↓ HTTP/JSON
┌─────────────────────────────────────────────────────────────────┐
│               BACKEND API (FastAPI, Python)                      │
│                                                                   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │              API Routes Layer                            │   │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐                 │   │
│  │  │ Chat    │  │ Admin   │  │ Session │                 │   │
│  │  │ Routes  │  │ Routes  │  │ Routes  │                 │   │
│  │  └─────────┘  └─────────┘  └─────────┘                 │   │
│  └──────────────────────────────────────────────────────────┘   │
│                              ↓                                    │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │           Service Layer (Business Logic)                 │   │
│  │  ┌──────────────┐  ┌─────────────┐  ┌──────────────┐    │   │
│  │  │ Chat Service │  │ Doc Service │  │Sess Service │    │   │
│  │  └──────────────┘  └─────────────┘  └──────────────┘    │   │
│  └──────────────────────────────────────────────────────────┘   │
│                              ↓                                    │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │           RAG Pipeline (Conversational)                  │   │
│  │                                                          │   │
│  │  ┌─────────────────────────────────────────────────┐    │   │
│  │  │ Safe Conversational RAG / Conversational RAG    │    │   │
│  │  │ ┌─────────────┐  ┌────────────┐                │    │   │
│  │  │ │ Conversation│  │   Query    │                │    │   │
│  │  │ │  Handler    │  │  Rewriter  │                │    │   │
│  │  │ └─────────────┘  └────────────┘                │    │   │
│  │  └─────────────────────────────────────────────────┘    │   │
│  │                 ↓         ↓         ↓                    │   │
│  │  ┌─────────────────┐ ┌──────────┐ ┌───────────────┐    │   │
│  │  │   Retrieval     │ │Generation│ │ Reliability   │    │   │
│  │  │   (FAISS RAG)   │ │ (LLM)    │ │ (Safety)      │    │   │
│  │  └─────────────────┘ └──────────┘ └───────────────┘    │   │
│  │     ↓                    ↓                 ↓             │   │
│  └──────────────────────────────────────────────────────────┘   │
│                              ↓                                    │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │        Data Layer (Persistence & Storage)                │   │
│  │  ┌──────────────┐  ┌────────────┐  ┌──────────────┐    │   │
│  │  │ FAISS Vector │  │  Session   │  │   Groq       │    │   │
│  │  │   Store      │  │   Store    │  │   (Llama 3)  │    │   │
│  │  └──────────────┘  └────────────┘  └──────────────┘    │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│              External Services & Infrastructure                  │
│  ┌──────────────────┐  ┌────────────────┐  ┌─────────────────┐ │
│  │ Groq API         │  │ Vector DB      │  │ Document Store  │ │
│  │ (Llama 3 Models) │  │ (FAISS)        │  │ (Processed Docs)│ │
│  └──────────────────┘  └────────────────┘  └─────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

### Data Flow: Query Processing

```
User Input (Chat Message)
        ↓
Session Context Retrieval
        ↓
Query Rewriting (Semantic Enhancement)
        ↓
Vector Similarity Search (FAISS)
        ↓
Document Chunk Retrieval
        ↓
Prompt Construction (LLM)
        ↓
Cloud LLM Inference (Groq - Llama 3)
        ↓
Response Formatting
        ↓
Confidence & Safety Checks
        ↓
User Response + Citations
```

---

## 🛠️ Tech Stack

### Backend
| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Framework** | FastAPI | Modern async web framework |
| **LLM** | Groq (Llama 3) | Fast cloud language model inference |
| **Embeddings** | Sentence Transformers | Document and query embeddings |
| **Vector DB** | FAISS (CPU) | Fast similarity search |
| **RAG** | LangChain | Orchestration and abstractions |
| **PDF Processing** | PyPDF, PDFPlumber | Extract text from documents |
| **Async** | Python async/await | Concurrent request handling |

### Frontend
| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Framework** | React 19 | UI component library |
| **Build Tool** | Vite | Fast development server & bundling |
| **Styling** | Tailwind CSS v4 | Utility-first CSS framework |
| **Animation** | Framer Motion | Smooth UI animations |
| **HTTP** | Axios | API communication |
| **Linting** | ESLint | Code quality |

### DevOps & Storage
- **Vector Storage**: `data/vectorstore/faiss_index/`
- **Document Storage**: `data/raw/` (university policies)
- **Processed Data**: `data/processed/`
- **Logs**: `data/logs/` (failed_queries.json)

---

## 📁 Project Structure

```
Project/
├── Backend/                           # Python FastAPI backend
│   ├── app/
│   │   ├── api/                      # API endpoints layer
│   │   │   ├── main.py              # FastAPI app initialization
│   │   │   ├── chat_api.py          # Chat endpoint handlers
│   │   │   ├── qa_api.py            # Q&A endpoint handlers
│   │   │   ├── safe_chat_api.py     # Safe chat with escalation
│   │   │   ├── routes/
│   │   │   │   ├── chat.py          # Chat routes
│   │   │   │   ├── admin.py         # Admin routes
│   │   │   │   └── session.py       # Session routes
│   │   │   └── schemas/             # Pydantic request/response models
│   │   │       ├── chat.py
│   │   │       └── session.py
│   │   │
│   │   ├── services/                # Business logic layer
│   │   │   ├── chat_service.py      # Chat processing
│   │   │   ├── document_service.py  # Document management
│   │   │   └── session_service.py   # Session management
│   │   │
│   │   └── rag/                     # RAG pipeline modules
│   │       ├── pipeline/            # End-to-end RAG pipelines
│   │       │   ├── rag_pipeline.py
│   │       │   ├── conversational_rag.py
│   │       │   └── safe_conversational_rag.py
│   │       │
│   │       ├── retrieval/           # Document retrieval
│   │       │   └── retriever.py    # FAISS vector search
│   │       │
│   │       ├── generation/          # LLM response generation
│   │       │   ├── llm.py          # Ollama integration
│   │       │   ├── generator.py    # Response generation
│   │       │   └── prompt.py       # Prompt templates
│   │       │
│   │       ├── ingestion/           # Document processing pipeline
│   │       │   ├── config.py       # Pipeline configuration
│   │       │   ├── pipeline.py     # Orchestration
│   │       │   ├── loaders/        # Document loaders
│   │       │   ├── processing/     # Data preprocessing
│   │       │   │   ├── cleaner.py      # Text cleaning
│   │       │   │   ├── chunker.py      # Text chunking
│   │       │   │   ├── categorizer.py  # Category assignment
│   │       │   │   └── metadata.py     # Metadata extraction
│   │       │   ├── embedding/      # Embedding generation
│   │       │   └── vectorstore/    # Vector store operations
│   │       │
│   │       ├── conversation/        # Conversation management
│   │       │   ├── chat_handler.py  # Message handling
│   │       │   ├── memory.py        # Conversation memory
│   │       │   ├── session_store.py # Session persistence
│   │       │   └── rewritter.py     # Query rewriting
│   │       │
│   │       └── reliability/         # Response quality & safety
│   │           ├── detector.py      # Error detection
│   │           ├── escalation.py    # Escalation logic
│   │           ├── fallback.py      # Fallback strategies
│   │           └── logger.py        # Event logging
│   │
│   ├── data/                        # Data storage
│   │   ├── raw/                    # Original policy documents
│   │   │   ├── academic_handbook_2024.txt
│   │   │   ├── attendance_policy.txt
│   │   │   ├── disciplinary_policy.txt
│   │   │   ├── examination_regulations_2024.txt
│   │   │   └── scholarship_policy.txt
│   │   ├── processed/              # Cleaned/chunked documents
│   │   ├── vectorstore/            # FAISS indices
│   │   │   └── faiss_index/
│   │   └── logs/                   # Application logs
│   │       └── failed_queries.json
│   │
│   ├── tests/                      # Unit and integration tests
│   ├── scripts/                    # Utility scripts
│   ├── notebooks/                  # Jupyter notebooks (analysis)
│   ├── requirements.txt            # Python dependencies
│   └── README.md                   # Backend README
│
├── frontend/                        # React + Vite frontend
│   ├── src/
│   │   ├── main.jsx               # App entry point
│   │   ├── App.jsx                # Root component
│   │   ├── App.css                # Global styles
│   │   │
│   │   ├── pages/
│   │   │   └── ChatPage.jsx       # Main chat interface
│   │   │
│   │   ├── components/            # Reusable components
│   │   │   ├── ChatWindow.jsx     # Chat conversation area
│   │   │   ├── MessageBubble.jsx  # Message display
│   │   │   ├── Sidebar.jsx        # Navigation sidebar
│   │   │   ├── AdminWindow.jsx    # Admin panel
│   │   │   ├── SourceViewer.jsx   # Citation source viewer
│   │   │   └── TypingIndicator.jsx # Loading indicator
│   │   │
│   │   ├── admin/                 # Admin pages
│   │   │   ├── AdminPage.jsx      # Admin dashboard
│   │   │   ├── UploadPanel.jsx    # Document upload
│   │   │   ├── FailedQueries.jsx  # Failed query tracking
│   │   │   ├── MetricsPanel.jsx   # Analytics
│   │   │   └── TicketsPanel.jsx   # Escalation tickets
│   │   │
│   │   ├── hooks/
│   │   │   └── useChat.js         # Chat state management
│   │   │
│   │   ├── services/
│   │   │   └── api.js             # API client (axios)
│   │   │
│   │   ├── assets/                # Images, icons
│   │   └── index.css              # Global styles
│   │
│   ├── public/                    # Static assets
│   ├── package.json               # NPM dependencies
│   ├── vite.config.js            # Vite configuration
│   ├── tailwind.config.js         # Tailwind configuration
│   ├── eslint.config.js           # ESLint configuration
│   └── README.md                  # Frontend README
│
└── README.md                       # This file
```

---

## 📋 Prerequisites

- **Python 3.10+** (for backend)
- **Node.js 18+** (for frontend)
- **npm or yarn** (package manager)
- **Ollama** with Mistral model installed
  - Install: [ollama.ai](https://ollama.ai)
  - Pull model: `ollama pull mistral`

### Recommended System Requirements
- **RAM**: 8GB minimum (16GB for smooth operation)
- **Storage**: 10GB for models and data
- **CPU**: Multi-core processor recommended

---

## 🚀 Installation

### 1. Clone the Repository
```bash
cd /path/to/your/workspace
# Workspace is already set up at: e:\College\TY\GenAi\Project
```

### 2. Backend Setup

```bash
cd Backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

**Backend Dependencies Overview:**
- `langchain` & `langchain-community`: RAG framework
- `faiss-cpu`: Vector similarity search
- `sentence-transformers`: Text embeddings
- `pypdf` & `pdfplumber`: PDF parsing
- `tiktoken`: Token counting
- `python-dotenv`: Environment variable management

### 3. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install
```

**Frontend Dependencies Overview:**
- `react` & `react-dom`: UI framework
- `vite`: Build tool
- `tailwindcss`: Styling
- `framer-motion`: Animations
- `axios`: HTTP client

---

## ⚙️ Configuration

### Backend Configuration

Create a `.env` file in the `Backend/` directory:

```env
# LLM Configuration
OLLAMA_MODEL=mistral
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_TEMPERATURE=0.2

# Vector Store Configuration
FAISS_INDEX_PATH=./data/vectorstore/faiss_index

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000

# CORS Configuration (for local development)
ALLOWED_ORIGINS=http://localhost:5173,http://127.0.0.1:5173

# Document Processing
RAW_DOCS_PATH=./data/raw
PROCESSED_DOCS_PATH=./data/processed
LOGS_PATH=./data/logs
```

### Frontend Configuration

The frontend is pre-configured in `src/services/api.js`:

```javascript
const API_BASE_URL = 'http://localhost:8000';
```

Modify if your backend runs on a different host/port.

---

## 🏃 Running the Application

### Step 1: Start Ollama

```bash
# Terminal 1: Start Ollama service
ollama serve

# In another terminal, ensure Mistral model is available:
ollama pull mistral
```

Ollama will be available at `http://localhost:11434`

### Step 2: Start Backend

```bash
# Terminal 2: Navigate to Backend
cd Backend

# Activate virtual environment (if not already active)
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Run FastAPI server
python -m uvicorn app.api.main:app --reload --host 0.0.0.0 --port 8000
```

Backend will be available at `http://localhost:8000`
- **API Docs**: http://localhost:8000/docs (Swagger UI)
- **Alternative Docs**: http://localhost:8000/redoc

### Step 3: Start Frontend

```bash
# Terminal 3: Navigate to frontend
cd frontend

# Start development server
npm run dev
```

Frontend will be available at `http://localhost:5173`

---

## 📚 API Documentation

### Base URL
```
http://localhost:8000
```

### Chat Endpoints

#### 1. Send Chat Message
```http
POST /api/chat/send
Content-Type: application/json

{
  "session_id": "user123",
  "message": "What is the attendance policy?"
}
```

**Response:**
```json
{
  "answer": "According to the attendance policy...",
  "citations": [
    {
      "source": "attendance_policy.txt",
      "chunk_id": 5,
      "content": "..."
    }
  ],
  "confidence": 0.95,
  "escalation": false
}
```

#### 2. Get Session History
```http
GET /api/session/{session_id}/history
```

**Response:**
```json
{
  "session_id": "user123",
  "messages": [
    {
      "role": "user",
      "content": "What is the attendance policy?",
      "timestamp": "2024-03-22T10:30:00Z"
    },
    {
      "role": "assistant",
      "content": "According to...",
      "timestamp": "2024-03-22T10:30:05Z"
    }
  ]
}
```

### Admin Endpoints

#### 1. Upload Documents
```http
POST /api/admin/upload
Content-Type: multipart/form-data

file: <binary_pdf_or_txt>
```

#### 2. Get Failed Queries
```http
GET /api/admin/failed-queries
```

#### 3. Get Metrics
```http
GET /api/admin/metrics
```

#### 4. Create Support Ticket
```http
POST /api/admin/tickets
Content-Type: application/json

{
  "query": "Question text",
  "reason": "escalation_reason",
  "session_id": "user123"
}
```

---

## 🔑 Key Modules Deep Dive

### 1. **RAG Pipeline** (`app/rag/pipeline/`)

**Conversational RAG** - Handles multi-turn conversations with memory

```python
# Flow:
Query + Session History → Query Rewriting → Vector Search → 
Document Retrieval → Prompt Construction → LLM Generation → 
Response Formatting & Safety Checks
```

**Components:**
- `chat_handler.py`: Manages conversation flow
- `memory.py`: Stores conversation context
- `rewritter.py`: Rewrites queries for better retrieval

### 2. **Retrieval System** (`app/rag/retrieval/`)

Uses FAISS for fast semantic similarity search:
```python
# Query → Embedding → Vector Search → Ranked Results
```

**Key Features:**
- Fast similarity search (optimal for large document sets)
- Configurable top-k retrieval
- Metadata filtering support

### 3. **Generation** (`app/rag/generation/`)

Integrates with Ollama for local LLM inference:
```python
# Prompt + Context → Ollama/Mistral → Structured Response
```

**Temperature**: 0.2 (low) for factual, consistent responses

### 4. **Document Ingestion** (`app/rag/ingestion/`)

Complete document processing pipeline:

```
Raw Documents
    ↓
Loaders (PDF/Text extraction)
    ↓
Cleaners (Text normalization)
    ↓
Chunkers (Semantic segmentation)
    ↓
Embedders (Vector generation)
    ↓
Vector Store (FAISS indexing)
```

### 5. **Reliability & Safety** (`app/rag/reliability/`)

Ensures response quality and handles out-of-scope queries:

- **Detector**: Identifies low-confidence responses
- **Escalation**: Routes queries to human reviewers
- **Fallback**: Provides alternative response strategies
- **Logger**: Tracks failed queries for improvement

---

## 👨‍💻 Development

### Run Tests
```bash
cd Backend
pytest tests/
```

### Code Quality
```bash
# Backend: Format code
black app/

# Backend: Lint
pylint app/

# Frontend: Lint
npm run lint
```

### Building for Production

**Backend:**
```bash
cd Backend
gunicorn app.api.main:app --workers 4 --bind 0.0.0.0:8000
```

**Frontend:**
```bash
cd frontend
npm run build
# Output: dist/
```

### Debugging

**Backend**: 
- Check `data/logs/failed_queries.json` for failed requests
- Use FastAPI Swagger UI: http://localhost:8000/docs

**Frontend**: 
- Open browser DevTools (F12)
- Check Network tab for API calls
- Check Console for errors

---

## 📊 Performance Metrics

### Expected Response Times (Local Setup)
- **Query Rewriting**: ~100ms
- **Vector Search**: ~50-200ms (depends on index size)
- **LLM Inference**: ~2-5 seconds
- **Total End-to-End**: ~3-6 seconds

### Optimization Tips
1. **Reduce chunk size** for faster retrieval
2. **Increase FAISS index partitions** for larger doc sets
3. **Use GPU acceleration** if available
4. **Cache embeddings** for repeated queries

---

## � Deployment

### Backend Deployment on Render

1. **Prerequisites**:
   - Groq API key (get from [Groq Console](https://console.groq.com/keys))
   - Render account (free tier available)

2. **Deploy to Render**:
   ```bash
   # Option 1: Using Render Dashboard
   # 1. Go to https://render.com
   # 2. Connect your GitHub repository
   # 3. Create a new Web Service
   # 4. Set build command: pip install -r requirements.txt
   # 5. Set start command: uvicorn app.api.main:app --host 0.0.0.0 --port $PORT

   # Option 2: Using render.yaml (Blueprints)
   # The render.yaml file is already configured in the Backend directory
   ```

3. **Environment Variables** (set in Render dashboard):
   ```
   GROQ_API_KEY=your_groq_api_key_here
   GROQ_MODEL=llama3-8b-8192
   GROQ_TEMPERATURE=0.2
   ALLOWED_ORIGINS=https://your-frontend-domain.onrender.com,https://your-backend-domain.onrender.com
   ```

4. **Frontend Deployment**:
   ```bash
   cd frontend
   npm run build
   # Deploy the dist/ folder to any static hosting service (Netlify, Vercel, etc.)
   ```

### Alternative Deployment Options

- **Railway**: Supports Ollama (if you want to keep local LLM)
- **DigitalOcean App Platform**: Good for full-stack deployments
- **AWS/GCP/Azure**: For enterprise deployments

### Cost Estimation (Render Free Tier)
- **Backend**: ~$0/month (750 hours free)
- **Frontend**: ~$0/month (static hosting)
- **Groq**: ~$0.10-0.20/1M tokens (very affordable)

---

## �🚨 Troubleshooting

### Ollama Connection Error
```
Error: Failed to connect to Ollama at http://localhost:11434
```
**Solution**: Ensure Ollama is running (`ollama serve`)

### CORS Error in Frontend
```
Access to XMLHttpRequest blocked by CORS
```
**Solution**: Check `ALLOWED_ORIGINS` in Backend `.env` and FastAPI CORS middleware

### Vector Store Not Found
```
FileNotFoundError: faiss_index not found
```
**Solution**: Run document ingestion pipeline or ingest sample documents via admin panel

### Out of Memory
```
MemoryError: Unable to allocate memory
```
**Solution**: 
- Reduce chunk size
- Reduce context window
- Use GPU (if available)

---

## 📝 License

[Add your license here]

---

## 👥 Contributors

- Development Team - Bachelor's Degree in AI

---

## 📧 Support

For issues, questions, or improvements:
- Create an issue in the project repository
- Contact: [your contact info]

---

## 🔄 Update Log

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2024-03-22 | Initial release |

---

**Last Updated**: March 22, 2024
