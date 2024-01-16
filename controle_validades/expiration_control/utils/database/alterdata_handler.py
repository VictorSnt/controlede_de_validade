from dotenv import load_dotenv
from os import environ
from .alterdata_connector import AlterdataConnector

load_dotenv()
def build_connection():
    db_alterdata = AlterdataConnector(
        environ['HOST'],
        environ['PORT'], 
        environ['DBNAME'], 
        environ['USER'], 
        environ['PASSWD']
    )
    return db_alterdata

