# Admin Dashboard UI Guide

Visual guide to the admin dashboard interface and components.

## 🎨 Color Palette

### Primary Colors
```
Admin Blue:
- 50:  #f0f9ff (lightest - backgrounds)
- 500: #0ea5e9 (primary - buttons)
- 600: #0284c7 (hover states)
- 900: #0c4a6e (darkest - emphasis)

Ink (Grayscale):
- 50:  #f9fafb (backgrounds)
- 600: #4b5563 (secondary text)
- 900: #111827 (primary text)
```

### Status Colors
```
Success: #10b981 (green) - Full Time, completed actions
Warning: #f59e0b (yellow) - Part Time, caution
Danger:  #ef4444 (red)    - Delete, errors
Info:    #3b82f6 (blue)   - Internship, general info
```

## 📐 Layout Structure

### Header (Sticky)
```
┌─────────────────────────────────────────────────────────────┐
│  [Icon] CareerIn Admin              [●Live] [Admin Avatar]  │
│         Dashboard & Management                               │
└─────────────────────────────────────────────────────────────┘
```

### Dashboard Overview Section
```
┌─────────────────────────────────────────────────────────────┐
│  Dashboard Overview                                          │
│  Manage job postings and track applications                 │
│                                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ 📋       │  │ 👥       │  │ 📊       │  │ 🔥       │   │
│  │ Total    │  │ Total    │  │ Average  │  │ Most     │   │
│  │ Jobs     │  │ Apps     │  │ Per Job  │  │ Popular  │   │
│  │          │  │          │  │          │  │          │   │
│  │   12     │  │   45     │  │   3.8    │  │ Full Time│   │
│  │          │  │          │  │          │  │          │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### Jobs Table Section
```
┌─────────────────────────────────────────────────────────────┐
│  Job Listings                        [+ Create New Job]     │
│  Manage and monitor all job postings                        │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ Title | Company | Type | Exp | Applicants | Actions  │ │
│  ├────────────────────────────────────────────────────────┤ │
│  │ Frontend Dev      │ Tech Corp  │ [Full Time] │        │ │
│  │ Building modern.. │            │ [Entry]     │ [5]    │ │
│  │                   │            │             │ ✏️ 🗑️  │ │
│  ├────────────────────────────────────────────────────────┤ │
│  │ Backend Dev       │ StartupCo  │ [Part Time] │        │ │
│  │ Node.js expert..  │            │ [Junior]    │ [3]    │ │
│  │                   │            │             │ ✏️ 🗑️  │ │
│  └────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## 🧩 Component Details

### Stats Card
```
┌─────────────────────────┐
│  Total Jobs       [📋] │
│                         │
│       12                │
│                         │
│  Active job postings    │
└─────────────────────────┘

Features:
- Large number display
- Icon with colored background
- Subtitle for context
- Hover shadow effect
```

### Job Row (in Table)
```
┌────────────────────────────────────────────────────────────┐
│ Frontend Developer                          │ Tech Corp    │
│ Building modern web applications with...    │              │
│                                             │ [Full Time]  │
│                                             │ [Entry]      │
│                                             │              │
│                                             │ [  5  ] View │
│                                             │              │
│ Posted 2 days ago                           │  ✏️  🗑️      │
└────────────────────────────────────────────────────────────┘

Features:
- Title + description preview
- Company name
- Type badge (colored)
- Experience badge (colored)
- Clickable applicant count
- Edit/Delete action buttons
- Relative time display
```

### Create Job Modal
```
┌──────────────────────────────────────┐
│  Create New Job              [✕]     │
├──────────────────────────────────────┤
│                                      │
│  Job Title *                         │
│  [_________________________]         │
│                                      │
│  Company *        Job Type *         │
│  [___________]    [▼ Select  ]       │
│                                      │
│  Description *                       │
│  [_________________________]         │
│  [_________________________]         │
│  [_________________________]         │
│                                      │
│  Required Skills *                   │
│  [Type and press Enter___]           │
│                                      │
│  [React ✕] [TypeScript ✕] [CSS ✕]   │
│                                      │
│  Salary Range (optional)             │
│  Min [________]  Max [________]      │
│                                      │
│          [Cancel] [Create Job]       │
└──────────────────────────────────────┘

Features:
- Two-column layout where appropriate
- Required field markers (*)
- Skill tag input with add/remove
- Dropdowns for predefined values
- Clear validation feedback
- Cancel/Submit buttons
```

### Applicants Modal
```
┌───────────────────────────────────────────────────────┐
│  Applicants                                    [✕]    │
│  Frontend Developer at Tech Corp                      │
├───────────────────────────────────────────────────────┤
│                                                        │
│  ┌─────────────────────────────────────────────────┐ │
│  │  [JD]  John Doe                     [Contact]   │ │
│  │        john@example.com                         │ │
│  │                                                  │ │
│  │        Career Goals: Become a senior frontend   │ │
│  │        developer specializing in React          │ │
│  │                                                  │ │
│  │        Skills:                                   │ │
│  │        [React] [JavaScript] [CSS] [TypeScript]  │ │
│  │                                                  │ │
│  │        📅 Applied 3 days ago                     │ │
│  └─────────────────────────────────────────────────┘ │
│                                                        │
│  ┌─────────────────────────────────────────────────┐ │
│  │  [SM]  Sarah Miller                 [Contact]   │ │
│  │        sarah@example.com                        │ │
│  │        ...                                       │ │
│  └─────────────────────────────────────────────────┘ │
│                                                        │
├───────────────────────────────────────────────────────┤
│  Total Applicants: 2                    [Close]       │
└───────────────────────────────────────────────────────┘

Features:
- Scrollable applicant list
- Avatar with initials
- Full user information
- Skills displayed as badges
- Contact button (opens email)
- Application date
- Footer with total count
```

### Delete Confirmation
```
┌───────────────────────────────────┐
│  ⚠️  Delete Job                   │
│     This action cannot be undone  │
│                                   │
│  Are you sure you want to delete  │
│  this job? All associated         │
│  applications will be affected.   │
│                                   │
│         [Cancel] [Delete Job]     │
└───────────────────────────────────┘

Features:
- Warning icon (red background)
- Clear messaging
- Destructive action button (red)
- Cancel option
```

## 🎭 Component States

### Button States
```
Primary Button:
Default:  Blue background (#0ea5e9)
Hover:    Darker blue (#0284c7)
Active:   Even darker
Disabled: 50% opacity + no pointer

Danger Button:
Default:  Red background (#ef4444)
Hover:    Darker red (#dc2626)
```

### Loading States
```
Full Page Loading:
┌─────────────────────┐
│                     │
│        ⟲           │
│   Loading jobs...   │
│                     │
└─────────────────────┘

Button Loading:
[  Creating...  ]
```

### Empty States
```
No Jobs:
┌─────────────────────────────┐
│          📋                 │
│                             │
│   No jobs posted yet        │
│                             │
│   Create your first job     │
│   posting to get started    │
└─────────────────────────────┘

No Applicants:
┌─────────────────────────────┐
│          👥                 │
│                             │
│   No applicants yet         │
│                             │
│   This job hasn't received  │
│   any applications          │
└─────────────────────────────┘
```

## 🎨 Typography

### Headings
```
H1 (Page Title):
  Font: Plus Jakarta Sans
  Size: 3xl (30px)
  Weight: Bold
  Color: ink-900

H2 (Section Title):
  Font: Plus Jakarta Sans
  Size: 2xl (24px)
  Weight: Bold
  Color: ink-900

H3 (Card Header):
  Font: Plus Jakarta Sans
  Size: lg (18px)
  Weight: Semibold
  Color: ink-900
```

### Body Text
```
Primary:
  Font: Inter
  Size: sm (14px)
  Weight: Regular
  Color: ink-900

Secondary:
  Font: Inter
  Size: sm (14px)
  Weight: Regular
  Color: ink-600

Small:
  Font: Inter
  Size: xs (12px)
  Weight: Regular
  Color: ink-500
```

## 🔲 Spacing & Sizing

### Layout Spacing
```
Container: max-w-7xl (1280px)
Padding: px-4 sm:px-6 lg:px-8
Gaps: gap-4 (1rem), gap-6 (1.5rem), gap-8 (2rem)
```

### Component Spacing
```
Card Padding: px-6 py-4
Button Padding: px-4 py-2
Input Padding: px-4 py-2
Modal Padding: p-6
```

### Component Sizes
```
Avatar: w-12 h-12 (48px)
Icon: w-5 h-5 (20px) or w-6 h-6 (24px)
Badge: px-2.5 py-0.5
Button: h-10 (40px)
```

## 🎯 Interactive Elements

### Hover Effects
```
Cards:
  Default: shadow-sm
  Hover: shadow-md
  Transition: all 200ms

Buttons:
  Default: solid background
  Hover: darker background
  Transition: all 200ms

Table Rows:
  Default: white background
  Hover: ink-50 background
  Transition: colors 200ms
```

### Focus States
```
Inputs/Selects:
  Border: 2px solid admin-500
  Ring: ring-2 ring-admin-500
  Outline: none

Buttons:
  Ring: ring-2 ring-offset-2
  Color: admin-500 (primary)
```

### Transitions
```
Modal:
  Enter: opacity 0 → 1, scale 95% → 100%
  Leave: opacity 1 → 0, scale 100% → 95%
  Duration: 200ms

Overlay:
  Enter: opacity 0 → 1
  Leave: opacity 1 → 0
  Duration: 200ms
```

## 📱 Responsive Design

### Breakpoints
```
Mobile:    < 640px   (sm)
Tablet:    640-1024px (sm-lg)
Desktop:   > 1024px  (lg+)
```

### Responsive Grid
```
Stats Cards:
Mobile:  1 column (grid-cols-1)
Tablet:  2 columns (md:grid-cols-2)
Desktop: 4 columns (lg:grid-cols-4)

Form Fields:
Mobile:  1 column (grid-cols-1)
Desktop: 2 columns (md:grid-cols-2)
```

## 🎪 Animations

### Loading Spinner
```css
@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
```

### Live Indicator
```css
@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}
```

### Hover Shadow
```css
transition: box-shadow 200ms ease;
hover:shadow-md
```

## 🎨 Badge Variants

### Job Type Badges
```
Full Time:   Green background (#10b981)
Part Time:   Yellow background (#f59e0b)
Internship:  Blue background (#3b82f6)
Freelance:   Purple background (#8b5cf6)
```

### Experience Level Badges
```
Student: Blue background (#3b82f6)
Entry:   Green background (#10b981)
Junior:  Purple background (#8b5cf6)
```

## 🔍 Accessibility

### Color Contrast
- All text meets WCAG AA standards
- Minimum 4.5:1 for normal text
- Minimum 3:1 for large text

### Keyboard Navigation
- Tab through interactive elements
- Enter to submit forms
- Escape to close modals
- Focus visible on all elements

### Screen Readers
- Semantic HTML (header, main, nav)
- ARIA labels where needed
- Alt text for icons (via title)
- Descriptive button text

## 💡 Design Patterns

### Feedback Patterns
```
Success: Green border + message
Error: Red border + message
Loading: Spinner + disabled state
Empty: Icon + helpful message
```

### Action Patterns
```
Primary Action: Right-aligned, blue
Secondary Action: Left-aligned, gray
Destructive: Confirmation required, red
```

### Data Display Patterns
```
Numbers: Large, bold
Labels: Small, gray
Status: Colored badges
Dates: Relative time
Lists: Cards or rows
```

---

## 🎨 Quick Reference

### Most Used Classes
```css
/* Layout */
.max-w-7xl .mx-auto .px-4 .py-8

/* Cards */
.card .card-header .card-body

/* Buttons */
.btn .btn-primary .btn-secondary .btn-danger

/* Badges */
.badge .badge-success .badge-warning

/* Text */
.text-ink-900 .text-ink-600 .text-ink-500

/* Spacing */
.gap-4 .gap-6 .gap-8 .mb-4 .mt-2
```

### Most Used Colors
```
Primary: text-admin-600, bg-admin-600
Text: text-ink-900, text-ink-600
Background: bg-white, bg-ink-50
Borders: border-ink-200
```

---

This guide ensures consistent, beautiful, and accessible design throughout the admin dashboard! 🎨

