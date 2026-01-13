##### I have crated a model in app level models.py, I have migrated, so I got a table in my Database. How can I push data to the table through the model now, from html form?

In the app level views.py, save 'General_user' model in the table in the following way:

```python
def function_name(request):
	# ...existing lines...
	user_data = General_user('var1': var1, 'var2': var2, )
	user_data.save()

	# or directly
	# General_user.objects.create('var1': var1, 'var2': var2, )
	return render(request, 'page.html')
```

##### I want to put different form validation messages from app level views.py to different places in html page?

