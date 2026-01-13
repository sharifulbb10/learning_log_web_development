##### What is an API?
- Application Programming Interface
- two-way communication bridge

##### What is REST API?
- Representational State Transfer
- Stateless

##### RESTful Operations
|		  |      URI     |
|---------|--------------|
|   GET   | `/students`  |
|   POST  | `/students`  |
|   PUT   | `/student/1` |
|  DELETE | `/student/1` |

##### How to install Django Rest Framework?
Google Django REST Framework, visit website, follow instruction.
```bash
pip install djangorestframework
# add this to the project level settings.py's INSTALLED_APPS list
```
##### Two types of URL endpoints
1. Web application endpoint
http://127.0.0.1:8000/students
2. API endpoint
http://127.0.0.1:8000/api/v1/students

##### What is Serializer?
Serializer is the converter of python dictionary to JSON format.