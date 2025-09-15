from collections import defaultdict

def solution(genres, plays):
    by_genre = defaultdict(list)
    for i, (g, p) in enumerate(zip(genres, plays)):
        by_genre[g].append((i, p))
        
    genre_order = sorted(by_genre.items(), key=lambda kv: sum(p for _, p in kv[1]), reverse=True) 
    
    answer = []
    
    for genre, tracks in genre_order:
        tracks.sort(key=lambda t: (-t[1], t[0]))
        
        answer.append(tracks[0][0])
        if len(tracks) >= 2:
            answer.append(tracks[1][0])
            
    return answer        