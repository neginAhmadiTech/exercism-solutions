def update_scores(teams, first_team, second_team, match_result):

    teams[first_team]["MP"] += 1
    teams[second_team]["MP"] += 1

    if match_result == "win":

        teams[first_team]["W"] += 1
        teams[first_team]["P"] += 3

        teams[second_team]["L"] += 1

    elif match_result == "draw":
        teams[first_team]["D"] += 1
        teams[first_team]["P"] += 1

        teams[second_team]["D"] += 1
        teams[second_team]["P"] += 1

    elif match_result == "loss":
        teams[first_team]["L"] += 1

        teams[second_team]["W"] += 1
        teams[second_team]["P"] += 3

    return teams


def sort_teams(teams):

    sorted_teams = sorted(teams.items(), key=lambda x: (-x[1]["P"], x[0]))

    return sorted_teams


def print_board(teams):
    result = ["Team                           | MP |  W |  D |  L |  P"]

    for team in teams:

        team_scores = team[1]
        formatted = (
            f"{team[0]:<30} | "
            f"{team_scores['MP']:2} | "
            f"{team_scores['W']:2} | "
            f"{team_scores['D']:2} | "
            f"{team_scores['L']:2} | "
            f"{team_scores['P']:2}"
        )
        result.append(formatted)

    return result


def tally(rows):

    teams = {}

    for row in rows:
        row = row.split(";")
        first_team, second_team, match_result = row

        teams.setdefault(first_team, {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0})
        teams.setdefault(second_team, {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0})

        teams = update_scores(teams, first_team, second_team, match_result)

    teams = sort_teams(teams)

    return print_board(teams)
