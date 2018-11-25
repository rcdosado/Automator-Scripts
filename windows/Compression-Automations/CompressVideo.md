FFMPEG CREATE COMPRESSED VIDEO
============================
Requirements:
 - FFMPEG for Windows
 - Terminal
 
Instruction:
 - copy paste below code to a text file named it like compressvid.bat
 - open your cmd, go to the location of compressvid.bat
 - type ```compressvid.bat yourinputvideo.avi yourinputaudio.mp3 youroutputfileWithoutextension```
 - for example ```compressvid.bat tutorial.avi audio.mp3 mytutorial```
   - will combine tutorial.avi+audio.mp3 (its your responsibility to make them sync)
   - then it will produce ```mytutorial.mp4``` video with lower size but quality video
 - Profit!

```batch 
@echo off

REM COMBINES .AVI & .MP3
ffmpeg -i %1 -i %2 -map 0:v -map 1:a -c copy -shortest %3

REM PRODUCE SMALLER VIDEO
ffmpeg -i %3 -vcodec libx264 -crf 20 %3.mp4
```
