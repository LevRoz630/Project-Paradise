---
layout: page
title: Adding Pages
permalink: /resources/adding-pages/
---

[← Resources]({{ '/resources/' | relative_url }})

---

## Quick Start

1. Create a `.md` file in the appropriate folder
2. Add front matter (title, layout, permalink)
3. Write content in Markdown
4. Commit and push to trigger deploy

---

## File Locations

| Content Type | Location | Layout |
|--------------|----------|--------|
| General pages | Root or relevant folder | `page` |
| Projects | `projects/` | `project` |
| Team members | `team/members/` | `person` |
| Supervisors | `team/supervisors/` | `person` |
| Competitions | `competitions/` | `page` |
| Write-ups | `competitions/write-ups/` | `page` |
| Resources | `resources/` | `page` |

---

## Front Matter Templates

### Standard Page

```yaml
---
layout: page
title: Your Page Title
permalink: /section/page-name/
---
```

### Team Member

```yaml
---
layout: person
title: Full Name
role: member
position: "Year, Major"
university: "University Name"
photo: /assets/images/name.jpg
github: https://github.com/username
linkedin: https://linkedin.com/in/username
---
```

### Supervisor

```yaml
---
layout: person
title: Full Name
role: supervisor
position: "Job Title"
github: https://github.com/username
linkedin: https://linkedin.com/in/username
---
```

---

## Content Formatting

### Navigation Links

Add breadcrumb navigation at the top of subpages:

```markdown
[← Parent Page]({{ '/parent/' | relative_url }})

---
```

### Tables

```markdown
| Column 1 | Column 2 |
|----------|----------|
| Data | Data |
```

### Badges

```html
<span class="badge">Python</span> <span class="badge">ML</span>
```

### Note Boxes

```html
<div class="note">
<p><strong>Note:</strong> Important information here.</p>
</div>
```

### Cards Grid

```html
<div class="cards-grid">
  <div class="card">
    <h3>Title</h3>
    <p>Description</p>
    <a href="#">Link</a>
  </div>
</div>
```

### External Links

```markdown
[Link Text ↗](https://example.com){:target="_blank"}
```

---

## Adding to Navigation

To add a page to the main header navigation, edit `_config.yml`:

```yaml
header_pages:
  - projects/index.md
  - competitions/index.md
  - team/index.md
  - resources/index.md
  - join.md
  - your-new-page.md  # Add here
```

---

## Adding Resources

Add entries to `_data/resources.yml`:

```yaml
- title: "Resource Name"
  url: "https://example.com"
  category: "books"  # getting-started, dev, courses, books, tools
  tags: ["tag1", "tag2"]
  description: "Short description"
  type: "external"  # external, internal, or book
```

For books without links:

```yaml
- title: "Book Title"
  category: "books"
  tags: ["topic"]
  description: "Author Name - Description (ISBN: 978-XXXXXXXXXX)"
  type: "book"
```

---

## Local Development

```bash
# Install dependencies (first time)
bundle install

# Run local server
bundle exec jekyll serve

# View at http://localhost:4000/Project-Paradise/
```

---

## Deployment

The site auto-deploys via GitHub Pages when changes are pushed to `main`.

| Step | Action |
|------|--------|
| 1 | Commit changes |
| 2 | Push to `main` |
| 3 | GitHub Actions builds site |
| 4 | Live at levroz630.github.io/Project-Paradise |

---

## File Naming

| Convention | Example |
|------------|---------|
| Lowercase | `my-page.md` not `My-Page.md` |
| Hyphens for spaces | `write-ups` not `write_ups` |
| Index files for sections | `projects/index.md` |
