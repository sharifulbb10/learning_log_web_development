### Mental Maps of Django Processes
---

##### <span style="color: darkred;">Quick links</span>
<div style="width: 100%; height: 2px; background-color: darkred;"></div>

📎 &nbsp; [<span style="color: darkred; font-weight: bold;">Work flow of url mapping in django</span>](#work-flow-of-url-mapping-in-django) <br/>
📎 &nbsp; [<span style="color: darkred; font-weight: bold;">How to navigate through html pages from server side django?</span>](#how-to-navigate-through-html-pages-from-server-side-django) <br/>
📎 &nbsp; [<span style="color: darkred; font-weight: bold;">How to add stylings and javascript to an existing html file with django?</span>](#how-to-add-stylings-and-javascript-to-an-existing-html-file-with-django) <br/>
📎 &nbsp; [<span style="color: darkred; font-weight: bold;">How to connect a database, django system and the website?</span>](#how-to-connect-a-database-django-system-and-the-website) <br/>
📎 &nbsp; [<span style="color: darkred; font-weight: bold;">How to post data to database table from html (say, user authentication)?</span>](#how-to-post-data-to-database-table-from-html-say-user-authentication) <br/>

##### <span style="color: forestgreen;">✅ Work flow of url mapping in django [\*](#mental-maps-of-django-processes)</span>
<div style="width: 100%; height: 1px; background-color: darkolivegreen; margin-top: -5px;"></div>

| 1  							 | 2             | 3                     | 4         | 5           | 6            |
|------------------|---------------|-----------------------|-----------|-------------|--------------|
| `folder/html file` | `./settings.py` | `app (website segment)` | `./urls.py` | `app/urls.py` | `app/views.py` |
| **Create a folder, add an html file** | **Set this folder as base directory** | **Create an app and a `urls.py` file** | **Include the path** | **Declare the path and a function** | **Define the function, tell it how to render html file** |

___

**How I connected an html page to django:**

1. Installed django
```bash
pip install django
django-admin --version
```
2. Started a project
```bash
django-admin startproject my_project
ls
```

3. Open a folder in the project folder `templates`, create an html file `home.html`.

4. Add `templates` folder in `./settings.py` file.

```python
from pathlib import Path
import os

# ...existing lines...

TEMPLATES = [
	# ...existing lines...
	'DIRS': [os.path.join(BASE_DIR, 'templates')],
	# ...existing lines...
]
```

5. Create an app `my_home` and `my_home/urls.py`.

```bash
python3 manage.py startapp my_home
```

6. Include `my_home/urls.py` in to the list of `./urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('my_home.urls')),
    path('admin/', admin.site.urls),
]
```

7. Edit `my_home/urls.py`:

```python
from django.urls import path, include
urlpatterns = [path('', include('calc.urls')), path('admin/', admin.site.urls)]
```

8. Edit `my_home/views.py`:

```python
from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'home.html')
```
___

##### <span style="color: forestgreen;">✅ How to navigate through html pages from server side django? [\*](#mental-maps-of-django-processes)</span>
<div style="width: 100%; height: 1px; background-color: darkolivegreen; margin-top: -5px;"></div>

| 1 | 2 | 3 | 4 |
|---|---|---|---|
| **1. In the base directory's html page, create a form** | **2. In local urls.py, add a path** | **3. In local views.py, add a function rendering a new html page** | **4. With jinja format, transfer the new html segment to base directory's html page** |

___

**What I did?**

1. Added a form in base html page.

```html
<h1>My Home Page</h1>
{% block content %}
	<form action="message" method="POST">
		{% csrf_token %}
		Put a short message: <input type="text" name="msg"/>
		<br/>
		<input type="submit" />
	</form>
{% endblock %}
```

2. In the local `urls.py`:

```pyhton
urlpatterns = [path('', views.home, name="home"), path('message', views.message, name="msg")]
```

3. In the local `views.py`:
```python
# Create your views here.
def home(request):
  return render(request, 'home.html')

def message(request):
  msg = request.POST['msg']
  return render(request, 'message.html', {'msg': msg})
```

4. Created a new html file - `templates/message.html`, in this:
```html
{% extends 'home.html' %}
{% block content %}
	<p>You have typed: <span style="color: red;">{{msg}}</span></p>
{% endblock %}
```
___

##### <span style="color: forestgreen;">✅ How to add stylings and javascript to an existing html file with django? [\*](#mental-maps-of-django-processes)</span>
<div style="width: 100%; height: 1px; background-color: darkolivegreen; margin-top: -5px;"></div>

| 1 | 2 | 3 | 4 |
|---|---|---|---|
| **Create a new folder - `static`, put `.css` and `.js` files here** | **In `./settings.py` file, set static file directory and root file directory ( naming `assets`)** | **Run command `python3 manage.py collectstatic`** | **load static in html file, modify src and href paths** |

___

**What I did?**

1. Initially, I created a folder `static` and also created `static/styles/style.css`, `static/js/script.js`. I added `style.css` and `script.js` to the home directory's html file.

2. In `./settings.py` file, I wrote:

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static')]	# added line
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')					# added line
```

3. From project directory's command line, executed:

```bash
python3 manage.py collectstatic
```

4. Modified base html file:

```html
{% load static %}
<DOCTYOE html>
	
<!-- existing lines -->

<!-- Modified <link rel="stylesheet" type="text/css" href="styles/style.css"> to -->
	<link rel="stylesheet" type="text/css" href="{% static 'styles/style.css' %}">

<!-- ... existing lines ... -->

<!-- Modified <script src="js/script.js"></script> to -->
	<script src="{% static 'js/script.js' %}"></script>
```
___

##### <span style="color: forestgreen;">✅ How to connect a database, django system and the website? [\*](#mental-maps-of-django-processes)</span>
<div style="width: 100%; height: 1px; background-color: darkolivegreen; margin-top: -5px;"></div>

| 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|
| **Create a database** | **Install a database adaptor** | **Configure the `DATABASES` in project level `settings.py` in Django** | **Configure a class in app level `models.py` (as per the table we want in DB)** | **Include the app in the project level `settings.py`'s `INSTALLED_APPS` list** | **Finally, migrate things** | **In case we want further DB table's modification, modify app level `models.py`, then migrate again** |

___

**What I did?**

1. Open a new Database from pgAdmin or Dbeaver:

`Right click on 'Database(1)' -> Select 'Create' -> Select 'Database..' -> Configure`

2. Installed a database adaptor/connector:

```bash
pip install psycopg2
```

3. Configured project level `settings.py`:

```python
# ...existing lines...

DATABASES = {
  'default': {
    # replacing 'sqlite3'
    'ENGINE': 'django.db.backends.postgresql',
    # replace with db_name here
    'NAME': 'telusko', 
    # set credentials as well - configured during postgreSQL setup
    'USER': 'postgres',
    'PASSWORD': '1234',
    # mention host
    'HOST': 'localhost'
  }
}
```

4. Configure the app level `models.py`:

```python
from django.db import models

# create your models here
class Destination(models.Model):

  # see official documentation of django model fields for reference
  name = models.CharField(max_length = 100)
  img = models.ImageField(upload_to = 'pics')
  desc = models.TextField()
  # price = models.IntegerField()   # we'll add it later
  offer = models.BooleanField(default = False)
```

5. Let the project level `settings.py` to know about this configuration:

```python
# ...existing lines...

# Application definition
INSTALLED_APPS = [
  'travello.apps.TravelloConfig',   # added line
  'django.contrib.admin', 
  # ...other configs...
]
```

6. Migration stage:

```bash
# to handle image upload (do once)
pip install Pillow

python manage.py makemigrations
# a new file '0001_initial.py' will be visible in 'travello' folder

# we have migrated the model only, no table is still created in database
# so need to migrate '0001_initial.py' from 'travello' folder 
python3 manage.py sqlmigrate travello 0001
python3 manage.py migrate
```

Finally, find a table in the database.

##### <span style="color: forestgreen;">✅ How to upload data to database table from django Admin Panel? [\*](#mental-maps-of-django-processes)</span>
<div style="width: 100%; height: 1px; background-color: darkolivegreen; margin-top: -5px;"></div>

<div style="text-align: center; font-weight: bold;">Create a super user with corresponding terminal command</div>
<div style="text-align: center; font-weight: bold;">'</div>
<div style="text-align: center; font-weight: bold;">Import and register the existing model to the app level <code>models.py</code></div>
<div style="text-align: center; font-weight: bold;">'</div>
<div style="text-align: center; font-weight: bold;">ADDITIONAL: For image and file upload, configure media path in the project level <code>urls.py</code></div>
<div style="text-align: center; font-weight: bold;">'</div>
<div style="text-align: center; font-weight: bold;">Include that media path to project level <code>settings.py</code></div>

##### <span style="color: forestgreen;">✅ How to post data to database table from html (say, user authentication)? [\*](#mental-maps-of-django-processes)</span>
<div style="width: 100%; height: 1px; background-color: darkolivegreen; margin-top: -5px;"></div>

<div style="text-align: center; font-weight: bold;">Create a form in a seperate html page</div>
<div style="text-align: center; font-weight: bold;">'</div>
<div style="text-align: center; font-weight: bold;">Create a new app (website segment)</div>
<div style="text-align: center; font-weight: bold;">'</div>
<div style="text-align: center; font-weight: bold;">Add path to app level <code>urls.py</code></div>
<div style="text-align: center; font-weight: bold;">'</div>
<div style="text-align: center; font-weight: bold;">Configure app level <code>views.py</code><br/><i>(set corresponding logics for user authentication)</i></div>
<div style="text-align: center; font-weight: bold;">'</div>
<div style="text-align: center; font-weight: bold;">Include path to project level <code>urls.py</code></div>