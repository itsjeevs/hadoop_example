#!/usr/bin/python
import sys


class GameResult:
    def __init__(self, score):
        self.score = score
        self.process()

    def process(self):
        home, away = self.score.split("-")

        self.home_goals = int(home.split(" ")[-1])
        self.home_team = " ".join(home.split(" ")[:-1]).strip()

        self.away_goals = int(away.split(" ")[0])
        self.away_team = " ".join(away.split(" ")[1:]).strip()

        self.home_goal_diff = self.home_goals - self.away_goals
        self.away_goal_diff = -self.home_goal_diff

        if self.home_goals > self.away_goals:
            self.home_winner = "1"
            self.away_winner = "0"
            self.is_draw = "0"
            self.home_points = "3"
            self.away_points = "0"
        elif self.home_goals < self.away_goals:
            self.home_winner = "0"
            self.away_winner = "1"
            self.is_draw = "0"
            self.home_points = "0"
            self.away_points = "3"
        else:
            self.home_points = "1"
            self.away_points = "1"
            self.is_draw = "1"
            self.home_winner = "0"
            self.away_winner = "0"

    def __str__(self):
        return "\n".join(
            ["\t".join(
                [self.home_team, "home", self.home_winner, self.is_draw, self.away_winner, str(self.home_goals),
                    str(self.away_goals), self.home_points]),
            "\t".join(
                [self.away_team, "away", self.away_winner, self.is_draw, self.home_winner, str(self.away_goals),
                    str(self.home_goals), self.away_points])])


valid_lines = []
for line in sys.stdin:
    if "*" in line:
        valid_lines.append(line.replace("*", "").strip())

for line in valid_lines:
    a_game = GameResult(line)
    print a_game