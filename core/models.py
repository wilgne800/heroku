from django.db import models

class Poduto(models.Model):
    nome = models.CharField('nome',max_length=100)
    preco = models.DecimalField('preco', decimal_places=2, max_digits=15)
    descricao = models.CharField('descricao',max_length=250)
    estoque = models.IntegerField('estoque', default=0)
    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField('nome',max_length=100)
    sobrenome = models.CharField('sobrenome',max_length=100)
    emal = models.EmailField('emal',max_length=100)
    def __str__(self):
        return self.nome