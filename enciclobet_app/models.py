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

        def __init__(self):
            self.equipe = models.TextField()
            self.marcouPrimeiroNoHT = Detalhamento()
            self.marcouPrimeiro = Detalhamento()
            self.marcouPrimeiroEVenceu = Detalhamento()
            self.marcouPrimeiroENaoVenceu = Detalhamento()
            self.sofreuPrimeiroNoHT = Detalhamento()
            self.sofreuPrimeiro = Detalhamento()
            self.sofreuPrimeiroEVenceu = Detalhamento()
            self.sofreuPrimeiroENaoVenceu = Detalhamento()
            self.numJogos = models.IntegerField()
            self.forma = models.TextField()

            self.gols0a15 = models.IntegerField()
            self.gols16a30 = models.IntegerField()
            self.gols31a45 = models.IntegerField()
            self.gols46a60 = models.IntegerField()
            self.gols61a75 = models.IntegerField()
            self.gols76a90 = models.IntegerField()



    def __init__(self):
        self.resultCasa = Result()
        self.resultVisitante = Result()