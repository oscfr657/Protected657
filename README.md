
# Protected657 #

A Django app to keep files protected, works with Nginx.

## Compatible ##

### Tested with ###

``` Python
django==5.0.0
```

## Installation ###
  
### Pip requirements ###

> pip install -r requirements.txt

## Setup ##

### Nginx ###

``` bash
    location /internal/ {
        internal;
        alias /home/app/protected/files/;
    }
```

### Django settings ###

To your settings file,

``` Python
    PROTECTED_MEDIA_ROOT = BASE_DIR / 'protected/files'
```

and add to the INSTALLED_APPS

``` Python
    'protected657',
```

### Database configuration ###

> python manage.py migrate

### Django url ###

To the django projects' url.py add

``` python
from django.urls import path

```

and

``` python
urlpatterns += [
    path('protected/', include('protected657.urls', namespace='protected657')),
  ]
```

## For development ##

### Testing ###

#### API ####


``` python
python manage.py test protected657
```

#### GUI ####

``` bash
cd tests

npm install cypress --save-dev

npx cypress open

npx cypress run

```

### Build a new release ###

``` bash
    pip install black
    black . --skip-string-normalization
```

``` python
python -m build --sdist
```

### TODO: ###

    Improve documentation
    More sests
    Code comments
    pytest
    pytest-html-reporter
