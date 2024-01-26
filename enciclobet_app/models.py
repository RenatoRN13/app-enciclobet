from django.db import models

# Create your models here.

class Infos(models.Model):
    class Result(models.Model):
        def __init__(self, **entries):
            self.__dict__.update(entries)

        def __init__(
                self,
                equipe,
                marcouPrimeiroNoHT,
                marcouPrimeiro,
                marcouPrimeiroEVenceu,
                marcouPrimeiroENaoVenceu,
                sofreuPrimeiroNoHT,
                sofreuPrimeiro,
                sofreuPrimeiroEVenceu,
                sofreuPrimeiroENaoVenceu,
                numJogos,
                forma,
                gols0a15,
                gols16a30,
                gols31a45,
                gols46a60,
                gols61a75,
                gols76a90,
            ):
            self.equipe = equipe
            
            self.marcouPrimeiroNoHT = {
                'valor': marcouPrimeiroNoHT,
                'porcentagem': marcouPrimeiroNoHT/numJogos,
                'oddJusta': 1 / (marcouPrimeiroNoHT / numJogos ) if marcouPrimeiroNoHT != 0 else 0
            }
            self.marcouPrimeiro = {
                'valor': marcouPrimeiro,
                'porcentagem': marcouPrimeiro/numJogos,
                'oddJusta': 1 / (marcouPrimeiro/numJogos) if marcouPrimeiro != 0 else 0
            }
            self.marcouPrimeiroEVenceu = {
                'valor': marcouPrimeiroEVenceu,
                'porcentagem': marcouPrimeiroEVenceu/numJogos,
                'oddJusta': 1 / (marcouPrimeiroEVenceu/numJogos) if marcouPrimeiroEVenceu != 0 else 0
            }
            self.marcouPrimeiroENaoVenceu = {
                'valor': marcouPrimeiroENaoVenceu,
                'porcentagem': marcouPrimeiroENaoVenceu/numJogos,
                'oddJusta': 1 / (marcouPrimeiroENaoVenceu/numJogos) if marcouPrimeiroENaoVenceu != 0 else 0
            }
            self.sofreuPrimeiroNoHT = {
                'valor': sofreuPrimeiroNoHT,
                'porcentagem': sofreuPrimeiroNoHT/numJogos,
                'oddJusta': 1 / (sofreuPrimeiroNoHT/numJogos) if sofreuPrimeiroNoHT != 0 else 0
            }
            self.sofreuPrimeiro = {
                'valor': sofreuPrimeiro,
                'porcentagem': sofreuPrimeiro/numJogos,
                'oddJusta': 1 / (sofreuPrimeiro/numJogos) if sofreuPrimeiro != 0 else 0
            }
            self.sofreuPrimeiroEVenceu = {
                'valor': sofreuPrimeiroEVenceu,
                'porcentagem': sofreuPrimeiroEVenceu/numJogos,
                'oddJusta': 1 / (sofreuPrimeiroEVenceu/numJogos) if sofreuPrimeiroEVenceu != 0 else 0
            }
            self.sofreuPrimeiroENaoVenceu = {
                'valor': sofreuPrimeiroENaoVenceu,
                'porcentagem': sofreuPrimeiroENaoVenceu/numJogos,
                'oddJusta': 1 / (sofreuPrimeiroENaoVenceu/numJogos) if sofreuPrimeiroENaoVenceu != 0 else 0
            }
            
            self.numJogos = numJogos
            self.forma = forma
            
            self.gols0a15 = gols0a15
            self.gols16a30 = gols16a30
            self.gols31a45 = gols31a45
            self.gols46a60 = gols46a60
            self.gols61a75 = gols61a75
            self.gols76a90 = gols76a90