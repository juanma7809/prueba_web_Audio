import numpy as np  # procesamiento matricial

import matplotlib.pyplot as plt  # para mostrar imagenes
plt.rcParams['image.cmap'] = 'gray'
#%matplotlib inline

# para leer/guardar videos
import imageio

# Crear un objeto lector de videos
file_name= "webDepresion/prueba.mp4"
print("Abriendo video...")
vid_reader = imageio.get_reader(file_name)

# ver los metadatos del video
mdata = vid_reader.get_meta_data()
print(mdata)

# convertir el video a un arreglo numpy
print("Convirtiendo video a Numpy array...")

# dimensiones
cant_frames= vid_reader.get_length()
print(cant_frames)
dimensiones = (0, mdata['source_size'][1], mdata['source_size'][0], 3)
print(dimensiones)
# se crea un arreglo numpy de 4 dimensiones (nframes, filas, columnas, 3)
video_np = np.zeros(dimensiones)

# lista con los frames del video. Cada frame es una imagen
lista_video = list(vid_reader)

# iterar por todas las imagenes del video
for i in range(cant_frames):
    video_np[i,:,:,:]=lista_video[i]

# convertir a rango 0-1
video_np = video_np/255

# cerrar lector de video
vid_reader.close()

# mostrar una imagen para corroborar el video
plt.imshow(video_np[30,:,:,:])

print("...Listo")