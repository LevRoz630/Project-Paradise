# Project Paradise - Jekyll Site

This repository contains the Project Paradise website, migrated from a Notion export to a Jekyll-based GitHub Pages site.

## Site Structure

```
Project-Paradise/
├── _config.yml                 # Jekyll configuration
├── Gemfile                     # Ruby dependencies
├── index.md                    # Homepage
├── _layouts/                   # Page layouts
│   ├── default.html
│   ├── page.html
│   ├── project.html
│   └── person.html
├── _includes/                  # Reusable components
│   ├── header.html
│   ├── footer.html
│   ├── navigation.html
│   └── head.html
├── _data/                      # Data files
│   ├── team_members.yml
│   └── supervisors.yml
├── assets/
│   ├── css/main.css
│   └── images/profile-icon.jpg
├── projects/                   # Project pages
│   ├── index.md
│   ├── platform/
│   ├── research-publications/
│   └── internship-prep-platform/
├── competitions/               # Competition pages
│   ├── index.md
│   ├── write-ups/
│   ├── potential/
│   └── promising/
├── team/                       # Team pages
│   ├── index.md
│   ├── members/
│   └── supervisors/
└── resources/                  # Resources
    ├── index.md
    └── repo-conventions.md
```

## Content Summary

### Migrated Content
- ✅ **29 markdown files** successfully migrated from Notion
- ✅ **All internal links** converted from Notion format to Jekyll paths
- ✅ **2 CSV files** converted to YAML data files
- ✅ **Images** deduplicated and organized
- ✅ **Landing pages** created for all major sections

### Content Organization
- **Projects**: 3 main projects (Platform, Research Publications, Internship Prep)
- **Competitions**: Write-ups, 40+ potential competitions, 6 promising competitions
- **Team**: 1 member, 1 supervisor (empty profiles removed)
- **Resources**: Curated books, courses, articles, and tools

## Local Testing

### Prerequisites
- Ruby (2.7 or higher)
- Bundler

### Installation & Testing

1. **Install dependencies:**
   ```bash
   gem install bundler jekyll
   bundle install
   ```

2. **Serve the site locally:**
   ```bash
   bundle exec jekyll serve --livereload
   ```

3. **View in browser:**
   Open http://localhost:4000

### Build Site

```bash
bundle exec jekyll build
```

The built site will be in the `_site/` directory.

## Link Validation

To validate that all links are working correctly:

```bash
# Install html-proofer
bundle add html-proofer

# Build and validate
bundle exec jekyll build
bundle exec htmlproofer ./_site --disable-external --allow-hash-href
```

## GitHub Pages Deployment

### Option 1: Automatic Deployment (Recommended)

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Migrate Notion export to Jekyll for GitHub Pages"
   git push origin main
   ```

2. **Enable GitHub Pages:**
   - Go to repository Settings
   - Navigate to "Pages" section
   - Set Source to "main" branch, root directory
   - Click Save

3. **Access your site:**
   - Your site will be available at: `https://levroz630.github.io/Project-Paradise`
   - GitHub Pages will automatically rebuild when you push changes

### Option 2: Custom Domain

If you want to use a custom domain:
1. Add a `CNAME` file with your domain name
2. Configure DNS settings with your domain provider
3. Enable "Enforce HTTPS" in GitHub Pages settings

## Customization

### Updating Content

- **Add new project:** Create markdown file in `projects/[project-name]/index.md`
- **Add competition write-up:** Create file in `competitions/write-ups/`
- **Add team member:**
  1. Add entry to `_data/team_members.yml`
  2. Create profile page in `team/members/[name].md`

### Styling

Custom CSS is in `assets/css/main.css`. The site uses the Minima theme as a base, which you can override.

### Theme Changes

To change themes, update `_config.yml`:
```yaml
theme: minima  # Change to: jekyll-theme-cayman, minimal-mistakes, etc.
```

Popular alternatives:
- `jekyll-theme-cayman` - Clean GitHub-styled theme
- `minimal-mistakes` - Feature-rich, highly customizable
- `just-the-docs` - Documentation-focused theme

## Migration Details

### What Was Changed

1. **File naming:** Removed Notion hash IDs (e.g., `21938a8638f880bc97bdcf2692df8d70`)
2. **Directory structure:** Organized by content type (Projects/Competitions/Team/Resources)
3. **Links:** Converted URL-encoded Notion links to clean Jekyll paths
4. **Front matter:** Added YAML metadata to all pages
5. **Assets:** Deduplicated images and moved to `assets/images/`
6. **Data files:** Converted CSV to YAML for Jekyll data integration

### What Was Removed

- 9 empty pages (8 "Untitled" members, 1 "Untitled" supervisor, 1 stub)
- Duplicate image files
- CSV files (converted to YAML)

### Known Issues

- Some Notion.so links in competition write-ups table point to unpublished pages (converted to # anchors)
- External links preserved but not validated

## Maintenance

### Regular Updates

- **Monthly:** Review and update competition deadlines
- **Quarterly:** Check external links for 404s
- **Per project:** Add new team members/supervisors as they join

### Content Workflow

```bash
# Create new branch for content updates
git checkout -b content/new-feature

# Make changes to markdown files
# ...

# Test locally
bundle exec jekyll serve

# Commit and push
git add .
git commit -m "Add new competition write-up"
git push origin content/new-feature

# Create PR and merge to main
# GitHub Pages will auto-deploy
```

## Troubleshooting

### Build Fails

**Issue:** Jekyll build fails with dependency errors

**Solution:**
```bash
bundle update
bundle install
```

### Links Not Working

**Issue:** Internal links return 404

**Solution:** Check that:
- Filenames are lowercase with hyphens (kebab-case)
- Links use Jekyll permalink format: `/section/page/`
- Front matter includes correct permalink

### Images Not Loading

**Issue:** Images show broken

**Solution:**
- Verify images are in `assets/images/`
- Check paths use `/assets/images/filename.jpg`
- Ensure images were committed to repository

## Support

- **Jekyll Documentation:** https://jekyllrb.com/docs/
- **GitHub Pages:** https://docs.github.com/en/pages
- **Minima Theme:** https://github.com/jekyll/minima

## License

Content and documentation for Project Paradise. Check individual projects and resources for their respective licenses.

---

**Last Updated:** January 2026
**Migration Script:** `migrate.py`
**Jekyll Version:** 4.3.0
