import psycopg2
import psycopg2.extras
from config import *

def get_connection_and_cursor():
    try:
        if db_password != "":
            db_connection = psycopg2.connect("dbname='{0}' user='{1}' password='{2}'".format(db_name, db_user, db_password))
            print("Success connecting to database")
        else:
            db_connection = psycopg2.connect("dbname='{0}' user='{1}'".format(db_name, db_user))
    except:
        print("Unable to connect to the database. Check server and credentials.")
        sys.exit(1) # Stop running program if there's no db connection.

    db_cursor = db_connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    return db_connection, db_cursor

conn, cur = get_connection_and_cursor()


def execute_and_print(query, numer_of_results=1):
    cur.execute(query)
    results = cur.fetchall()
    for r in results[:numer_of_results]:
        print(r)
    print('--> Result Rows:', len(results))
    print()


# AVG in minutes
print('==> Get average playtime in minutes of all tracks')
# execute_and_print(""" select ... from "Track" """)

# GROUP BY conditional
print('==> Get average playtime of all tracks for each Album and having avg playtime upto 4 minutes')
# execute_and_print(""" select "AlbumId", ... from "Track" group by ... having ... """, 5)

# INNER JOIN ON condition with group by
print('==> Get AlbumTitle, count of all tracks per AlbumTitle')
# execute_and_print("""select ...
#     from ... INNER JOIN ... ON (...)
#     group by ... order by ... """, 5)

# INNER JOIN ON condition with group by and conditional
print('==> Get AlbumTitle, count of all tracks per AlbumTitle containing more than 20 tracks')
# execute_and_print("""select ...
#     from ... INNER JOIN ... ON (...)
#     group by ... having ... """, 5)

# Subquery as a column
print('==> Get Name, AlbumTitle of all tracks using Subquery')
# execute_and_print("""select "Name", (...) from "Track" """, 5)

# Subquery as a column with filter condition
print('==> Get Name, AlbumTitle of all tracks using Subquery if Name contains fast or Fast')
# execute_and_print("""select "Name", (...) from "Track"  where ... """, 5)

# Subquery as a where condition
print('==> Get Name, AlbumId of all tracks if Album Title is Iron Maiden (using subquery and case insensitive)')
# execute_and_print("""select "Name", "AlbumId" from "Track"  where
#     "AlbumId" = (...) """, 5)
