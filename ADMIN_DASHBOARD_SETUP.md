# Admin Dashboard - Complete Setup Guide

## Overview

A dedicated admin dashboard has been created for managing jobs and viewing applicants. This runs as a **separate application** on port **3001**, completely independent from the main FrontEnd application (port 3000).

## 📁 Project Structure

```
job-portal-hackathon/
├── Backend/                    # FastAPI backend (port 8000)
├── FrontEnd/                   # Main user platform (port 3000)
└── AdminDashboard/             # Admin dashboard (port 3001) ✨ NEW
    ├── assets/css/             # Tailwind + custom styles
    ├── components/             # Vue components
    │   ├── ApplicantsModal.vue
    │   ├── CreateJobModal.vue
    │   ├── JobsTable.vue
    │   └── StatsCard.vue
    ├── composables/            # API & data management
    │   ├── useAdminApi.ts
    │   ├── useApplicants.ts
    │   └── useJobs.ts
    ├── pages/
    │   └── index.vue           # Main dashboard page
    ├── app.vue
    ├── nuxt.config.ts
    ├── package.json
    ├── README.md               # Full documentation
    └── QUICK_START.md          # Quick setup guide
```

## 🚀 Quick Start

### 1. Install Dependencies
```bash
cd AdminDashboard
npm install
```

### 2. Ensure Backend is Running
```bash
cd Backend
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 3. Start Admin Dashboard
```bash
cd AdminDashboard
npm run dev
```

### 4. Access Dashboard
Open your browser to: **http://localhost:3001**

## ✨ Features

### Dashboard Overview
- **Real-time Statistics**: Total jobs, applications, averages, and trends
- **Beautiful UI**: Modern, scrollable design with custom admin theme
- **Responsive Layout**: Works on desktop and tablet devices

### Job Management
- **Create Jobs**: Full form with validation for all job fields
- **Edit Jobs**: Update any job details inline
- **Delete Jobs**: Safe deletion with confirmation dialog
- **View Details**: See all job information at a glance

### Applicant Tracking
- **View Applicants**: See everyone who applied for each job
- **Applicant Details**: Full name, email, skills, career goals
- **Contact Feature**: Email applicants directly
- **Application Timeline**: See when each person applied

## 🔌 API Endpoints Used

### From applications.py
- `GET /applications/dashboard` - Get all jobs with applicant counts
- `GET /applications/job/{job_id}/applicants` - Get applicants for specific job

### From jobs.py
- `POST /jobs/` - Create new job
- `PUT /jobs/{job_id}` - Update job
- `DELETE /jobs/{job_id}` - Delete job

## 🎨 Design & Theme

### Color Scheme
- **Primary**: Admin Blue (#0ea5e9) - Professional and trustworthy
- **Success**: Green - For completed actions
- **Warning**: Yellow - For caution states
- **Danger**: Red - For delete actions

### UI Components
- **Stats Cards**: Dashboard metrics with icons
- **Jobs Table**: Sortable, filterable table view
- **Modals**: Create/Edit Job, View Applicants
- **Badges**: Job type, experience level indicators
- **Buttons**: Primary, secondary, danger variants

## 📊 Dashboard Sections

### 1. Statistics Overview
Four key metrics displayed at the top:
- Total Jobs Posted
- Total Applications Received
- Average Applicants per Job
- Most Popular Job Type

### 2. Jobs Table
Columns include:
- Job Title & Description preview
- Company Name
- Job Type (Full Time, Part Time, etc.)
- Experience Level (Student, Entry, Junior)
- Applicant Count (clickable)
- Posted Date
- Actions (Edit, Delete)

### 3. Create/Edit Job Modal
Form fields:
- Job Title *required*
- Company *required*
- Job Type *required* (dropdown)
- Job Location (dropdown)
- Experience Level *required* (dropdown)
- Description *required* (textarea)
- Salary Range (min/max)
- Required Skills *required* (tag input)

### 4. Applicants Modal
Shows for each applicant:
- Profile initial avatar
- Full name and email
- Career goals
- Skills (as badges)
- Application date
- Contact button (opens email)

## 🔧 Configuration

### Change Backend URL
Edit `AdminDashboard/nuxt.config.ts`:
```typescript
runtimeConfig: {
  public: {
    apiBase: 'http://localhost:8000' // Change this
  }
}
```

### Change Port
Edit `AdminDashboard/package.json`:
```json
"scripts": {
  "dev": "nuxt dev --port 3001" // Change port here
}
```

## 🛠️ Technical Stack

- **Framework**: Nuxt 4 (Vue 3)
- **Styling**: Tailwind CSS
- **Icons**: Heroicons
- **HTTP**: Native fetch API
- **State**: Vue 3 Composition API (ref, computed)
- **Type Safety**: TypeScript throughout

## 📋 Workflow Example

### Complete Admin Workflow:
1. **Admin opens dashboard** at http://localhost:3001
2. **Views statistics** - sees 5 jobs, 12 total applications
3. **Clicks "Create New Job"**
   - Fills in: "Full Stack Developer" at "Tech Corp"
   - Adds skills: React, Node.js, PostgreSQL
   - Sets as Full Time, Entry level
   - Submits form
4. **Job appears in table** with 0 applicants
5. **Users apply** via main platform (port 3000)
6. **Admin refreshes** or returns to dashboard
7. **Sees applicant count** increased to 3
8. **Clicks "View"** on applicant count
9. **Modal opens** showing all 3 applicants with details
10. **Clicks "Contact"** to email an applicant
11. **Edits job** if needed via edit button
12. **Deletes old jobs** when no longer needed

## 🐛 Troubleshooting

### Backend Connection Failed
```bash
# Test backend
curl http://localhost:8000/health

# Should return: {"status":"ok"}
```

### CORS Issues
Backend already configured for port 3001 in `Backend/main.py`:
```python
allow_origins=[
    "http://localhost:3000",
    "http://localhost:3001",  # Admin dashboard
    ...
]
```

### Port Already in Use
**Windows:**
```bash
netstat -ano | findstr :3001
taskkill /PID <PID> /F
```

**Mac/Linux:**
```bash
lsof -ti:3001 | xargs kill -9
```

### Build Issues
```bash
cd AdminDashboard
rm -rf node_modules .nuxt .output
npm install
npm run dev
```

## 🔐 Security Notes

**Current State**: No authentication implemented
**Recommended**: Add admin authentication before production

To add authentication:
1. Create admin login system
2. Store admin token
3. Add middleware to protect routes
4. Send token with API requests
5. Backend validates admin role

## 🚢 Production Deployment

### Build for Production
```bash
cd AdminDashboard
npm run build
```

### Preview Production Build
```bash
npm run preview
```

### Deploy Options
- **Static**: Use `npm run generate` for static hosting
- **SSR**: Deploy `.output` directory to Node.js server
- **Docker**: Add Dockerfile similar to FrontEnd

## 📈 Future Enhancements

Possible improvements:
- [ ] Admin authentication & authorization
- [ ] Advanced search and filtering
- [ ] Export applicants to CSV/PDF
- [ ] Email templates for bulk contact
- [ ] Application status tracking (pending, reviewed, rejected)
- [ ] Interview scheduling
- [ ] Analytics dashboard with charts
- [ ] Bulk job operations
- [ ] Activity logs and audit trail
- [ ] Multi-admin support with roles

## 📚 Additional Resources

- **Full Documentation**: `AdminDashboard/README.md`
- **Quick Start**: `AdminDashboard/QUICK_START.md`
- **Backend API**: Check `Backend/app/api/endpoints/`
- **Main Frontend**: `FrontEnd/` directory

## ✅ Testing Checklist

- [ ] Backend running on port 8000
- [ ] Admin dashboard accessible at port 3001
- [ ] Can create new job successfully
- [ ] Can edit existing job
- [ ] Can delete job with confirmation
- [ ] Can view applicants for a job
- [ ] Stats update correctly after changes
- [ ] Email contact button works
- [ ] UI is responsive and scrollable
- [ ] No console errors in browser

## 🎯 Summary

✅ **Separate Application**: Completely independent from main platform
✅ **Different Port**: Runs on 3001 (main platform on 3000)
✅ **Same Backend**: Uses existing FastAPI backend on port 8000
✅ **Full CRUD**: Create, Read, Update, Delete jobs
✅ **Applicant Tracking**: View all applicants with details
✅ **Modern UI**: Beautiful, responsive, user-friendly interface
✅ **Type Safe**: Full TypeScript support
✅ **Production Ready**: Build and deploy like any Nuxt app

**You now have a complete admin dashboard to manage your job portal!** 🎉

