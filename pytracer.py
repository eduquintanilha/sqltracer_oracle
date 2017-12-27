#!/usr/bin/python

import cx_Oracle
import datetime

con = cx_Oracle.connect('user/password@host_ip/sid')
data = datetime.datetime.now().strftime('%d-%m-%Y_%Hh%Mm')
nome_arquivo = "%s.txt" % (data)
arquivo = open(nome_arquivo,"a")




cur = con.cursor()

sql = "SELECT  OSUSER \
              ,SESS.TERMINAL \
              ,SESS.PROGRAM \
              ,SESS.MODULE \
              ,SESS.ACTION \
              ,SQL_TEXT \
         FROM  V$SESSION SESS JOIN V$SQL SQL \
                    ON (SESS.SQL_ADDRESS = SQL.ADDRESS \
                       AND SQL.HASH_VALUE = SESS.SQL_HASH_VALUE \
                       AND SESS.SQL_CHILD_NUMBER = SQL.CHILD_NUMBER) \
         WHERE  SESS.STATUS = 'ACTIVE' "

while 1 > 0:
    data_log = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    cur.execute(sql)
    dados = str(cur.fetchone())
    dados = "%s - %s" % (data_log,dados)
    for i in dados:
        arquivo.write(i)

    arquivo.write("\n\n")

arquivo.close()
cur.close()
con.close()
