import re, sys, random, shutil, os, time

def main():

    while True:
        try:
            clear_terminal()
            terminal = shutil.get_terminal_size((80,20)).columns
            difficulty = get_difficulty(terminal)
            clear_terminal()
            if run_terminal_game(get_board_size(terminal),difficulty,terminal) == "restart":
                continue
        except (KeyboardInterrupt, EOFError):
                handle_quit(terminal)


#----------------------
#      STARTER
#----------------------

def run_terminal_game(size, difficulty, terminal, seed = None):

    move_count =0
    board = generate_puzzle(size, difficulty, seed)
    while True:
         show_game(board, move_count, difficulty, terminal)
         move = choose_your_move(terminal, len(board))
         if move[0] == "quit":
            handle_quit(terminal)
         elif move[0] == "restart":
             clear_terminal()
             return "restart"
         elif move[0] == "help":
             if handle_help(terminal):
                continue
         elif move[0] == "invalid":
             print(center_block("\n  Invalid input.\n  Use [help] for advice. \n",terminal))
         elif move[0] == "move":
              board = toggle_cells(board,move[1],move[2])
              move_count += 1
              if has_won(board):
                   handle_win(board, move_count, difficulty, terminal)
                   while True:
                        move = choose_your_move_win(terminal, len(board))
                        if move[0] in ["quit", "restart"]:
                                if move[0] == "quit":
                                    handle_quit(terminal)
                                elif move[0] == "restart":
                                    clear_terminal()
                                    return "restart"
                        else:
                            clear_terminal()
                            print(center_block("\n\n\n  Invalid input.\n\n  Use [quit] or [restart] \n",terminal))
                            continue



def get_board_size(terminal):

    while True:

        print();print("Choose your board size:".center(terminal))
        try:
            size = int(input(" " * (terminal // 2 - 5) + ">" + " " * 3))
            if size > 12 or size < 3:
                raise ValueError
        except (TypeError,ValueError):
            clear_terminal()
            print(center_block("\nInvalid board size. Choose from 3 - 12.\n",terminal ))
            continue
        except EOFError:
            handle_quit(terminal)
        else:
            return size

def get_difficulty(terminal):

    while True:
        try:
            print();print(center_block("""Choose your Difficulty:\n"""
                                    """[Hard] - [Normal] - [Easy]\n""", terminal))
            difficulty = clean_input(input("" +" " * (terminal // 2 - 7) + ">" + " " *4))
        except EOFError:
            handle_quit(terminal)
        else:
            if difficulty in ["EASY","NORMAL","HARD"]:
                return difficulty
            else:
                clear_terminal()
                print(center_block("\nInvalid difficulty. Choose Easy, Normal or Hard.\n",terminal ))

def generate_puzzle(size, difficulty = "EASY", seed = None):

    rand = random.Random(seed)

    while True:
        generated_board = get_board(size)
        for _ in range(difficulty_to_moves(difficulty)):
            toggle_cells(generated_board, rand.randint(0, size-1), rand.randint(0,size-1) )
        if not has_won(generated_board):
            return generated_board

#----------------------
#      CLI HELPER
#----------------------

def choose_your_move_win(terminal, size):

    print()
    try:
        move = parse_input(input(" " * (terminal // 2 - 5) + ">" + " " ),size)
    except EOFError:
        handle_quit(terminal)
    else:
        return move


def choose_your_move(terminal, size):

    print();print("Choose your Move:".center(terminal))
    move = parse_input(input(" " * (terminal // 2 - 5) + ">" + " " * 3 ),size)

    return move

def handle_quit(terminal):

    clear_terminal()
    sys.exit(center_block("\n\n\n\n\n\n  GOODBYE!\n\n\n\n\n\n", terminal))


def handle_help(terminal):

    clear_terminal()
    print(center_block(""" MOVE"""
                       """\n  ___________\n"""
                       """\n  type in like \n"""
                       """   [b2] - [A3] - [e4]\n\n"""
                       """\n QUIT"""
                       """\n  ___________\n"""
                       """\n  type in [quit]\n\n"""
                       """\n  RESTART"""
                       """\n  ___________\n"""
                       """\n  type in [restart]\n\n"""

                         """  Continue?\n""",terminal))
    input(" " * (terminal // 2 - 5) + ">" + " " * 4)
    return True

def handle_win(board, move_count, difficulty, terminal):

    clear_terminal()
    repeat_win_sequence(board, move_count, difficulty, terminal)
    clear_terminal()
    print(center_block("""\n\n\nCONGRATULATIONS!\n"""
                        """\ntype [restart] for another game\n"""
                        """\ntype [quit] for quitting""" ,terminal))
    ...

def show_game(board, move_count, difficulty, terminal):

    clear_terminal()
    print(center_block(format_board(board),terminal))
    print(center_block(format_stats(move_count, count_lights_on(board), difficulty),terminal))
    print(center_block("""\ntype [help] for advice\n""" ,terminal))

#----------------------
#      MOVER
#----------------------

def toggle_cells(board, row, column):

    for _row, _column in get_neighbors(len(board),row, column):
                board[_row][_column] = not (board[_row][_column])

    return board

def toggle_cell(board, row, column):

     board[row][column] = not board[row][column]

     return board

#----------------------
#       FORMAT
#----------------------

def format_stats(move_count, lights_on, difficulty):

    return f"\nMOVE COUNT: {move_count} | LIGHTS ON: {lights_on} | DIFFICULTY: {difficulty.upper()}"

def center_block(text,width):
     lines = text.splitlines()
     centered_lines = []
     for line in lines:
        centered_line = line.center(width)
        centered_lines.append(centered_line)

     return"\n".join(centered_lines)

def format_board(board, on_symbol="O", off_symbol="."):

     lines = [] ; columns = []
     lines.append("")
     for column in range(len(board)):
          columns.append(str(column+1))

     header ="  " + "  ".join(columns)
     border ="   +-"+ "---" * (len(board)) + "+"
     lines.append(header);lines.append(border)

     for row in range(len(board)):
        row_label = (chr(ord("A") + row))
        symbols = []
        for column in range(len(board)):
             if board[row][column]:
                  symbols.append(on_symbol)
             else:
                  symbols.append(off_symbol)
        rows = f"{row_label}  | " + "  ".join(symbols) + "  |"
        lines.append(rows)
     lines.append(border); lines.append("")

     return "\n".join(lines)


#----------------------
#      INPUT
#----------------------


def clean_input(text):

     text = re.sub(r"[^a-zA-Z0-9]", "", text)
     return text.upper()

def parse_input(text, size):

     text = clean_input(text)

     if text in ["QUIT", "RESTART", "HELP"]:
        return (text.lower(),None,None)
     else:
        if len(text) < 2 or not text[0].isalpha() or not text[1:].isdigit():
             return ("invalid", None, None)
        else:
            row_letter = ord(text[0]) - ord("A")
            col_number = int(text[1:])-1
            if valid_pos(size, row_letter, col_number):
                return ("move", row_letter, col_number)
     return ("invalid", None, None)


#----------------------
#      HELPER
#----------------------

def clear_terminal():
     os.system("cls" if os.name == "nt" else "clear")

def get_board(size):

    board = []
    for _ in range(size):
          new_row = []
          for _ in range(size):
              new_row.append(False)
          board.append(new_row)

    return board

def valid_pos(size, row, column):

  return ( 0 <= row < size) and (0 <= column < size)

def get_neighbors(size, row, column):

    candidates = [
        (row, column),
        (row-1, column),
        (row+1, column),
        (row, column-1),
        (row, column+1),
    ]

    affected = []
    for candidate_row, candidate_column in candidates:
            if valid_pos(size, candidate_row, candidate_column):
                affected.append((candidate_row, candidate_column))

    return affected

def count_lights_on(board):

    counter = 0
    for row in range(len(board)):
        for column in range(len(board)):
             if board[row][column] == True:
                  counter+=1
    return counter

def has_won(board):

    return not count_lights_on(board)

def difficulty_to_moves(difficulty):

    difficulty = clean_input(difficulty)
    if difficulty == "EASY":
        return 1
    elif difficulty == "NORMAL":
        return 5
    elif difficulty == "HARD":
         return 9
    else:
         return 5



#----------------------
#      VISUALS
#----------------------


def toggle_all_cells(board, move_count, difficulty, terminal):

    for row in range(len(board)):
        for column in range(len(board)):
             toggle_cell(board, row, column)
    time.sleep(0.2)
    show_game(board, move_count, difficulty, terminal)

    return board

def repeat_win_sequence(board, move_count, difficulty, terminal):

    toggle_all_cells(board, move_count, difficulty, terminal)
    time.sleep(0.3)
    toggle_all_cells(board, move_count, difficulty, terminal)
    time.sleep(0.5)
    toggle_all_cells(board, move_count, difficulty, terminal)
    time.sleep(0.3)
    toggle_all_cells(board, move_count, difficulty, terminal)
    time.sleep(0.5)
    toggle_all_cells(board, move_count, difficulty, terminal)
    time.sleep(0.5)




#---------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__== "__main__":
     main()

