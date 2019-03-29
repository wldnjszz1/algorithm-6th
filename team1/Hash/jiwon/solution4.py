def solution(genres, plays):
    ggenres = list(set(genres))
    album = dict()
    answer = list()
    for i in range(len(ggenres)):
        playcount = list()
        for j in range(len(genres)):
            if ggenres[i] == genres[j]:
                playcount.append(plays[j])
        album[ggenres[i]] = playcount
    album = sorted(album.items(), key = lambda t:sum(t[1]), reverse=True)
    for a in album:
        a[1].sort(reverse=True)
    for g in range(len(album)):
        if len(album[g]) >= 2:
            for i in range(2):
                for j in range(len(plays)):
                    if album[g][1][i] == plays[j]:
                        answer.append(j)
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))

# 정확성 46.7 나머지오답 런타임에러
