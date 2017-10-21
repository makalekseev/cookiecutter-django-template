# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Setting up a Development Environment

### Running tests

## Configuration Variables

The project can be fully configured using the following environment variables. Either via a .env file or environment variables in your shell.

- DJANGO_DEBUG (Default: False)
- DJANGO_SECRET_KEY (Default: None)
- DJANGO_ALLOWED_HOSTS (Default: example.com)
- DJANGO_LANGUAGE_CODE (Default: en-us)
- DJANGO_TIME_ZONE (Default: UTC)
- DATABASE_URL (Default: postgres://localhost/{{cookiecutter.project_slug}})
- DJANGO_STATIC_HOST (Default: '')
- DJANGO_LOG_LEVEL (Default: INFO)
- RAVEN_DSN (Default: '')
- DJANGO_ACCOUNT_ALLOW_REGISTRATION (Default: True)

## Changelog

**{% now 'utc', '%Y-%m-%d' %}**

- Initial checkin.

## License

This template is licensed under the **MIT License**. See the LICENSE file.