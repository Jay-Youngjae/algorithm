def solution(genres, plays):
    answer = []
    set_genres = list(set(genres))
    
    # 장르 별 재생 횟수 합 구하기
    genre_sum = []
    for g in set_genres:
        total = 0
        for i in range(len(genres)):
            if genres[i] == g:
                total += plays[i]
        genre_sum.append((g, total))
    
    genre_sum.sort(key = lambda x:x[1], reverse = True)
    
    for g, h in genre_sum:
        songs = []
        for i in range(len(genres)):
            if genres[i] == g:
                songs.append((i, plays[i]))
        songs.sort(key=lambda x: (-x[1], x[0]))
        print(songs)
        for i, j in songs[:2]:
            answer.append(i)
   
    return answer