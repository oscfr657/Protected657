
# Protected657 #

A Django app to keep files protected, works with Nginx.

## Compatible ##

### Tested with ###

``` Python
django>=3.2.9
```

## Installation ###
  
### Pip requirements ###

> pip install -r requirements.txt

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

### Collectstatic ###

> python3 manage.py collectstatic

## For development ##

### Build a new release ###

``` bash
    pip install black
    black . --skip-string-normalization
```

``` python
python3 -m build --sdist
```
