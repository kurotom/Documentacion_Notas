"""
classPjs contain all enemies and player for the game.
Write here to create more enemies.
"""

class Entity(object):

    def __str__(self):
        string = f'Name: {self.name}\nHealth: {self.vida}'
        return string


class You(Entity):

    def __init__(self, name, health, key=False):
        self.name = name
        self.vida = health
        self.key = key



class Enemy(object):

    enemies = [
        'skeleton',
        'zombie',
        'zombie_skeleton',
    ]
    
    def __str__(self):
        return f'Name: {self.name}   Health: {self.vida}'


class Zombie(Enemy):

    def __init__(self):
        self.name = 'Zombie'
        self.vida = 10


class ZombieSkeleton(Enemy):

    def __init__(self):
        self.name = 'Zombie skeleton'
        self.vida = 15


class Skeleton(Enemy):

    def __init__(self):
        self.name = 'Skeleton'
        self.vida = 20
