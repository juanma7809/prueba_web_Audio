from pytube import YouTube

# URL del video de YouTube
youtube_url = "https://www.youtube.com/watch?v=hvBkBC5zi5A&list=RDhvBkBC5zi5A&start_radio=1&ab_channel=EddieSantiago-Topic"

# Descargar el video
youtube_video = YouTube(youtube_url)
video_stream = youtube_video.streams.get_highest_resolution()
video_stream.download(output_path="")
