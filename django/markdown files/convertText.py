def convert(text):
	text = text.strip()
	text_ = text.lower()
	replaceMe = ["?", "`", "'", "\"", "(", ")"]
	for i in replaceMe:
		text_ = text_.replace(i, "")
	newText = text_.replace(" ", "-")
	newText = "#" + newText
	text = "<span style=\"color: seagreen; font-weight: bold;\">" + text + "</span>"
	
	print('\n',text, '\n')
	print(newText, '\n')

text = "Mental Maps of Django Processes"
convert(text)

'''
* [<span style="color: seagreen; font-weight: bold;">How to check whether django is installed or not in a folder?</span>](#how-to-check-whether-django-is-installed-or-not-in-a-folder)
* [<span style="color: seagreen; font-weight: bold;">How to create python virtual environment?</span>](#how-to-create-python-virtual-environment)
* [<span style="color: seagreen; font-weight: bold;">How to install django?</span>](#how-to-install-django)
* [<span style="color: seagreen; font-weight: bold;">How to create a django project?</span>](#how-to-create-a-django-project)
* [<span style="color: seagreen; font-weight: bold;">How to run our django project?</span>](#how-to-run-our-django-project)
* [<span style="color: seagreen; font-weight: bold;">What is app in django?</span>](#what-is-app-in-django)
* [<span style="color: seagreen; font-weight: bold;">How to create an app in django?</span>](#how-to-create-an-app-in-django)
* [<span style="color: seagreen; font-weight: bold;">How to render 'hello world' to the server page of django project (url mapping)?</span>](#how-to-render-hello-world-to-the-server-page-of-django-project-url-mapping)
* [<span style="color: seagreen; font-weight: bold;">What is `django templates`?</span>](#what-is-django-templates)
* [<span style="color: seagreen; font-weight: bold;">How to render a webpage in django server (using django template)?</span>](#how-to-render-a-webpage-in-django-server-using-django-template)
* [<span style="color: seagreen; font-weight: bold;">how to render any dynamic data to the webpage in django?</span>](#how-to-render-any-dynamic-data-to-the-webpage-in-django)
* [<span style="color: seagreen; font-weight: bold;">How to do an operation (addition of two numbers) in webpage with django?</span>](#how-to-do-an-operation-addition-of-two-numbers-in-webpage-with-django)
* [<span style="color: seagreen; font-weight: bold;">What is the difference between GET and POST method?</span>](#what-is-the-difference-between-get-and-post-method)
* [<span style="color: seagreen; font-weight: bold;">What is MVT framework?</span>](#what-is-mvt-framework)
* [<span style="color: seagreen; font-weight: bold;">How can we connect a frontend website to django?</span>](#how-can-we-connect-a-frontend-website-to-django)
* [<span style="color: seagreen; font-weight: bold;">How can we render data dynamically to an html webpage?</span>](#how-can-we-render-data-dynamically-to-an-html-webpage)
* [<span style="color: seagreen; font-weight: bold;">How to run an `if` conditional statement in django?</span>](#how-to-run-an-if-conditional-statement-in-django)
* [<span style="color: seagreen; font-weight: bold;">What is `ORM` in django?</span> ](#what-is-orm-in-django)
* [<span style="color: seagreen; font-weight: bold;">What is postgreSQL and pgAdmin?</span> ](#what-is-postgresql-and-pgadmin)
* [<span style="color: seagreen; font-weight: bold;">How to create a database in PostgreSQL?</span>](#how-to-create-a-database-in-postgresql)
* [<span style="color: seagreen; font-weight: bold;">How to connect postgreSQL database with our django project?</span>](#how-to-connect-postgresql-database-with-our-django-project)

* [<span style="color: seagreen; font-weight: bold;">How to bring modification in the database table from django?</span>](#how-to-bring-modification-in-the-database-table-from-django )
* [<span style="color: seagreen; font-weight: bold;">How to pass data to database table from django project?</span> ](#how-to-pass-data-to-database-table-from-django-project)
* []()
* []()
'''