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
