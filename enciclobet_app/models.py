from django.db import models

# Create your models here.

class Infos(models.Model):
    class Result(models.Model):
        def __init__(self, **entries):
                self.__dict__.update(entries)

        class Detalhamento(models.Model):
            valor = models.IntegerField()
            porcentagem = models.FloatField()
            oddJusta = models.FloatField()

        equipe = models.TextField()
        marcouPrimeiroNoHT = Detalhamento()
        marcouPrimeiro = Detalhamento()
        marcouPrimeiroEVenceu = Detalhamento()
        marcouPrimeiroENaoVenceu = Detalhamento()
        sofreuPrimeiroNoHT = Detalhamento()
        sofreuPrimeiro = Detalhamento()
        sofreuPrimeiroEVenceu = Detalhamento()
        sofreuPrimeiroENaoVenceu = Detalhamento()
        numJogos = models.IntegerField()
        forma = models.TextField()

        gols0a15 = models.IntegerField()
        gols16a30 = models.IntegerField()
        gols31a45 = models.IntegerField()
        gols46a60 = models.IntegerField()
        gols61a75 = models.IntegerField()
        gols76a90 = models.IntegerField()




    resultCasa = Result()
    resultVisitante = Result()