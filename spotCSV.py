#!/usr/bin/env python3
 
import csv
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

id ="26fab87a077c48e782fa39882d3fc095"
secret ="2159605056754585a57ae323be6f39a7"

# connecting with spotify api
auth_manager = SpotifyClientCredentials(client_id=id,client_secret=secret)
sp = spotipy.Spotify(auth_manager=auth_manager)
def extractData():
    #prompts the user for the playlist code
    playlist_code = input("Enter the Playlist Link: \n")
    playlist_dict = sp.playlist(playlist_code)
    no_of_songs = playlist_dict["tracks"]["total"]
    song_list = []
    artists_list = []
    tracks = playlist_dict["tracks"]
    items = tracks["items"]
    offset=0
    i=0
    while i<no_of_songs:
        song = items[i-offset]["track"]["name"]
        artists = [k["name"] for k in items[i-offset]["track"]["artists"]]
        artists = ','.join(artists)
        song_list.append(song)
        artists_list.append(artists)
        if (i+1)%100 == 0:
            tracks = sp.next(tracks)
            items = tracks["items"]
            offset = i+1
        i+=1
    
    global final_data 
    final_data = list(zip(song_list,artists_list))
def makeCSV():
    Details = ["Name","Artists"]
    rows = final_data
    with open("final.csv",'w', newline='') as f:
        write = csv.writer(f)
        write.writerow(Details)
        write.writerows(rows)
        f.close()

def download():
    # open up the csv file and read the data into a list
    with open('final.csv', newline="") as f:
        reader = csv.reader(f)
        data = list(reader)
 
    # skip the first line which contains headings
    for item in data[1:]:
        # create a song name to search for using the artist and song title
        fullname = item[0] + " " + item[1]
        fullname = fullname.replace("'", "")
        # download the audio as an mp3 using youtube-dl
        youtubedl_cmd = "yt-dlp -f 'ba' -x --audio-format mp3 --add-metadata 'ytsearch:%(fullname)s' -o '%(title)s.mp3'" \
            % { 'fullname':fullname,
                'title':fullname }           
        os.system("clear")
        os.system(youtubedl_cmd)
extractData()
makeCSV()
download()
os.system("rm final.csv")