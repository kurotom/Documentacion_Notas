import random
from time import sleep
from classPjs import Skeleton, Zombie, ZombieSkeleton


class Scene(object):
    pass


class StartPath(Scene):

    def open(self, list_maps):
        print("""
        You wake up into a dark room, you can see four doors,
        this doors have numbers and you have select one.
        You can return to previous rooms.
        (You feel cold, and vision is poor.)\n
        """)
        print('Location:  Principal Room')
        print("""
        +-----------------------------------------------------+
        |                                                     |
        |      +---+       +---+       +---+       +---+      |
        |      | 1 |       | 2 |       | 3 |       | 4 |      |
        |      |   |       |   |       |   |       |   |      |
        +----- +---+ ----- +---+ ----- +---+ ----- +---+ -----+\n
        """)
        room = input(' \u2694  ')

        if room == '1':
            return list_maps[0]
        elif room == '2':
            return list_maps[1]
        elif room == '3':
            return list_maps[2]
        elif room == '4':
            return list_maps[3]
        elif room == 'quit':
            return False
        else:
            print('\n')
            print('(Well, you not have movements)')
            print('(See arround the room, no more things interesting.)')
            print('\n')
            input('(Press Enter)\n')
            return 'start'


class SomeThingRoom(Scene):

    def open(self):
        print("Nothing here. Maybe going back to \nthe principal room would be for the best.")
        print('Location:  Some room')
        # room = int(input(' \u2694  '))
        input('(Press Enter to return)\n')
        return 'start'


class EnemyRoom(Scene):

    def encountment(self, player, max_enemies, fromchestkey=False):
        pj = player

        list_enemies = [
            Zombie(),
            ZombieSkeleton(),
            Skeleton(),
        ]
        enemies = []

        minEnemies = 0
        if fromchestkey:
            minEnemies = 1
        else:
            minEnemies = 0
        for i in range(random.randint(minEnemies, max_enemies)):
            enemies.append(list_enemies[i])

        print('Location:  Room with pillars')
        if len(enemies) > 0:
            print(f"\nYou see {len(enemies)} enemies.")
            for i in enemies:
                print(f'> {i.name} -- {i.vida}')
            print("\nActions:\n1) Attack  2) Return")
            action = input(' \u2694  ')

            if action == '1':
                while len(enemies) > 0 and pj.vida > 0:
                    for i in range(len(enemies)):
                        x = random.choice(enemies)
                        index = enemies.index(x)

                        turnos = [x, pj]
                        while pj.vida > 0 and x.vida > 0 and len(turnos) > 1:
                            a = random.choice(turnos)
                            if a == pj:
                                print('\n')
                                print(f'Turn of "{a.name}"')
                                print("*" * 20 + " Stats " + "*" * 20)
                                print(f"         You\t\tEnemy")
                                print("--------+" + "-" * 38)
                                print(f"Name   | {pj.name}\tvs\t{x.name}")
                                print(f"Health | {pj.vida}\tvs\t{x.vida}")
                                print("--------+" + "-" * 38)
                                print("Attacks:\n1) normal(2)   2) strong(3)   3) very strong(4)   4) Quit battle\n")

                                resAttack = input(' \u2694  ')

                                if resAttack == '1':
                                    x.vida = x.vida - 2
                                    print(f"You attack: 2 ==>  {x.vida}")
                                elif resAttack == '2':
                                    x.vida = x.vida - 3
                                    print(f"You attack: 3 ==>  {x.vida}")
                                elif resAttack == '3':
                                    x.vida = x.vida - 4
                                    print(f"You attack: 4 ==>  {x.vida}")

                                elif resAttack == '4':
                                    # print(turnos)
                                    # print(enemies)
                                    # print(enemies.index(x))
                                    turnos.pop(turnos.index(x))
                                    enemies.pop(enemies.index(x))

                                    print('(Quitting the battle)')
                                    # print(enemies, len(enemies))

                                    r = random.randint(1, 10)

                                    if r != 7:
                                        if r > 0 and r < 6:
                                            pj.vida = pj.vida - r
                                            print('(Before you leaving the battle the enemy hurt you)')
                                            print(f'(Damage of {r}, ouch!)')
                                            print(f'(Your healt is {pj.vida})')
                                            print('\n')
                                            # print(enemies, len(enemies))
                                            if len(enemies) == 0:
                                                sleep(2)
                                                return 'start'
                                else:
                                    print('Attacking missing.')
                                    print()

                                print('\n')
                                sleep(2)

                                if x.vida < 0:
                                    print('\n')
                                    motds_victory = [
                                        f'Enemy {x.name} has been defeated, hurra.!',
                                        f'Enemy {x.name} has been destroyed.',
                                        f'Target {x.name} eliminated.',
                                        f'Hasta la vista, baby! - ({x.name})',
                                    ]
                                    enemies.pop(enemies.index(x))
                                    print(random.choice(motds_victory))
                                    print('\n')
                                    sleep(1)
                            else:
                                print('\n')
                                print(f'Turn of {x.name}')
                                print("{-}" * 15)
                                print('Enemy Attacking')
                                sleep(2)
                                damage = random.randint(0, 4)
                                pj.vida = pj.vida - damage
                                print(f"{x.name} attack you, {damage} -->  {pj.vida}")
                                print("{-}" * 15)
                                print('\n')
                                sleep(2)
                if pj.vida < 0:
                    return 'death'
            elif action == '2':
                motds = [
                    'You decided to run away.',
                    'You are returning, wise choice.'
                ]
                print('\n')
                print(random.choice(motds))
                input('(Press Enter to return)\n')
                print('\n')
                return 'start'
            else:
                print('No actions, enemy_room')
                return 'enemy_room'
        else:
            print('\n')
            print('Wow, nothing for here, it\'s too calm, too calm.')
            input('(Press Enter to return)\n')
            print('\n')
            return 'start'


class ChestKey(Scene):

    def enter(self, player):
        turn = random.choice(['peace', 'battle'])
        print('\nLocation: Room with something curious.')
        if turn == 'peace':
            if player.key:
                print('\n')
                print('You already got a key!')
                print('Nothing more here.')
                print('\n')
                input('(Press Enter to return)\n')
            else:
                player.key = True
                print('\n')
                print('With no enemies, you can see a chest in the back of the room.')
                print('(You open the chest.)')
                print('(Opening chest ...)')
                sleep(2)
                print('(You get a key, with this key you can escape this...\nI don\'t know what is this.)')
                print('\n')
                sleep(1)
                print('Nothing more here.')
                input('(Press Enter to return)\n')

            return 'start'

        elif turn == 'battle':
            print('\n')
            print('(Ooh sh.., i see enemies...)')
            enemies = random.randint(1, 3)
            return [player, enemies]


class RoomNothing(Scene):

    def enter(self):
        print()
        print('Location: Room quiet\n')
        print('This room has no enemies, it has a table and chairs.')
        print('On the table are milk and cookies.')
        print('You eat cookies and drink milk without worries, after all,\nyou woke up in a place with little light and some enemies,\nwho cares.')
        print('**  Your health has been restored.  **')
        print()
        input('(Press Enter to continue)\n')
        return 'choicepath'


class ChoicePath(Scene):

    def enter(self):

        print('\n')
        print('Location: Decisions')
        print('(Select your path)')
        print("""
        +-----------------------------------------------+
        |                                               |
        |            +---+             +---+            |
        |            | 1 |             | 2 |            |
        |            |   |             |   |            |
        +----------- +---+ ----------- +---+ -----------+\n
        """)

        selection = input(' \u2694  ')

        choice = ['death', 'finish']
        random.shuffle(choice)
        if selection == '1':
            return choice[0]
        elif selection == '2':
            return choice[1]
        else:
            return 'choicepath'


class Death(Scene):

    def printDeath(self):
        deaths = [
            f'---   You died!   ---',
            '---   No this time, try again.   ---',
            '---   Requiescat In Pace   ---',
        ]
        print('\n')
        print(random.choice(deaths))
        sleep(2)
        print('\n')
        return False


class Finish(Scene):

    def printFinish(self):
        finish = [
            'Woohoo!, you finish this shi.!',
            'Yeah, this game is too boring.',
            'The end? ...',
            'It is the ... end.'
        ]
        print('\n')
        print('----  Your finis this game  ----')
        print(random.choice(finish))
        sleep(2)
        print('\n')
