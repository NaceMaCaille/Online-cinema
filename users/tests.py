from django.test import TestCase

import psycopg2

conn = psycopg2.connect(
    dbname="cinema",
    user="postgres",
    password="2467",
    host="localhost",
    port="5432"
)

print("OK")
