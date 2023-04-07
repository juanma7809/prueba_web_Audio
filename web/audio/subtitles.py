import moviepy.editor as mp

# cargar video y subtítulos
video = mp.VideoFileClip("video.mp4")
subtitles = mp.SubtitlesClip("conversaciones.txt")

# agregar subtítulos al video
result = mp.CompositeVideoClip([video, subtitles.set_position(('center', 'bottom'))])

# guardar video resultante
result.write_videofile("video_con_subtitulos.mp4")