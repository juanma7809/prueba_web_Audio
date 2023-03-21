from io import BytesIO
from moviepy.video.io.VideoFileClip import VideoFileClip

class Video(object):

    def __init__(self):
        self.ruta = "C:/Users/home/Desktop/webDepresion/webDepresion/video/"

    def dividir_video_clips(self, video_path, clip_duration):
        # Cargar el archivo de video
        video_clip = VideoFileClip(video_path)

        # Generar lista de clips
        clips = []
        for i, start_time in enumerate(range(0, int(video_clip.duration), clip_duration)):
            end_time = min(start_time + clip_duration, video_clip.duration)
            clip = video_clip.subclip(start_time, end_time)
            clip_path = f"cancion{i+1}.mp4"
            clip.write_videofile(clip_path)
            clips.append(clip)

        # Liberar recursos
        video_clip.close()
        for clip in clips:
            clip.close()


    def sensurar_video(self, ruta_video):
        import cv2

        # Inicializa el detector de rostros Haar
        face_cascade = cv2.CascadeClassifier(self.ruta + "haarcascade_frontalface_default.xml")

        # Carga el video
        video = cv2.VideoCapture(ruta_video)

        # Crea una máscara para ocultar los ojos
        mask = cv2.imread(self.ruta + "mask.png", cv2.IMREAD_UNCHANGED)

        # Lee los frames del video
        while True:
            ret, frame = video.read()
            if not ret:
                break

            # Convierte el frame a escala de grises
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detecta rostros en el frame
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            # Recorre los rostros detectados
            for (x, y, w, h) in faces:
                # Recorta el rostro
                face = frame[y:y + h, x:x + w]

                # Redimensiona la máscara para ajustarse al tamaño del rostro
                mask = cv2.resize(mask, (w, h), interpolation=cv2.INTER_CUBIC)

                # Crea un canal alpha para la máscara
                mask_gray = cv2.cvtColor(mask, cv2.COLOR_BGRA2GRAY)
                _, mask_alpha = cv2.threshold(mask_gray, 0, 255, cv2.THRESH_BINARY)
                mask = cv2.merge((mask_alpha, mask_alpha, mask_alpha))

                # Aplica la máscara sobre el rostro
                face = cv2.bitwise_and(face, mask)

                # Reemplaza el rostro en el frame original
                frame[y:y + h, x:x + w] = face

            # Muestra el frame resultante
            cv2.imshow("Frame", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        # Libera la cámara y destruye las ventanas
        video.release()
        cv2.destroyAllWindows()


a = Video()
a.dividir_video_clips("cancion.mp4", 180)
