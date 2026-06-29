from songs import songs

def get_songs_by_mood(mood):
    matching_songs = []

    for song in songs:
        if song['mood'] == mood:
            matching_songs.append(song)
    
    return matching_songs


