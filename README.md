
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

#### 1. Install Selenium ####

``` bash
    pip install -U selenium
```

#### 2. Install a Chromedriver ####

    ! Selenium and Snap issues

    https://github.com/SeleniumHQ/selenium/issues/7788#issuecomment-764804891

    https://github.com/mozilla/geckodriver/issues/2055

#### Run tests ####

``` bash
    python manage.py test protected657
```

#### Postman ####

    It's required to set the username, password and host variables for Postman to function.
    The door_logo43.png file used in the POST tests can be found in the tests folder.

### Build a new release ###

``` bash
    pip install black
    black . --skip-string-normalization
```

``` python
python3 -m build --sdist
```

### TODO: ###

    Improve documentation
    More sests
    Code comments
