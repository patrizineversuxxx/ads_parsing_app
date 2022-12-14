from peewee import *

db = PostgresqlDatabase('test', host='localhost',
                        port=5432, user='dummy', password='123456')