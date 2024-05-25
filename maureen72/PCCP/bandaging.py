def solution(bandage, health, attacks):
    t, x, y = bandage
    max_health = health
    current_health = health
    attack_index = 0
    attack_times = [attack[0] for attack in attacks]
    attack_damage = [attack[1] for attack in attacks]
    
    time = 0
    while attack_index < len(attacks):
        time += 1
        if time in attack_times:
            current_health -= attack_damage[attack_times.index(time)]
            attack_index += 1
            
            if current_health <= 0:
                return -1
        else:
            for _ in range(t):
                if time in attack_times:
                    current_health -= attack_damage[attack_times.index(time)]
                    attack_index += 1
                    
                    if current_health <= 0:
                        return -1
                    break
                else:
                    current_health = min(current_health + x, max_health)
                    time += 1
            
            if time not in attack_times:
                current_health = min(current_health + y, max_health)
                
    return current_health
