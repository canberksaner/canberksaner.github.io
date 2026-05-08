---
group: Honors & Awards
date: 2026-01-03
show: true
width: 12
---

<div class="card-body p-4">
  <div class="mx-2 my-1">


    <ul class="list-unstyled mb-0">
  {% for item in site.data.honors_awards %}
  <li class="media mb-2">
    <div class="media-body">
      <div>{{ item.name }}</div>
      <div class="small d-flex">
        <div>
          <strong>{{ item.org }}</strong>
          {% if item.note %}
            <span class="text-muted">({{ item.note }})</span>
          {% endif %}
        </div>
        {% if item.date and item.date != "" %}
          <div class="mt-auto ml-auto no-break">
            <em>{{ item.date }}</em>
          </div>
        {% endif %}
      </div>
    </div>
  </li>
  {% endfor %}
</ul>


  </div>
</div>
