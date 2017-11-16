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

# PART 1
# ------

# All columns
print('==> Get all columns of all tracks')
cur.execute('...')
results = cur.fetchall()
print(results[0])
print('--> Result Rows:', len(results))
print()

def execute_and_print(query, numer_of_results=1):
    cur.execute(query)
    results = cur.fetchall()
    for r in results[:numer_of_results]:
        print(r)
    print('--> Result Rows:', len(results))
    print()


# Single column
print('==> Get names of all tracks')
# execute_and_print('select ... from ... ')

# Multiple columns
print('==> Get Name, AlbumId of all tracks')
# execute_and_print('select ... from ... ')

# Multiple columns conditional using equals operator
print('==> Get Name and AlbumId of all tracks with AlbumId 3')
# execute_and_print('select ... from ... where ... ')

# VARIATION: Multiple columns conditional using comparison operator
print('==> Get Name and AlbumId of all tracks with AlbumId upto 5')
# execute_and_print('select ... from ... where ... ')

# VARIATION: Multiple columns conditional using 'in' operator
print('==> Get Name and AlbumId of all tracks with AlbumId 3, 5, and 7')
# execute_and_print('select ... from "Track" where ... in (...)')

# Multiple columns conditional like
print('==> Get Name and AlbumId of all tracks if Name contains fast')
# execute_and_print("""select "Name", "AlbumId" from "Track" where ... like ... """)

# VARIATION: Multiple columns conditional case insensitive like
print('==> Get Name and AlbumId of all tracks if Name contains fast or Fast')
# execute_and_print("""select "Name", "AlbumId" from "Track" where ... ilike ...""")

# PART 2
# ------

# get count of Tracks
print('==> Get count of all tracks using *')
# execute_and_print(""" select ... from "Track" """)

# VARIATION: Difference between count(*), count("TrackId"), count("Composer")
print('==> Get count of all tracks using TrackId')
# execute_and_print(""" select ... from "Track" """)

print('==> Get count of all tracks using Composer')
# execute_and_print(""" select ... from "Track" """)

# get count of Tracks conditional
print('==> Get count of all tracks with AlbumId 3')
# execute_and_print(""" select ... from "Track" where ...""")

# AVG
print('==> Get average playtime of all tracks')
# execute_and_print(""" select ... from "Track" """)

# AVG conditional
print('==> Get average playtime of all tracks with AlbumId 3')
# execute_and_print(""" select ... from "Track" where ... """)

# PART 3
# ------

# GROUP BY
print('==> Get average playtime of all tracks for each Album')
# execute_and_print(""" select "AlbumId", ... from "Track" group by ... """)

# ORDER BY
print('==> Get average playtime of all tracks for each Album and order them by AlbumId')
# execute_and_print(""" select "AlbumId", ... from "Track" group by ... order by ... """, 5)

# ORDER BY DESC
print('==> Get Name, AlbumId of all tracks and sort them by Name in descending order')
# execute_and_print('select "Name", "AlbumId" from "Track" order by ...', 5)

# ORDER BY Multiple different orders
print('==> Get Name, AlbumId of all tracks and sort them by AlbumId, and then by Name in descending order')
# execute_and_print('select "Name", "AlbumId" from "Track" order by ...', 5)

# PART 4
# ------

# INNER JOIN ON condition
print('==> Get Name, AlbumTitle of all tracks')
# execute_and_print("""select ...
#     from ... INNER JOIN ... ON (...) """)

# INNER JOIN ON condition with filter conditions
print('==> Get Name, AlbumTitle of all tracks if Name contains fast or Fast')
# execute_and_print("""select ...
#     from ... INNER JOIN ... ON (...)
#     where ... """, 5)
