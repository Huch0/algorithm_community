def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    time = 0
    cache = []
    cache_items = 0

    for i, city in enumerate(cities):
        city = city.lower()
        index = cache.index(city) if city in cache else -1

        if index < 0:  # miss
            time += 5

            if cache_items == cacheSize:  # Exchange
                cache.pop()
                cache.insert(0, city)
            else:  # Add to cache
                cache.insert(0, city)
                cache_items += 1

        else:  # hit
            time += 1
            cache.pop(index)
            cache.insert(0, city)
    return time
