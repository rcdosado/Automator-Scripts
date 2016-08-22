#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys


con = None

try:
    param = sys.argv[1]
    con = psycopg2.connect(database='dbname', user='dbuser',password='p4ssw0rd') 
    cur = con.cursor()    
    query = "select firstname, lastname,expertise from expertpool_employee where lastname ILIKE '%s'" % param
    cur.execute(query)
    result = cur.fetchall()
    # import pdb;pdb.set_trace()

    for row in result:
        print row[0], row[1]
        print row[2]
        print ""

    

except psycopg2.DatabaseError, e:
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()