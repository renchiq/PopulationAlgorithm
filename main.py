from Bat import Bat

iterations_count = 10
population_size = 3

# fi = f_min + betta * (f_max - f_min)
# vit = vit-1 + (xit - x_best) * fi
# x_best - текущая глобальная лучшая позиция

# f_frequency = 2
f_min = 0
f_max = 10

# x_position = 4
x_best = 0

# v_velocity = 3
# a_loudness = 1
# r_pulse = 0

bats = []

# initializing start values f, x, v, a, r
# for bat in range(population_size):
#     bats.append(Bat())

for iteration in range(iterations_count):
    for bat in bats:
        # initializing start values f, x, v, a, r
        if iteration == 0:
            bats.append(Bat())
