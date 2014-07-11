#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = None

try:
    con = lite.connect('db.sqlite3')
    
    cur = con.cursor()    
    cur.execute('SELECT SQLITE_VERSION()')
    cur.execute('SELECT * FROM worldbuilder_area')
    data = cur.fetchone()
    
    print "SQLite version: %s" % data                
    
except lite.Error, e:
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close()