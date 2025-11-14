# Start All Services - CareerIn Platform

Quick reference for starting all services in the correct order.

## 🚀 Start Everything

### Option 1: Manual (Recommended for Development)

Open **3 separate terminals**:

#### Terminal 1: Backend API
```bash
cd Backend
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
**Wait for**: "Application startup complete"
**Access**: http://localhost:8000/docs (API documentation)

---

#### Terminal 2: User Platform
```bash
cd FrontEnd
npm run dev
```
**Wait for**: "Nuxt is listening"
**Access**: http://localhost:3000 (Main platform)

---

#### Terminal 3: Admin Dashboard
```bash
cd AdminDashboard
npm run dev
```
**Wait for**: "Nuxt is listening"
**Access**: http://localhost:3001 (Admin dashboard)

---

## ✅ Verify Everything is Running

1. **Backend Health Check**:
   ```bash
   curl http://localhost:8000/health
   # Should return: {"status":"ok","version":"..."}
   ```

2. **User Platform**:
   - Open: http://localhost:3000
   - Should see: Landing page with hero

3. **Admin Dashboard**:
   - Open: http://localhost:3001
   - Should see: Admin dashboard with stats

---

## 🎯 Quick Test Flow

### Test Admin Dashboard:
1. Go to http://localhost:3001
2. Click "Create New Job"
3. Fill in:
   - Title: "Test Developer"
   - Company: "Test Corp"
   - Type: "Full Time"
   - Experience: "Entry"
   - Description: "Test job posting"
   - Skills: Add "JavaScript"
4. Submit - job should appear in table

### Test User Platform:
1. Go to http://localhost:3000
2. Click "Sign Up" and create account
3. Go to "Jobs" section
4. Find the job you created
5. Click "Apply"
6. Return to admin dashboard
7. Click applicant count on the job
8. See your application!

---

## 🛑 Stop All Services

Press `Ctrl+C` in each terminal window, or:

**Windows (PowerShell):**
```powershell
# Stop all Python processes
Get-Process python | Stop-Process

# Stop all Node processes
Get-Process node | Stop-Process
```

**Mac/Linux:**
```bash
# Stop by port
kill $(lsof -ti:8000)  # Backend
kill $(lsof -ti:3000)  # User Platform
kill $(lsof -ti:3001)  # Admin Dashboard
```

---

## 📋 Service URLs Summary

| Service | Port | URL | Purpose |
|---------|------|-----|---------|
| Backend API | 8000 | http://localhost:8000 | REST API |
| API Docs | 8000 | http://localhost:8000/docs | Swagger UI |
| User Platform | 3000 | http://localhost:3000 | Public website |
| Admin Dashboard | 3001 | http://localhost:3001 | Admin interface |

---

## 🐛 Common Issues

### Port Already in Use
```bash
# Find what's using the port
# Windows
netstat -ano | findstr :3001

# Mac/Linux
lsof -ti:3001

# Kill the process
# Windows
taskkill /PID <PID> /F

# Mac/Linux
kill -9 <PID>
```

### Backend Won't Start
```bash
# Check Python version (needs 3.9+)
python --version

# Reinstall dependencies
cd Backend
pip install -r requirements.txt
```

### Frontend Won't Start
```bash
# Clear cache and reinstall
cd FrontEnd  # or AdminDashboard
rm -rf node_modules .nuxt
npm install
```

### Database Connection Error
```bash
# Check if PostgreSQL is running
# Start Docker container if using docker-compose
docker-compose up -d
```

---

## 🔄 Development Workflow

### Making Changes:

**Backend Changes:**
- Edit files in `Backend/app/`
- Server auto-reloads (with `--reload` flag)
- Test at http://localhost:8000/docs

**Frontend Changes:**
- Edit files in `FrontEnd/app/`
- Hot reload automatically updates
- View at http://localhost:3000

**Admin Dashboard Changes:**
- Edit files in `AdminDashboard/`
- Hot reload automatically updates
- View at http://localhost:3001

---

## 📊 First Time Setup Checklist

- [ ] Database is running (PostgreSQL)
- [ ] Backend dependencies installed (`pip install -r requirements.txt`)
- [ ] Frontend dependencies installed (`cd FrontEnd && npm install`)
- [ ] Admin dependencies installed (`cd AdminDashboard && npm install`)
- [ ] Backend is running on port 8000
- [ ] Frontend is running on port 3000
- [ ] Admin Dashboard is running on port 3001
- [ ] Created test job in admin dashboard
- [ ] Registered test user in user platform
- [ ] Applied for job as user
- [ ] Viewed applicant in admin dashboard

---

## 💡 Pro Tips

1. **Keep terminals visible**: Use terminal multiplexers or split screens
2. **Watch logs**: Keep an eye on each terminal for errors
3. **Use API docs**: http://localhost:8000/docs for testing endpoints
4. **Browser DevTools**: F12 to see network requests and console errors
5. **Clear cache**: Hard refresh (Ctrl+Shift+R) if changes don't appear

---

## 🎉 You're Ready!

All services should now be running. Happy coding! 🚀

