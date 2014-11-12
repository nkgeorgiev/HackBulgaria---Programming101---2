import sqlite3
import sys


class MagicReservationSystem:
    def __init__(self):
        self.db = sqlite3.connect("cinema_reservation.db")
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()

    def show_movies(self):
        print("Current movies:")
        result = self.cursor.execute('''SELECT * FROM movies ORDER BY rating''')
        for row in result:
            print("[{}] - {} ({})".format(row["id"], row["name"], row["rating"]))

    def show_movie_projections(self, movie_id, date=False):
        movie_name = self.cursor.execute("SELECT name from movies WHERE id = ?", (movie_id,))
        for row in movie_name:
            name = row["name"]
            break

        if date is False:
            result = self.cursor.execute('''SELECT movies.name, projections.*
            FROM movies
                INNER JOIN projections
                ON movies.id = projections.movie_id
            WHERE movies.id = ?
            ORDER BY projections.date, projections.time
             ''', (movie_id, ))
        else:
            result = self.cursor.execute('''SELECT movies.name, projections.*
            FROM movies
                INNER JOIN projections
                ON movies.id = projections.movie_id
            WHERE movies.id = ? AND projections.date = ?
            ORDER BY projections.date, projections.time
             ''', (movie_id, date))
        print("Projections for movie '{}':".format(name))
        for row in result:
            print("[{}] - {} {} ({})".format(row["id"], row["date"],
                  row["time"], row["type"]))

    def print_seats(self, projection_id):
        print("Available seats (marked with a dot):")
        result = self.cursor.execute('''SELECT row, col FROM reservations WHERE projection_id = ?
            ''', (projection_id, ))
        taken_seats = []
        for row in result:
            taken_seats.append((row["row"], row["col"]))

        print("   1 2 3 4 5 6 7 8 9 10")
        for i in range(1, 11):
            if i < 10:
                print(i, end="  ")
            else:
                print(i, end=' ')
            for j in range(1, 11):
                if (i, j) not in taken_seats:
                    print('.', end=' ')
                else:
                    print('X', end=' ')
            print()
        return taken_seats

    def make_reservation(self):
        #step 1
        name = input("Step 1 (User): Enter name> ")
        num_tickets = input("Step 1 (User): Enter number of tickets> ")
        self.show_movies()

        #step 2
        movie_id = input("Step 2 (Movie): Choose a movie> ")
        self.show_movie_projections(movie_id)

        #step 3
        projection_id = input("Step 3 (Projection): Choose a projection> ")
        taken_seats = self.print_seats(projection_id)

        #step 4
        seats = []
        i = 0
        while i < int(num_tickets):
            seat = input("Step 4 (Seats): Choose seat {} (separated by one space)>".format(i+1)).split(" ")
            seat = (int(seat[0]), int(seat[1]))

            if seat[0] > 10 or seat[0] < 1 or seat[1] > 10 or seat[1] < 1:
                print("Lol no")

            elif seat in taken_seats:
                print("This seat is already taken!")

            else:
                seats.append(seat)
                i += 1

        movie = self.cursor.execute('''SELECT * from movies WHERE id = ?''', (movie_id,))
        print("This is your reservation:")
        for row in movie:
            print("Movie: {} {}".format(row["name"], row["rating"]))

        projection = self.cursor.execute('''SELECT * from projections WHERE id = ?''', (projection_id, ))
        for row in projection:
            print("Date and Time: {} {} ({})".format(row["date"], row["time"], row["type"]))

        print("Seats:", end=' ')
        for i in seats:
            print(i, end=' ')
        print()

        #step 5
        choice = input("Step 5 (Confirm - type 'finalize') > ")
        if choice == "finalize":
            for seat in seats:
                self.cursor.execute('''INSERT INTO reservations(username, projection_id, row, col)
                    VALUES(?,?,?,?)''',(name, projection_id, seat[0], seat[1]))
            self.db.commit()
            print("Thanks")
        elif choice == "give_up":
            sys.exit(0)

    def menu(self):
        command = input("Enter command> ").split()
        while(command[0] != "exit"):
            command[0] = "exit"
m = MagicReservationSystem()
# m.show_movies()
# m.show_movie_projections(1)
# m.show_movie_projections(1, "2014-04-02")
# m.print_seats(1)
m.make_reservation()
