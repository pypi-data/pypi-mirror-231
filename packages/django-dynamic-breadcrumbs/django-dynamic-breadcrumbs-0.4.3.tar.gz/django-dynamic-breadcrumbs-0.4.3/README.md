django-dynamic-breadcrumbs
=====

[![Django CI](https://github.com/marcanuy/django-dynamic-breadcrumbs/actions/workflows/django.yml/badge.svg)](https://github.com/marcanuy/django-dynamic-breadcrumbs/actions/workflows/django.yml)
[![Coverage Status](https://coveralls.io/repos/github/marcanuy/django-dynamic-breadcrumbs/badge.svg?branch=main)](https://coveralls.io/github/marcanuy/django-dynamic-breadcrumbs?branch=main)
[![PyPI version](https://img.shields.io/pypi/v/django-dynamic-breadcrumbs)](https://pypi.org/project/django-dynamic-breadcrumbs/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Downloads](https://static.pepy.tech/badge/django-dynamic-breadcrumbs)](https://pepy.tech/project/django-dynamic-breadcrumbs)
[![Documentation Status](https://readthedocs.org/projects/django-dynamic-breadcrumbs/badge/?version=latest)](https://django-dynamic-breadcrumbs.readthedocs.io/en/latest/?badge=latest)

`django-dynamic-breadcrumbs` is a Django app to generate HTML breadcrumbs
dynamically from URL paths.

At `https://example.com/reference/instrument/guitar/`, shows:
`Home > Reference > Instrument > Guitar`.

# Quick start

## 1. Install

~~~
pip install django-dynamic-breadcrumbs
~~~

## 2. Add to settings

Add "dynamic_breadcrumbs" label to your INSTALLED_APPS settings:

    INSTALLED_APPS = [
        ...
        'dynamic_breadcrumbs',
    ]

Add `dynamic_breadcrumbs.context_processors.breadcrumbs` to **context_processors**:

~~~ python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
				#...
                "dynamic_breadcrumbs.context_processors.breadcrumbs",
            ],
        },
    },
]
~~~

## 3. Add template

Include the `dynamic_breadcrumbs/breadcrumbs.html` in your base template.

~~~
{% if breadcrumbs %}
<div class="container">
    {% include "dynamic_breadcrumbs/breadcrumbs.html" with breadcrumbs=breadcrumbs%}
</div>
{% endif %}
~~~

Now each time you visit a page which makes use of the above template,
it will have the breadcrumbs generated from the URL path.

## 4. (Optional) Customization

Tweak default [settings](https://django-dynamic-breadcrumbs.readthedocs.io/en/latest/ref/settings.html).

# Documentation

Full docs at: https://django-dynamic-breadcrumbs.readthedocs.io/

# License

MIT
