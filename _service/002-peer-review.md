---
group: Peer Review
date: 2026-01-02
show: true
width: 12
---

<div class="card-body p-4">
  <div class="mx-2 my-1">

    <ul class="square-list mb-0">
      {% for journal in site.data.peer_review %}
      <li>{{ journal }}</li>
      {% endfor %}
    </ul>

  </div>
</div>
