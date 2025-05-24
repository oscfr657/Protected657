
# Protected657 #

A Django app to keep files protected, works with Nginx.

## Compatible ##

### Tested with ###

``` Python
Django==5.2.1
djangorestframework==3.16.0
python-magic==0.4.27
```

## Installation ###
  
### Pip requirements ###

``` bash
pip install -r requirements.txt
```

## Setup ##

### Nginx ###

``` bash
location /internal/ {
    internal;
    alias /home/app/protected/files/;
}
```

### Django settings ###

To your settings file add

``` Python
PROTECTED_MEDIA_ROOT = BASE_DIR / 'protected/files'
```

and add to the INSTALLED_APPS

``` Python
'protected657',
```

### Database configuration ###

``` bash
python manage.py migrate
```

### Django url ###

To the django projects' url.py add

``` Python
from django.urls import path
```

and

``` Python
urlpatterns += [
    path('protected/', include('protected657.urls', namespace='protected657')),
  ]
```

## For development ##

### Testing ###

#### Setup ####

##### Browsers #####

Install Google-Chrome and Firefox.

To run tests in Docker you can try to add to your Dockerfile

``` bash
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install -y ./google-chrome-stable_current_amd64.deb
RUN apt install -y firefox-esr
```

#### Django tests ####

##### Pip install #####

``` bash
pip install selenium webdriver-manager
```

##### Run tests #####

``` bash
python manage.py test protected657
```

#### Cypress ####

``` bash
cd tests/gui_tests
npm install cypress --save-dev
npx cypress open
npx cypress run
```

### Build a new release ###

``` bash
pip install black
black . --skip-string-normalization
```

``` bash
python -m build --sdist
```

### TODO: ###

    Srceen size responsive design
    Improve documentation
    More tests
    Code comments
    pytest
    pytest-html-reporter
