#!/usr/bin/env python3
 
import csv
import os
import time
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#Edit these lines with the id and secret from the spotify developer account
id ="Enter Id Here"
secret ="Enter Secret Here"

burnChoice = input("Do you want you to burn to a cd? (Note that burning a cd will remove the mp3 files when it is finished) Y/N \n") 

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
    downloadCount = 1
    files = []  
     # open up the csv file and read the data into a list
    with open('final.csv', newline="") as f:
        reader = csv.reader(f)
        data = list(reader)

    # skip the first line which contains headings
    for item in data[1:]:
        
        # create a song name to search for using the artist and song title
        fullname = item[0] + " " + item[1]
        fullname = fullname.replace("'", "")
        filename = fullname.replace(".","")
        filename = filename.replace(" ","_")
        filename = filename.replace("$","s")
        filename = filename.replace("!","")
        filename = filename.replace("/","")
        filename = filename.replace("=","")
        filename = filename.replace("\n","")
        filename = filename.replace("Remastered","")
        filename = filename.replace("-","")
        filename = filename.replace("___","_")
        filename = filename.replace("(","")
        filename = filename.replace(")","")
        filename = filename.replace("&","and")
        filename = filename.replace("Album Version","")

        # download the audio as an mp3 using youtube-dl
        youtubedl_cmd = "yt-dlp -f 'ba' -x --audio-format mp3 'ytsearch:%(fullname)s' -o '%(count)s_%(title)s.mp3'" \
            % { 'fullname':fullname,
                'title':filename,
                'count':downloadCount}           
        os.system("clear")
        os.system(youtubedl_cmd)
        files.append(str(downloadCount) + "_" + filename + ".mp3")
        downloadCount = downloadCount + 1
    

    if burnChoice == "y" or burnChoice == "Y":
        driveLine = os.popen('lsblk | grep rom').read()
        driveLine = "/dev/" + driveLine[0:3]
       
        braseroCmd = "brasero -a --device=%(drive)s --immediately" \
            % {'drive':driveLine}
        i = 0
        for i in range(len(files)):
            braseroCmd = braseroCmd + " " + files[i]
            i = i + 1
        #print(braseroCmd)
        #os.system(braseroCmd)
        print("Finished Burning to CD! Exiting...")
        os.system("rm *.mp3")
        #time.sleep(10)
        #os.system("clear")
        #exit()

    elif burnChoice == "n" or burnChoice == "N":
        print("All Finished! Exiting...")
        time.sleep(1)
        os.system("clear")
        exit()

    else:
        print("You entered an invalid input.")
extractData()
makeCSV()
download()
os.system("rm final.csv")
