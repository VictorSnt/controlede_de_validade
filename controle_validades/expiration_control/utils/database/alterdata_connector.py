from contextlib import contextmanager
from typing import Any, Type
import psycopg2


class AlterdataConnector:

    def __init__(self, host: str, port: str, dbname: str, user: str, password: str):
        self.host = host
        self.port = port
        self.dbname = dbname
        self.user = user
        self.password = password
        self.error = None
        self.conn = None
        self.cursor = None
    
    @contextmanager
    def connect(self) -> Type["AlterdataConnector"]:
        try:
            conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                dbname=self.dbname,
                user=self.user,
                password=self.password
            )
            self.conn = conn
            self.cursor = self.conn.cursor()
            self.error = None
            yield self
        
        except psycopg2.Error as e:
            raise e
        
        finally:
            self.closeconnection()
            

    def get_product(self, cdprincipal: str
        ) -> list[dict[str, Any]]|list[None]:

        if not self.cursor:
            raise psycopg2.Error("Você não esta conectado em nenhum banco")
    
        try:
            if not cdprincipal.isnumeric():
              raise ValueError("cdprincipal must bem numeric string on alterdata_connector")  
            query = f"""
            SELECT iddetalhe, dsdetalhe, cdprincipal FROM wshop.detalhe
            WHERE cdprincipal = '{cdprincipal}'
            """
            self.cursor.execute(query, cdprincipal)
        
            columns = [desc[0] for desc in self.cursor.description]
            rows = self.cursor.fetchall()
            results_list = [
                {column: value for column, value in zip(columns, row)}
                    for row in rows
            ]

            return results_list or []

        except psycopg2.Error as e:
            raise e
            
    def get_image(self, idproduto):
        
        if not self.cursor:
            raise psycopg2.Error("Você não esta conectado em nenhum banco")
    
        try:
            if not idproduto:
              raise ValueError("cdprincipal must bem numeric string on alterdata_connector")  
            query = f"""
            SELECT foto FROM wshop.detalhefoto
            WHERE iddetalhe = '{idproduto}'
            """
            self.cursor.execute(query)
        
            columns = [desc[0] for desc in self.cursor.description]
            rows = self.cursor.fetchall()
            results_list = [
                {column: value for column, value in zip(columns, row)}
                    for row in rows
            ]

            return results_list or []

        except psycopg2.Error as e:
            raise e
    
    def closeconnection(self) -> None:

        try:
            self.cursor.close()
            self.conn.close()
            self.error = None
            return True

        except psycopg2.Error as e:
            raise e
            
