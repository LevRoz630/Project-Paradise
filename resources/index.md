---
layout: page
title: Resources
permalink: /resources/
---

<div class="note">
<p><strong>This is a shared bookshelf.</strong> Books, blog posts, YouTube videos, tools, competition write-ups — if it helped you learn, it belongs here.</p>
<p style="margin-bottom: 0;">Want to add something? Drop it in our <a href="https://github.com/LevRoz630/Project-Paradise/discussions/categories/resources-suggestions" target="_blank">GitHub Discussions ↗</a> with a line about why it was useful, and we'll add it with your name.</p>
</div>

---

<div class="resource-filters">
  <div class="filter-row">
    <span class="filter-label">Category:</span>
    <button class="filter-chip active" data-filter="all">All</button>
    <button class="filter-chip" data-filter="getting-started">Getting Started</button>
    <button class="filter-chip" data-filter="dev">Dev</button>
    <button class="filter-chip" data-filter="courses">Courses</button>
    <button class="filter-chip" data-filter="books">Books</button>
    <button class="filter-chip" data-filter="tools">Tools</button>
  </div>
  <div class="filter-row">
    <span class="filter-label">Tags:</span>
    <div class="tag-filters">
      {% assign all_tags = "" | split: "" %}
      {% for resource in site.data.resources %}
        {% for tag in resource.tags %}
          {% unless all_tags contains tag %}
            {% assign all_tags = all_tags | push: tag %}
          {% endunless %}
        {% endfor %}
      {% endfor %}
      {% assign sorted_tags = all_tags | sort %}
      {% for tag in sorted_tags %}
        <button class="tag-chip" data-tag="{{ tag }}">{{ tag }}</button>
      {% endfor %}
    </div>
  </div>
  <div class="filter-actions">
    <button class="clear-filters" id="clear-tags">Clear tags</button>
    <span class="result-count" id="result-count"></span>
  </div>
</div>

<div class="resources-grid">
{% for resource in site.data.resources %}
  <div class="resource-card" data-category="{{ resource.category }}" data-tags="{{ resource.tags | join: ',' }}">
    <h4>
      {% if resource.type == 'internal' %}
        <a href="{{ resource.url | relative_url }}">{{ resource.title }}</a>
      {% elsif resource.type == 'book' %}
        {{ resource.title }}
      {% else %}
        <a href="{{ resource.url }}" target="_blank">{{ resource.title }} <span class="external-icon">↗</span></a>
      {% endif %}
    </h4>
    <p>{{ resource.description }}</p>
    <div class="resource-tags">
      {% for tag in resource.tags %}<span class="resource-tag">{{ tag }}</span>{% endfor %}
    </div>
  </div>
{% endfor %}
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const categoryFilters = document.querySelectorAll('.filter-chip');
  const tagFilters = document.querySelectorAll('.tag-chip');
  const cards = document.querySelectorAll('.resource-card');
  const clearBtn = document.getElementById('clear-tags');
  const resultCount = document.getElementById('result-count');

  let activeCategory = 'all';
  let activeTags = new Set();

  function getTagsForCategory(category) {
    const tags = new Set();
    cards.forEach(card => {
      if (category === 'all' || card.dataset.category === category) {
        card.dataset.tags.split(',').forEach(tag => tags.add(tag));
      }
    });
    return tags;
  }

  function updateTagVisibility() {
    const availableTags = getTagsForCategory(activeCategory);
    tagFilters.forEach(chip => {
      const tag = chip.dataset.tag;
      if (availableTags.has(tag)) {
        chip.style.display = '';
      } else {
        chip.style.display = 'none';
        if (activeTags.has(tag)) {
          activeTags.delete(tag);
          chip.classList.remove('active');
        }
      }
    });
  }

  function updateResults() {
    let visible = 0;
    cards.forEach(card => {
      const cardCategory = card.dataset.category;
      const cardTags = card.dataset.tags.split(',');

      const categoryMatch = activeCategory === 'all' || cardCategory === activeCategory;
      const tagMatch = activeTags.size === 0 || [...activeTags].some(tag => cardTags.includes(tag));

      if (categoryMatch && tagMatch) {
        card.style.display = '';
        visible++;
      } else {
        card.style.display = 'none';
      }
    });
    resultCount.textContent = visible + ' resource' + (visible !== 1 ? 's' : '');
  }

  categoryFilters.forEach(filter => {
    filter.addEventListener('click', function() {
      categoryFilters.forEach(f => f.classList.remove('active'));
      this.classList.add('active');
      activeCategory = this.dataset.filter;
      updateTagVisibility();
      updateResults();
    });
  });

  tagFilters.forEach(filter => {
    filter.addEventListener('click', function() {
      const tag = this.dataset.tag;
      if (activeTags.has(tag)) {
        activeTags.delete(tag);
        this.classList.remove('active');
      } else {
        activeTags.add(tag);
        this.classList.add('active');
      }
      updateResults();
    });
  });

  clearBtn.addEventListener('click', function() {
    activeTags.clear();
    tagFilters.forEach(f => f.classList.remove('active'));
    updateResults();
  });

  updateTagVisibility();
  updateResults();
});
</script>

---

<div class="note" style="background: var(--bg-gray); border-left-color: var(--text-light);">
<p style="margin-bottom: 0;"><strong style="color: var(--text);">Books:</strong> ISBNs are provided for purchasing or library access. For academic/personal use, books may also be available on <a href="https://annas-archive.li/" target="_blank">Anna's Archive ↗</a>. Please respect copyright laws in your jurisdiction.</p>
</div>

