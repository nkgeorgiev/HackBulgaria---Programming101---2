from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import desc
import random

Base = declarative_base()


class Highscore(Base):
    __tablename__ = "highscores"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    result = Column(Integer)

    def __str__(self):
        return "{} with {} points".format(self.name, self.result)

    def __repr__(self):
        return self.__str__()


class Expression:
    def __init__(self):
        self.functions = {"+": lambda x, y: x + y, "-": lambda x, y: x - y,
                          "*": lambda x, y: x * y, "/": lambda x, y: x // y,
                          "^": lambda x, y: x ** y, "%": lambda x, y: x % y}

    def generate_expression(self):
        op = random.choice(list(self.functions.keys()))
        if op == "^":
            a = random.randint(1, 5)
            b = random.randint(1, 3)
        else:
            a = random.randint(-10, 10)
            b = random.randint(1, 10)
        expr = "{} {} {} = ".format(a, op, b)
        ans = self.functions[op](a, b)
        return (expr, str(ans))

    def play(self):
        name = input("Enter your player name> ")
        print("Welcome {}! Let the game begin!".format(name))
        points = 0
        while True:
            print("Question #{}:".format(points+1))
            expr, ans = self.generate_expression()
            user_ans = input(expr)
            if user_ans != ans:
                print("Incorrect! Ending game. You score is: {}".format(points))
                return (name, points)
            points += 1
            print("Correct!")


class DoYouEvenMath:
    def __init__(self):
        self.engine = create_engine("sqlite:///highscores.db")
        Base.metadata.create_all(self.engine)
        self.session = Session(bind=self.engine)
        self.expr = Expression()

    def menu(self):
        print("Welcome to the \"Do you even math?\" game!\n"
              "Here are your options:\n"
              "- start\n"
              "- highscores")
        while True:
            choice = input("?> ")
            if choice == "start":
                name, result = self.expr.play()
                self.session.add(Highscore(name=name, result=result))
                self.session.commit()
            elif choice == "highscores":
                print("This is the current top10:")
                highscores = self.session.query(Highscore).order_by(desc(Highscore.result)).limit(10)
                i = 1
                for highscore in highscores:
                    print(str(i) + ". " + str(highscore))
                    i += 1
            elif choice == "exit":
                break
            else:
                print("Wrong Command")


def main():
    d = DoYouEvenMath()
    d.menu()
if __name__ == '__main__':
    main()
