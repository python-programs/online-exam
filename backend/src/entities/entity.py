# coding=utf-8

from datetime import datetime

from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pypyodbc
import urllib
from flask import current_app


""" POSTGRESQL
# db_url = 'localhost:2261'  # http://127.0.0.1:49221/?key=b90f3443-5c17-4e41-baee-d92fd3e4fc30
# db_name = 'online-exam'
# db_user = 'postgres'
# db_password = 'Organo@2261!'
# engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
# engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
# engine = pypyodbc.connect('Driver={SQL Server};Server=192.169.156.224;Database=X4everApp;uid=X4everAppUser;pwd=Organo@1243')
# engine = psycopg2.connect(host=db_url,database=db_name,user=db_user,password=db_password)
"""
try:
    print('Starting...')
    db_driver = 'SQL Server Native Client 10.0'
    db_server = '192.169.156.224'
    db_name = 'X4everApp'
    db_user = 'X4everAppUser'
    db_password = 'Organo@1243'

    print('Implementing...')
    # params = urllib.parse.quote_plus("")
    # engine = pypyodbc.connect(f'Driver={db_driver};Server={db_server};Database={db_name};uid={db_user};pwd={db_password}')


    params = urllib.parse.quote_plus(f'DRIVER={db_driver};SERVER={db_server};DATABASE={db_name};UID={db_user};PWD={db_password}')
    engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)



    db_url_escaped = current_app.config.get('SQLALCHEMY_DATABASE_URI').replace('%', '%%')
    config.set_main_option('sqlalchemy.url', db_url_escaped)


except ConnectionError:
    print('Error')
    print(ConnectionError);

try:
    print('Executing...')
    Session = sessionmaker(bind=engine)
except ConnectionError:
    print('Error Occurred')

Base = declarative_base()


class Entity:
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    last_updated_by = Column(String)

    def __init__(self, created_by):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by

    def __exit__(self, exc_type, exc_val, exc_tb):
        engine.close()