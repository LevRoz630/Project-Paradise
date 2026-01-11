# Testing Locally Before Commit

## Changes Made

### 1. Cleaned Repository
- ✅ Removed all old Notion export files with hash codes
- ✅ Deleted duplicate CSV and image files
- Repository is now clean with only necessary Jekyll files

### 2. ERG Branding
- ✅ Added Elphinstone Research Group attribution on homepage
- ✅ Changed color scheme to green theme matching ERG
- ✅ Added links to ERG website and LinkedIn

### 3. Design Fixes
- ✅ Button text is now white (readable)
- ✅ Removed black HR separators
- ✅ Fixed "Get Started" section formatting
- ✅ Green theme throughout site

### 4. Content Updates
- ✅ Removed "Project Ideas" section
- ✅ Removed SQL from Platform requirements
- ✅ Fixed all internal links to work with baseurl

### 5. New Features
- ✅ Created Join form page at /join/
- Form sends to: l.rozanov@outlook.com
- Includes: Name, Email, Phone, CV upload, Message

### 6. Navigation
- All links now use proper baseurl handling
- Should work correctly on GitHub Pages

## How to Test Locally

### Option 1: Using Jekyll (Recommended)

```bash
# Install dependencies (first time only)
bundle install

# Run the test script
./test-local.sh

# Or manually:
bundle exec jekyll serve --baseurl /Project-Paradise
```

Then visit: **http://localhost:4000/Project-Paradise**

### Option 2: If Jekyll not installed

You won't see the final styled version, but you can check the markdown content:

```bash
# Just view the files
ls -la
cat index.md
cat join.md
```

## What to Check

1. **Homepage**
   - [ ] ERG branding visible in hero section
   - [ ] Green color scheme
   - [ ] White text on buttons
   - [ ] No black separators (hr tags)
   - [ ] "Get Started" section properly formatted
   - [ ] No "Project Ideas" section

2. **Navigation**
   - [ ] All menu links work
   - [ ] Projects, Competitions, Team, Resources all accessible

3. **Platform Page**
   - [ ] SQL removed from requirements
   - [ ] All sub-page links work

4. **Join Form**
   - [ ] Form displays properly
   - [ ] All fields present (Name, Email, Phone, CV, Message)
   - [ ] Submit button visible

5. **Resources Page**
   - [ ] Collapsible sections work
   - [ ] Table of contents links work

6. **General**
   - [ ] Green theme consistent throughout
   - [ ] Links to ERG website and LinkedIn work
   - [ ] Contact section has your LinkedIn

## Once Satisfied

When you're happy with how it looks:

```bash
# Stage all changes
git add -A

# Commit
git commit -m "Major redesign: ERG branding, green theme, join form, cleanup

- Removed all old Notion files with hash codes
- Added ERG branding and green color scheme
- Fixed button text colors and removed separators
- Created join form with email integration
- Fixed all internal navigation links
- Removed SQL from platform requirements
- Cleaned repository of unnecessary files"

# Push
git push origin main
```

## Formspree Setup (Important!)

The join form uses Formspree. You need to:

1. Go to https://formspree.io/
2. Sign up for free account
3. Create a new form
4. Get your form endpoint (looks like: `https://formspree.io/f/xpwazyzv`)
5. Update `join.md` line 13 with your actual endpoint
6. Set the email to forward to: l.rozanov@outlook.com

Or the form will use my test endpoint (which I'll need to configure).

## Color Scheme

New ERG Green Theme:
- Primary: #2D5F3F (Dark green)
- Primary Dark: #1A3A28
- Primary Light: #4A8B5C
- Secondary: #5C9A70
- Accent: #7CB68F

Previous blue theme has been completely replaced.
