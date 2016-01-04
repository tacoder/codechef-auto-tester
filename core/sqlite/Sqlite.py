import sqlite3
import os
from core import Constants
global conn, cur

def initializeDatabase():
    global conn, cur
    newdb = False
    if not os.path.isfile(Constants.CONFIG_DIR + Constants.DB_FILE_NAME):
        newdb = True
    conn = sqlite3.connect(Constants.CONFIG_DIR + Constants.DB_FILE_NAME)
    cur = conn.cursor()
    if newdb:
        cur.executescript("""
        create table contestList (contestName,contestCode primary key);

        """)
# c = conn.cursor()

# c.execute()

def executeQuery(query, params = []):
    if params == []:
        queryResult = cur.execute(query)
    else:
        queryResult = cur.executemany(query, params)
    conn.commit()
    return queryResult

def finalizeDatabase():
    conn.close()

def rollback():
    conn.rollback()