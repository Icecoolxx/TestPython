import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = "binhpnsv.database.windows.net"
    SQL_DATABASE = "binhpnDb"
    SQL_USER_NAME = "binhpn"
    SQL_PASSWORD = "Emnhoem543"
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = "binhpnstaccount"
    BLOB_STORAGE_KEY = "txNEH/BBiHvfQSS/r4NWgRaxMPe6Z21NRuDlR1zUW3nYAIRbOy5ZWq1eXadPyEtIROAZuAfssczq+ASto/dUEQ=="
    BLOB_CONTAINER = "images"
