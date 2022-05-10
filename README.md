# spotDL
program for exporting spotify playlists as mp3s. takes in a playlist link, spits out a csv, and pipes it to ytdlp. Has support for burning with brasero. Made this becaue my aux port is broke.

# REQUIREMENTS
spotipy pip module

spotify developer account

yt-dlp

brasero (for burning only)
# KNOWN ISSUES
I'm pretty sure it doesn't work on Windows. I haven't tested it. It uses rm and clear. I don't think that works on windows.

The playlist needs to be public or the program crashes. Yes I could easily code an error message. No I will not. RTFM

If the title of the song is also the title of an album, yt-dlp will often try to download the full album. That is almost never the intended behaviour. I have no idea how to fix that.

# USAGE
Edit spot2CD.py to include the ID and secret for the development account (Lines 10 and 11, right after the module imports)

Put spot2CD.py into the directory you want to download the playlist to and run it. Input the playlist link. Hit enter. Program should populate the directory with N_Title_Artist.mp3, then remove the final.csv when it's done. 

# Tweaks
Line 62 defines the variable "youtubedl_cmd". Edit this variable with whatever flavour of youtube dl suits your fancy. You can use a different fork of youtube-dl, or convert to another format. The world really is your oyester.

If you choose to burn a CD, it will also remove the mp3 files. You can change that by commenting out line 105.

The automatic CD burner detection works on both machines I've tested it on. If it doesn't work for you, try poking around with lines 93-97, or just manually define the device to be used by editing the driveLine variable.

# Credits
Most of this code was shamelessly stolen and hodgepogegd together from an article from 6 years ago and a code tutorial to figure out the api. Much love to you all. Also thanks to the devs of brasero.
