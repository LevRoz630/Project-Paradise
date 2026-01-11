# Project Paradise

Jekyll-based website for Project Paradise, a student quantitative research and trading competition project.

## Structure

```
Project-Paradise/
├── _config.yml          # Jekyll configuration
├── Gemfile             # Ruby dependencies
├── index.md            # Homepage
├── _layouts/           # Page templates
├── _includes/          # Reusable components
├── _data/              # YAML data files
├── assets/
│   ├── css/
│   └── images/
├── projects/           # Project documentation
├── competitions/       # Competition information
├── team/              # Team profiles
└── resources/         # Learning materials
```

## Content

- **Projects**: Platform (backtesting tool), Research Publications, Internship Prep Platform
- **Competitions**: Write-ups, potential competitions list (40+), promising competitions
- **Team**: Member and supervisor profiles
- **Resources**: Books, courses, articles, interview prep materials

## Local Development

### Requirements
- Ruby 2.7+
- Bundler

### Setup

```bash
gem install bundler jekyll
bundle install
```

### Run Locally

```bash
bundle exec jekyll serve
```

View at http://localhost:4000

### Build

```bash
bundle exec jekyll build
```

Output in `_site/` directory.

## Deployment

### GitHub Pages

1. Push to GitHub:
   ```bash
   git add .
   git commit -m "Update site"
   git push origin main
   ```

2. Enable GitHub Pages:
   - Go to repository Settings > Pages
   - Source: main branch, root directory
   - Save

3. Site URL: `https://levroz630.github.io/Project-Paradise`

GitHub Pages builds automatically on push to main.

## Configuration

Edit `_config.yml` to update:
- Site title and description
- Base URL and site URL
- Social media links
- Navigation structure

## Customization

### Content Updates

- **Add project**: Create file in `projects/[name]/index.md`
- **Add competition**: Create file in `competitions/write-ups/[name].md`
- **Add team member**: Add to `_data/team_members.yml` and create profile

### Styling

Edit `assets/css/style.scss` for design changes.

### Theme

Current theme: Minima with custom styling. To change:
```yaml
# _config.yml
theme: [theme-name]
```

## Migration

Original Notion export migrated using `migrate.py`:
- Removed Notion hash IDs from filenames
- Converted internal links to Jekyll format
- Organized content into sections
- Converted CSV files to YAML

## Link Validation

```bash
bundle add html-proofer
bundle exec jekyll build
bundle exec htmlproofer ./_site --disable-external
```

## Maintenance

Update content by editing markdown files in respective directories. Changes push automatically to GitHub Pages when merged to main.

## License

Project documentation and content.
