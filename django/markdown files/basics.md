### DJango Basics
___

##### <span style="color: darkred;">Quick links</span>
<div style="width: 100%; height: 2px; background-color: darkred;"></div>

📎 &nbsp; [<span style="color: darkred; font-weight: bold;">How to check whether django is installed or not in a folder?</span>](#how-to-check-whether-django-is-installed-or-not-in-a-folder) <br/>
📎 &nbsp; [<span style="color: darkred; font-weight: bold;">How to create python virtual environment?</span>](#how-to-create-python-virtual-environment) <br/>
📎 &nbsp; [<span style="color: darkred; font-weight: bold;">How to install django?</span>](#how-to-install-django) <br/>
📎 &nbsp; [<span style="color: darkred; font-weight: bold;">How to create a django project?</span>](#how-to-create-a-django-project) <br/>
📎 &nbsp; [<span style="color: darkred; font-weight: bold;">How to run our django project?</span>](#how-to-run-our-django-project) <br/>
📎 &nbsp; [<span style="color: darkred; font-weight: bold;">What is app in django?</span>](#what-is-app-in-django) <br/>
📎 &nbsp; [<span style="color: darkred; font-weight: bold;">How to create an app in django?</span>](#how-to-create-an-app-in-django) <br/>
📎 &nbsp; [<span style="color: darkred; font-weight: bold;">How to render 'hello world' to the server page of django project (url mapping) </spanbr/>?</span>](#how-to-render-hello-world-to-the-server-page-of-django-project-url-mapping) <br/>
📎 &nbsp; [<span style="color: darkred; font-weight: bold;">What is `django templates`?</span>](#what-is-django-templates) <br/>
📎 &nbsp; [<span style="color: darkred; font-weight: bold;">How to render a webpage in django server (using django template) </spanbr/>?</span>](#how-to-render-a-webpage-in-django-server-using-django-template) <br/>
📎 &nbsp; [<span style="color: darkred; font-weight: bold;">how to render any dynamic data to the webpage in django?</span>](#how-to-render-any-dynamic-data-to-the-webpage-in-django) <br/>
📎 &nbsp; [<span style="color: darkred; font-weight: bold;">How to do an operation (addition of two numbers) </spanbr/> in webpage with django?</span>](#how-to-do-an-operation-addition-of-two-numbers-in-webpage-with-django) <br/>
📎 &nbsp; [<span style="color: darkred; font-weight: bold;">What is the difference between GET and POST method?</span>](#what-is-the-difference-between-get-and-post-method) <br/>
📎 &nbsp; [<span style="color: darkred; font-weight: bold;">What is MVT framework?</span>](#what-is-mvt-framework) <br/>
📎 &nbsp; [<span style="color: darkred; font-weight: bold;">How can we connect a frontend website to django?</span>](#how-can-we-connect-a-frontend-website-to-django) <br/>
📎 &nbsp; [<span style="color: darkred; font-weight: bold;">How can we render data dynamically to an html webpage?</span>](#how-can-we-render-data-dynamically-to-an-html-webpage) <br/>
📎 &nbsp; [<span style="color: darkred; font-weight: bold;">How to run an `if` conditional statement in django?</span>](#how-to-run-an-if-conditional-statement-in-django) <br/>
📎 &nbsp; [<span style="color: darkred; font-weight: bold;">What is `ORM` in django?</span> ](#what-is-orm-in-django) <br/>
📎 &nbsp; [<span style="color: darkred; font-weight: bold;">What is postgreSQL and pgAdmin?</span> ](#what-is-postgresql-and-pgadmin) <br/>
📎 &nbsp; [<span style="color: darkred; font-weight: bold;">How to create a database in PostgreSQL?</span>](#how-to-create-a-database-in-postgresql) <br/>
📎 &nbsp; [<span style="color: darkred; font-weight: bold;">How to connect postgreSQL database with our django project?</span>](#how-to-connect-postgresql-database-with-our-django-project) <br/>
📎 &nbsp; [<span style="color: darkred; font-weight: bold;">How to bring modification in the database table from django?</span>](#how-to-bring-modification-in-the-database-table-from-django ) <br/>
📎 &nbsp; [<span style="color: darkred; font-weight: bold;">How to pass data to database table from django project?</span> ](#how-to-pass-data-to-database-table-from-django-project) <br/>
📎 &nbsp; [<span style="color: darkred; font-weight: bold;">How to authenticate user login and user registration?</span> ](#how-to-authenticate-user-login-and-user-registration) <br/>

<br/>


##### <span style="color: forestgreen;">✅ how to check whether django is installed or not in a folder?</span> [\*](#django-basics)
In the command line, write and check:

```bash
django-admin --version
```

##### <span style="color: forestgreen;">✅ how to create python virtual environment?</span> [\*](#django-basics)

In the command line, write and check:
```bash
pip install virtualenvwrapper-win
mkvirtualenv test
# Here `test` is the folder name
```

Alternative approach (better):
```bash
# replace "." with a folder name 
# if you want to wrap things inside the folder

python3 -m venv .
source ./bin/activate
```

##### <span style="color: forestgreen;">✅ How to install django?</span> [\*](#django-basics)

```bash
pip install django 
```

##### <span style="color: forestgreen;">✅ How to create a django project?</span> [\*](#django-basics)
Go to the project folder, open terminal in that directory and run:

```bash
django-admin startproject telusko
# telusko is the folder name to be created
```

##### <span style="color: forestgreen;">✅ how to run our django project?</span> [\*](#django-basics)
Go to the  project folder directory in the terminal and run:

```bash
python3 manage.py runserver
```

##### <span style="color: forestgreen;">✅ What is app in django?</span> [\*](#django-basics)
An `app` is a particular segment in django project, which is created to perform a particular operation (webpage segments like user login, homepage, gallery, etc). 


##### <span style="color: forestgreen;">✅ How to create an app in django?</span> [\*](#django-basics)
Go to the project folder directory in terminal, run the virtual environment, then create an app:

```bash
# run virtual environment
source ./bin/activate

# start an app
python3 manage.py startapp calc    # `calc` is the app name here
```

##### <span style="color: forestgreen;">✅ How to render 'hello world' to the server page of django project (url mapping)?</span> [\*](#django-basics)
In the `calc` folder, create `urls.py` file.

In calc/urls.py, write:

```python
from django.urls import path
from . import views
urlpatterns = [path('', views.home, name='home')]
```
In the calc/views.py, write:
```python
from django.http import HttpResponse
def home(request):
  return HttpResponse("Hello World!")
```
In the telusko/urls.py, write:
```python
from django.urls import path, include
urlpatterns = [path('', include('calc.urls')), path('admin/', admin.site.urls)]
```

##### <span style="color: forestgreen;">✅ What is `django templates`?</span> [\*](#django-basics)
A `django template` is a way to render an HTML webpage to the django server.


##### <span style="color: forestgreen;">✅ How to render a webpage in django server (using django template)?</span> [\*](#django-basics)

Create a folder named anything of choice (in our case, 'templates') inside the project folder.

Inside the `templates` folder, create `home.html`.

Write some html content there.

In the `telusko/settings.py` file, bring some modification:

```python
from pathlib import Path, os

# ... existing lines ...

TEMPLATES = [

# ... existing lines ...

  'DIRS': [os.path.join(BASE_DIR, 'templates')],
  # here 'templates' is the folder name which we created earlier, and it contains the html file

# ... existing lines ...
]
```

In the `calc/views.py`, bring some modification:

```python
def home(request):
  return render(request, 'home.html')
  # here 'home.html' is the html file we created inside 'templates' folder
```

##### <span style="color: forestgreen;">✅ how to render any dynamic data to the webpage in django?</span> [\*](#django-basics)

We will see such thing with an example.

Modify the `calc/views.py` file:

```python
def home(request):
  return render(request, 'home.html', {'name': 'Asharful!!!'})
  # here, name is a key of a dictionary, which has some value, we will render it to templates/home.html
```
Modify the `templates/home.html` file:

```html
<h1>Hello {{name}}</h1>
<!--- here, name variable will render its value to the page. --->
```
We will see this another example:

Create `templates/base.html`

In the `templates/base.html`, write:

```html
<!DOCTYPE html
<html>
  …
  <body style="background-color: cyan">

    <!-- This is called JINJA template -->
    <!-- We can render other html data or content inside this block from other html files-->
    {% block content%}
      
    {% endblock%}

  </body>
</html>
```
In the `templates/home.html`, modify:

```python
{% extends 'base.html' %}
{% block content %}
  <h1>Hello {{name}}!!!!</h1>
{% endblock %}
```


##### <span style="color: forestgreen;">✅ How to do an operation (addition of two numbers) in webpage with django?</span> [\*](#django-basics)

In templates/home.html, bring some modification:
``` html
<form action="add" method="post">
  {% csrf_token %} <!-- to avoid CSRF error -->
  Enter 1st number: <input type="text" name="num1"/><br/>
  Enter 2nd number: <input type="text" name="num2"/>
  <input type="submit"/>
</form>
```
Create a new file – `templates/result.html`

In `calc/urls.html`, modify:

```python
urlpatterns = [path('', views.home, name="home"),
path("add", views.add, name="add")
]
```
In calc/views.py:
```python 
def home(request):
  return render(request, "home.html", {"name": "Navin"})
def add(request):
  val1 = int(request.POST['num1'])
  val2 = int(request.POST['num2'])
  res = val1 + val2
  return render(request, "result.html", {"result": res})
```
In `templates/result.html`, write:
```html
{% extends 'base.html'%}
{% block content %}
  Result: {{res}}
{% endblock%}
```

##### <span style="color: forestgreen;">✅ What is the difference between GET and POST method?</span> [\*](#django-basics)
`GET` is used to retrive data from the server.
`POST` is usded to send data to the server.
*`GET` – get data from the server; `POST` – post data to the server.*


##### <span style="color: forestgreen;">✅ What is MVT framework?</span> [\*](#django-basics)
Software engineering has several software development frameworks. One is MVT – Model, View, Template framework.
<img src="https://media.licdn.com/dms/image/v2/D5612AQHCvSpWQ9ZpuQ/article-cover_image-shrink_600_2000/article-cover_image-shrink_600_2000/0/1720761581067?</span>e=2147483647&v=beta&t=am6BQrVBPA-NdY8On1fbh7SrEgxEY69f1V0ZQ1X6tAA" style="display: block; margin: 0 auto; width: 50%;" />


##### <span style="color: forestgreen;">✅ How can we connect a frontend website to django?</span> [\*](#django-basics)

We will see this with an example.<br/>
Download Travello website template from ColorLib website.<br/>
Run development environment and go to project folder.<br/>
Add a new app:

```bash
python3 manage.py startapp travello    # travello is the name of the app
```
Copy the `index.html` file from the website folder to `templates` folder.<br/>

Create a new file - `travello/urls.py` and write inside it:
```python
from django.urls import path
from . import views
urlpatterns = [path('', views.index, name='index')]
```
In the `travello/views.py` file, modify:

```python
from django.shortcuts import render
def index(request):
  return render(request, 'index.html')
```
In `telusko/urls.py`, modify:

```python
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
  path('', include('travello.urls')), path('admin/', admin.site.urls)
]
```
Now if we refresh our url in the browser, we will see the raw html version of the website, that's because, we didn't bring its css and js files till now. (We can check the missing files from the web console.) To make it styled properly, let's follow the rest of the tutorials.

Create a new folder, `static`, inside the `projects/telusko` folder.<br/>
Copy all the folders from the downloaded website folder to `static` folder.<br/>
In the `telusko/settings.py` file, modify:

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
  os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
# django will create this 'assets' folder itself and arrange all the files from 'static' folder to it.
# But we need to pass a command to make django create this folder.
```
In the command line, write:

```bash
python3 manage.py collectstatic
# now the 'assets' folder will be visible in the project directory.
```
Now we need to add a line to the `index.html` file:

```html
{% load static %}
<!DOCTYPE html> ...
```
Now we need to change all the 'href' attribute paths as the following (we can trace where we need to change noticing the web console):

```html
<div… rel="stylesheet" href="{% static 'style.bootstrap4/bootstrap.min.css' %}">…</div>
```
After bringing all the changes to the 'index.html' file, we will see the complete webpage in the browser after a reload.


##### <span style="color: forestgreen;">✅ How can we render data dynamically to an html webpage?</span> [\*](#django-basics)
First, we will simply change a price data on our static webpage.<br/>
In the `travello/views.py`, modify it:

```python
def index(request):
  return render(request, "index.html", {"price": 1000})
```
In the `templates/index.html` file, search where is "`price $2,499`" is. Replace "`2,499`" with "`1000`":

```html
<div ...>...Price ${{price}}…</div>
```
Then we will see the changed price there after refreshing the static page in browser.

**Now we will see, how to render html content dynamically from django in a broader scope with an example.**

We will set some logics in `travello/models.py` file:

```python
from django.db import models
# create your models here
class Destination:
  id : int
  name: str
  img: str 
  desc: str 
  price: int
```

Now in `travello/views.py` file, modify it:
```python
from django.shortcuts import render
from .models import Destination  # lines added
# create your views here
def index(request):
  
  # values for first destination data
  dest1 = Destination()
  dest1.name = 'Mumbai'
  dest1.desc = 'The City That Never Sleeps'
  dest1.price = 700

  # values for second destination data
  dest2 = Destination()
  dest2.name = 'Bangaluru'
  dest2.desc = 'Beautiful City With Busy Streets'
  dest2.price = 799

  # values for third destination data
  dest3 = Destination()
  dest3.name = 'Hydarabad'
  dest3.desc = 'Biriyani comes first, then Sherwani'
  dest3.price = 699

  return render(request, "index.html", {"dest1" : dest1, "dest2": dest2, "dest3": dest3})
```
Simultaneously bring those modifications to the `templates/index.html` file:

```html
<!-- existing lines ... -->
<!-- Destination 1-->
<div class="destinatioin item">
  <div class="destination_image">
    <img .../>
    <div ...><a href=...>Special Offer</a></div>
  </div>
  <div class="destination_content">
    <div class="destination_name"> <a href="destinations.html">{{dest1.name}}</a> </div>
    <div class="destination_subtitles"> <p>{{dest1.desc}}</p> </div>
    <div class="destination_price">From ${{dest1.price}}</div>
  </div>
</div>

<!-- Destination 2-->
<div class="destinatioin item">
  <div class="destination_image">
    <img .../>
    <div ...><a href=...>Special Offer</a></div>
  </div>
  <div class="destination_content">
    <div class="destination_name"> <a href="destinations.html">{{dest2.name}}</a> </div>
    <div class="destination_subtitles"> <p>{{dest2.desc}}</p> </div>
    <div class="destination_price">From ${{dest2.price}}</div>
  </div>
</div>

<!-- Destination 3-->
<div class="destinatioin item">
  <div class="destination_image">
    <img .../>
    <div ...><a href=...>Special Offer</a></div>
  </div>
  <div class="destination_content">
    <div class="destination_name"> <a href="destinations.html">{{dest2.name}}</a> </div>
    <div class="destination_subtitles"> <p>{{dest2.desc}}</p> </div>
    <div class="destination_price">From ${{dest2.price}}</div>
  </div>
</div>
```

**But we haven't change the images in the webpage. Now we'll do that, and also, we'll write the code in little bit improved way.**

`travello/views.py` file: 

```python
from django.shortcuts import render
from .models import Destination  # lines added
# create your views here
def index(request):
  
  # values for first destination data
  dest1 = Destination()
  dest1.name = 'Mumbai'
  dest1.desc = 'The City That Never Sleeps'
  dest1.img = 'destination_1.jpg'
  dest1.price = 700

  # values for second destination data
  dest2 = Destination()
  dest2.name = 'Bangaluru'
  dest2.desc = 'Beautiful City With Busy Streets'
  dest2.img = 'destination_2.jpg'
  dest2.price = 799

  # values for third destination data
  dest3 = Destination()
  dest3.name = 'Hydarabad'
  dest3.desc = 'Biriyani comes first, then Sherwani'
  dest3.img = 'destination_3.jpg'
  dest3.price = 699

  dests = [dest1, dest2, dest3]  # we've included everything in a list

  return render(request, "index.html", {"dests" : dests})
```

`templates/index.html` file:

```html
{% load static %}
{% static "images" as baseUrl %}  <!-- added line -->
<!DOCTYPE html>
<html>

<!-- existing lines ... -->

<!-- Instead of manually referring data, we'll run a loop for all three destinations -->
{% for dest in dests %}
  <!-- destination -->
  <div class="destinatioin item">
    <div class="destination_image">
      <!-- 
        <img ... src="{% static 'images/{{dest.img}}' %}"/>

        This will cause an error. Because we can't use JINJA format inside JINJA
        So, we have made a variable 'baseUrl', see the top of html file'
      -->
      <img ... src="{{baseUrl}}/{{dest.img}}" />
      <div ...><a href=...>Special Offer</a></div>
    </div>
    <div class="destination_content">
      <div class="destination_name"> <a href="destinations.html">{{dest.name}}</a> </div>
      <div class="destination_subtitles"> <p>{{dest.desc}}</p> </div>
      <div class="destination_price">From ${{dest.price}}</div>
    </div>
  </div>

<!-- existing lines -->

</html>
{% endfor %}
```

##### <span style="color: forestgreen;">✅ How to run an `if` conditional statement in django?</span> [\*](#django-basics)

We'll change the 'Special Offer' tag based on the conditional `if...else` logic on the images of html file.

In `travello/models.py` file, add one more `offer` variable:

```python
from django.db import models
# create your models here
class Destination:
  id : int
  name : str
  img : str 
  desc : str 
  price : int
  offer : bool
```

In `travello/views.py` file: 

```python
from django.shortcuts import render
from .models import Destination  # lines added
# create your views here
def index(request):
  
  # values for first destination data
  dest1 = Destination()
  dest1.name = 'Mumbai'
  dest1.desc = 'The City That Never Sleeps'
  dest1.img = 'destination_1.jpg'
  dest1.price = 700
  dest1.offer = False

  # values for second destination data
  dest2 = Destination()
  dest2.name = 'Bangaluru'
  dest2.desc = 'Beautiful City With Busy Streets'
  dest2.img = 'destination_2.jpg'
  dest2.price = 799
  dest2.offer = True

  # values for third destination data
  dest3 = Destination()
  dest3.name = 'Hydarabad'
  dest3.desc = 'Biriyani comes first, then Sherwani'
  dest3.img = 'destination_3.jpg'
  dest3.price = 699
  dest3.offer = False

  dests = [dest1, dest2, dest3]  # we've included everything in a list

  return render(request, "index.html", {"dests" : dests})
```

`templates/index.html` file:

```html
<!-- existing lines ... -->

{% for dest in dests %}
  <!-- destination -->
  <div class="destinatioin item">
    <div class="destination_image">
      <img ... src="{{baseUrl}}/{{dest.img}}" />
      <!-- added segment -->
      {% if dest.offer==true %}   
        <div ...><a href=...>Special Offer</a></div>
      {% endif %}
    </div>
    <div class="destination_content">
      <div class="destination_name"> <a href="destinations.html">{{dest.name}}</a> </div>
      <div class="destination_subtitles"> <p>{{dest.desc}}</p> </div>
      <div class="destination_price">From ${{dest.price}}</div>
    </div>
  </div>

<!-- existing lines -->

</html>
{% endfor %}
```
##### <span style="color: forestgreen;">✅ What is `ORM` in django?</span> [\*](#django-basics) 

`ORM` stands for Object Relational Mapper. `ORM` dynamically connects a webpage to a database and web to db data transfer becomes automated.

In `ORM` theory, the table_name in DB is the class name of python language, each column heading is each variable in that class, and each row is each object. For instance:

`DB`

**Table - Students**

|Id         | Name        | Roll_No     | Contact_info  |
|-----------|-------------|-------------|---------------|
| 01        | Shariful    | 001         | 123 Street    |
| 02        | Arif        | 002         | 7#Circle Road |

`Equivalent Python script`

```python
class Students:
  id : int
  name : str
  roll_no : int
  contact_info : str 

student_data_1 = Students()   # object for row 1 data
student_data_2 = Students()   # object for row 2 data

student_data_1.id = 01
student_data_1.name = 'Shariful'
student_data_1.roll_no = 001
student_data_1.contact_info = '123 Street'

student_data_2.id = 02
student_data_2.name = 'Arif'
student_data_2.roll_no = 002
student_data_2.contact_info = '7#Circle Road'
```

##### <span style="color: forestgreen;">✅ What is postgreSQL and pgAdmin?</span> [\*](#django-basics)
`postgreSQL` is a database engine and `pgAdmin` is a UI setup for postgreSQL. We'll use postgreSQL as our database engine here. So we need to intall and configure them in our device.

##### <span style="color: forestgreen;">✅ How to create a database in PostgreSQL?</span> [\*](#django-basics)

1. Right click on `Database(1)`
2. Select: `Create` -> `Database...`
3. Set database name (write '*telusko*' for our case) and other configuration, click `Save`

But note that, we have database now but not any table yet. We can use SQL language to create a table, but we will do that from our django project.

##### <span style="color: forestgreen;">✅ How to connect postgreSQL database with our django project?</span> [\*](#django-basics)

Go to `telusko/settings.py` and configure the 'DATABASES' settings there:

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

Now we need a **connector/database adaptor** to connect our django project with database. So we need to install `psycopg2`.

```bash
# open virtual environment and run
pip install psycopg2
```

Now we need a model to connect our database. So we need to configure `travello/models.py` file:

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

At this stage, we need to do **migration**. But we first need to configure the `telusko/settings.py` file, and then we need to install a library **Pillow** as we will upload image to our database.

`telusko/settings.py`:

```python
# ...existing lines...

# Application definition
INSTALLED_APPS = [
  'travello.apps.TravelloConfig',   # added line
  'django.contrib.admin', 
  # ...other configs...
]
```

`bash`:

```bash
# keep virtual environment on and wrtie
pip install Pillow
```

Now, it's time for migration:

```bash
python manage.py makemigrations
# a new file '0001_initial.py' will be visible in 'travello' folder

# we have migrated the model only, no table is still created in database
# so need to migrate '0001_initial.py' from 'travello' folder 
python3 manage.py sqlmigrate travello 0001
python3 manage.py migrate
```

Now go to `browser` -> `pgAdmin`, right click on `telusko`/`Schemas(1)`/`Tables`, select '`Refresh..`', we'll see our table names. To see data, right click on '`travello_destination`', select '`View/Edit Data`' -> '`All Rows`'

##### <span style="color: forestgreen;">✅ How to bring modification in the database table from django?</span>  [\*](#django-basics)

We intentionally didn't keep 'price' column or 'price' variable earlier to demonstrate how to modify table. We will add this currently.

First, modify `travello/models.py` file:

```python
from django.db import models

# create your models here
class Destination(models.Model):

  # see official documentation of django model fields for reference
  name = models.CharField(max_length = 100)
  img = models.ImageField(upload_to = 'pics')
  desc = models.TextField()
  price = models.IntegerField()   # uncommented
  offer = models.BooleanField(default = False)
```

In the next stage, we can alter the table from postgesSQL database using sql language. But we will do it from our django project.

Now, migrate files with terminal command:

```bash
python3 manage.py makemigrations
python3 manage.py migrate

# this will add an addtional file '0002_destination_price.py' in the travello/migrations folder
```

##### <span style="color: forestgreen;">✅ How to pass data to database table from django project?</span> [\*](#django-basics)

We have created database table, connected with our django project, but haven't put any data there. We'll do that now.

We can do that in two ways:

1. By creating a page where a general user can push data to database
2. By creating an admin-panel where only the admin/superuser can push data to database.

The later way is comparitably difficult, but we'll do that now.

If we visit `localhost:8000/admin` page, we'll see an admin page provided by django by-dafault. To access this, we first need to create a superuser account.

In terminal, write:

```bash
python manage.py createsuperuser
# then set your credentials
```

We can now get access to admin page, but we want to create a dashboard to upload to data to database. Below is how we'll create it.

In travello/admin.py file:

```python
from django.contrib import admin

# we have to import our 'Destination' model here
from .models import Destination

# Register your model here
admin.site.register(Destination)
```

Now we'll see an option to open our dashboard at the admin page now!

But in the `Destination` dashboard, we have kept an option to upload image. In database, only the image path will be added. And images will be reserved in folder or path in our project. So we need to do some staff now.

In the `telusko/settings.py` file, we need to the path for media: 

```python
# ...existing lines...

STATIC_URL = '/static/'
STATICFILES_DIRS = [
  os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

MEDIA_URL = '/media'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

We also need to modify `settings/urls.py` file:

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings            # added line
from django.conf.urls.static import static  # added line

# ...existing lines...

urlpatterns = [
  path('', include('travello.urls')),
  path('/admin', admin.site.urls),
]

# added part
urlpatterns = urlpatterns + static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)
```

If we add data from `Destination` dashboard from admin-panel now, data will be added to the database (at pgAdmin).

We're almost done, leaving a final part. Modify `travello/views.py` file:

```python
# ...existing lines...
def index(request):

  dests = Destination.objects.all()

  return render(request, "index.html", {'dests': dests})
```

But we'll not be able to see the images in `index.html` file, that's because we need to modify the `src` path of the images in `templates/index.html` file now:

```html
<!-- ...existing lines... -->

{% for dest in dests %}
  <!-- destination -->
  <div class="destinatioin item">

    <!-- ...existing lines... -->
    <img src={{dest.img.url}} />
    <!-- ...existing lines... -->

  </div>
<!-- ...existing lines... -->
```


##### <span style="color: forestgreen;">✅ How to authenticate user login and user registration?</span> [\*](#django-basics)

Create a seperate app `accounts`

```bash
python3 manage.py startapp accounts
```
Create `accounts/urls.py` file and edit it:

```python
from django.urls import path
from . import views

urlpatterns = [
  path('register', views.register, name='register'),
]
```

In project level `urls.py`:

```python
# ...existing lines...

urlpatterns = [
  path('', include('travello.urls')),
  path('admin/', admin.site.urls),
  path('accounts/', include('accounts.urls')),   # added line
]

# ...existing lines...
```

In `accounts/views.py`:

```python
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

def register(request):
  if request.method == 'POST':
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    password1 = request.POST['password1']
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    email = request.POST['email']

    if password1==password2:
      if User.objects.filter(username=username).exists():
        messages.info(request, 'Username taken')
        return redirect('register')
      elif User.objects.filter(username=email).exists():
        messages.info(request, "Email taken")
        return redirect('register')
      else:
        user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
        user.save()
        print('user created')

    else:
      messages.info(request, "password not matching...")
      return redirect('register')

    return redirect('/')
  
  else:
    return render(request, 'register.html')
```

Now, create `templates/register.html`:

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Registration</title>
</head>
<body>
  <form action="register" method="post">
    {% csrf_token %}
    <!-- We already have a default auth_user table in our database -->
    <input type="text" name="first_name" placeholder="First name"/><br/>
    <input type="text" name="last_name" placeholder="Last name"/><br/>
    <input type="text" name="username" placeholder="Username"/><br/>
    <input type="email" name="email" placeholder="example@example.com"/><br/>
    <input type="password" name="password1" placeholder="Password"/><br/>
    <input type="password" name="password2" placeholder="Repeat password"/><br/>
    <input type="Submit"/><br/>
  </form>

  <div>
    {% for message in messages %}
      <h3>{{message}}</h3>
    {% endfor %}
  </div>
</body>
</html>
```

In `template/index.html`, replace some anchor links with 'login'/'logout' and 'registration' link.

```html
<!-- <li><a href="about.html">About</a></li>
<li><a href="#">Services</a></li>
<li><a href="news.html">News</a></li> -->
<li><a href="accounts/register">Register</a></li>
<li><a href="news.html">News</a></li>
```

Refresh `localhost:8000/accounts/register` to see our form, for user account registration.

[Go to top](#django-basics)