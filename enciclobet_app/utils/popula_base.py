import pandas as pd
import requests
from enciclobet_app.utils import CONSTANTES
from enciclobet_app.utils import scripts

from enciclobet_app.utils.conexao import Conexao
from pandas import read_excel

class PopulaBase:

    @staticmethod
    def start():
        con=Conexao()
        con.criarTabelas()

        
        # url = "https://github.com/futpythontrader/YouTube/raw/main/x_FutPythonTrader_Base_de_Dados_2022_2024_x.xlsx"
        # resp = requests.get(url)

        file_name = 'enciclobet_app\\utils\\dados_temporada_atual.xlsx'
        # with open(file_name, 'wb') as output:
        #     output.write(resp.content)

        df = read_excel(file_name, engine='openpyxl') 

        jogosCadastrados = con.consultar("select id_jogo from jogos")

        loadingImpresso = 1
        for index, row in df.iterrows():

            loadingPorcentagem = index/len(jogosCadastrados) * 100
            if(loadingPorcentagem > loadingImpresso):
                print("loading ", loadingImpresso, "%")
                loadingImpresso+=1
                
            
            if row[CONSTANTES.Id_Jogo] not in jogosCadastrados:
            # if '/' in row[CONSTANTES.Season]:

                # Inserindo dados na tabela de gols
                golsA = row[CONSTANTES.Goals_A_Minutes].replace("[", "").replace("]", "").replace("\'", "").split(',')
                golsH = row[CONSTANTES.Goals_H_Minutes].replace("[", "").replace("]", "").replace("\'", "").split(',')

                minuto = '0'
                acrescimo = '0'

                if golsH[0]:
                    for x in golsH:
                        if "+" in x:
                            minuto = x.split("+")[0]
                            acrescimo = x.split("+")[1]
                        else:
                            minuto = x

                        con.manipular(scripts.insertGols.format(
                                row[CONSTANTES.Id_Jogo],
                                "\'H\'",
                                "\'" + row[CONSTANTES.Home].replace("\'", "\'\'") + "\'",
                                minuto.strip(),
                                acrescimo.strip(),
                        ))

                minuto = '0'
                acrescimo = '0'

                if golsA[0]:
                    for x in golsA:
                        if "+" in x:
                            minuto = x.split("+")[0]
                            acrescimo = x.split("+")[1]
                        else:
                            minuto = x

                        con.manipular(scripts.insertGols.format(
                                row[CONSTANTES.Id_Jogo],
                                "\'A\'",
                                "\'" + row[CONSTANTES.Away].replace("\'", "\'\'") + "\'",
                                minuto.strip(),
                                acrescimo.strip(),
                        ))
                
                
                # Inserindo dados na tabela de odds
                con.manipular(scripts.insertOdds.format(
                    row[CONSTANTES.Id_Jogo],
                    row[CONSTANTES.HT_Odds_H],
                    row[CONSTANTES.HT_Odds_D],
                    row[CONSTANTES.HT_Odds_A],
                    row[CONSTANTES.HT_Odds_Over05],
                    row[CONSTANTES.HT_Odds_Under05],
                    row[CONSTANTES.HT_Odds_Over15],
                    row[CONSTANTES.HT_Odds_Under15],
                    row[CONSTANTES.HT_Odds_Over25],
                    row[CONSTANTES.HT_Odds_Under25],
                    row[CONSTANTES.FT_Odds_H],
                    row[CONSTANTES.FT_Odds_D],
                    row[CONSTANTES.FT_Odds_A],
                    row[CONSTANTES.FT_Odds_Over05],
                    row[CONSTANTES.FT_Odds_Under05],
                    row[CONSTANTES.FT_Odds_Over15],
                    row[CONSTANTES.FT_Odds_Under15],
                    row[CONSTANTES.FT_Odds_Over25],
                    row[CONSTANTES.FT_Odds_Under25],
                    row[CONSTANTES.Odds_BTTS_Yes],
                    row[CONSTANTES.Odds_BTTS_No],
                    row[CONSTANTES.Odds_DuplaChance_1X],
                    row[CONSTANTES.Odds_DuplaChance_12],
                    row[CONSTANTES.Odds_DuplaChance_X2],
                    row[CONSTANTES.Odds_Corners_H],
                    row[CONSTANTES.Odds_Corners_D],
                    row[CONSTANTES.Odds_Corners_A],
                    row[CONSTANTES.Odds_Corners_Over75],
                    row[CONSTANTES.Odds_Corners_Over85],
                    row[CONSTANTES.Odds_Corners_Over95],
                    row[CONSTANTES.Odds_Corners_Over105],
                    row[CONSTANTES.Odds_Corners_Over115],
                ))


                # Inserindo dados na tabela de jogos
                con.manipular(scripts.insertJogos.format(
                    row[CONSTANTES.Id_Jogo],
                    f'\'{row[CONSTANTES.League]}\'',
                    f'\'{row[CONSTANTES.Season]}\'',
                    f'\'{row[CONSTANTES.Date]}\'',
                    row[CONSTANTES.Rodada],
                    "\'" + row[CONSTANTES.Home].replace("\'", "\'\'") + "\'",
                    "\'" + row[CONSTANTES.Away].replace("\'", "\'\'") + "\'",
                    row[CONSTANTES.HT_Goals_H],
                    row[CONSTANTES.HT_Goals_A],
                    row[CONSTANTES.HT_TotalGoals],
                    row[CONSTANTES.FT_Goals_H],
                    row[CONSTANTES.FT_Goals_A],
                    row[CONSTANTES.FT_TotalGoals],
                    row[CONSTANTES.FT_Corners_H],
                    row[CONSTANTES.FT_Corners_A],
                    row[CONSTANTES.FT_TotalCorners],
                    row[CONSTANTES.PPG_Home_Pre],
                    row[CONSTANTES.PPG_Away_Pre],
                    row[CONSTANTES.PPG_Home],
                    row[CONSTANTES.PPG_Away],
                    row[CONSTANTES.XG_Home_Pre],
                    row[CONSTANTES.XG_Away_Pre],
                    row[CONSTANTES.XG_Total_Pre],
                    row[CONSTANTES.ShotsOnTarget_H],
                    row[CONSTANTES.ShotsOnTarget_A],
                    row[CONSTANTES.ShotsOffTarget_H],
                    row[CONSTANTES.ShotsOffTarget_A],
                    row[CONSTANTES.Shots_H],
                    row[CONSTANTES.Shots_A],
                ))
        
        print('finalizado')

        con.fechar()