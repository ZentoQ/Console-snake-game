from random import randint
from time import sleep
import os
import keyboard
from colorama import init, Fore, Style

init()

game_map = [['*' for _ in range(12)] for _ in range(32)]
snake = [(2, 0)]
player_row, player_col = snake[0]
direction = (0, 1)

def place_food():
    while True:
        row = randint(0, 4)
        col = randint(0, 11)
        if (row, col) not in snake:
            return (row, col)

def print_map(food):
    os.system('cls')
    for row in range(5):
        for col in range(12):
            if (row, col) in snake:
                print(Fore.GREEN + '-' + Style.RESET_ALL, end=' ')
            elif (row, col) == food:
                print(Fore.RED + 'O' + Style.RESET_ALL, end=' ')
            else:
                print('*', end=' ')
        print()

food = place_food()

while True:
    if keyboard.is_pressed('w'):
        direction = (-1, 0)
    elif keyboard.is_pressed('s'):
        direction = (1, 0)
    elif keyboard.is_pressed('a'):
        direction = (0, -1)
    elif keyboard.is_pressed('d'):
        direction = (0, 1)
    
    player_row, player_col = snake[0]
    new_row = player_row + direction[0]
    new_col = player_col + direction[1]
    
    if (new_row < 0 or new_row >= 5 or new_col < 0 or new_col >= 12 or (new_row, new_col) in snake):
        print("Игра окончена!")
        break

    snake.insert(0, (new_row, new_col))

    if (new_row, new_col) == food:
        food = place_food()
    else:
        snake.pop()

    print_map(food)
    sleep(0.2)