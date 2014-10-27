import requests
import random


class TeamMatcher:
    def __init__(self):
        self.r = None
        self.students = []
        self.courses = {}
        self.get_request("https://hackbulgaria.com/api/students")
        self.get_courses()


    def get_request(self, remote):
        self.r = requests.get(remote, verify=False)
        if self.r.status_code == 200:
            self.students = self.r.json()

    def get_courses(self):
        courses = set()
        for student in self.students:
            for course in student["courses"]:
                courses.add(course["name"])

        for i, course in enumerate(courses):
            self.courses[i] = course

    def list_courses(self):
        for i in self.courses.keys():
            string = "[{}] {}".format(i, self.courses[i])
            print(string)

    def match_teams(self, course_id, team_size, group_time):
        available_students = []
        for student in self.students:
            if student["available"]:
                for course in student["courses"]:
                    if course["group"] == group_time and course["name"] == self.courses[course_id]:
                        available_students.append(student["name"])

        i = 0
        while len(available_students) > 0:
            if i == team_size:
                i = 0
                print("========================")
            else:
                a = random.randint(0, len(available_students) - 1)
                if i < team_size:
                    print(available_students[a])
                    available_students.pop(a)
                    i +=1




    def menu(self):

        print("Hello, you can use one the following commands: ")
        print("list_courses - this lists all the courses that are available now.")
        print("match_teams <course_id>, <team_size>, <group_time>: ")
        print("Exit to exit\n")
        while True:
            choice = input("> ")
            choice = choice.split(" ")
            if choice[0] == "list_courses":
                self.list_courses()
                print()
            elif choice[0] == "match_teams" and len(choice) == 4:
                self.match_teams(int(choice[1]), int(choice[2]), int(choice[3]))
                print()
            elif choice[0] == "Exit":
                break
            else:
                print("Wrong Input")
                print()


def main():
    t = TeamMatcher()
    t.menu()

if __name__ == '__main__':
    main()
