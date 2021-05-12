# django-floc-disable

Django middleware to disable Google's Federated Learning of Cohorts (`FLoC`) tracking

## Python / Django Support

- Python 3.6+
- Django versions 3+

## Usage

Install django-floc-disable:

```shell
pip install django-floc-disable
```

Add it to your `INSTALLED_APPS`:

```python
MIDDLEWARE = (
    # ...
    'django_floc_disable.middleware.FLoCDisableMiddleware',
    # ...
)
```

This will set the `Permissions-Policy` header to a value of
`interest-cohort=()` for every request served by Django.

## Support

* Issues: <https://github.com/nhymxu/django-floc-disable/issues>
* Here you can [donate](https://dungnt.net/donate.html) for this project.

## License

The MIT License (MIT). Please see [License File](LICENSE.txt) for more information.