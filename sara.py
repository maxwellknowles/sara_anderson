#imports
from pickle import GET
from streamlit_elements import elements, mui, dashboard
import streamlit as st
import streamlit.components.v1 as components
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import cv2
import numpy as np
import pyautogui

#Authentication - without user
cid = st.secrets["cid"]
secret = st.secrets["secret"]
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

st.set_page_config(layout='wide', page_icon="love")

st.title("Sara's Vibe...")

#col1, col2 = st.columns(2)
#with col1:
    #song_link = st.text_input("Song link")
    #song_link = "https://open.spotify.com/track/5pEmeoMUW38w1oU3kPelvR?si=12128542935342d5"
    #color1 = st.color_picker('Pick your first color', '#00f900')
    #color2 = st.color_picker('Pick your second color', '#00f900')
    #color3 = st.color_picker('Pick your third color', '#00f900')
#with col2:
    #image = st.text_input("Image")
    #giphy = st.text_input("Giphy")
color1 = '#7ca850'
color2 = '#50a8a8'
color3 = '#7c50a8'
color4 = '#A85050'
image1 = "https://github.com/maxwellknowles/sara_anderson/blob/main/IMG_20220220_183818_064.jpg?raw=true"
image2 = "https://github.com/maxwellknowles/sara_anderson/blob/main/IMG_20220329_081958_401.jpg?raw=true"
image3 = "https://github.com/maxwellknowles/sara_anderson/blob/main/IMG_20220806_162723595_HDR.jpg?raw=true"
giphy = "https://media4.giphy.com/media/kiFnWnL8cWRNu/giphy.webp?cid=ecf05e47jicpbfoj70oz7zz1hekd5zfhmxx7d9a2ppazcvgx&rid=giphy.webp&ct=g"
song_link = "https://open.spotify.com/track/5pEmeoMUW38w1oU3kPelvR?si=12128542935342d5"
song = sp.track(song_link)
song_image = song["album"]["images"][0]["url"]
id = song["id"]
src="https://open.spotify.com/embed/track/"+id+"?utm_source=generator" 
spotify = """
    <iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/57ezFUyt9FZPi0OAq1OekN?utm_source=generator" width="100%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
    """
#spotify = re.sub(r'% src %', src, spotify)
spotify = components.html(spotify, height=375)

with elements("dashboard"):

    layout = [
        # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
        dashboard.Item("first_item", 0, 0, 4, 3, isDraggable=True, isResizable=True, ),
        dashboard.Item("second_item", 2, 4, 5, 2, isDraggable=True, isResizable=True),
        dashboard.Item("third_item", 0, 3, 2, 3, isDraggable=True, isResizable=True),
        dashboard.Item("fourth_item", 4, 0, 2, 4, isDraggable=True, isResizable=True),
        dashboard.Item("fifth_item", 10, 0, 2, 4, isDraggable=True, isResizable=True),
        dashboard.Item("sixth_item", 6, 0, 4, 3, isDraggable=True, isResizable=True),
        dashboard.Item("seventh_item", 8, 4, 4, 2, isDraggable=True, isResizable=True),
        dashboard.Item("eigth_item", 7, 3, 1, 3, isDraggable=True, isResizable=True),
    ]

    #def handle_layout_change(updated_layout):
        # You can save the layout in a file, or do anything you want with it.
        # You can pass it back to dashboard.Grid() if you want to restore a saved layout.
        #st.write(updated_layout)

    with dashboard.Grid(layout):
        #mui.icon.Looks(key="first_item")
        mui.Box(
            component="img",
        src=image1, 
        key="first_item")
        mui.Box(
            component="img",
        src=giphy, 
        key="second_item")
        mui.Paper(
        sx={"bgcolor":color1},
        elevation=12,
        key="third_item")
        mui.Paper(
        sx={"bgcolor":color2}, 
        elevation=12,
        key="fourth_item")
        mui.Paper(
        sx={"bgcolor":color3},
         elevation=12,
        key="fifth_item")
        mui.Box(
            component="img",
        src=image2, 
        key="sixth_item")
        mui.Box(
            component="img",
        src=image3, 
        key="seventh_item")
        mui.Paper(
        sx={"bgcolor":color4},
         elevation=12,
        key="eigth_item")
