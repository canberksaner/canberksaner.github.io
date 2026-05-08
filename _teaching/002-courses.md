---
group: Courses Supported
date: 2025-01-01
show: true
width: 12
class: card border-0 shadow-sm bg-white
---


<div class="card-body p-4">

  <!-- ================= Lecture based ================= -->
  {% if site.data.teaching_courses.lecture_based %}
  <h4 class="mt-3 mb-2">Lecture-based</h4>

  <div class="row">

    {% assign lectures = site.data.teaching_courses.lecture_based %}
    {% assign half_lect = lectures | size | divided_by: 2 | plus: 0 %}

    <div class="col-lg-6">
      <ul class="list-unstyled mb-1">
        {% for c in lectures limit: half_lect %}
        <li class="media mb-2">
          <img src="{{ c.logo | relative_url }}" alt="{{ c.uni }}" style="width: 30px;" class="mr-2 mt-1">
          <div class="media-body">
            <div><strong>{{ c.code }}</strong> {{ c.title }}</div>
            <div class="small text-muted">{{ c.uni }}</div>
            {% if c.level %}
            <div class="small text-muted"><em>{{ c.level }}</em></div>
            {% endif %}
          </div>
        </li>
        {% endfor %}
      </ul>
    </div>

    <div class="col-lg-6">
      <ul class="list-unstyled mb-1">
        {% for c in lectures offset: half_lect %}
        <li class="media mb-2">
          <img src="{{ c.logo | relative_url }}" alt="{{ c.uni }}" style="width: 30px;" class="mr-2 mt-1">
          <div class="media-body">
            <div><strong>{{ c.code }}</strong> {{ c.title }}</div>
            <div class="small text-muted">{{ c.uni }}</div>
            {% if c.level %}
            <div class="small text-muted"><em>{{ c.level }}</em></div>
            {% endif %}
          </div>
        </li>
        {% endfor %}
      </ul>
    </div>

  </div>
  {% endif %}

  <!-- ================= Lab / Project based ================= -->
  {% if site.data.teaching_courses.lab_project_based %}
  <h4 class="mt-4 mb-2">Lab and Project-based</h4>

  <div class="row">

    {% assign labs = site.data.teaching_courses.lab_project_based %}
    {% assign half_lab = labs | size | divided_by: 2 | plus: 1 %}

    <div class="col-lg-6">
      <ul class="list-unstyled mb-1">
        {% for c in labs limit: half_lab %}
        <li class="media mb-2">
          <img src="{{ c.logo | relative_url }}" alt="{{ c.uni }}" style="width: 30px;" class="mr-2 mt-1">
          <div class="media-body">
            <div><strong>{{ c.code }}</strong> {{ c.title }}</div>
            <div class="small text-muted">{{ c.uni }}</div>
            {% if c.level %}
            <div class="small text-muted"><em>{{ c.level }}</em></div>
            {% endif %}
          </div>
        </li>
        {% endfor %}
      </ul>
    </div>

    <div class="col-lg-6">
      <ul class="list-unstyled mb-1">
        {% for c in labs offset: half_lab %}
        <li class="media mb-2">
          <img src="{{ c.logo | relative_url }}" alt="{{ c.uni }}" style="width: 30px;" class="mr-2 mt-1">
          <div class="media-body">
            <div><strong>{{ c.code }}</strong> {{ c.title }}</div>
            <div class="small text-muted">{{ c.uni }}</div>
            {% if c.level %}
            <div class="small text-muted"><em>{{ c.level }}</em></div>
            {% endif %}
          </div>
        </li>
        {% endfor %}
      </ul>
    </div>

  </div>
  {% endif %}
  
<p class="text-muted mt-3 mb-2">
    All courses listed above were supported in the role of Teaching Assistant.
</p>

</div>
