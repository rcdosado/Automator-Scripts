FFMPEG CREATE COMPRESS VIDEO
============================
Requirements:
 - FFMPEG for Windows
 - Terminal

```batch 
@echo off
REM RE ENCODE AUDIO
REM ffmpeg -i %1 -i %2 -map 0 -map 1:a -c copy -c:a libmp3lame -b:a 192k -shortest %3

REM SYNTAX
REM > combine.bat video.avi audio.mp3 outputvideo.avi

REM COMBINES .AVI & .MP3
ffmpeg -i %1 -i %2 -map 0:v -map 1:a -c copy -shortest %3

REM PRODUCE SMALLER VIDEO
ffmpeg -i %3 -vcodec libx264 -crf 20 output.mp4
```
