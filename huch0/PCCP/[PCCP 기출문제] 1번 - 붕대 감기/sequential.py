def solution(bandage, health, attacks):
    t, x, y = bandage
    cur_hp = max_hp = health
    heal_time = 0  # consecutive heal time
    prev_time = 0  # previous attack time

    for atk_time, damage in attacks:
        heal_time += (atk_time - prev_time) - 1

        # cur_hp = heal over time + additional heal
        # cur_hp can't exceeds max_hp
        cur_hp = min(max_hp, cur_hp + heal_time * x + (heal_time // t) * y)
        cur_hp -= damage

        if cur_hp <= 0:  # Die
            return -1

        heal_time = 0  # set 0 as it's attacked
        prev_time = atk_time

    return cur_hp
