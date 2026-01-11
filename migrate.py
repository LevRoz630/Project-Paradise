#!/usr/bin/env python3
"""
Migration script: Notion export → Jekyll
Transforms Notion export files into clean Jekyll structure
"""

import os
import re
import shutil
import yaml
import csv
from pathlib import Path
from urllib.parse import unquote
from typing import Dict, List, Tuple

# Configuration
SOURCE_DIR = Path(".")
NOTION_HASH_PATTERN = r'\s+[a-f0-9]{24}(?=\.md|\.csv|$)'

# Complete file mapping: Notion export → Jekyll structure
FILE_MAP = {
    # Homepage
    "Project Paradise 21938a8638f880bc97bdcf2692df8d70.md": "index.md",

    # Projects - Platform
    "Platform 2df38a8638f880ceaf4df38261334c75.md": "projects/platform/index.md",
    "Platform/Problem Statement 2e038a8638f880dab3e9c4fdc352bc6e.md": "projects/platform/problem-statement.md",
    "Platform/Solutions on the market 2e038a8638f880f2ae88f8d622eac196.md": "projects/platform/solutions-on-market.md",
    "Platform/Data Source 2e038a8638f880d99740faa507a3f4e1.md": "projects/platform/data-source.md",
    "Platform/Helpful Resources 2e238a8638f880f890daf601a0e5f1bd.md": "projects/platform/helpful-resources.md",
    "Platform/Outline 2e038a8638f880459607d96ef1732f09.md": "projects/platform/outline/index.md",
    "Platform/Outline/Update from last plan 2e438a8638f8801ea6daeb0ca834fe38.md": "projects/platform/outline/update-from-last-plan.md",

    # Projects - Research Publications
    "Research Publications 2df38a8638f880e39614c004e68472bd.md": "projects/research-publications/index.md",
    "Research Publications/Outline 2e138a8638f8809fa032e7cbc1883974.md": "projects/research-publications/outline.md",

    # Projects - Internship Prep Platform
    "TBC - Internship Prep Platform 2e238a8638f88056a12df6a75217617d.md": "projects/internship-prep-platform/index.md",
    "TBC - Internship Prep Platform/Problem Statement 2e238a8638f880c89231cb9bd18e3552.md": "projects/internship-prep-platform/problem-statement.md",
    "TBC - Internship Prep Platform/Existing Solutions 2e238a8638f880a980d9fddf60081af0.md": "projects/internship-prep-platform/existing-solutions.md",
    "TBC - Internship Prep Platform/Helpful Resources 2e238a8638f8809489b4e5788891df8f.md": "projects/internship-prep-platform/helpful-resources.md",
    "TBC - Internship Prep Platform/Outline 2e238a8638f880448658c7b25632f953.md": "projects/internship-prep-platform/outline.md",

    # Competitions - Write-ups
    "Competition Write-Ups 21938a8638f880bb8a5fd674ebf570a8.md": "competitions/write-ups/index.md",
    "Competition Write-Ups/HKU-TA-2 2e238a8638f8802bb5b1cb190fd2ca6d.md": "competitions/write-ups/hku-ta-2.md",
    "Competition Write-Ups/Write-Up Conventions 25938a8638f8809b99b7ef3922b4f3ed.md": "competitions/write-ups/conventions.md",

    # Competitions - Potential
    "Potential Competitions 21938a8638f88007bd06cf065efc78e3.md": "competitions/potential/index.md",

    # Competitions - Promising
    "Promising competitions to take part in (upd 9th Ja 2e338a8638f8805bbdced63932827de3.md": "competitions/promising/index.md",
    "Promising competitions to take part in (upd 9th Ja/Untitled/Harvard Undergraduate Trading Competition 2e338a8638f880a283f2c04ab92efdde.md": "competitions/promising/harvard-utc.md",
    "Promising competitions to take part in (upd 9th Ja/Untitled/UChicago Trading Competition 2e338a8638f880fca565ef55765661e0.md": "competitions/promising/uchicago-tc.md",
    "Promising competitions to take part in (upd 9th Ja/Untitled/Global Quant Trading Challenge 2e338a8638f880b1b993cb4972a59dcc.md": "competitions/promising/global-quant-challenge.md",
    "Promising competitions to take part in (upd 9th Ja/Untitled/Ensimag IF - Algorithmic trading 2025 2e338a8638f8802d9859cbb205353d71.md": "competitions/promising/ensimag-algorithmic-trading.md",
    "Promising competitions to take part in (upd 9th Ja/Untitled/Rotman International Trading Competition 2e338a8638f880bda52add3b307d5321.md": "competitions/promising/rotman-itc.md",
    "Promising competitions to take part in (upd 9th Ja/Untitled/Yale Undergraduate Trading Competition 2e338a8638f8808790f0f46557f8c959.md": "competitions/promising/yale-utc.md",

    # Team - Members
    "Project Members/John Johnson 2e438a8638f88025846ffbb3da360d50.md": "team/members/john-johnson.md",

    # Team - Supervisors
    "Project Supervisors/Jackie Jack 2e438a8638f8807ea15ac1abb314a76d.md": "team/supervisors/jackie-jack.md",

    # Resources
    "Repo Conventions 25938a8638f88067827be74756f5e6d1.md": "resources/repo-conventions.md",
}

# Link mapping for URL conversions (old paths → new Jekyll paths)
LINK_MAP = {
    # Projects
    "Project%20Paradise/Platform%202df38a8638f880ceaf4df38261334c75.md": "/projects/platform/",
    "Platform 2df38a8638f880ceaf4df38261334c75.md": "/projects/platform/",
    "Platform/Problem%20Statement%202e038a8638f880dab3e9c4fdc352bc6e.md": "/projects/platform/problem-statement/",
    "Platform/Solutions%20on%20the%20market%202e038a8638f880f2ae88f8d622eac196.md": "/projects/platform/solutions-on-market/",
    "Platform/Outline%202e038a8638f880459607d96ef1732f09.md": "/projects/platform/outline/",
    "Platform/Data%20Source%202e038a8638f880d99740faa507a3f4e1.md": "/projects/platform/data-source/",
    "Platform/Helpful%20Resources%202e238a8638f880f890daf601a0e5f1bd.md": "/projects/platform/helpful-resources/",
    "Outline/Update%20from%20last%20plan%202e438a8638f8801ea6daeb0ca834fe38.md": "/projects/platform/outline/update-from-last-plan/",
    "Research%20Publications%202df38a8638f880e39614c004e68472bd.md": "/projects/research-publications/",
    "Project%20Paradise/Research%20Publications%202df38a8638f880e39614c004e68472bd.md": "/projects/research-publications/",
    "Research Publications/Outline 2e138a8638f8809fa032e7cbc1883974.md": "/projects/research-publications/outline/",

    # Competitions
    "Project%20Paradise/Competition%20Write-Ups%2021938a8638f880bb8a5fd674ebf570a8.md": "/competitions/write-ups/",
    "Competition Write-Ups 21938a8638f880bb8a5fd674ebf570a8.md": "/competitions/write-ups/",
    "Project%20Paradise/Competitions%202e338a8638f8803f9846ed300640eddd.md": "/competitions/",
    "Project%20Paradise/Potential%20Competitions%2021938a8638f88007bd06cf065efc78e3.md": "/competitions/potential/",
    "Potential Competitions 21938a8638f88007bd06cf065efc78e3.md": "/competitions/potential/",
    "Project%20Paradise/Promising%20competitions%20to%20take%20part%20in%20(upd%209th%20Ja%202e338a8638f8805bbdced63932827de3.md": "/competitions/promising/",

    # Team
    "Project%20Paradise/Project%20Members%202e438a8638f8806f895aec4a6a5443c4.csv": "/team/members/",
    "Project%20Paradise/Project%20Supervisors%202e438a8638f880ff88e4c218c63a11b6.csv": "/team/supervisors/",

    # Resources
    "Project%20Paradise/Repo%20Conventions%2025938a8638f88067827be74756f5e6d1.md": "/resources/repo-conventions/",
    "Repo Conventions 25938a8638f88067827be74756f5e6d1.md": "/resources/repo-conventions/",
}

# Files to skip/delete
SKIP_FILES = [
    "Competitions 2e338a8638f8803f9846ed300640eddd.md",  # Stub file
    "Project Members/Untitled 2e438a8638f8801f97e9cac1171aba0e.md",
    "Project Members/Untitled 2e438a8638f880559a94cc834e7ab6b9.md",
    "Project Members/Untitled 2e438a8638f880808ff5cec46ffd3a5c.md",
    "Project Members/Untitled 2e438a8638f8808baa4afda95461f25e.md",
    "Project Members/Untitled 2e438a8638f880908addd5ff0935ed96.md",
    "Project Members/Untitled 2e438a8638f880b3bf52e68a6f5848d4.md",
    "Project Members/Untitled 2e438a8638f880b7a188c84248a905d4.md",
    "Project Members/Untitled 2e438a8638f880e39d5ff2f805e02b18.md",
    "Project Supervisors/Untitled 2e438a8638f88055a35eff8a0b89bf36.md",
]


def strip_notion_hash(text: str) -> str:
    """Remove Notion hash IDs from text"""
    return re.sub(NOTION_HASH_PATTERN, '', text)


def convert_links(content: str) -> str:
    """Convert Notion-style links to Jekyll-friendly links"""

    def replace_link(match):
        link_text = match.group(1)
        link_path = match.group(2)

        # Skip external links (http/https)
        if link_path.startswith(('http://', 'https://')):
            return f"[{link_text}]({link_path})"

        # URL decode
        decoded_path = unquote(link_path)

        # Check if it's in our link map
        if link_path in LINK_MAP:
            new_path = LINK_MAP[link_path]
            return f"[{link_text}]({new_path})"

        # Try with stripped hash
        clean_path = strip_notion_hash(decoded_path)

        # Try to find match in LINK_MAP by checking values
        for old_path, new_path in LINK_MAP.items():
            old_decoded = unquote(old_path)
            old_clean = strip_notion_hash(old_decoded)
            if old_clean == clean_path:
                return f"[{link_text}]({new_path})"

        # If it's a .csv link, convert to team pages
        if link_path.endswith('.csv'):
            if 'Members' in link_path:
                return f"[{link_text}](/team/members/)"
            elif 'Supervisors' in link_path:
                return f"[{link_text}](/team/supervisors/)"

        # Update image paths
        if link_path.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            image_name = Path(link_path).name
            if 'profile-icon' in image_name:
                return f"[{link_text}](/assets/images/profile-icon.jpg)"
            return f"[{link_text}](/assets/images/{image_name})"

        # Remove broken Notion.so links
        if 'notion.so' in link_path.lower():
            return f"[{link_text}](#)" # Convert to anchor

        # Return as-is if no match found
        return match.group(0)

    # Pattern to match markdown links
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    return re.sub(pattern, replace_link, content)


def extract_title(content: str) -> str:
    """Extract title from first H1 heading"""
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    return match.group(1).strip() if match else "Untitled"


def determine_layout(dest_path: Path) -> str:
    """Determine appropriate layout based on destination path"""
    path_str = str(dest_path)

    if 'projects/' in path_str and not path_str.endswith('index.md'):
        return 'page'
    elif 'projects/' in path_str:
        return 'project'
    elif 'team/' in path_str and path_str.count('/') > 2:  # Individual person pages
        return 'person'
    else:
        return 'page'


def add_front_matter(content: str, dest_path: Path, title: str) -> str:
    """Add YAML front matter to content"""

    layout = determine_layout(dest_path)

    # Build permalink (remove .md, ensure trailing slash for directories)
    permalink = '/' + str(dest_path.with_suffix('')).replace('\\', '/') + '/'
    if permalink.endswith('index/'):
        permalink = permalink[:-6]  # Remove 'index/' but keep trailing slash

    # Base metadata
    metadata = {
        'layout': layout,
        'title': title,
        'permalink': permalink,
    }

    # Add project-specific metadata
    if layout == 'project':
        # We could extract this from content, but for now use defaults
        pass

    # Add person-specific metadata
    if layout == 'person':
        if 'members' in str(dest_path):
            metadata['role'] = 'member'
        elif 'supervisors' in str(dest_path):
            metadata['role'] = 'supervisor'
        metadata['photo'] = '/assets/images/profile-icon.jpg'

    # Convert to YAML and prepend to content
    front_matter = yaml.dump(metadata, sort_keys=False, allow_unicode=True)
    return f"---\n{front_matter}---\n\n{content}"


def migrate_file(source_path: Path, dest_path: Path) -> None:
    """Migrate a single file with all transformations"""

    print(f"Migrating: {source_path} → {dest_path}")

    # Read source file
    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Convert links
    content = convert_links(content)

    # Extract title
    title = extract_title(content)

    # Add front matter
    content = add_front_matter(content, dest_path, title)

    # Create destination directory
    dest_path.parent.mkdir(parents=True, exist_ok=True)

    # Write to destination
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(content)


def csv_to_yaml(csv_path: Path, yaml_path: Path) -> None:
    """Convert CSV to YAML data file, filtering out empty rows"""

    print(f"Converting CSV: {csv_path} → {yaml_path}")

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        # Filter rows that have at least some non-empty values
        data = [row for row in reader if any(v and v.strip() for v in row.values())]

    # Create directory
    yaml_path.parent.mkdir(parents=True, exist_ok=True)

    # Write YAML
    with open(yaml_path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False)


def migrate_assets() -> None:
    """Handle asset migration (images)"""

    print("Migrating assets...")

    # Create assets directory
    assets_dir = Path("assets/images")
    assets_dir.mkdir(parents=True, exist_ok=True)

    # Copy profile icon (deduplicate)
    profile_icon_sources = [
        "profile-icon-design-free-vector.jpg",
        "profile-icon-design-free-vector 1.jpg"
    ]

    for source in profile_icon_sources:
        if Path(source).exists():
            shutil.copy(source, assets_dir / "profile-icon.jpg")
            print(f"Copied: {source} → assets/images/profile-icon.jpg")
            break


def main():
    """Main migration process"""

    print("=" * 60)
    print("Project Paradise: Notion → Jekyll Migration")
    print("=" * 60)
    print()

    # Phase 1: Migrate markdown files
    print("Phase 1: Migrating markdown files...")
    migrated_count = 0
    skipped_count = 0

    for source_file, dest_file in FILE_MAP.items():
        source_path = SOURCE_DIR / source_file
        dest_path = Path(dest_file)

        if not source_path.exists():
            print(f"⚠️  Source not found: {source_path}")
            continue

        if source_file in SKIP_FILES:
            print(f"⏭️  Skipping: {source_file}")
            skipped_count += 1
            continue

        try:
            migrate_file(source_path, dest_path)
            migrated_count += 1
        except Exception as e:
            print(f"❌ Error migrating {source_file}: {e}")

    print(f"\n✅ Migrated {migrated_count} files")
    print(f"⏭️  Skipped {skipped_count} files")

    # Phase 2: Convert CSV to YAML
    print("\nPhase 2: Converting CSV files to YAML...")
    csv_files = [
        ("Project Members 2e438a8638f8806f895aec4a6a5443c4.csv", "_data/team_members.yml"),
        ("Project Supervisors 2e438a8638f880ff88e4c218c63a11b6.csv", "_data/supervisors.yml"),
    ]

    for csv_file, yaml_file in csv_files:
        csv_path = SOURCE_DIR / csv_file
        yaml_path = Path(yaml_file)

        if csv_path.exists():
            try:
                csv_to_yaml(csv_path, yaml_path)
            except Exception as e:
                print(f"❌ Error converting {csv_file}: {e}")

    # Phase 3: Migrate assets
    print("\nPhase 3: Migrating assets...")
    try:
        migrate_assets()
    except Exception as e:
        print(f"❌ Error migrating assets: {e}")

    print("\n" + "=" * 60)
    print("✅ Migration complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Review migrated files for accuracy")
    print("2. Create landing pages for each section")
    print("3. Test locally: bundle exec jekyll serve")
    print("4. Validate links: bundle exec htmlproofer ./_site")
    print()


if __name__ == "__main__":
    main()
