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

    return sorted(teams.items(), key=lambda x: (-x[1]["P"], x[0]))


def build_board(teams):
    result = ["Team                           | MP |  W |  D |  L |  P"]

    for team_name, scores in teams:

        formatted = (
            f"{team_name:<30} | "
            f"{scores["MP"]:2} | "
            f"{scores["W"]:2} | "
            f"{scores["D"]:2} | "
            f"{scores["L"]:2} | "
            f"{scores["P"]:2}"
        )
        result.append(formatted)

    return result


def tally(rows):

    teams = {}

    for row in rows:
        splitted_row = row.split(";")
        first_team, second_team, match_result = splitted_row

        teams.setdefault(first_team, {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0})
        teams.setdefault(second_team, {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0})

        update_scores(teams, first_team, second_team, match_result)

    teams = sort_teams(teams)

    return build_board(teams)
