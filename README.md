<h1 align="center">Django Clear S2S</h1>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/Lenders-Cooperative/django-password-history)](https://github.com/Lenders-Cooperative/django-password-history/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/Lenders-Cooperative/django-password-history/pulls)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

</div>

---

<p align="center"> A Django module for Thomson Reuters ClearID System to System search.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting-started)
- [Running Tests](#running-tests)
- [Usage](#usage)
- [Built Using](#built-using)
- [Authors](#authors)
- [Acknowledgments](#acknowledgements)

## About

A Django module for Thomson Reuters ClearID System to System search.

## Getting Started

Follow these instructions to install and setup django-soap in your django project.

### Prerequisites

This package relies on `requests`, `xmltodict`, `Django-SOAP`, and of course `Django`. 

### Installing

```
pip install django-clear-s2s
```

## Running Tests

```
python manage.py test
```

## Usage

In order to use the system you must add djangosoap to your installed apps in your settings.py file.

```python
INSTALLED_APPS = [
    'django_clear_s2s'
]
```

To start using the package you'll have to create some variables in your settings.py

```python
#Thompson Reuters
TR_CLEAR_S2S_HOST = ...
TR_CLEAR_S2S_SCOPES = ...
TR_CLEAR_S2S_USER = ...
TR_CLEAR_S2S_PASS = ...
TR_CLEAR_S2S_ACCESS_TOKEN = ...
TR_CLEAR_S2S_CERT_PATH = ...
TR_CLEAR_S2S_CERT_KEY_PATH = ...
TR_CLEAR_S2S_CLIENT_ID = ...
TR_CLEAR_S2S_CLIENT_SECRET = ...
```

Now, let's send that template over with some values

```python
from djangosoap.utils.ThomsonReuters import ThomsonReuters


def search_person(request):
    _dict = {
        'first_name':'JANE',
        'last_name':'SAMPLE-DOCUMENT',
        'dob':'1951-01-01',
        'ssn':'999-99-9990',
        'street':'240 Summit Avenue',
        'city':'Saint Paul',
        'state':'MN',
        'zip_code':'55102',
        'phone_number':'651-396-0726',
        'npi_number':'9999999999'
    }
    response1, response2 = self.client.person_search(**_dict)
```


## Built Using

- [Django](https://www.djangoproject.com/) - Web Framework
- [Cookiecutter Django Package](https://github.com/pydanny/cookiecutter-djangopackage) - Cookie Cutter Django Package

## Authors
- [Stephen](https://github.com/sal-git) - Working on behalf of Lender's Cooperative


## Acknowledgements

- Inspiration
