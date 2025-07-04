
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
  
``` bash
pip install git+https://github.com/oscfr657/protected657.git@main
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

### Clone ###

``` bash
git clone git+https://github.com/oscfr657/protected657.git@main .
```

### Pip requirements ###

``` bash
pip install -r requirements.txt
```

### Docker compose yaml file ###

``` bash
- protected_volume:/home/web/protected
```

and

``` bash
  protected_volume: {}
```

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
npx cypress run  --headed
```

### Build a new release ###

``` bash
python3 -m venv env
source env/bin/activate
python3 -m pip install black
python3 -m black . -S -t py310 -t py311 -t py312 --diff
python3 -m black . -S -t py310 -t py311 -t py312
```

Update version in VERSION.txt

Update CHANGELOG.md

``` bash
python3 -m pip install build
python3 -m build --sdist
```

``` bash
   git commit -a -m 'Cangelog message.'
   git push
```

### TODO: ###

    Srceen size responsive design
    Add a delete file button to list template
    Improve documentation
    More tests
    Code comments
    pytest
    pytest-html-reporter
