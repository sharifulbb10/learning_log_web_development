### django big questions
---

1. do i need to use react routers while using django, because django serves jinja format plus url mapping to navigate pages?

[answer explained]()
**Short answer:**

* You **do NOT need React Router** if Django handles page routing (Django templates or small React components).
* You **DO need React Router** if React is a **full frontend (SPA)** and Django is only a **backend/API**.
* If React is built and served by Django, **React Router is still needed**.
* **Learn Django first**, then learn React Router when building a full React-based app.

**Rule of thumb:**
👉 *Django routes pages on the server; React Router routes pages in the browser.*
