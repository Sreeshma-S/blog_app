# Blog Application 
The objective of the project is to develop a blog application with user authentication, CRUD operations, and API for managing blog posts.

### Setup

Clone the repository:

```sh
git clone -b master https://github.com/Sreeshma-S/blog_app.git
```

Create a virtual environment and activate it:

```sh

cd blogapp

python -m venv myvenv

.\venv\Scripts\activate
```

Then install the dependencies:

```sh
(venv) pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies:
```sh
(venv) python manage.py makemigrations

(venv) python manage.py migrate

(venv) python manage.py runserver
```

And navigate to `http://127.0.0.1:8000/` in your browser to view the localhost.


### Demo
- Get started with new user registration
- Login with your registered credentials
- In home page you can see blogs existing blogs.
- In order to create new blog click on the sidebar to create, edit or delete your own blog
- Once you have successfully posted the blog, it appears in "My Blog" section which you can edit and delete.
- Other users blogs are available for view option

Below are the API Endpoints:

To view list of blogs: 
http://127.0.0.1:8000/api/blog/list/'

To create new blog:
http://127.0.0.1:8000/api/blog/create'

To view a blog post:
http://127.0.0.1:8000/api/blog/<int:pk>/'

To edit a blog post:
http://127.0.0.1:8000/api/blog/update/<int:pk>/'

To delete a blog post:
http://127.0.0.1:8000/api/blog/delete/<int:pk>/'

