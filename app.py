import streamlit as st
from mood import get_songs_by_mood
st.title("Mood Based Recommendations")
st.write("Select your current mood:")
mood = st.selectbox("Mood", ["happy", "aggressive", "calm", "sad", "energetic", "dreamy"])
if st.button("Get Recommendations"):
    songs = get_songs_by_mood(mood)
    st.subheader("Recommended Song")

    for song in songs:
        st.write(f"Title: {song['title']}")
        st.write(f"Artist: {song['artist']}")
        st.write(f"Album: {song['album']}")