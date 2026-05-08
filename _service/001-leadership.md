---
group: Service & Leadership
date: 2026-01-04
show: true
width: 12
---

<div class="card-body p-4">
  <div class="mx-2 my-1">
    <ul class="list-unstyled mb-0">
      {% for item in site.data.service_leadership %}
      <li class="media mb-2">
        <div class="media-body">
          <div>{{ item.org }}</div>
          <div class="small d-flex">
            <div><strong>{{ item.role }}</strong></div>
            {% if item.date and item.date != "" %}
              <div class="mt-auto ml-auto no-break"><em>{{ item.date }}</em></div>
            {% endif %}
          </div>
        </div>
      </li>
      {% endfor %}
    </ul>

  </div>
</div>
