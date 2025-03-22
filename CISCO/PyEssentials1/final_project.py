__author__ = "G30v4"
__copyright__ = "MIT License"
__credits__ = ["CISCO", "NetAcad"]
__version__ = "0.0.1"

'''
Name: Tic-Tac-Toe
Descriptions:

la maquina (por ejemplo, el programa) jugará utilizando las 'X's;
el usuario (por ejemplo, tu) jugarás utilizando las 'O's;
el primer movimiento es de la maquina - siempre coloca una 'X' en el centro del tablero;
todos los cuadros están numerados comenzando con el 1 (observa el ejemplo para que tengas una referencia)
el usuario ingresa su movimiento introduciendo el número de cuadro elegido - el número debe de ser valido, por ejemplo un valor entero mayor que 0 y menor que 10, y no puede ser un cuadro que ya esté ocupado;
el programa verifica si el juego ha terminado - existen cuatro posibles veredictos: el juego continua, el juego termina en empate, tu ganas, o la maquina gana;
la maquina responde con su movimiento y se verifica el estado del juego;
no se debe implementar algún tipo de inteligencia artificial - la maquina elegirá un cuadro de manera aleatoria, eso es suficiente para este juego.

+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Ingresa tu movimiento: 1

board[row][column]

from random import randrange
 
for i in range(10):
    print(randrange(8))
'''

from random import randrange

def display_board(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    
    for row in range(len(board)):
        print('''+-------+-------+-------+
|       |       |       |
''', end="")
        for column in range(len(board)):
            print("|  ", board[row][column], end="   ")
        print('''|
|       |       |       |
''', end="")
    print('+-------+-------+-------+')   


def enter_move(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    while True:
        try:
            print()
            empty_cells = make_list_of_free_fields(board)
            select_cell = int(input("Ingresa tu movimiento: "))
            cell_tuple = ((select_cell-1)//3, (select_cell-1)%3)
            if cell_tuple in empty_cells:
                board[cell_tuple[0]][cell_tuple[1]] = 'O'
                display_board(board)
                check_victory = victory_for(board, 'O')
                if not check_victory:
                    draw_move(board)
            elif select_cell < 1 or select_cell > 10:
                print("Número no permitido, selecciona otro")
            else:
                print("Celda ocupada, selecciona otra")
        except ValueError:
            print("El valor ingresado no es valido, ingresa un numero")


def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos. 
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    empty_cells = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] != 'X' and board[r][c] != 'O':
                empty_cells.append((r,c))
    if len(empty_cells) == 0:
        print("\n¡Ha habido un empate!")
        quit()
    return empty_cells


def victory_for(board, sign):
    # La función analiza el estatus del tablero para verificar si 
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    status = False
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        status = True
    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        status = True
    else:
        for i in range(0, len(board)):
            if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
                status = True
            elif board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
                status = True
    if status == True and sign == 'X':
        print("\n¡Ha Ganado la maquina!")
        quit()
    elif status == True and sign == 'O':
        print("\n¡Has Ganado!")
        quit()
    return status


def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    empty_cell = make_list_of_free_fields(board)
    rand_tuple = randrange(0,len(empty_cell))
    cell_tuple = empty_cell[rand_tuple]
    board[cell_tuple[0]][cell_tuple[1]] = 'X'
    print("\nJugada de la maquina: ")
    display_board(board)
    check_victory = victory_for(board, 'X')
    if not check_victory:
        enter_move(board)


board_tmp = [r for r in range(1,10)]
board_tmp[len(board_tmp)//2] = 'X'
board=[]
for r in range(0,3):
    board.append(board_tmp[r*3:(r*3+3)])
    
display_board(board)
make_list_of_free_fields(board)

''' Eval positions
for i in range(1,10):
    print("\nPos:", i, " -> ", (i-1)//3, (i-1)%3)
'''
enter_move(board)
