import cv2 


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
a.sensurar_video("C:/Users/home/Desktop/webDepresion/webDepresion/video/k.mp4")
