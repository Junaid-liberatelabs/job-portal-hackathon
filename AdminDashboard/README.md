# CareerIn Admin Dashboard

A separate, dedicated admin dashboard for managing jobs and viewing applicants on the CareerIn platform. This dashboard runs independently on port **3001** and connects to the same backend API.

## Features

- **Dashboard Overview**: Real-time statistics including total jobs, applications, and analytics
- **Job Management**: Create, edit, and delete job postings
- **Applicant Tracking**: View all applicants for each job with detailed information
- **User-Friendly Interface**: Modern, scrollable, and responsive design
- **Live Updates**: Real-time data fetching from backend API

## Tech Stack

- **Nuxt 4**: Vue 3 framework with file-based routing
- **Tailwind CSS**: Utility-first styling with custom admin theme
- **TypeScript**: Type-safe composables and components
- **Heroicons**: Professional icon library

## Project Structure

```
AdminDashboard/
├── assets/
│   └── css/
│       └── main.css              # Tailwind + custom styles
├── components/
│   ├── ApplicantsModal.vue       # View job applicants
│   ├── CreateJobModal.vue        # Create/edit jobs
│   ├── JobsTable.vue             # Jobs listing table
│   └── StatsCard.vue             # Dashboard statistics card
├── composables/
│   ├── useAdminApi.ts            # API fetch wrapper
│   ├── useApplicants.ts          # Applicants data management
│   └── useJobs.ts                # Jobs data management
├── pages/
│   └── index.vue                 # Main dashboard page
├── app.vue                       # Root component
├── nuxt.config.ts                # Nuxt configuration
├── package.json                  # Dependencies
└── README.md                     # This file
```

## Getting Started

### Prerequisites

1. Backend server running on `http://localhost:8000`
2. Node.js 18+ installed
3. npm or yarn package manager

### Installation

1. Navigate to the AdminDashboard directory:
```bash
cd AdminDashboard
```

2. Install dependencies:
```bash
npm install
```

### Running the Dashboard

Start the development server on port 3001:
```bash
npm run dev
```

The admin dashboard will be available at: **http://localhost:3001**

### Production Build

Build for production:
```bash
npm run build
```

Preview production build:
```bash
npm run preview
```

## API Integration

The dashboard connects to these backend endpoints:

### Jobs Endpoints
- `GET /applications/dashboard` - Get all jobs with applicant counts
- `POST /jobs/` - Create a new job
- `PUT /jobs/{job_id}` - Update a job
- `DELETE /jobs/{job_id}` - Delete a job

### Applications Endpoints
- `GET /applications/job/{job_id}/applicants` - Get all applicants for a job

## Usage Guide

### Dashboard Overview
- View key statistics at a glance
- Monitor total jobs, applications, and averages
- See the most popular job type

### Creating a Job
1. Click "Create New Job" button
2. Fill in required fields:
   - Job Title
   - Company
   - Job Type (Full Time, Part Time, Internship, Freelance)
   - Experience Level (Student, Entry, Junior)
   - Description
   - Required Skills (at least 1)
3. Optional fields:
   - Job Location (Remote, Hybrid, On-site)
   - Salary Range (min/max)
4. Click "Create Job"

### Editing a Job
1. Click the edit icon (pencil) on any job row
2. Modify fields as needed
3. Click "Update Job"

### Viewing Applicants
1. Click the applicant count or "View" button on any job
2. See detailed applicant information:
   - Full name and email
   - Skills
   - Career goals
   - Application date
3. Contact applicants via email directly

### Deleting a Job
1. Click the delete icon (trash) on any job row
2. Confirm deletion in the popup
3. Job and related data will be removed

## Configuration

### API Base URL
Update in `nuxt.config.ts`:
```typescript
runtimeConfig: {
  public: {
    apiBase: 'http://localhost:8000' // Change if backend runs elsewhere
  }
}
```

### Port Configuration
Change port in `package.json`:
```json
"scripts": {
  "dev": "nuxt dev --port 3001"  // Change port here
}
```

## Design System

### Colors
- **Admin Primary**: Blue theme (#0ea5e9)
- **Success**: Green (#10b981)
- **Warning**: Yellow (#f59e0b)
- **Danger**: Red (#ef4444)

### Components
All components follow a consistent design pattern:
- Cards with subtle shadows
- Smooth hover transitions
- Responsive layouts
- Accessible forms and buttons

## Troubleshooting

### Tailwind CSS Warnings in VS Code
If you see "Unknown at rule @tailwind" warnings:
- VS Code settings are included in `.vscode/` folder
- Reload VS Code window (Ctrl+Shift+P → "Reload Window")
- Warnings are cosmetic and don't affect functionality

### Backend Connection Issues
- Ensure backend is running on port 8000
- Check CORS settings in backend (should allow localhost:3001)
- Verify API endpoints are accessible

### Port Already in Use
```bash
# Kill process on port 3001 (Windows)
netstat -ano | findstr :3001
taskkill /PID <PID> /F

# Kill process on port 3001 (Mac/Linux)
lsof -ti:3001 | xargs kill
```

### Build Errors
```bash
# Clear cache and reinstall
rm -rf node_modules .nuxt .output
npm install
```

## Development Notes

- The dashboard is completely separate from the main FrontEnd application
- No authentication is currently implemented (add as needed)
- All data fetches are real-time from the backend
- Components are designed to be reusable and maintainable

## Future Enhancements

- Admin authentication and authorization
- Advanced filtering and search
- Export applicant data (CSV, PDF)
- Email templates for contacting applicants
- Application status tracking
- Analytics and reporting features
- Bulk operations for jobs

## Support

For issues or questions:
1. Check backend logs for API errors
2. Check browser console for frontend errors
3. Verify network requests in browser DevTools
4. Ensure all dependencies are installed correctly

