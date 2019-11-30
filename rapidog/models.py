from django.db import models

# Create your models here.

class Produto(models.Model):
    tipos_produto = [
    ('alimentacao', 'Alimentação'),
    ('acessorios', 'Acessórios'),
    ('higiene', 'Higiene'),
    ('brinquedos', 'Brinquedos'),
    ]

    nome_produto = models.CharField(max_length=80)
    marca = models.CharField(max_length=80)
    codigo_produto = models.CharField(max_length=1000)
    preco = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    disponivel = models.BooleanField(default=True)
    quantidade = models.IntegerField(default=1)
    categoria = models.CharField(max_length=15, choices=tipos_produto)
    descricao = models.CharField(max_length=400)
    imagem = models.ImageField(upload_to='', null=True, blank=True)

    def __str__(self):
        return self.nome_produto
