import requests
import csv


class hackFMIMatcher:
    def __init__(self):
        self.mentors = {}
        self.get_mentors()
        self.teams = []

    def get_mentors(self):
        r = requests.get("https://raw.github.com/Hackfmi/HackFMI-4/master/mentors.md")
        string = r.text
        l = string.split("\n")
        for line in l:
            if line.startswith("###"):
                self.mentors[line[4:]] = {}


        # with open("mentors.csv", "wt") as ofile:
        #     writer = csv.writer(ofile, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        #     for mentor in mentors:
        #         writer.writerow([mentor])

    def load_teams(self, filename):
        teams = []
        with open(filename,newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter='|', quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                teams.append(row)
        return teams

    def menu(self):
        filename = input("Enter filename > ")
        teams = self.load_teams(filename)
        for team in teams:
            self.teams.append((team[0], team[len(team)-1]))
            for i in range(1,len(team)-1):
                team[i] = team[i][1:len(team[i])-1]
                if team[i]  in self.mentors.keys():
                    if i not in self.mentors[team[i]].keys():
                        self.mentors[team[i]][i] = set()
                    self.mentors[team[i]][i].add(team[0])

        print(self.mentors)
        for mentor in self.mentors:
            pass

matcher = hackFMIMatcher()
matcher.menu()

