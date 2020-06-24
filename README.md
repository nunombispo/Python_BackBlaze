# Python Backblaze

The idea for this script came from my necessity to store my large media library in the cloud instead of my NAS.

Since I will not see all the movies and tvshows at the same time, my goal was to have a simple sync of the folder structure so that a media library application like Plex and Emby could map the library.

This allows to have the complete media library structure occuping only a few KBs of disk space and still being managed in a media library app and when I desire to see a specific movie or tvshow that will be downloaded.

Python BackBlaze B2 allows to interface BackBlaze for diverse funcionalities regarding a media library that mainly resides in B2 and that can the synced to several local media paths:
- Sync a folder structure from B2 to a media path (supports differents paths for TvShows and Movies)
- Allows to download a specific movie from B2 to a media folder (by searching the movie by name)
- Allows to download a specific tv show episode from B2 to a media folder (by searching for the tvshow by name and selecting the season and episode)
- A menu allows access to all this options and also to manage the settings which resides in a JSON file

In case a media file has already been downloaded, where a folder sync is perform it will ignore that file so that downloads are not overwritten.

All files are saved with 1KB so that they are not empty empty and be be used, they are saved as text but with the full file name and extension so they are full recognize by Plex or Emby.

A web version interface is in planning to interact with the script in a more modern way.

# How to use
- Install requirements with 'pip install -r requirements.txt'
- Run the Sync.py with 'python Sync.py'
- From the menu options choose 'Settings'
- Update the settings with the required information

From then how you can use the menu for the several options.

The files are saved with this file path:
/[media path]/[bucket name]/[B2 folder structure]
