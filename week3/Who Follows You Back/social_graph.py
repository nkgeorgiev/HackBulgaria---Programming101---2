from graph import Graph
import requests

auth = ("*****", "")
url = "https://api.github.com/users/{}/following"


class SocialGraph:
    def __init__(self, username, depth):
        self.graph = Graph()
        self.username = username
        self.depth = depth
        self.get_following(self.username)

    def get_following(self, username):
        r = requests.get(url.format(username), auth=auth)
        for person in r.json():
            self.graph.add_edge(username, person["login"])

    def steps_to(self, username, username2):
        queue = [username]
        for i in range(self.depth):
            l = len(queue)
            for j in range(l):
                username = queue.pop(0)
                r = requests.get(url.format(username), auth=auth)
                for person in r.json():
                    self.graph.add_edge(username, person["login"])
                    queue.append(person["login"])
                    if person["login"] == username2:
                        return i+1;
        return False



    def following(self):
        return list(self.graph.get_neighbours_for(self.username))

    def is_following(self, username2):
        return username2 in self.following()


S = SocialGraph("VictorVangelov", 2)
l = S.following()
print(S.steps_to("VictorVangelov", "TodorBalabanov"))
print(S.graph)
