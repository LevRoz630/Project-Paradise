---
layout: page
title: Project Members
permalink: /team/members/
description: Students participating in Project Paradise
---

# Project Members

Our team members are students from various universities who share a passion for quantitative finance and algorithmic trading.

{% if site.data.team_members %}
<div class="team-cards">
{% for member in site.data.team_members %}
  <div class="card">
    {% if member.Photo %}
    <img src="{{ member.Photo }}" alt="{{ member.Name }}" class="person-photo" />
    {% endif %}
    <h3>{{ member.Name }}</h3>

    {% if member.University %}
    <p><strong>University:</strong> {{ member.University }}</p>
    {% endif %}

    {% if member["Area of Interest"] %}
    <p><strong>Interests:</strong> {{ member["Area of Interest"] }}</p>
    {% endif %}

    {% if member["Competitions/Projects"] %}
    <p><strong>Projects:</strong> {{ member["Competitions/Projects"] }}</p>
    {% endif %}

    {% if member.GitHub or member.LinkedIn %}
    <div class="person-links">
      {% if member.GitHub %}
      <a href="{{ member.GitHub }}" target="_blank">GitHub</a>
      {% endif %}
      {% if member.LinkedIn %}
      <a href="{{ member.LinkedIn }}" target="_blank">LinkedIn</a>
      {% endif %}
    </div>
    {% endif %}

    <a href="/team/members/{{ member.Name | slugify }}/">View Profile →</a>
  </div>
{% endfor %}
</div>
{% else %}
<p>Team member information coming soon.</p>
{% endif %}

---

## Current Members

### John Johnson
Student researcher working on HKU & Avenir Backtester Library and ML Paper.

[View full profile →](/team/members/john-johnson/)

---

<div class="note" style="background-color: #f6f8fa; padding: 1em; border-left: 4px solid #0366d6; margin: 2em 0;">
<strong>Note:</strong> This page is continuously updated as new members join the project. If you're interested in joining, check out our <a href="/team/">Team page</a> for more information.
</div>
