import os
from moviepy.editor import AudioFileClip

class Conversor:
    
    def __init__(self):
        pass
    
    def convert_mp4_to_wav(self, mp4_file, wav_file):
        # extraer el audio del archivo mp4
        audio_clip = AudioFileClip(mp4_file)
        
        # guardar el audio como un archivo wav
        audio_clip.write_audiofile(wav_file)
        
        # cerrar el clip
        audio_clip.close()
    
    def convert_all_mp4_to_wav(self, folder_path):
        for filename in os.listdir(folder_path):
            if filename.endswith('.mp4'):
                input_file = os.path.join(folder_path, filename)
                output_file = os.path.splitext(input_file)[0] + '.wav'
                self.convert_mp4_to_wav(input_file, output_file)

"""def main():
    name = "../video/wavs/"
    convert_all_mp4_to_wav(name)

main()"""