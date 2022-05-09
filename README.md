# spotDL
program for exporting spotify playlists as mp3s

#REQUIREMENTS
spotipy pip module
spotify developer account
yt-dlp
#KNOWN ISSUES
I'm pretty sure it doesn't work on Windows. I haven't tested it. It uses rm. I don't think that works on windows. 
#USAGE
Edit spotCSV.py to include the ID and secret for the development account. It is the lines right after the module imports.
put spotCSV.py into the directory you want to download the playlist to and run it. Input the playlist link. Hit enter. Program should download for you.
#Tweaks
Line 60ish defines the variable "youtubedl_cmd". Edit this variable with whatever flavour of youtube dl suits your fancy. You can use a different fork of youtube-dl, or convert to another format. The world really is your oyester.
#Credits
Most of this code was shamelessly stolen and hodgepogegd together from an article from 6 years ago and a code tutorial to figure out the api. Much love to you all.
