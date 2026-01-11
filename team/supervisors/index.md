---
layout: page
title: Project Supervisors
permalink: /team/supervisors/
description: Mentors and advisors guiding Project Paradise
---

# Project Supervisors

Our supervisors are experienced professionals in quantitative finance, trading, and software engineering who provide mentorship and guidance to Project Paradise members.

{% if site.data.supervisors %}
<div class="team-cards">
{% for supervisor in site.data.supervisors %}
  <div class="card">
    {% if supervisor.Photo %}
    <img src="{{ supervisor.Photo }}" alt="{{ supervisor.Name }}" class="person-photo" />
    {% endif %}
    <h3>{{ supervisor.Name }}</h3>

    {% if supervisor.Position %}
    <p><strong>Position:</strong> {{ supervisor.Position }}</p>
    {% endif %}

    {% if supervisor["Areas of Interest"] %}
    <p><strong>Areas of Interest:</strong> {{ supervisor["Areas of Interest"] }}</p>
    {% endif %}

    {% if supervisor.Bio %}
    <p>{{ supervisor.Bio }}</p>
    {% endif %}

    {% if supervisor.LinkedIn %}
    <div class="person-links">
      <a href="{{ supervisor.LinkedIn }}" target="_blank">LinkedIn</a>
    </div>
    {% endif %}

    <a href="/team/supervisors/{{ supervisor.Name | slugify }}/">View Profile →</a>
  </div>
{% endfor %}
</div>
{% else %}
<p>Supervisor information coming soon.</p>
{% endif %}

---

## Current Supervisors

### Jackie Jack
Burger Price Modeller at CrabsyCrabs

[View full profile →](/team/supervisors/jackie-jack/)

---

## Become a Mentor

Are you an experienced professional interested in mentoring the next generation of quantitative traders and researchers? We're always looking for supervisors who can:

- Provide technical guidance on projects
- Share industry insights and career advice
- Review research and code contributions
- Connect students with internship and job opportunities

If you're interested, please reach out to discuss how you can contribute to Project Paradise.

---

<div class="note" style="background-color: #f6f8fa; padding: 1em; border-left: 4px solid #0366d6; margin: 2em 0;">
<strong>Acknowledgment:</strong> We're grateful to our supervisors for their time, expertise, and dedication to helping students develop careers in quantitative finance.
</div>
