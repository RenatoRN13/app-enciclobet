import psycopg2
from enciclobet_app.utils import scripts
from datetime import datetime

class Conexao():
    _db=None;
    def __init__(self):
       self._db = psycopg2.connect(database="postgres",
                                    host="localhost",
                                    user="postgres",
                                    password="1234",
                                    port="5432")

    def manipular(self, sql:str):
       try:
           cursor = self._db.cursor()
           cursor.execute(sql)
           self._db.commit()
       except Exception as e:
          cursor.execute("ROLLBACK")
          self._db.commit()

          if 'duplicate key value' not in e.args[0]:
            with open("log.txt", "a") as file:
              file.write(f'===> {datetime.now().strftime("%d/%m/%Y, %H:%M:%S")} ERROR: {e}')
              file.write("======\n")
              file.write(sql.strip())
              file.write("\n======\n\n")
          return False;
       return True;

    def consultar(self, sql):
      rs=None
      try:
          cursor = self._db.cursor()
          cursor.execute(sql)
          rs=cursor.fetchall()
      except Exception as e:
          print(e)
          return None
      return rs
    
    def proximaPK(self, tabela, chave):
      sql='select max('+chave+') from '+tabela
      rs = self.consultar(sql)
      pk = rs.first()
      return pk+1
    
    def fechar(self):
      self._db.close()

    def criarTabelas(self):
       self.manipular(scripts.createTableGols)
       self.manipular(scripts.createTableOdds)
       self.manipular(scripts.createTableJogos)
