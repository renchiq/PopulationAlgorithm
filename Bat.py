from random import randint, random


class Bat:
    def __init__(self):
        self.f_frequency = random() * 10
        self.x_position = random() * 15
        self.v_velocity = random() * 15
        self.a_loudness = random()
        self.r_pulse = random()

    def __str__(self):
        return f'f Frequency = {self.f_frequency}\n' \
               f'x Position = {self.x_position}\n' \
               f'v Velocity = {self.v_velocity}\n' \
               f'a Loudness = {self.a_loudness}\n' \
               f'r Pulse = {self.r_pulse}'


bat = Bat()
bat2 = Bat()
lst = [bat, bat2]

for elem in lst:
    elem.r_pulse += 10

