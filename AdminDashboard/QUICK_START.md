# Quick Start Guide - CareerIn Admin Dashboard

## 🚀 Fast Setup (3 Steps)

### Step 1: Backend Running ✓
Make sure the backend is running on port 8000:
```bash
cd Backend
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Step 2: Install Dependencies
```bash
cd AdminDashboard
npm install
```

### Step 3: Start Admin Dashboard
```bash
npm run dev
```

🎉 **Done!** Open http://localhost:3001 in your browser

---

## 📋 What You Can Do

### Dashboard Features
- ✅ View all jobs with applicant counts
- ✅ Create new job postings
- ✅ Edit existing jobs
- ✅ Delete jobs
- ✅ View detailed applicant information
- ✅ Contact applicants via email
- ✅ See real-time statistics

### Creating Your First Job

1. Click **"Create New Job"** button
2. Fill in the form:
   ```
   Title: Frontend Developer
   Company: Tech Corp
   Job Type: Full Time
   Experience: Entry
   Description: Looking for a talented frontend developer...
   Skills: React, TypeScript, Tailwind (press Enter after each)
   ```
3. Click **"Create Job"**

### Viewing Applicants

1. Look at the "Applicants" column in the jobs table
2. Click the applicant count or **"View"** button
3. See all applicant details:
   - Name, email, skills
   - Career goals
   - When they applied
4. Click **"Contact"** to send them an email

---

## 🎨 Dashboard Layout

```
┌─────────────────────────────────────────────────────┐
│  Header: CareerIn Admin Dashboard                   │
├─────────────────────────────────────────────────────┤
│  Dashboard Overview (Stats Cards)                   │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐  │
│  │ Total   │ │ Total   │ │ Average │ │ Most    │  │
│  │ Jobs    │ │ Apps    │ │ Per Job │ │ Popular │  │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘  │
├─────────────────────────────────────────────────────┤
│  Job Listings Table                [Create New Job] │
│  ┌─────────────────────────────────────────────┐   │
│  │ Title | Company | Type | Exp | Apps | ... │   │
│  ├─────────────────────────────────────────────┤   │
│  │ Frontend Dev | Tech | Full | Entry | 5 | ⚙️│   │
│  │ Backend Dev  | Corp | Full | Junior| 3 | ⚙️│   │
│  └─────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────┘
```

---

## 🔧 Common Issues

### Backend Not Connected
**Error**: "Failed to fetch jobs"
**Solution**: 
```bash
# Check if backend is running
curl http://localhost:8000/health

# Should return: {"status":"ok","version":"..."}
```

### Port 3001 Already in Use
**Windows**:
```bash
netstat -ano | findstr :3001
taskkill /PID <PID> /F
```

**Mac/Linux**:
```bash
lsof -ti:3001 | xargs kill
```

### Dependencies Not Installing
```bash
# Clear everything and reinstall
rm -rf node_modules package-lock.json
npm install
```

---

## 🔐 Important Notes

- **No Authentication**: This is an admin dashboard without auth (add if needed)
- **Same Backend**: Uses the same backend as the main platform
- **Separate Port**: Runs on port 3001 (main platform on 3000)
- **Real-Time Data**: All changes reflect immediately

---

## 🎯 Next Steps

After setting up:
1. Create a few test jobs
2. Use the main platform (port 3000) to apply for jobs
3. Return to admin dashboard to see applicants
4. Practice editing and deleting jobs
5. Contact applicants via email

---

## 📞 Need Help?

1. Check backend logs: Look at terminal running backend
2. Check browser console: F12 → Console tab
3. Check network requests: F12 → Network tab
4. Verify backend URL in `nuxt.config.ts`

---

## ✨ Pro Tips

- **Multiple Jobs**: Create several jobs to see statistics
- **Applicant Details**: Click applicant counts to see full details
- **Skill Filtering**: Skills are displayed as badges for easy reading
- **Responsive Design**: Works on desktop and tablet
- **Live Stats**: Dashboard stats update automatically after changes

Happy Managing! 🎉

