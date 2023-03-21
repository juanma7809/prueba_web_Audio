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
        conversations.append(('Desconocido', lines[0], 0, audio_data.duration))
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


# archivo de entrada
filename = "nueva/prub.0.wav"

# leer archivo y reconocer texto con la librería SpeechRecognition
r = sr.Recognizer()
with sr.AudioFile('nueva/prub.0.wav') as source:
    audio_data = r.record(source)

# encontrar conversaciones en el texto y guardar en archivo
print("ANTES DE ENCONTRAR A LOS SUJETOS:")
conversations = find_conversations(audio_data)
print(conversations, "DESPUES")
save_conversations(conversations, 'conversaciones.txt')

# imprimir conversaciones
for speaker, conversation in conversations:
    print(f"{speaker}: {conversation}")