import speech_recognition as sr
import re

def find_conversations(audio_file_path):
    conversations = []
    r = sr.Recognizer()
    try:
        with sr.AudioFile(audio_file_path) as source:
            audio_data = r.record(source)
            text = r.recognize_google(audio_data, language='es-ES')
            audio_duration = source.DURATION
    except:
        print("line 2")
        return []
    print("line 1")
    pattern = re.compile(r"([A-Z]+):\s+(.*)")
    lines = text.split('\n')
    if len(lines) == 1:
        conversations.append(('Desconocido', lines[0], 0, audio_duration))
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
    
# cargar archivo de audio
audio_file = "nueva/prub.0.wav"

# Cargar archivo de audio en formato wav

conversations = find_conversations(audio_file)
print("line")
# imprimir conversaciones encontradas
for conv in conversations:
    print(conv, "a")