from GraphManager import GraphManager


class ChooseLocationViewModel:
    def __init__(self, graph_manager: "GraphManager"):
        self.graph_manager = graph_manager
        self.bar_results = ""
        self.club_results = ""
        self.brewery_results = ""

    def calculate_bar_walk_results(self):
        self.bar_results = self.graph_manager.get_bar_results()

    def calculate_club_walk_results(self):
        self.club_results = self.graph_manager.get_club_results()

    def calculate_brewery_walk_results(self):
        self.brewery_results = self.graph_manager.get_brewery_results()
