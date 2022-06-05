import scenes


class Map(object):
    rooms = {
        'start': scenes.StartPath(),
        'somethingroom': scenes.SomeThingRoom(),
        'enemy_room': scenes.EnemyRoom(),
        'chestkey': scenes.ChestKey(),
        'roomnothing': scenes.RoomNothing(),
        'choicepath': scenes.ChoicePath(),
        'death': scenes.Death(),
        'finish': scenes.Finish()
    }

    def __init__(self, start):
        self.start = start

    def next_map(self, map_next):
        value = Map.rooms.get(map_next)
        return value

    def open_map(self):
        return self.next_map(self.start)
