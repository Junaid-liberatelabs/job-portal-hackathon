# Admin Dashboard Architecture

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        CareerIn Platform                         │
└─────────────────────────────────────────────────────────────────┘

┌──────────────────┐         ┌──────────────────┐         ┌──────────────────┐
│   User Platform  │         │ Admin Dashboard  │         │   Backend API    │
│   Port: 3000     │────────▶│   Port: 3001     │────────▶│   Port: 8000     │
│                  │         │                  │         │                  │
│  - Landing Page  │         │  - Job CRUD      │         │  - FastAPI       │
│  - Job Browsing  │         │  - Applicants    │         │  - PostgreSQL    │
│  - Applications  │         │  - Statistics    │         │  - Auth/JWT      │
│  - Profile       │         │  - Management    │         │  - Embeddings    │
└──────────────────┘         └──────────────────┘         └──────────────────┘
         │                            │                            │
         │                            │                            │
         └────────────────────────────┴────────────────────────────┘
                                      │
                               ┌──────▼──────┐
                               │  PostgreSQL  │
                               │  + pgvector  │
                               │  Port: 5432  │
                               └──────────────┘
```

## Admin Dashboard Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                     Admin Dashboard (Port 3001)                      │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  ┌───────────────────────────────────────────────────────────┐     │
│  │                    Dashboard Page (/)                      │     │
│  │  ┌─────────────────────────────────────────────────────┐  │     │
│  │  │  Stats Cards (Total Jobs, Apps, Avg, Popular)      │  │     │
│  │  └─────────────────────────────────────────────────────┘  │     │
│  │  ┌─────────────────────────────────────────────────────┐  │     │
│  │  │  Jobs Table Component                               │  │     │
│  │  │  - View all jobs with applicant counts             │  │     │
│  │  │  - Edit/Delete actions                             │  │     │
│  │  └─────────────────────────────────────────────────────┘  │     │
│  └───────────────────────────────────────────────────────────┘     │
│                          │                │                          │
│                          ▼                ▼                          │
│              ┌────────────────┐  ┌────────────────┐               │
│              │ Create/Edit    │  │  Applicants    │               │
│              │  Job Modal     │  │    Modal       │               │
│              └────────────────┘  └────────────────┘               │
│                                                                       │
└─────────────────────────────────────────────────────────────────────┘
```

## Component Hierarchy

```
app.vue
└── pages/index.vue (Main Dashboard)
    ├── StatsCard.vue (x4)
    │   └── Icon + Data
    │
    ├── JobsTable.vue
    │   └── Job Rows
    │       ├── Job Info
    │       ├── Applicant Count (clickable)
    │       └── Action Buttons
    │
    ├── CreateJobModal.vue
    │   └── Form Fields
    │       ├── Text Inputs
    │       ├── Dropdowns
    │       ├── Textarea
    │       └── Skills Chip Input
    │
    └── ApplicantsModal.vue
        └── Applicant Cards
            ├── User Info
            ├── Skills Badges
            └── Contact Button
```

## Data Flow

### 1. Fetching Jobs with Applicants
```
Dashboard Page
    │
    ├──▶ useJobs() composable
    │       │
    │       ├──▶ fetchJobsWithApplicants()
    │       │       │
    │       │       └──▶ useAdminApi()
    │       │               │
    │       │               └──▶ GET /applications/dashboard
    │       │                       │
    │       │                       └──▶ Backend returns:
    │       │                             [{ job: {...}, applicants_count: N }]
    │       │
    │       └──▶ Updates jobsWithApplicants ref
    │
    └──▶ JobsTable displays data
```

### 2. Creating a Job
```
Dashboard Page
    │
    ├──▶ Click "Create New Job"
    │       │
    │       └──▶ CreateJobModal opens
    │               │
    │               ├──▶ User fills form
    │               │       - Title, company, type, skills, etc.
    │               │
    │               ├──▶ Submit form
    │               │       │
    │               │       └──▶ useJobs().createJob()
    │               │               │
    │               │               └──▶ POST /jobs/
    │               │                       │
    │               │                       └──▶ Backend creates job
    │               │                               │
    │               │                               └──▶ Returns job data
    │               │
    │               ├──▶ Modal closes
    │               │
    │               └──▶ Dashboard refreshes
    │                       │
    │                       └──▶ New job appears in table
```

### 3. Viewing Applicants
```
Dashboard Page
    │
    ├──▶ JobsTable shows jobs
    │       │
    │       ├──▶ Click applicant count
    │       │       │
    │       │       └──▶ Emit 'view-applicants' event
    │       │
    │       └──▶ Dashboard receives event
    │               │
    │               └──▶ ApplicantsModal opens
    │                       │
    │                       ├──▶ useApplicants().fetchApplicantsByJob(jobId)
    │                       │       │
    │                       │       └──▶ GET /applications/job/{jobId}/applicants
    │                       │               │
    │                       │               └──▶ Backend returns:
    │                       │                     [{ user: {...}, applied_at: "..." }]
    │                       │
    │                       └──▶ Modal displays applicants
    │                               │
    │                               └──▶ User can contact via email
```

## Composables Architecture

### useAdminApi.ts
```typescript
Purpose: HTTP client wrapper
- Handles fetch requests
- Sets headers (Content-Type, etc.)
- Error logging
- Response parsing

Used by: useJobs, useApplicants
```

### useJobs.ts
```typescript
Purpose: Job data management
State:
  - jobsWithApplicants: Ref<JobWithApplicantsCount[]>
  - loading: Ref<boolean>
  - error: Ref<string | null>

Methods:
  - fetchJobsWithApplicants()
  - createJob(data)
  - updateJob(id, data)
  - deleteJob(id)

Used by: Dashboard page, JobsTable, CreateJobModal
```

### useApplicants.ts
```typescript
Purpose: Applicants data management
State:
  - applicants: Ref<ApplicantInfo[]>
  - loading: Ref<boolean>
  - error: Ref<string | null>

Methods:
  - fetchApplicantsByJob(jobId)

Used by: ApplicantsModal
```

## API Endpoints Used

### Jobs Endpoints (from Backend/app/api/endpoints/jobs.py)
```
POST   /jobs/              - Create new job
PUT    /jobs/{job_id}      - Update job
DELETE /jobs/{job_id}      - Delete job
```

### Applications Endpoints (from Backend/app/api/endpoints/applications.py)
```
GET /applications/dashboard                    - Get jobs with applicant counts
GET /applications/job/{job_id}/applicants     - Get applicants for specific job
```

## State Management

### Local State (Vue Composition API)
```typescript
// Dashboard page maintains:
const isCreateModalOpen = ref(false)
const isApplicantsModalOpen = ref(false)
const editingJob = ref<Job | null>(null)
const selectedJob = ref<Job | null>(null)

// Composables maintain:
const jobsWithApplicants = ref<JobWithApplicantsCount[]>([])
const applicants = ref<ApplicantInfo[]>([])
const loading = ref(false)
const error = ref<string | null>(null)
```

### No Global State
- No Pinia/Vuex needed
- Each composable manages its own state
- Props/events for component communication

## Styling Architecture

### Tailwind Configuration
```
Base Colors:
  - admin-* (blue theme for admin)
  - ink-* (gray scale)
  - Success (green)
  - Warning (yellow)
  - Danger (red)

Component Classes:
  - .btn, .btn-primary, .btn-secondary, .btn-danger
  - .card, .card-header, .card-body
  - .badge, .badge-primary, .badge-success, etc.
  - .input (form inputs)
```

### CSS Organization
```
assets/css/main.css
  │
  ├── @layer base
  │     └── Global HTML element styles
  │
  ├── @layer components
  │     ├── Buttons (.btn-*)
  │     ├── Inputs (.input)
  │     ├── Cards (.card-*)
  │     └── Badges (.badge-*)
  │
  └── @layer utilities
        └── Custom utilities (.scrollbar-thin)
```

## Performance Considerations

### Optimization Strategies
1. **Lazy Loading**: Modals only render when open (v-if)
2. **Efficient Re-fetching**: Only fetch when data changes
3. **Minimal Re-renders**: Computed properties for derived data
4. **Event Delegation**: Parent handles child events
5. **Debouncing**: Can add for search/filter inputs

### Bundle Size
- Small bundle due to minimal dependencies
- Nuxt auto-imports reduce boilerplate
- Tree-shaking removes unused code
- Tailwind purges unused styles

## Security Considerations

### Current State
- No authentication implemented
- All endpoints publicly accessible
- CORS enabled for localhost:3001

### Recommended for Production
```typescript
// Add auth middleware
export default defineNuxtRouteMiddleware((to, from) => {
  const token = useCookie('admin_token')
  if (!token.value) {
    return navigateTo('/login')
  }
})

// Add token to API requests
headers['Authorization'] = `Bearer ${adminToken}`
```

## Error Handling

### API Errors
```typescript
try {
  const data = await apiFetch('/endpoint')
  // Success
} catch (e: any) {
  error.value = e.data?.detail || e.message || 'Failed'
  // Display error in UI
}
```

### User Feedback
- Loading states during API calls
- Error messages in red banners
- Success feedback via modal close + refresh
- Confirmation dialogs for destructive actions

## Testing Strategy

### Manual Testing Checklist
- [ ] Create job with all fields
- [ ] Create job with required fields only
- [ ] Edit existing job
- [ ] Delete job
- [ ] View applicants (empty state)
- [ ] View applicants (with data)
- [ ] Contact applicant via email
- [ ] Stats update after job creation
- [ ] Error handling (disconnect backend)

### Future Automated Testing
- Unit tests for composables
- Component tests with Vue Test Utils
- E2E tests with Playwright/Cypress
- API integration tests

## Deployment Architecture

### Production Setup
```
┌─────────────────────┐
│   Reverse Proxy     │
│   (Nginx/Caddy)     │
└──────────┬──────────┘
           │
    ┌──────┴──────┐
    │             │
┌───▼────┐   ┌───▼────┐
│ Admin  │   │  User  │
│ :3001  │   │ :3000  │
└───┬────┘   └───┬────┘
    │            │
    └──────┬─────┘
           │
      ┌────▼─────┐
      │ Backend  │
      │  :8000   │
      └────┬─────┘
           │
      ┌────▼─────┐
      │PostgreSQL│
      │  :5432   │
      └──────────┘
```

### Environment Variables
```env
# .env
NUXT_PUBLIC_API_BASE=https://api.careerin.com
```

### Build Commands
```bash
# Build admin dashboard
cd AdminDashboard
npm run build

# Output: .output/ directory (SSR)
# or: dist/ directory (static)
```

## Future Enhancements

### Planned Features
1. **Authentication**
   - Admin login page
   - JWT token storage
   - Protected routes

2. **Advanced Filtering**
   - Search jobs by title/company
   - Filter by date range
   - Sort by applicant count

3. **Analytics**
   - Charts with ECharts
   - Application trends
   - Job performance metrics

4. **Bulk Operations**
   - Select multiple jobs
   - Bulk delete
   - Bulk edit

5. **Email System**
   - Custom email templates
   - Bulk email to applicants
   - Email tracking

### Scalability
- Add Redis for caching
- Implement pagination for large datasets
- Use WebSocket for real-time updates
- Add search indexing (Elasticsearch)

---

This architecture provides a solid foundation for the admin dashboard while remaining simple and maintainable. 🚀

