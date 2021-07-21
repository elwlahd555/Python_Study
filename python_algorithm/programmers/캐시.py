def solution(cacheSize, cities):
    answer = 0
    cache = []
    low_cities = [city.lower() for city in cities]
    if cacheSize != 0:
        for city in low_cities:
            if city in cache:
                cache.pop(cache.index(city))
                cache.append(city)
                answer += 1
            else:
                if len(cache) < cacheSize:
                    cache.append(city)
                    answer += 5
                else:
                    cache.pop(0)
                    cache.append(city)
                    answer += 5

    else:
        answer = len(cities) * 5

    return answer


cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

print(solution(cacheSize, cities))
