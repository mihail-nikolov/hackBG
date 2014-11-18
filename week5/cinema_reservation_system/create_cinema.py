import sqlite3

conn = sqlite3.connect("cinema.db")
cursor = conn.cursor()

cursor.execute("""PRAGMA foreign_key = ON""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Movies
                                (id INTEGER PRIMARY KEY,
                                name TEXT,
                                rating REAL)""")

conn.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS Projections
                                (id INTEGER PRIMARY KEY,
                                movie_id INTEGER,
                                type TEXT,
                                movie_date DATE,
                                time TEXT,
                                FOREIGN KEY (movie_id) REFERENCES Movies(id))""")

conn.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS Reservations
                                (id INTEGER PRIMARY KEY,
                                username TEXT,
                                projection_id INTEGER,
                                row INTEGER, col INTEGER,
                                FOREIGN KEY (projection_id) REFERENCES Projections(id))""")

conn.commit()
