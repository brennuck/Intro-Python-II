# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f"Name: {self.name}\nCurrent Room: {self.current_room}"

    def move(self, direction):
        movement = {
            'S': self.current_room.s_to,
            'N': self.current_room.n_to,
            'W': self.current_room.w_to,
            'E': self.current_room.e_to
        }
        # self.current_room = movement[direction]
        if movement[direction] is None:
            print('!--- You ran into a wall ---!')
        else:
            self.current_room = movement[direction]