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

class Loja(models.Model):
    estados = [
        ('SP', 'SP'),
    ]

    cidades = [
        ('SAO', 'São Paulo')
    ]

    bairros = [
        ('Bela Vista', 'Bela Vista'),
        ('Consolação', 'Consolação'),
        ('Jd Paulista', 'Jardim Paulista'),
        ('Perdizes', 'Perdizes'),
        ('Vila Mariana', 'Vila Mariana'),
    ]

    nome_loja = models.CharField(max_length=100)
    descricao_loja = models.CharField(max_length=400)
    endereco = models.CharField(max_length=200)
    bairro = models.CharField(max_length=30, choices=bairros)
    cidade = models.CharField(max_length=30, choices=cidades)
    estado = models.CharField(max_length=2, choices=estados)
    verificado = models.BooleanField(default=True)
    logotipo = models.ImageField(upload_to='', null=True, blank=True)
    banho = models.BooleanField(default=True)
    preco_banho = models.DecimalField(decimal_places=2, max_digits=20, default=0, blank=True, null=True)
    tosa = models.BooleanField(default=True)
    preco_tosa = models.DecimalField(decimal_places=2, max_digits=20, default=0, blank=True, null=True)
    combo = models.BooleanField(default=True)
    preco_combo = models.DecimalField(decimal_places=2, max_digits=20, default=0, blank=True, null=True)
    anunciar = models.BooleanField(default=False)
    anuncio = models.ImageField(upload_to='', null=True, blank=True)

    def __str__(self):
        return self.nome_loja

class Newsletter(models.Model):
    email = models.EmailField(max_length=140)

    def __str__(self):
        return self.email