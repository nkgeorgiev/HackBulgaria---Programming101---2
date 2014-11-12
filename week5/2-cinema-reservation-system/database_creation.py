import sqlite3
import os


def create_movies_db():
    db = sqlite3.connect("cinema_reservation.db")
    db.execute("PRAGMA foreign_keys = ON")
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies(id INTEGER PRIMARY KEY, name TEXT,
                       rating TEXT)
    ''')
    cursor.execute('''INSERT INTO movies(name, rating)
                  VALUES(?,?)''', ("The Hunger Games: Catching Fire", 7.9))
    cursor.execute('''INSERT INTO movies(name, rating)
                  VALUES(?,?)''', ("Wreck-It Ralph", 7.8))
    cursor.execute('''INSERT INTO movies(name, rating)
                  VALUES(?,?)''', ("Her", 8.3))
    db.commit()


def create_projections_db():
    db = sqlite3.connect("cinema_reservation.db")
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS projections(id INTEGER PRIMARY KEY,movie_id INTEGER,
         type TEXT, date TEXT, time TEXT,
         FOREIGN KEY(movie_id) REFERENCES movies(id))
    ''')
    cursor.execute('''INSERT INTO projections(movie_id, type, date, time)
                  VALUES(?,?,?,?)''', (1, "3D", "2014-04-01", "19:10"))
    cursor.execute('''INSERT INTO projections(movie_id, type, date, time)
                  VALUES(?,?,?,?)''', (1, "2D", "2014-04-01", "19:00"))
    cursor.execute('''INSERT INTO projections(movie_id, type, date, time)
                  VALUES(?,?,?,?)''', (1, "4DX", "2014-04-02", "21:00"))
    cursor.execute('''INSERT INTO projections(movie_id, type, date, time)
                  VALUES(?,?,?,?)''', (3, "2D", "2014-04-05", "20:20"))
    cursor.execute('''INSERT INTO projections(movie_id, type, date, time)
                  VALUES(?,?,?,?)''', (2, "3D", "2014-04-02", "22:00"))
    cursor.execute('''INSERT INTO projections(movie_id, type, date, time)
                  VALUES(?,?,?,?)''', (2, "2D", "2014-04-02", "19:30"))
    db.commit()


def create_reservations_db():
    db = sqlite3.connect("cinema_reservation.db")
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservations(id INTEGER PRIMARY KEY,username TEXT,
         projection_id INTEGER, row INTEGER, col INTEGER,
         FOREIGN KEY(projection_id) REFERENCES projections(id))
    ''')
    cursor.execute('''INSERT INTO reservations(username, projection_id, row, col)
                  VALUES(?,?,?,?)''', ("RadoRado", 1, 2, 1))
    cursor.execute('''INSERT INTO reservations(username, projection_id, row, col)
                  VALUES(?,?,?,?)''', ("RadoRado", 1, 3, 5))
    cursor.execute('''INSERT INTO reservations(username, projection_id, row, col)
                  VALUES(?,?,?,?)''', ("RadoRado", 1, 7, 8))
    cursor.execute('''INSERT INTO reservations(username, projection_id, row, col)
                  VALUES(?,?,?,?)''', ("Ivo", 3, 1, 1))
    cursor.execute('''INSERT INTO reservations(username, projection_id, row, col)
                  VALUES(?,?,?,?)''', ("Ivo", 3, 1, 2))
    cursor.execute('''INSERT INTO reservations(username, projection_id, row, col)
                  VALUES(?,?,?,?)''', ("Mysterious", 5, 2, 3))
    cursor.execute('''INSERT INTO reservations(username, projection_id, row, col)
                  VALUES(?,?,?,?)''', ("Mysterious", 5, 2, 4))
    db.commit()


def main():
    if not os.path.exists("cinema_reservation.db"):
        create_movies_db()
        create_projections_db()
        create_reservations_db()
    db = sqlite3.connect("cinema_reservation.db")
    cursor = db.cursor()
    res = cursor.execute('''SELECT  movies.name, projections.date, reservations.username
        FROM movies
        INNER JOIN projections
        ON movies.id = projections.movie_id
            INNER JOIN reservations
            ON projections.id = reservations.projection_id
        ''')
    for row in res:
        print(row)

if __name__ == '__main__':
    main()
