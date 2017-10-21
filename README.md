# Cookiecutter Django Template

Powered by [Cookiecutter](https://github.com/audreyr/cookiecutter) is a template for jumpstarting a production-ready Django project.

## Features

- For Django 1.11 and Python 3.6.
- [Pipenv](https://pipenv.readthedocs.io/en/latest/) is used for dependency and virtualenv management.
- [12-factor](https://12factor.net/) based settings via [django-environ](https://github.com/joke2k/django-environ).
- Secure by default. SSL is the way to go.
- Registration via [django-allauth](http://django-allauth.readthedocs.io/en/latest/index.html).
- Comes with custom user model ready to go.
- [Whitenoise](http://whitenoise.evans.io/en/stable/index.html) is used for serving static files.
- [Sentry](https://sentry.io/welcome/) can be added for error logging.
- [pytest](https://docs.pytest.org/en/latest/) is supported via [pytest-django](https://pytest-django.readthedocs.io/en/latest/) and with some extra candy provided by [pytest-sugar](https://pivotfinland.com/pytest-sugar/)
- [jQuery 3](https://jquery.com/), [Font Awesome 4.7](http://fontawesome.io), [Bootstrap 4](http://getbootstrap.com) and [intercooler.js](http://intercoolerjs.org) are included by the default template.
- SASS support is provided by [libsass](https://hongminhee.org/libsass-python/) and [django-libsass](https://github.com/torchbox/django-libsass).
- [MIT License](https://choosealicense.com/licenses/mit/) is the default license.

## Usage

```bash
$ pip install cookiecutter
$ cookiecutter https://github.com/oliverandrich/cookiecutter-django-template
$ cd your_new_project
$ pipenv install --three --dev
$ pipenv shell
```

You will be prompted for some values. Provide them, then a Django project is created for you. Enjoy!

## Project Layout

Yes, I love to group my apps inside the project folder inside a folder named `apps`.

```
$ tree -a project_name/
project_name/
├── .coveragerc
├── .env
├── .gitignore
├── LICENSE
├── Pipfile
├── Pipfile.lock
├── README.md
├── manage.py
├── project_name
│   ├── __init__.py
│   ├── apps
│   │   ├── __init__.py
│   │   └── users
│   │       ├── __init__.py
│   │       ├── adapters.py
│   │       ├── admin.py
│   │       ├── apps.py
│   │       ├── migrations
│   │       │   ├── 0001_initial.py
│   │       │   ├── __init__.py
│   │       ├── models.py
|   |       ├── templates
|   |       │   └── .gitkeep
│   │       ├── tests.py
│   │       └── views.py
│   ├── settings.py
│   ├── static
│   │   ├── .gitkeep
│   │   ├── css
│   │   │   ├── .gitkeep
│   │   │   └── project.scss
│   │   ├── images
│   │   │   └── .gitkeep
│   │   └── js
│   │       ├── .gitkeep
│   │       └── project.js
│   ├── templates
│   │   ├── .gitkeep
│   │   ├── 403_csrf.html
│   │   ├── 404.html
│   │   ├── 500.html
│   │   ├── base.html
│   │   └── index.html
│   ├── urls.py
│   └── wsgi.py
└── pytest.ini
```

## Configuration variables of the resulting project

The project can be fully configured using the following environment variables. Either via a .env file or environment variables in your shell.

- DJANGO_DEBUG (Default: False)
- DJANGO_SECRET_KEY (Default: None)
- DJANGO_ALLOWED_HOSTS (Default: localhost)
- DJANGO_LANGUAGE_CODE (Default: en-us)
- DJANGO_TIME_ZONE (Default: UTC)
- DATABASE_URL (Default: mysql://root@localhost/{{cookiecutter.project_slug}})
- DJANGO_STATIC_HOST (Default: '')
- DJANGO_LOG_LEVEL (Default: INFO)
- RAVEN_DSN (Default: '')
- DJANGO_ACCOUNT_ALLOW_REGISTRATION (Default: True)

DJANGO_DEBUG and DJANGO_SECRET_KEY are set to reasonable defaults by a cookiecutter post_gen_project hook. They are stored in a .env file in the fresh project directory. Besides creating the .env file, the post_gen_project hook also initializes the git repository.

## License

This template is licensed under the **MIT License**. See the LICENSE file.