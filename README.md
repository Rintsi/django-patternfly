# django-patternfly

Patternfly integration for Django. Ported from [django-bootstrap4](https://github.com/zostera/django-bootstrap4)

DISCLAIMER: This is a port done over the weekend for R'n'D purposes. It is NOT
usable in it's current state

## Goal

The goal of this project is to seamlessly blend Django and PatternFly.

## Requirements

Python 3.6 or newer with Django >= 2.2 or newer.

## Documentation

The full documentation is (will be) at https://django-patternly.readthedocs.io/

## Installation

1. Install using pip:

   ```shell script
   pip install django-patternfly
   ```


2. Add to `INSTALLED_APPS` in your `settings.py`:

   ```python
   INSTALLED_APPS = (
       # ...
       "patternfly",
       # ...
   )
   ```

3. In your templates, load the `patternfly` library and use the `patternfly_*` tags:

## Example template

```djangotemplate
{% load patternfly %}

{# Display a form #}

<form action="/url/to/submit/" method="post" class="form">
    {% csrf_token %}
    {% bootstrap_form form %}
    {% buttons %}
        <button type="submit" class="btn btn-primary">Submit</button>
    {% endbuttons %}
</form>
```

## Development

Install poetry

```shell script
$ conda install -c conda-forge poetry
```

## Bugs and suggestions

If you have found a bug or if you have a request for additional functionality, please use the issue tracker on GitHub.

https://github.com/Rintsi/django-patternfly/issues

## License

You can use this under BSD-3-Clause. See [LICENSE](LICENSE) file for details.

## Author

Developed and maintained by [Rintsi](https://linkedin.com/in/rintsi).

Please see [AUTHORS.md](AUTHORS.md) for a list of contributors.
