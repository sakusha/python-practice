#Ghost Game
from random import randint
print(' Ghost Game ')
feeling_brave=True
score=0
while feeling_brave:
    ghost_door=randint(1, 3)
    print(' There are three doors. ')
    print(' And there is a ghost one of these doors. ')
    print(' Which door will you open? ')
    door=input(' 1,2,or 3? ')
    door_num=int(door)
    if door_num==ghost_door:
        print(' Ghost!!! ')
        feeling_brave=False
    else:
        print(' There was no ghost! ')
        print(' You can go into next door. ')
        score=score+1
print(' Run Away!!! ')
print(' Game Over! Your score is ',score,'. ')
