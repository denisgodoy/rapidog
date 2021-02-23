![python](https://img.shields.io/badge/python-306998) ![django](https://img.shields.io/badge/django-092e20) ![javascript](https://img.shields.io/badge/javascript-f7df1e) ![html](https://img.shields.io/badge/html-e34f26) ![css](https://img.shields.io/badge/css-264de4)

# rapidog :dog:
#### Python project with Django model-template-view framework.

- [Creating Models](https://github.com/denisgodoy/rapidog#creating-models)
- [Constructing Templates](https://github.com/denisgodoy/rapidog#constructing-templates)
- [Rendering Views](https://github.com/denisgodoy/rapidog#rendering-views)
- [Generating query results](https://github.com/denisgodoy/rapidog#generating-query-results)

![RAPIDOG#1](https://user-images.githubusercontent.com/56933400/108790199-e0906d00-755a-11eb-91e1-3da5bb1c2ecf.jpg)

## Creating Models
Importing Djangos' models.

```python
from django.db import models
```

Creating Classes/Models to the server-side and populating information.

```python
class Usuario(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
```

## Constructing Templates
* Template tags are mandatory on Django. The base ```layout.html``` requires  ```{% load static %}``` to load assets.
* A base HTML layout should be ```header```, ```body``` and ```footer```. 
* The block content inside the base layout ```body``` is where all other pages should be rendered.

```
{% block content %}

{% endblock %}
```

All other pages that'll render within ```layout.html``` requires an extension from the base layout.
 
```
{% extends 'layout.html' %}
```

## Rendering Views
Importing Django dependencies and models to be displayed.

 ```python
from django.shortcuts import render
from rapidog.models import *
```

Rendering 5 products by category on the main products page, if marked as available.

```python
def produtos(request):
    alimentacao = Produto.objects.filter(disponivel=True, categoria='alimentacao').order_by('-id')[:5]
    higiene = Produto.objects.filter(disponivel=True, categoria='higiene').order_by('-id')[:5]
    brinquedos = Produto.objects.filter(disponivel=True, categoria='brinquedos').order_by('-id')[:5]
```

Context is necessary to access objects' properties on template.

```python
    context = {
        'alimentacao': alimentacao,
        'higiene': higiene,
        'brinquedos': brinquedos
    }

    return render(request, 'produtos.html', context)
```

## Generating query results

Importing Django's native Q application to ```views.py```.

```python
from django.db.models import Q
```

Method to get user's input and validate within the category, showing only current available products.

```python
def alimentacao(request):
    query = request.GET.get('q','')
    alimentacao = Produto.objects.filter(disponivel=True, categoria='alimentacao').order_by('-id')
```
If there's a query, the user can search by either name or brand, filtering products.

```python
    if query:
            queryset = (Q(nome_produto__icontains=query)) | (Q(marca__icontains=query))
            resultados = Produto.objects.filter(queryset, categoria='alimentacao').order_by('-id')
    else:
        resultados = []
```

Rendering products that match the queryset.

```python
    context = {
        'query': query,
        'resultados': resultados,
        'alimentacao': alimentacao,
    }

    return render(request, 'alimentacao.html', context)
```

![RAPIDOG#2](https://user-images.githubusercontent.com/56933400/108771449-6f40c200-753a-11eb-8333-c97496c39047.gif)
