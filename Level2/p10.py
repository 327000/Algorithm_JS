#캐시
def solution(cacheSize, cities):
    cnt = 0
    cache_list = []

    if cacheSize == 0:
        return len(cities) * 5

    for i in cities:
        if len(cache_list) < cacheSize:
            if i.lower() in cache_list:
                cache_list.remove(i.lower())
                cache_list.append(i.lower())
                cnt += 1
            else:
                cache_list.append(i.lower())
                cnt = cnt + 5
        else:
            if i.lower() in cache_list:
                cache_list.remove(i.lower())
                cache_list.append(i.lower())
                cnt += 1
            else:
                cache_list.remove(cache_list[0])
                cache_list.append(i.lower())
                cnt = cnt + 5
    return cnt
