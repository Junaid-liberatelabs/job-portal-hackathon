# Admin Dashboard - Quick Reference Card

## 🚀 Start Dashboard
```bash
cd AdminDashboard
npm install
npm run dev
```
**URL**: http://localhost:3001

---

## 🔑 Key Files

| File | Purpose |
|------|---------|
| `pages/index.vue` | Main dashboard page |
| `components/JobsTable.vue` | Jobs table display |
| `components/CreateJobModal.vue` | Create/edit job form |
| `components/ApplicantsModal.vue` | View applicants |
| `composables/useJobs.ts` | Jobs CRUD logic |
| `composables/useApplicants.ts` | Applicants logic |
| `assets/css/main.css` | Styles & design system |

---

## 🎯 Common Tasks

### Create a Job
1. Click "Create New Job" button
2. Fill required fields (title, company, type, experience, description, skills)
3. Click "Create Job"

### Edit a Job
1. Click edit icon (✏️) in jobs table
2. Modify fields
3. Click "Update Job"

### Delete a Job
1. Click delete icon (🗑️) in jobs table
2. Confirm deletion
3. Done

### View Applicants
1. Click applicant count in jobs table
2. View all applicant details
3. Click "Contact" to email

---

## 🔌 API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/applications/dashboard` | Get jobs with counts |
| GET | `/applications/job/{id}/applicants` | Get applicants |
| POST | `/jobs/` | Create job |
| PUT | `/jobs/{id}` | Update job |
| DELETE | `/jobs/{id}` | Delete job |

---

## 🎨 Component Props

### JobsTable
```vue
<JobsTable
  :jobs="jobsWithApplicants"
  @view-applicants="handleView"
  @edit-job="handleEdit"
  @delete-job="handleDelete"
/>
```

### CreateJobModal
```vue
<CreateJobModal
  :is-open="isOpen"
  :edit-job="jobToEdit"
  @close="handleClose"
  @job-created="handleCreated"
  @job-updated="handleUpdated"
/>
```

### ApplicantsModal
```vue
<ApplicantsModal
  :is-open="isOpen"
  :job="selectedJob"
  @close="handleClose"
/>
```

---

## 🧩 Composables Usage

### useJobs()
```typescript
const {
  jobsWithApplicants,  // Ref<JobWithApplicantsCount[]>
  loading,              // Ref<boolean>
  error,                // Ref<string | null>
  fetchJobsWithApplicants,  // () => Promise<void>
  createJob,            // (data) => Promise<Job>
  updateJob,            // (id, data) => Promise<Job>
  deleteJob             // (id) => Promise<void>
} = useJobs()
```

### useApplicants()
```typescript
const {
  applicants,           // Ref<ApplicantInfo[]>
  loading,              // Ref<boolean>
  error,                // Ref<string | null>
  fetchApplicantsByJob  // (jobId) => Promise<void>
} = useApplicants()
```

---

## 🎨 Design Tokens

### Colors
```css
admin-600:  #0284c7  /* Primary buttons */
ink-900:    #111827  /* Text */
ink-600:    #4b5563  /* Secondary text */
green-600:  #10b981  /* Success */
red-600:    #ef4444  /* Danger */
```

### Common Classes
```css
.btn              /* Base button */
.btn-primary      /* Blue button */
.btn-danger       /* Red button */
.card             /* Card container */
.badge            /* Status badge */
.input            /* Form input */
```

---

## 🐛 Troubleshooting

### Backend Not Connected
```bash
# Test backend
curl http://localhost:8000/health
```

### Port 3001 In Use
```bash
# Windows
netstat -ano | findstr :3001
taskkill /PID <PID> /F

# Mac/Linux
lsof -ti:3001 | xargs kill
```

### Clear Cache
```bash
rm -rf node_modules .nuxt .output
npm install
```

---

## 📊 Statistics Calculation

```typescript
// Total jobs
jobsWithApplicants.value.length

// Total applications
jobsWithApplicants.value.reduce((sum, item) => 
  sum + item.applicants_count, 0
)

// Average per job
totalApplications / totalJobs

// Most popular type
Object.entries(typeCount)
  .sort((a, b) => b[1] - a[1])[0][0]
```

---

## 🔧 Configuration

### Change API URL
`nuxt.config.ts`:
```typescript
runtimeConfig: {
  public: {
    apiBase: 'http://localhost:8000'
  }
}
```

### Change Port
`package.json`:
```json
"dev": "nuxt dev --port 3001"
```

---

## 📝 Form Validation

### Required Fields (Create Job)
- ✅ Title
- ✅ Company
- ✅ Job Type
- ✅ Experience Level
- ✅ Description
- ✅ Skills (at least 1)

### Optional Fields
- Job Location
- Salary Range (min/max)

---

## 🎯 Job Type Options
- FULL_TIME
- PART_TIME
- INTERNSHIP
- FREELANCE

## 🎯 Experience Level Options
- STUDENT
- ENTRY
- JUNIOR

## 🎯 Location Options
- REMOTE
- HYBRID
- ON_SITE

---

## 🔄 Data Flow

```
User Action
    ↓
Component Event
    ↓
Page Handler
    ↓
Composable Method
    ↓
API Call
    ↓
Backend Response
    ↓
Update State
    ↓
UI Re-renders
```

---

## 📁 Project Structure

```
AdminDashboard/
├── assets/css/         # Styles
├── components/         # Vue components
├── composables/        # Logic & API
├── pages/              # Routes
├── app.vue             # Root
├── nuxt.config.ts      # Config
└── package.json        # Dependencies
```

---

## 🧪 Testing Checklist

- [ ] Dashboard loads
- [ ] Stats display correctly
- [ ] Can create job
- [ ] Can edit job
- [ ] Can delete job
- [ ] Can view applicants
- [ ] Loading states work
- [ ] Error handling works

---

## 🚢 Production Commands

```bash
# Build
npm run build

# Preview
npm run preview

# Deploy .output/ directory
```

---

## 📚 Documentation

| File | Content |
|------|---------|
| `README.md` | Full documentation |
| `QUICK_START.md` | 3-step setup |
| `ARCHITECTURE.md` | System design |
| `UI_GUIDE.md` | Design system |
| `FEATURES_CHECKLIST.md` | All features |
| `QUICK_REFERENCE.md` | This file |

---

## 💡 Pro Tips

1. Keep backend running in separate terminal
2. Use browser DevTools (F12) for debugging
3. Check Network tab for API calls
4. Console shows request/response logs
5. Ctrl+Shift+R for hard refresh

---

## 🎉 Quick Wins

### First Use
```bash
cd AdminDashboard
npm install && npm run dev
# Open http://localhost:3001
# Click "Create New Job"
# Fill form and submit
# Done! 🎉
```

### Daily Use
1. Start dashboard: `npm run dev`
2. Create/edit/delete jobs
3. View applicants
4. Contact candidates
5. Monitor statistics

---

**That's it! You're ready to manage jobs like a pro.** 🚀

*Print this page for quick reference!*

