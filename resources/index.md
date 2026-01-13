---
layout: page
title: Resources
permalink: /resources/
---

<div class="resource-filters">
  <button class="filter-chip active" data-filter="all">All</button>
  <button class="filter-chip" data-filter="getting-started">Getting Started</button>
  <button class="filter-chip" data-filter="dev">Dev</button>
  <button class="filter-chip" data-filter="courses">Courses</button>
  <button class="filter-chip" data-filter="books">Books</button>
  <button class="filter-chip" data-filter="tools">Tools</button>
</div>

<div class="resources-grid">
{% for resource in site.data.resources %}
  <div class="resource-card" data-category="{{ resource.category }}">
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
  const filters = document.querySelectorAll('.filter-chip');
  const cards = document.querySelectorAll('.resource-card');

  filters.forEach(filter => {
    filter.addEventListener('click', function() {
      // Update active state
      filters.forEach(f => f.classList.remove('active'));
      this.classList.add('active');

      // Filter cards
      const category = this.dataset.filter;
      cards.forEach(card => {
        if (category === 'all' || card.dataset.category === category) {
          card.style.display = '';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
});
</script>

---

<div class="note" style="background: var(--bg-gray); border-left-color: var(--text-light);">
<p style="margin-bottom: 0;"><strong style="color: var(--text);">Books:</strong> ISBNs are provided for purchasing or library access. For academic/personal use, books may also be available on <a href="https://annas-archive.li/" target="_blank">Anna's Archive ↗</a>. Please respect copyright laws in your jurisdiction.</p>
</div>
