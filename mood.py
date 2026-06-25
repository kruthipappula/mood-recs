from songs import songs

def get_songs_by_mood(mood):
    return [song for song in songs if song['mood'] == mood]

