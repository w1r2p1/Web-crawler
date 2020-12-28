class GameInfo:
    home_team = ""
    guest_team = ""
    date = ""
    time = ""
    home_team_odd = ""
    guest_team_odd = ""
    even_odd = ""

    # , home_team_odd, guest_team_odd, even_odd

    def __init__(self, home_team, guest_team, date, time, home_team_odd, guest_team_odd, even_odd):
        self.home_team = home_team
        self.guest_team = guest_team
        self.date = date
        self.time = time
        self.home_team_odd = home_team_odd
        self.guest_team_odd = guest_team_odd
        self.even_odd = even_odd

    def __str__(self):
        return "Home team: " + self.home_team + "\n" + "Guest team: " + self.guest_team + "\n" + \
               "Date: " + self.date + "\n" + "Time: " + self.time + '\n' + "Home team odd: " + self.home_team_odd + "\n" \
                   + "Guest team odd: " + self.guest_team_odd + "\n"+ "Even odd: " + self.even_odd 

