from moviepy.editor import VideoFileClip
import os 

video = VideoFileClip('C:/Users/home/Desktop/Web-Depresion/webDepresion/test/prueba.mp4')
audio = video.audio
nuevo = video.without_audio()
nuevo.write_videofile('nuevo.mp4')
audio.write_audiofile('audio.mp3')