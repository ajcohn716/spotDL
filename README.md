# spotDL
program for exporting spotify playlists as mp3s. takes in a playlist link, spits out a csv, and pipes it to ytdlp. There's probably a better way than this.

# REQUIREMENTS
spotipy pip module

spotify developer account

yt-dlp
# KNOWN ISSUES
I'm pretty sure it doesn't work on Windows. I haven't tested it. It uses rm and clear. I don't think that works on windows.
The playlist needs to be public or the program crashes. Yes I could easily code an error message. No I will not. RTFM
# USAGE
Edit spotCSV.py to include the ID and secret for the development account (Lines 10 and 11, right after the module imports)

Put spotCSV.py into the directory you want to download the playlist to and run it. Input the playlist link. Hit enter. Program should populate the directory with TITLE ARTIST.mp3, then remove the final.csv when it's done. 

# Tweaks
Line 62 defines the variable "youtubedl_cmd". Edit this variable with whatever flavour of youtube dl suits your fancy. You can use a different fork of youtube-dl, or convert to another format. The world really is your oyester.
# Credits
Most of this code was shamelessly stolen and hodgepogegd together from an article from 6 years ago and a code tutorial to figure out the api. Much love to you all.
