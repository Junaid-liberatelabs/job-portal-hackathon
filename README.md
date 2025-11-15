# CareerIn - AI-Powered Youth Employment Platform

A comprehensive, production-ready job portal platform with AI-powered recommendations, featuring a main user platform, dedicated admin dashboard, and intelligent career guidance system.

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Architecture](#-architecture)
- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Quick Start](#-quick-start)
- [Installation & Setup](#-installation--setup)
- [Configuration](#-configuration)
- [API Documentation](#-api-documentation)
- [Development Guide](#-development-guide)
- [Deployment](#-deployment)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

## 🚀 Project Overview

CareerIn is a full-stack employment platform designed to connect job seekers with opportunities through AI-powered matching, personalized career guidance, and comprehensive learning resources. The platform consists of three integrated components:

1. **Backend API** (Port 8000) - FastAPI-based RESTful API with PostgreSQL and pgvector
2. **User Platform** (Port 3000) - Nuxt 4 frontend for job seekers
3. **Admin Dashboard** (Port 3001) - Nuxt 4 admin interface for job and applicant management

### Key Capabilities

- **AI-Powered Job Matching**: Hybrid recommendation system using TF-IDF and vector embeddings
- **Career Guidance**: AI chatbot (Oppy) for personalized career advice
- **Skill Analysis**: Automated CV parsing and skill extraction
- **Career Roadmap**: Visual career progression planning with interactive graphs
- **Skill Gap Analysis**: AI-generated reports identifying skill deficiencies
- **CV Export**: Professional CV generation in PDF/LaTeX formats
- **Learning Resources**: Curated catalog of courses and educational materials

## 🏗️ Architecture

### System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    CareerIn Platform                         │
└─────────────────────────────────────────────────────────────┘

┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│  User Platform   │    │ Admin Dashboard  │    │   Backend API    │
│   Port: 3000     │───▶│   Port: 3001     │───▶│   Port: 8000     │
│                  │    │                  │    │                  │
│  - Landing Page  │    │  - Job CRUD      │    │  - FastAPI       │
│  - Job Browsing  │    │  - Applicants    │    │  - PostgreSQL    │
│  - Applications  │    │  - Statistics    │    │  - pgvector      │
│  - Profile       │    │  - Management    │    │  - LangChain      │
│  - Chat (Oppy)   │    │                  │    │  - OpenAI        │
└──────────────────┘    └──────────────────┘    └──────────────────┘
         │                       │                         │
         │                       │                         │
         └───────────────────────┴─────────────────────────┘
                                 │
                          ┌──────▼──────┐
                          │  PostgreSQL  │
                          │  + pgvector  │
                          │  Port: 5432  │
                          └──────────────┘
```

### Project Structure

```
job-portal-hackathon/
├── Backend/                          # FastAPI Backend
│   ├── app/
│   │   ├── api/
│   │   │   ├── endpoints/           # API route handlers
│   │   │   │   ├── auth.py         # Authentication
│   │   │   │   ├── jobs.py         # Job management
│   │   │   │   ├── resources.py    # Learning resources
│   │   │   │   ├── applications.py # Job applications
│   │   │   │   ├── recommendations.py # AI recommendations
│   │   │   │   ├── skill_analysis.py # CV skill extraction
│   │   │   │   ├── skill_gap_analysis.py # Skill gap reports
│   │   │   │   ├── career_roadmap.py # Career planning
│   │   │   │   ├── cv_export.py    # CV generation
│   │   │   │   └── agen_chat.py    # AI chatbot
│   │   │   └── schemas/            # Pydantic models
│   │   ├── db/
│   │   │   ├── model/              # SQLAlchemy models
│   │   │   └── crud/               # Database operations
│   │   ├── llm/
│   │   │   ├── workflow/           # LangChain workflows
│   │   │   └── prompts/            # LLM prompt templates
│   │   ├── services/               # Business logic
│   │   └── core/                   # Configuration
│   └── main.py                     # Application entry point
│
├── FrontEnd/                        # User Platform (Nuxt 4)
│   ├── app/
│   │   ├── pages/                  # File-based routing
│   │   │   ├── index.vue          # Landing page
│   │   │   ├── dashboard.vue       # User dashboard
│   │   │   ├── jobs/              # Job listings
│   │   │   ├── resources/         # Learning resources
│   │   │   ├── profile/           # User profile
│   │   │   ├── chat/              # AI chatbot (Oppy)
│   │   │   ├── skill-gap-analysis.vue
│   │   │   └── career-roadmap.vue
│   │   ├── components/            # Vue components
│   │   ├── composables/           # Reusable logic
│   │   ├── stores/                # Pinia stores
│   │   └── layouts/               # Page layouts
│   └── nuxt.config.ts
│
├── AdminDashboard/                  # Admin Interface (Nuxt 4)
│   ├── pages/
│   │   └── index.vue              # Main dashboard
│   ├── components/
│   │   ├── JobsTable.vue          # Jobs listing
│   │   ├── CreateJobModal.vue     # Job CRUD
│   │   ├── ApplicantsModal.vue   # Applicant viewer
│   │   └── StatsCard.vue          # Statistics
│   ├── composables/               # API integration
│   └── nuxt.config.ts
│
└── docker-compose.yml              # Docker configuration
```

## ✨ Features

### User Platform Features

#### Core Functionality
- **User Authentication**: Secure JWT-based authentication with registration and login
- **Profile Management**: Comprehensive profile with skills, education, experience, and career preferences
- **Job Browsing**: Filterable job listings with search, pagination, and sorting
- **Job Applications**: Apply to jobs with automatic skill matching
- **Learning Resources**: Curated catalog of courses, tutorials, and educational materials
- **Dashboard**: Personalized overview with recommendations and statistics

#### AI-Powered Features
- **Job Recommendations**: Hybrid recommendation system (TF-IDF + vector embeddings)
- **Skill Matching**: Automatic skill-based job matching with percentage scores
- **CV Analysis**: Upload CV to automatically extract and add skills to profile
- **Skill Gap Analysis**: AI-generated reports identifying missing skills for target roles
- **Career Roadmap**: Interactive visual roadmap with nodes and connections (vis.js)
- **AI Chatbot (Oppy)**: Multi-threaded conversational AI for career guidance
  - Streaming responses with character-by-character display
  - Thread management (create, view, delete conversations)
  - Persistent conversation history
- **CV Export**: Generate professional CVs in PDF or LaTeX format

#### User Experience
- **Landing Page**: Immersive hero section with Three.js particle effects
- **Smooth Scrolling**: Lenis-powered smooth scroll animations
- **Responsive Design**: Mobile-first design with Tailwind CSS
- **Real-time Updates**: Live data synchronization with backend

### Admin Dashboard Features

#### Dashboard Overview
- **Real-time Statistics**: Total jobs, applications, averages, and trends
- **Data Cards**: 8+ insightful metrics including:
  - Total jobs and applications
  - Average applicants per job
  - Most popular job type
  - Recent jobs and resources
  - Top tags and categories
  - Free vs paid resources

#### Job Management
- **Create Jobs**: Full-featured job creation form with all fields
- **Edit Jobs**: Inline editing with pre-filled forms
- **Delete Jobs**: Safe deletion with confirmation dialogs
- **View Applicants**: Detailed applicant information per job
- **Pagination**: Client-side pagination (5 items per page)

#### Applicant Management
- **Applicant Details**: View name, email, skills, career goals
- **Contact Applicants**: Direct email links for communication
- **Application Tracking**: View application dates and history

### Backend API Features

#### Authentication & Authorization
- JWT token-based authentication
- Password hashing with bcrypt
- Protected routes with dependency injection
- User session management

#### AI & ML Services
- **Embedding Service**: OpenAI embeddings for semantic search
- **Recommendation Engine**: Hybrid TF-IDF + vector similarity
- **LangChain Workflows**: Multi-agent AI systems for:
  - Skill extraction from CVs
  - Skill gap analysis
  - Career roadmap generation
  - Conversational AI (Oppy chatbot)

#### Data Management
- PostgreSQL with pgvector extension for vector storage
- SQLAlchemy ORM for database operations
- Efficient CRUD operations with proper indexing
- Database migrations and seeding

## 🔧 Technology Stack

### Backend
- **Framework**: FastAPI (Python 3.11+)
- **Database**: PostgreSQL 15+ with pgvector extension
- **ORM**: SQLAlchemy 2.0
- **Authentication**: JWT (python-jose, passlib)
- **AI/ML**: 
  - LangChain & LangGraph for agent workflows
  - OpenAI API for embeddings and LLM
  - Vector similarity search with pgvector
- **PDF Processing**: PyPDF2 for CV parsing
- **LaTeX**: pdflatex for CV generation
- **Validation**: Pydantic v2 for data validation

### Frontend (User Platform)
- **Framework**: Nuxt 4 (Vue 3 Composition API)
- **Styling**: Tailwind CSS with custom design system
- **State Management**: Pinia
- **3D Graphics**: Three.js
- **Smooth Scrolling**: Lenis
- **Charts**: ECharts (vue-echarts)
- **Animations**: Anime.js
- **Icons**: Heroicons
- **Type Safety**: TypeScript

### Admin Dashboard
- **Framework**: Nuxt 4 (Vue 3)
- **Styling**: Tailwind CSS
- **Type Safety**: TypeScript
- **Icons**: Heroicons

### Development Tools
- **Package Management**: npm (Frontend), pip/uv (Backend)
- **Version Control**: Git
- **API Documentation**: FastAPI auto-generated OpenAPI/Swagger
- **Code Quality**: TypeScript, ESLint, Prettier

## 🚀 Quick Start

### Prerequisites

- **Python 3.11+** with pip or uv
- **Node.js 18+** with npm
- **PostgreSQL 15+** with pgvector extension
- **OpenAI API Key** (for AI features)
- **LaTeX Distribution** (for CV export - optional)

### 1. Clone Repository

```bash
git clone <repository-url>
cd job-portal-hackathon
```

### 2. Backend Setup

```bash
cd Backend

# Install dependencies (using uv recommended)
uv pip install -r requirements.txt
# OR
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your database and API keys

# Initialize database
python -m app.db.init_db

# Seed database (optional)
python seed_db.py

# Start backend server
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Backend will be available at: **http://localhost:8000**
API docs at: **http://localhost:8000/docs**

### 3. User Platform Setup

```bash
cd FrontEnd

# Install dependencies
npm install

# Set up environment variables
cp .env.example .env
# Edit .env with API base URL

# Start development server
npm run dev
```

User platform will be available at: **http://localhost:3000**

### 4. Admin Dashboard Setup

```bash
cd AdminDashboard

# Install dependencies
npm install

# Set up environment variables
cp .env.example .env
# Edit .env with API base URL

# Start development server
npm run dev
```

Admin dashboard will be available at: **http://localhost:3001**

## 📦 Installation & Setup

### Detailed Backend Installation

#### 1. Database Setup

```bash
# Install PostgreSQL (if not installed)
# Ubuntu/Debian:
sudo apt-get install postgresql postgresql-contrib

# macOS:
brew install postgresql

# Windows: Download from postgresql.org

# Install pgvector extension
# Ubuntu/Debian:
sudo apt-get install postgresql-15-pgvector

# macOS:
brew install pgvector

# Create database
createdb careerin_db

# Connect and enable extension
psql careerin_db
CREATE EXTENSION vector;
\q
```

#### 2. Backend Dependencies

```bash
cd Backend

# Using uv (recommended - faster)
uv pip install -r requirements.txt

# OR using pip
pip install -r requirements.txt

# Key dependencies:
# - fastapi
# - uvicorn[standard]
# - sqlalchemy
# - psycopg2-binary
# - pgvector
# - langchain
# - langchain-openai
# - langgraph
# - openai
# - python-jose[cryptography]
# - passlib[bcrypt]
# - pydantic
# - python-multipart
```

#### 3. Environment Configuration

Create `Backend/.env`:

```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/careerin_db

# Security
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# OpenAI
OPENAI_API_KEY=your-openai-api-key

# Application
PROJECT_NAME=CareerIn
VERSION=1.0.0
DEBUG=True
ENVIRONMENT=development
```

### Detailed Frontend Installation

#### 1. User Platform

```bash
cd FrontEnd

# Install dependencies
npm install

# Key dependencies:
# - nuxt@^4.0.0
# - @nuxtjs/tailwindcss
# - pinia
# - @pinia/nuxt
# - three
# - lenis
# - echarts
# - vue-echarts
# - animejs
# - @heroicons/vue
```

#### 2. Environment Configuration

Create `FrontEnd/.env`:

```env
NUXT_PUBLIC_API_BASE=http://localhost:8000
```

#### 3. Admin Dashboard

```bash
cd AdminDashboard

# Install dependencies
npm install

# Environment configuration
# Create AdminDashboard/.env:
NUXT_PUBLIC_API_BASE=http://localhost:8000
```

## ⚙️ Configuration

### Backend Configuration

#### Database Connection

Edit `Backend/app/core/config.py` or use environment variables:

```python
DATABASE_URL=postgresql://user:password@localhost:5432/careerin_db
```

#### CORS Settings

Edit `Backend/main.py`:

```python
allow_origins=[
    "http://localhost:3000",  # User platform
    "http://localhost:3001",  # Admin dashboard
    "http://localhost:8000",  # Backend (if needed)
]
```

#### OpenAI Configuration

Set `OPENAI_API_KEY` in environment variables or `.env` file.

### Frontend Configuration

#### API Base URL

Edit `FrontEnd/nuxt.config.ts` or `AdminDashboard/nuxt.config.ts`:

```typescript
runtimeConfig: {
  public: {
    apiBase: process.env.NUXT_PUBLIC_API_BASE || 'http://localhost:8000'
  }
}
```

#### Port Configuration

Edit `package.json` scripts:

```json
{
  "scripts": {
    "dev": "nuxt dev --port 3000"  // User platform
    // OR
    "dev": "nuxt dev --port 3001"  // Admin dashboard
  }
}
```

## 📚 API Documentation

### Authentication Endpoints

#### Register User
```http
POST /auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "securepassword",
  "full_name": "John Doe"
}
```

#### Login
```http
POST /auth/login
Content-Type: application/x-www-form-urlencoded

username=user@example.com&password=securepassword
```

Response includes `access_token` for authenticated requests.

### Job Endpoints

#### List Jobs
```http
GET /jobs/?skip=0&limit=100&job_type=FULL_TIME&experience_level=ENTRY&skills=Python,React
Authorization: Bearer <token>
```

#### Get Job Details
```http
GET /jobs/{job_id}
Authorization: Bearer <token>
```

#### Create Job (Admin)
```http
POST /jobs/
Authorization: Bearer <token>
Content-Type: application/json

{
  "title": "Frontend Developer",
  "company": "Tech Corp",
  "description": "We are looking for...",
  "job_type": "FULL_TIME",
  "required_skills": ["React", "TypeScript"],
  "recommended_experience_level": "ENTRY"
}
```

### Recommendation Endpoints

#### Get Job Recommendations
```http
GET /recommendations/jobs?limit=10
Authorization: Bearer <token>
```

Returns jobs ranked by similarity score (0-1).

#### Get Resource Recommendations
```http
GET /recommendations/resources?limit=10
Authorization: Bearer <token>
```

### Application Endpoints

#### Apply to Job
```http
POST /applications/
Authorization: Bearer <token>
Content-Type: application/json

{
  "job_id": "job-uuid"
}
```

#### Get User Applications
```http
GET /applications/
Authorization: Bearer <token>
```

#### Get Job Applicants (Admin)
```http
GET /applications/job/{job_id}/applicants
Authorization: Bearer <token>
```

### AI-Powered Endpoints

#### CV Skill Analysis
```http
POST /skill-analysis/analyze
Authorization: Bearer <token>
Content-Type: multipart/form-data

file: <PDF file>
```

#### Skill Gap Analysis
```http
POST /skill-gap-analysis/skill-gap-analysis
Authorization: Bearer <token>
Content-Type: application/json

{
  "target_role": "Senior Frontend Developer",
  "target_skills": ["React", "TypeScript", "Node.js"]
}
```

#### Get Skill Gap Report
```http
GET /skill-gap-analysis/skill-gap-analysis
Authorization: Bearer <token>
```

#### Generate Career Roadmap
```http
POST /career-roadmap/career-roadmap
Authorization: Bearer <token>
Content-Type: application/json

{
  "timeframe": "6 months",
  "available_learning_time": "10 hours per week"
}
```

#### Get Career Roadmap
```http
GET /career-roadmap/career-roadmap
Authorization: Bearer <token>
```

#### CV Export
```http
GET /cv/cv-export?format=pdf
Authorization: Bearer <token>
```

Formats: `pdf`, `html`, `latex`, `latex-view`

### Chat Agent Endpoints

#### Initialize Chat
```http
POST /agent-chat/agent-chat/init
Authorization: Bearer <token>
```

Returns `thread_id` for conversation.

#### Send Message
```http
POST /agent-chat/agent-chat/message
Authorization: Bearer <token>
Content-Type: application/json

{
  "user_message": "How do I become a frontend developer?",
  "thread_id": "thread-uuid"
}
```

#### Get All Conversations
```http
POST /agent-chat/agent-chat/conversation
Authorization: Bearer <token>
```

Returns list of thread IDs.

#### Get Conversation History
```http
GET /agent-chat/agent-chat/conversation/{thread_id}
Authorization: Bearer <token>
```

### User Endpoints

#### Get User Profile
```http
GET /users/me
Authorization: Bearer <token>
```

#### Update User Profile
```http
PUT /users/me
Authorization: Bearer <token>
Content-Type: application/json

{
  "full_name": "John Doe",
  "education_level": "Bachelor's",
  "preferred_career_track": "Web Development"
}
```

#### Add Skill
```http
POST /users/me/skills
Authorization: Bearer <token>
Content-Type: application/json

{
  "skill": "React"
}
```

#### Remove Skill
```http
DELETE /users/me/skills
Authorization: Bearer <token>
Content-Type: application/json

{
  "skill": "React"
}
```

### Resource Endpoints

#### List Resources
```http
GET /resources/?skip=0&limit=100&tags=programming,web
```

#### Create Resource (Admin)
```http
POST /resources/
Authorization: Bearer <token>
Content-Type: application/json

{
  "name": "React Course",
  "description": "Learn React from scratch",
  "url": "https://example.com/course",
  "tags": ["React", "JavaScript"]
}
```

## 💻 Development Guide

### Development Workflow

#### Running All Services

Open 3 terminal windows:

**Terminal 1 - Backend:**
```bash
cd Backend
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 - User Platform:**
```bash
cd FrontEnd
npm run dev
```

**Terminal 3 - Admin Dashboard:**
```bash
cd AdminDashboard
npm run dev
```

### Code Structure

#### Backend Structure

- **API Endpoints**: `app/api/endpoints/` - Route handlers
- **Schemas**: `app/api/schemas/` - Pydantic models for validation
- **Database Models**: `app/db/model/` - SQLAlchemy models
- **CRUD Operations**: `app/db/crud/` - Database queries
- **Services**: `app/services/` - Business logic
- **LLM Workflows**: `app/llm/workflow/` - LangChain agent graphs
- **Prompts**: `app/llm/prompts/` - LLM prompt templates

#### Frontend Structure

- **Pages**: `app/pages/` - File-based routing
- **Components**: `app/components/` - Reusable Vue components
  - `ui/` - Base UI components (Button, Card, Input, Modal)
  - `features/` - Feature-specific components (JobCard, CourseCard)
  - `layout/` - Layout components (Navigation, Footer)
- **Composables**: `app/composables/` - Reusable logic
- **Stores**: `app/stores/` - Pinia state management
- **Layouts**: `app/layouts/` - Page layouts

### Best Practices

#### Backend
- Use type hints throughout
- Follow FastAPI dependency injection patterns
- Validate all inputs with Pydantic
- Handle errors gracefully with HTTPException
- Use async/await for I/O operations
- Log important events

#### Frontend
- Use Composition API with `<script setup>`
- TypeScript for type safety
- Composables for reusable logic
- Pinia for global state
- Tailwind utility classes for styling
- Component props validation

### Testing

#### Backend Testing
```bash
cd Backend
pytest tests/
```

#### Frontend Testing
```bash
cd FrontEnd
npm run test
```

### Code Quality

#### Linting
```bash
# Backend
cd Backend
ruff check .
black .

# Frontend
cd FrontEnd
npm run lint
```

## 🚢 Deployment

### Production Build

#### Backend

```bash
cd Backend

# Install production dependencies
pip install -r requirements.txt

# Set production environment variables
export DATABASE_URL=postgresql://...
export SECRET_KEY=...
export OPENAI_API_KEY=...

# Run with production server
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

#### Frontend (User Platform)

```bash
cd FrontEnd

# Build for production
npm run build

# Preview production build
npm run preview

# Deploy .output/ directory to hosting service
# (Vercel, Netlify, AWS, etc.)
```

#### Admin Dashboard

```bash
cd AdminDashboard

# Build for production
npm run build

# Preview production build
npm run preview

# Deploy .output/ directory
```

### Docker Deployment

```bash
# Build and run with docker-compose
docker-compose up -d

# Or build individually
docker build -t careerin-backend ./Backend
docker build -t careerin-frontend ./FrontEnd
docker build -t careerin-admin ./AdminDashboard
```

### Environment Variables (Production)

#### Backend
```env
DATABASE_URL=postgresql://user:pass@db:5432/careerin
SECRET_KEY=<strong-secret-key>
OPENAI_API_KEY=<your-key>
ENVIRONMENT=production
DEBUG=False
```

#### Frontend
```env
NUXT_PUBLIC_API_BASE=https://api.careerin.com
```

## 🐛 Troubleshooting

### Common Issues

#### Backend Connection Issues

**Problem**: Frontend cannot connect to backend

**Solutions**:
```bash
# Check backend is running
curl http://localhost:8000/health

# Check CORS settings in Backend/main.py
# Ensure frontend URL is in allow_origins

# Check firewall/port blocking
netstat -an | grep 8000
```

#### Database Connection Errors

**Problem**: Cannot connect to PostgreSQL

**Solutions**:
```bash
# Check PostgreSQL is running
sudo systemctl status postgresql  # Linux
brew services list | grep postgresql  # macOS

# Verify connection string
psql $DATABASE_URL

# Check pgvector extension
psql careerin_db -c "SELECT * FROM pg_extension WHERE extname = 'vector';"
```

#### Port Already in Use

**Windows**:
```bash
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

**Mac/Linux**:
```bash
lsof -ti:8000 | xargs kill
# OR
kill -9 $(lsof -t -i:8000)
```

#### Frontend Build Errors

**Problem**: TypeScript or build errors

**Solutions**:
```bash
# Clear cache and reinstall
rm -rf node_modules .nuxt .output
npm install

# Check Node.js version (requires 18+)
node --version

# Clear npm cache
npm cache clean --force
```

#### OpenAI API Errors

**Problem**: AI features not working

**Solutions**:
- Verify `OPENAI_API_KEY` is set correctly
- Check API key has sufficient credits
- Verify API key permissions
- Check rate limits

#### CV Export Issues

**Problem**: CV export fails

**Solutions**:
- Ensure LaTeX is installed (for PDF generation)
- Check file permissions
- Verify user has profile data
- Check backend logs for errors

### Debugging Tips

#### Backend Logging
```python
from app.core.logging_config import get_logger
logger = get_logger(__name__)
logger.info("Debug message")
```

#### Frontend Debugging
- Use browser DevTools (F12)
- Check Network tab for API calls
- Check Console for errors
- Use Vue DevTools extension

#### Database Debugging
```bash
# Connect to database
psql careerin_db

# Check tables
\dt

# Check data
SELECT * FROM users LIMIT 5;
```

## 🤝 Contributing

### Development Setup

1. Fork the repository
2. Clone your fork
3. Create a feature branch
4. Make changes
5. Test thoroughly
6. Submit a pull request

### Code Style

- **Backend**: Follow PEP 8, use Black for formatting
- **Frontend**: Follow Vue 3 style guide, use Prettier
- **Commits**: Use conventional commit messages

### Pull Request Process

1. Update documentation if needed
2. Add tests for new features
3. Ensure all tests pass
4. Update CHANGELOG.md
5. Request review

## 📝 License

See [LICENSE](LICENSE) file for details.

## 📞 Support

For issues, questions, or contributions:
- Open an issue on GitHub
- Check existing documentation
- Review API documentation at `/docs` endpoint

---

**Built with ❤️ for empowering youth employment**
