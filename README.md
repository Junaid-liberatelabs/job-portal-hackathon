# CareerIn - AI-Powered Youth Employment Platform

A comprehensive job portal platform with AI-powered recommendations, featuring a main user platform and a dedicated admin dashboard for managing jobs and applications.

## 🚀 Project Overview

CareerIn consists of three main components:

1. **Backend** (Port 8000) - FastAPI with PostgreSQL + pgvector
2. **FrontEnd** (Port 3000) - User-facing platform built with Nuxt 4
3. **AdminDashboard** (Port 3001) - Admin interface for job and applicant management

## 📁 Project Structure

```
job-portal-hackathon/
├── Backend/                    # FastAPI backend (port 8000)
│   ├── app/
│   │   ├── api/endpoints/     # API endpoints
│   │   ├── db/                # Database models & CRUD
│   │   └── services/          # AI/ML services
│   └── main.py
├── FrontEnd/                   # Main platform (port 3000)
│   ├── app/
│   │   ├── pages/             # User pages
│   │   ├── components/        # Vue components
│   │   └── composables/       # API integration
│   └── nuxt.config.ts
├── AdminDashboard/             # Admin dashboard (port 3001) ✨
│   ├── components/            # Admin components
│   ├── composables/           # Admin API
│   ├── pages/                 # Dashboard pages
│   └── README.md
└── Database/                   # PostgreSQL with pgvector
```

## 🎯 Features

### User Platform (FrontEnd)
- AI-powered job recommendations
- Skills-based matching
- Learning resources catalog
- User profile management
- Job applications tracking
- Beautiful landing page with animations

### Admin Dashboard (AdminDashboard)
- Real-time statistics and analytics
- Create, edit, and delete jobs
- View all applicants per job
- Contact applicants via email
- Modern, scrollable interface
- Live data updates

### Backend API
- RESTful API with FastAPI
- PostgreSQL with pgvector for AI embeddings
- User authentication with JWT
- Job and application management
- Vector similarity search for recommendations

## 🚀 Quick Start

### 1. Start Backend
```bash
cd Backend
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 2. Start User Platform
```bash
cd FrontEnd
npm install
npm run dev
# Opens at http://localhost:3000
```

### 3. Start Admin Dashboard
```bash
cd AdminDashboard
npm install
npm run dev
# Opens at http://localhost:3001
```

## 📚 Documentation

### Admin Dashboard (NEW!)
- 🚀 **Quick Start**: [AdminDashboard/QUICK_START.md](AdminDashboard/QUICK_START.md) - Start here!
- 📖 **Complete Guide**: [ADMIN_DASHBOARD_SETUP.md](ADMIN_DASHBOARD_SETUP.md)
- 🎨 **Visual Summary**: [ADMIN_DASHBOARD_VISUAL_SUMMARY.md](ADMIN_DASHBOARD_VISUAL_SUMMARY.md)
- ✅ **Implementation Summary**: [ADMIN_DASHBOARD_COMPLETE.md](ADMIN_DASHBOARD_COMPLETE.md)
- 📑 **Documentation Index**: [AdminDashboard/INDEX.md](AdminDashboard/INDEX.md)

### Other Documentation
- **Frontend Implementation**: [FRONTEND_IMPLEMENTATION_SUMMARY.md](FRONTEND_IMPLEMENTATION_SUMMARY.md)
- **Backend API**: Check `Backend/app/api/endpoints/`
- **Start All Services**: [START_ALL.md](START_ALL.md)

## 🔧 Technology Stack

### Backend
- FastAPI
- PostgreSQL with pgvector
- SQLAlchemy ORM
- JWT authentication
- OpenAI embeddings

### Frontend (User Platform)
- Nuxt 4 (Vue 3)
- Tailwind CSS
- Pinia (state management)
- Three.js (3D visuals)
- Lenis (smooth scrolling)

### Admin Dashboard
- Nuxt 4 (Vue 3)
- Tailwind CSS
- TypeScript
- Heroicons

## 🌐 Port Configuration

| Service | Port | URL |
|---------|------|-----|
| Backend API | 8000 | http://localhost:8000 |
| User Platform | 3000 | http://localhost:3000 |
| Admin Dashboard | 3001 | http://localhost:3001 |
| PostgreSQL | 5432 | localhost:5432 |

## 🎨 Admin Dashboard Features

### Dashboard Overview
- Total jobs posted
- Total applications received
- Average applicants per job
- Most popular job type

### Job Management
- **Create Jobs**: Full form with all job details
- **Edit Jobs**: Update job information inline
- **Delete Jobs**: Safe deletion with confirmation
- **View Stats**: See applicant counts for each job

### Applicant Tracking
- View all applicants for each job
- See applicant details (name, email, skills, career goals)
- Contact applicants directly via email
- Track application dates

## 🔐 Security Notes

- Backend CORS is configured for ports 3000 and 3001
- Admin dashboard currently has no authentication (add before production)
- JWT authentication available for user platform
- All API requests use secure headers

## 📊 Workflow Examples

### Admin Workflow
1. Open admin dashboard at http://localhost:3001
2. View statistics on dashboard
3. Click "Create New Job"
4. Fill in job details and required skills
5. Submit to create job
6. Wait for users to apply via main platform
7. Click applicant count to view applicants
8. Contact applicants via email
9. Edit or delete jobs as needed

### User Workflow
1. Visit main platform at http://localhost:3000
2. Sign up / Log in
3. Browse jobs with AI recommendations
4. Apply for jobs
5. View application status in dashboard
6. Explore learning resources
7. Update profile and skills

## 🛠️ Development

### Install All Dependencies
```bash
# Backend
cd Backend
pip install -r requirements.txt

# Frontend
cd ../FrontEnd
npm install

# Admin Dashboard
cd ../AdminDashboard
npm install
```

### Run in Development Mode
Open 3 terminal windows:

**Terminal 1 - Backend:**
```bash
cd Backend
python -m uvicorn main:app --reload
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

## 🚢 Production Build

### Frontend
```bash
cd FrontEnd
npm run build
npm run preview
```

### Admin Dashboard
```bash
cd AdminDashboard
npm run build
npm run preview
```

### Backend
```bash
cd Backend
# Configure production settings in app/core/config.py
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

## 🐛 Troubleshooting

### Backend Connection Issues
```bash
# Test backend health
curl http://localhost:8000/health
```

### Port Already in Use
**Windows:**
```bash
netstat -ano | findstr :3001
taskkill /PID <PID> /F
```

**Mac/Linux:**
```bash
lsof -ti:3001 | xargs kill
```

### CORS Errors
Ensure `Backend/main.py` includes your port in CORS origins:
```python
allow_origins=[
    "http://localhost:3000",
    "http://localhost:3001",
    ...
]
```

## 📈 Future Enhancements

- [ ] Admin authentication system
- [ ] Advanced analytics and reporting
- [ ] Application status workflow
- [ ] Interview scheduling
- [ ] Email templates
- [ ] Export functionality (CSV, PDF)
- [ ] Bulk operations
- [ ] Activity logs
- [ ] Multi-admin support

## 📝 License

See [LICENSE](LICENSE) file for details.

## 🤝 Contributing

This is a hackathon project. For contributions or questions, please refer to the documentation in each subdirectory.

---

**Quick Links:**
- [Admin Dashboard Setup Guide](ADMIN_DASHBOARD_SETUP.md)
- [Admin Quick Start](AdminDashboard/QUICK_START.md)
- [Frontend Summary](FRONTEND_IMPLEMENTATION_SUMMARY.md)
