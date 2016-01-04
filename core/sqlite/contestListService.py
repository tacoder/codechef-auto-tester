from core.sqlite import Sqlite
import sqlite3

def insertContest(contestName,contestCode):
    try:
        Sqlite.executeQuery("insert into contestList values (?,?)",[(contestName,contestCode)])
        Sqlite.executeQuery("create table ? (problemName,problemCode)",[(contestCode)])
        return True
    except sqlite3.IntegrityError:
        print("Integrity while inserting contest: name:" + contestName + ", contestCode" + contestCode)
        return False

def insertProblemIntoContest(contestCode,problemName,problemCode):
    try:
        Sqlite.executeQuery("insert into ? values (?,?)",[(contestCode,problemName,problemCode)])
        return True
    except sqlite3.IntegrityError:
        print("Integrity while inserting contest: contestCode:" + contestCode + ", problemName:" + problemName + ", problemCode:" + problemCode)
        return False
