# django-floc-disable

[![unit test](https://github.com/nhymxu/django-floc-disable/actions/workflows/test-python.yml/badge.svg?branch=main)](https://github.com/nhymxu/django-floc-disable/actions/workflows/test-python.yml)

Django middleware to disable Google's Federated Learning of Cohorts (`FLoC`) tracking

New version is Topics API

## Python / Django Support

- Python 3.8+
- Django versions 3+

## Usage

Install django-floc-disable:

```shell
pip install django-floc-disable
```

Add it to your `MIDDLEWARE` tuple in `settings.py`:

```python
MIDDLEWARE = (
    # ...
    'django_floc_disable.middleware.FLoCDisableMiddleware',
    # ...
)
```

This will set the `Permissions-Policy` header to a value of `browsing-topics=()` for every request served by Django.

Reference:
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Permissions-Policy/browsing-topics
- https://developers.google.com/privacy-sandbox/private-advertising/topics/web/controls#opt_out_as_a_developer

## Support

* Issues: <https://github.com/nhymxu/django-floc-disable/issues>
* Here you can [donate](https://dungnt.net/donate.html) for this project.

## License

The MIT License (MIT). Please see [License File](LICENSE.txt) for more information.
