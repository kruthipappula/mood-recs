import random
import streamlit as st
from mood import get_songs_by_mood

st.set_page_config(page_title="Mood Recs", 
                   page_icon=":musical_note:", layout="centered")



st.title("Mood Roulette :musical_note:")
st.write("Pick your current mood then generate:")

if 'shown_songs' not in st.session_state:
    st.session_state.shown_songs = []

if 'current_song' not in st.session_state:
    st.session_state.current_song = None

mood = st.selectbox("Choose your mood:", ["happy", "aggressive", "chill", "sad", "energetic", "dreamy", "confident", "dark", "romantic", "nostalgic"])

if 'last_mood' not in st.session_state:
    st.session_state.last_mood = None

if mood!= st.session_state.last_mood:
    st.session_state.shown_songs = []
    st.session_state.current_song = None
    st.session_state.last_mood = mood


if st.button("Generate song", type="primary"):
    all_matching_songs = get_songs_by_mood(mood)
    available_songs = []

    for song in all_matching_songs:
        if song['title'] not in st.session_state.shown_songs:
            available_songs.append(song)

    if len(available_songs) == 0:
        st.session_state.shown_songs = []
        available_songs = all_matching_songs
        st.warning("You've seen all the songs for this mood! Starting over.")
    
    chosen_song = random.choice(available_songs)

    st.session_state.current_song = chosen_song
    st.session_state.shown_songs.append(chosen_song['title'])

    if st.session_state.current_song:
        song = st.session_state.current_song
        st.write(f"Title: {song['title']}")
        st.write(f"Artist: {song['artist']}")
        st.write(f"Album: {song['album']}")

        if 'cover_art' in song:
            st.image(song['cover_art'], width=300)
        if 'spotify_link' in song:
            st.markdown(f"[Listen on Spotify]({song['spotify_link']})")
