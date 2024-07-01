# py-desktop-cleaner
A Python script that cleans certain types of files from the desktop and places them in a series of subdirectories in the /OneDrive/Desktop Organizer/ subdirectory of the user's home directory. If the sub-directories do not already exist then they are created.  

This project is based on a YouTube tutorial by [Tiff In Tech](https://www.youtube.com/channel/UC4MZ7zUHb5eAxU75Dc_nqdQ) called [Code With Me: Automating My Life With Python | Build a file organizer](https://www.youtube.com/watch?v=P7e5-n9FuXU). I have modified it to support more file types and to move the files to a Desktop Organizer directory in OneDrive. I plan to add more functionality in the future.  

## Supported File Types

- Audio: .mp3, .ogg, .wav  
- Documents: .pdf, .rtf, .txt  
- Images: .bmp, .gif, .jpg, .png  
- Spreadsheets: .xls, xlsx  
- Videos: .avi, .mkv, .mov, .mp4, .wmv  

## WARNING
I am not responsible for loss of your dank memes if you run this script and something goes wrong.  

## Installation
```
git clone https://github.com/BrendanGasparin/py-desktop-cleaner.git
```

## Execution
Navigate to the directory where you cloned the repository at the command line and type:

```
python ./desktop-organizer.py
```
