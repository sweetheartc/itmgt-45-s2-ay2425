def relationship_status(from_member, to_member, social_graph):
    from_follows_to = to_member in social_graph[from_member]["following"]
    to_follows_from = from_member in social_graph[to_member]["following"]

    if from_follows_to and to_follows_from:
        return "friends"
    elif from_follows_to:
        return "follower"
    elif to_follows_from:
        return "followed by"
    else:
        return "no relationship"

def tic_tac_toe(board):
    size = len(board)

    for row in board:
        if row.count(row[0]) == size and row[0] != "":
            return row[0]

    for col in range(size):
        column = [board[row][col] for row in range(size)]
        if column.count(column[0]) == size and column[0] != "":
            return column[0]

    main_diag = [board[i][i] for i in range(size)]
    if main_diag.count(main_diag[0]) == size and main_diag[0] != "":
        return main_diag[0]

    anti_diag = [board[i][size - 1 - i] for i in range(size)]
    if anti_diag.count(anti_diag[0]) == size and anti_diag[0] != "":
        return anti_diag[0]

    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    total_time = 0
    current_stop = first_stop

    while current_stop != second_stop:
        for (start, end), info in route_map.items():
            if start == current_stop:
                total_time += info["travel_time_mins"]
                current_stop = end
                break

    return total_time