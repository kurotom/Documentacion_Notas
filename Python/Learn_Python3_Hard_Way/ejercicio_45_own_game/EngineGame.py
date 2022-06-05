import random
from classPjs import You
from mapping import Map
from sys import argv


class Engine(object):
    def __init__(self, scene_map, debugGame=False):
        self.scene_map = scene_map
        self.debugGame = debugGame
        if self.debugGame:
            print(self.scene_map.rooms)

    def play(self):
        print('')
        print('(You hear someone\'s words.)')
        print('Tell me your name...')
        print('Not afraid.')
        print('Tell me your name.')
        print('\nEnter your name')
        nameplayer = input(' \u2694  ')
        health = 20
        playerPJ = You(nameplayer, health)

        current = self.scene_map.open_map()
        last = self.scene_map.next_map('finish')

        keys = ['somethingroom', 'enemy_room', 'chestkey', 'roomnothing']
        random.shuffle(keys)
#
        if self.debugGame:
            print(keys)
#
        while True:
            if current == self.scene_map.rooms.get('start'):
                # use class StStartPath()
                lap = current.open(keys)
                if lap == False:
                    print('Leaving the game')
                    break
                current = self.scene_map.next_map(lap)

            elif current == self.scene_map.rooms.get('somethingroom'):
                # use class SomeThingRoom()
                lap = current.open()
                current = self.scene_map.next_map(lap)

            elif current == self.scene_map.rooms.get('enemy_room'):
                # use class EnemyRoom()
                totalEnemies = random.randint(0, 3)
                lap = current.encountment(player=playerPJ, max_enemies=totalEnemies, fromchestkey=False)
                current = self.scene_map.next_map(lap)

            elif current == self.scene_map.rooms.get('chestkey'):
                # use class ChestKey()
                listStat = current.enter(player=playerPJ)
                if type(listStat) == list:
                    battle = self.scene_map.rooms.get('enemy_room')
                    step = battle.encountment(player=listStat[0], max_enemies=listStat[1], fromchestkey=True)
                    current = self.scene_map.next_map(step)
                else:
                    current = self.scene_map.next_map(listStat)

            elif current == self.scene_map.rooms.get('roomnothing'):
                # use class RoomNothing()
                enterRoom = current.enter()
                current = self.scene_map.next_map(enterRoom)

            elif current == self.scene_map.rooms.get('choicepath'):
                # use class ChoicePath()
                enterChoice = current.enter()
                current = self.scene_map.next_map(enterChoice)

            elif current == self.scene_map.rooms.get('death'):
                # use class Death()
                current.printDeath()
                break

            elif current == self.scene_map.rooms.get('finish'):
                break

        last.printFinish()


if __name__ == '__main__':
    a_map = Map('start')

    try:
        if argv[1] == 'debug':
            game = Engine(a_map, debugGame=True)
    except IndexError:
        game = Engine(a_map, debugGame=False)

    game.play()
