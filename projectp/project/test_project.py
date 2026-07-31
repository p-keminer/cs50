from project import get_board, get_neighbors, valid_pos, toggle_cells, toggle_cell, has_won, count_lights_on
from project import clean_input, parse_input, get_board_size, generate_puzzle
import pytest

def test_get_board_size():
    with pytest.raises(TypeError):
        get_board_size("abc")
    with pytest.raises(TypeError):
        get_board_size("144")


def test_valid_pos():
    assert valid_pos(len(get_board(5)),3 ,2)    == True
    assert valid_pos(len(get_board(7)), 10, 6)  == False
    assert valid_pos(len(get_board(5)), 4, 4)   == True
    assert valid_pos(len(get_board(3)), 0, 0)   == True
    assert valid_pos(len(get_board(3)), -1, 0)  == False

def test_get_neighbors():
    assert get_neighbors(len(get_board(3)),0 ,0)    == [(0,0),(1,0),(0,1)]
    assert get_neighbors(len(get_board(5)), 2, 2)   == [(2,2),(1,2),(3,2),(2,1),(2,3)]
    assert get_neighbors(len(get_board(5)), 4, 4)   == [(4,4),(3,4),(4,3)]
    assert get_neighbors(len(get_board(7)), 4, 4)   == [(4,4),(3,4),(5,4),(4,3),(4,5)]

#    1 2 3 4 5
#A  00,01,02,03,04      1.mid      0,0
#B  10,11,12,13,14      2.top      -1,0
#C  20,21,22,23,24      3.down     +1,0
#D  30,31,32,33,34      4.left     0,-1
#E  40,41,42,43,44      5.right    0,+1


def test_toggle_cells():
    test_board = get_board(3)
    toggle_cell(test_board,0,0)
    toggle_cell(test_board,1,0)
    toggle_cell(test_board,0,1)

    assert count_lights_on(test_board) == 3

    assert toggle_cells(get_board(3), 0, 0) == test_board
    assert toggle_cells(get_board(3), 1, 0) != test_board

    test_board_2 = get_board(5)
    toggle_cell(test_board_2,2,2); toggle_cell(test_board_2,1,2)
    toggle_cell(test_board_2,3,2); toggle_cell(test_board_2,2,1)
    toggle_cell(test_board_2,2,3)

    assert count_lights_on(test_board_2) == 5

    assert toggle_cells(get_board(5), 2, 2) == test_board_2
    assert toggle_cells(get_board(5), 3, 2) != test_board_2

def test_toggle_cell():
    assert toggle_cell(get_board(3),2,2) != get_board(3)

    test_board_3 = get_board(3)
    test_board_3[2][2] = not test_board_3[2][2]
    assert test_board_3 == toggle_cell(get_board(3),2,2)
    assert count_lights_on(test_board_3) == 1

def test_has_won():
    assert has_won(get_board(3)) == True
    test_board_4 = get_board(3)
    assert has_won(test_board_4) == True
    toggle_cells(test_board_4, 1,1)
    assert has_won(test_board_4) == False
    toggle_cell(test_board_4, 1,1)
    assert has_won(test_board_4) == False

def test_count_lights_on():
    assert count_lights_on(toggle_cells(get_board(3),2,2)) == 3
    assert count_lights_on(toggle_cell(get_board(3),2,2)) == 1
    assert count_lights_on(toggle_cells(get_board(3),1,1)) == 5

def test_clean_input():
    assert clean_input(" b3 ") == "B3"
    assert clean_input(" quIt ") == "QUIT"
    assert clean_input(" qu%I-t ") == "QUIT"
    assert clean_input(" b+.,:*3 - ") == "B3"

def test_parse_input():
    assert parse_input(" b3 ", 5) == ("move", 1 , 2)
    assert parse_input(" quIt ", 3) == ("quit",None,None)
    assert parse_input(" res%ta-rt ", 3) == ("restart",None,None)
    assert parse_input(" b+.,:*3 - ", 5) == ("move", 1 , 2)
    assert parse_input(" b+.afsd,:*3 - ", 5) == ("invalid", None , None)
    assert parse_input(" help - ", 5) == ("help", None , None)
    assert parse_input(" bb3 ", 5) == ("invalid", None , None)

def test_generate_puzzle_dev_seed():
    #assert count_lights_on(generate_puzzle(5, clean_input("normal"), 10)) == 10
    #assert count_lights_on(generate_puzzle(5, clean_input("normal"))) != 10
    #assert count_lights_on(generate_puzzle(5, clean_input("easy"), 10)) == 9
    #assert count_lights_on(generate_puzzle(5, clean_input("easy"))) != 9
    #assert count_lights_on(generate_puzzle(5, clean_input("hard"), 10)) == 10
    #assert count_lights_on(generate_puzzle(5, clean_input("hard"))) != 10
    #assert count_lights_on(generate_puzzle(5, clean_input("normal"))) != count_lights_on(generate_puzzle(5, clean_input("normal"), 10)) == 10
    #test_count = count_lights_on(generate_puzzle(5, clean_input("easy")))
    #assert count_lights_on(generate_puzzle(5, clean_input("easy"), 10)) != test_count
    ...
