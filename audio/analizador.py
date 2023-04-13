import os
import re
import speech_recognition as sr

# funcion para identificar conversaciones
def find_conversations(audio_data):
    conversations = []
    r = sr.Recognizer()
    try:
        text = r.recognize_google(audio_data, language='es-ES')
    except:
        return []
    pattern = re.compile(r"([A-Z]+):\s+(.*)")
    lines = text.split('\n')
    print("aqui")
    if len(lines) == 1:
        conversations.append(('Desconocido', lines[0], 0, 1))
        return conversations
    speaker = ''
    conversation = ''
    offset_idx = 0
    offsets = audio_data.offset
    for line in lines:
        match = pattern.match(line)
        if match:
            if speaker and conversation:
                start_time = offsets[offset_idx][0]
                end_time = offsets[offset_idx][1]
                conversations.append((speaker, conversation, start_time, end_time))
                offset_idx += 1
            speaker = match.group(1)
            conversation = match.group(2)
        else:
            conversation += ' ' + line
    if speaker and conversation:
        start_time = offsets[offset_idx][0]
        end_time = offsets[offset_idx][1]
        conversations.append((speaker, conversation, start_time, end_time))
    return conversations

# funcion para guardar en archivo
def save_conversations(conversations, filename):
    with open(filename, 'w') as f:
        for i, (speaker, conversation, start_time, end_time) in enumerate(conversations):
            f.write(f"{i+1}\n{start_time:.2f} --> {end_time:.2f}\n{speaker}: {conversation}\n\n")


def process_audio_files(folder_path):
    # obtener una lista de archivos en la carpeta 'audio_files'
    file_names = [f for f in os.listdir(folder_path) if f.endswith('.wav')]

    # iterar sobre los archivos de audio y procesar cada uno
    for file_name in file_names:
        # construir la ruta completa del archivo
        file_path = os.path.join(folder_path, file_name)

        # leer el archivo y reconocer texto con la librería SpeechRecognition
        r = sr.Recognizer()
        with sr.AudioFile(file_path) as source:
            audio_data = r.record(source)

        # encontrar conversaciones en el texto y guardar en archivo
        conversations = find_conversations(audio_data)
        save_conversations(conversations, f'{file_name}.txt')

        # imprimir conversaciones
        print(f"Conversaciones en {file_name}:")