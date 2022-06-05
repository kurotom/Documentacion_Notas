import unittest
from . import classPjs, mapping, scenes, EngineGame


class TestAdventureGame(unittest.TestCase):

    def setUp(self):
        self.testpj = classPjs.You(name='test', health=10)
        self.enemy = classPjs.Zombie()
        self.rooms = mapping.Map.rooms

    def test_stats(self):
        self.assertEqual([self.testpj.name, self.testpj.vida], ['test', 10])
        self.assertEqual([self.enemy.name, self.enemy.vida], ['Zombie', 10])

    def test_str_pjs(self):
        self.assertEqual(self.testpj.__str__(), 'Name: test\nHealth: 10')

    def test_str_enemies(self):
        self.assertEqual(self.enemy.__str__(), 'Name: Zombie   Health: 10')

    def test_maps(self):
        y = [
            scenes.StartPath(),
            scenes.SomeThingRoom(),
            scenes.EnemyRoom(),
            scenes.ChestKey(),
            scenes.RoomNothing(),
            scenes.ChoicePath(),
            scenes.Death(),
            scenes.Finish()
        ]
        x = []
        l = list(self.rooms.values())
        for i in l:
            x.append(i in l)
        self.assertIs(all(x), True)

    def test_class_inherit(self):
        x = [
            issubclass(scenes.StartPath, scenes.Scene),
            issubclass(scenes.SomeThingRoom, scenes.Scene),
            issubclass(scenes.EnemyRoom, scenes.Scene),
            issubclass(scenes.ChestKey, scenes.Scene),
            issubclass(scenes.RoomNothing, scenes.Scene),
            issubclass(scenes.ChoicePath, scenes.Scene),
            issubclass(scenes.Death, scenes.Scene),
            issubclass(scenes.Finish, scenes.Scene),
            issubclass(classPjs.You, classPjs.Entity),
            issubclass(classPjs.Zombie, classPjs.Enemy)
        ]
        self.assertIs(True, True)



if __name__ == '__main__':
    unittest.main()
