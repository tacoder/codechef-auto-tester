import sqlite3
from core.Parser import getContest,getJsonDataFromUrl
from core import Constants
from core.sqlite import Sqlite

Sqlite.initializeDatabase()

getContest( 'DEC15', getJsonDataFromUrl( Constants.CODECHEF_API_URL + 'DEC15' ) )

try:
    Sqlite.executeQuery("insert into contestList values (?,?)", [("Random shitty challenge", "RSC16")])
except sqlite3.IntegrityError:
    print("Received integrity exception. seems its fucked")
    Sqlite.rollback()

for row in Sqlite.executeQuery("select * from contestList"):
    print(row)

for row in Sqlite.executeQuery("select * from DEC15"):
    print(row)
