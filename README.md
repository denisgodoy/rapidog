![python](https://img.shields.io/badge/python-306998) ![django](https://img.shields.io/badge/django-092e20) ![javascript](https://img.shields.io/badge/javascript-f7df1e) ![html](https://img.shields.io/badge/html-e34f26) ![css](https://img.shields.io/badge/css-264de4)

# rapidog :dog:
#### Python project with Django model-template-view framework.

- [Creating models](https://github.com/denisgodoy/rapidog#creating-models)
- [Generating query results](https://github.com/denisgodoy/rapidog#generating-query-results)

![RAPIDOG#1](https://user-images.githubusercontent.com/56933400/108790199-e0906d00-755a-11eb-91e1-3da5bb1c2ecf.jpg)

## Creating models
Migrating Classes' tables to the server-side and populating information for Users, Products and Stores on the ecommerce.

```ruby

class Usuario(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
```

## Generating query results

Method to receive user's input and validate within the category, showing only current available products.

```ruby
def alimentacao(request):
    query = request.GET.get('q','')
    alimentacao = Produto.objects.filter(disponivel=True, categoria='alimentacao').order_by('-id')
```
If there's a query, the user can search by either name or brand, filtering products.

```ruby
    if query:
            queryset = (Q(nome_produto__icontains=query)) | (Q(marca__icontains=query))
            resultados = Produto.objects.filter(queryset, categoria='alimentacao').order_by('-id')
    else:
        resultados = []
```

Rendering products that match the queryset.

```ruby

    context = {
        'query': query,
        'resultados': resultados,
        'alimentacao': alimentacao,
    }

    return render(request, 'alimentacao.html', context)
```

![RAPIDOG#2](https://user-images.githubusercontent.com/56933400/108771449-6f40c200-753a-11eb-8333-c97496c39047.gif)
