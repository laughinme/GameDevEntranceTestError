time = 17
subtract = -3
damage = 131
all_damage=0

for attack in range(time*2):
    all_damage += damage + subtract * attack

print(all_damage)
