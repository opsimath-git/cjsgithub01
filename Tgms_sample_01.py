import cx_Oracle

import os
os.putenv('NLS_LANG', '.UTF8')

connection = cx_Oracle.connect('tgmsapp', 'tgmsapp', 'localhost/TGMS')

cursor = connection.cursor()

cursor.execute(""" select dp from DP_TAG_MASTER""")

for dp in cursor:
    print("Tag is : ", dp)
