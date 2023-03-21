import cv2 
from moviepy.video.io.VideoFileClip import VideoFileClip

class Video(object):

    def __init__(self,):
        self.ruta = "C:/Users/home/Desktop/webDepresion/webDepresion/video/"
        pass

    def dividir_video_frames_jpg(self):

        # Cargar el video
        cap = cv2.VideoCapture("ruta_del_video.mp4")

        # Obtener eñ número de frames
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        # Dividir el video en frames
        for i in range(total_frames):
            ret, frame = cap.read()
            if not ret:
                break
            cv2.inwrite("frame_{}.jpg".format(i), frame)

        # Liberar el video
        cap.release()

    def dividir_video_clips(self):
        # Ruta del archivo de video original
        video_path = "cancion.mp4"

        # Tamaño de la parte del archivo que se leerá en cada iteración
        chunk_size = 1024 * 1024  # 1 MB

        # Abrir el archivo de video
        with open(video_path, "rb") as video:
            # Inicializar el objeto de archivo de video
            video_clip = None
            video_pos = 0

            # Leer y procesar el archivo en partes
            while True:
                # Leer una parte del archivo
                chunk = video.read(chunk_size)
                if not chunk:
                    break  # Fin del archivo

                # Procesar la parte del archivo
                if video_clip is None:
                    # Cargar el archivo de video
                    video_clip = VideoFileClip(chunk)
                else:
                    # Agregar la parte del archivo al clip
                    video_clip = video_clip.set_start(video_pos).append(VideoFileClip(chunk))

                # Actualizar la posición actual del archivo de video
                video_pos += len(chunk)

        # Duración de cada clip en segundos
        clip_duration = 30

        # Generar lista de clips
        clips = []
        for i, start_time in enumerate(range(0, int(video_clip.duration), clip_duration)):
            end_time = min(start_time + clip_duration, video_clip.duration)
            clip = video_clip.subclip(start_time, end_time)
            clip_path = f"ruta/al/archivo/clip_{i+1}.mp4"
            clip.write_videofile(clip_path)
            clips.append(clip)

        # Liberar recursos
        video_clip.close()
        for clip in clips:
            clip.close()


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
a.dividir_video_clips()
