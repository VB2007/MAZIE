def score_list(diff, s):
    board=list()
    with open('score_boards/'+str(diff)+'_score_board.txt', 'r+') as file_path:
        board.append(file_path.read().strip('\n'))
        board.append(str(s//30))
        board.sort()
        file_path.write('\n'.join(board))
