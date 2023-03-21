import os
import subprocess

def split_file(input_file, chunk_size_mb):
    input_size = os.path.getsize(input_file)
    chunk_size = chunk_size_mb * 1024 * 1024
    num_chunks = input_size // chunk_size + 1

    with open(input_file, 'rb') as f:
        for i in range(num_chunks):
            chunk_file_name = '{}.{}.mp3'.format(os.path.splitext(input_file)[0], i)
            with open(chunk_file_name, 'wb') as chunk_file:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                chunk_file.write(chunk)
                subprocess.call(['ffmpeg', '-i', chunk_file_name, '{}.{}.wav'.format(os.path.splitext(input_file)[0], i)])


def main():
    name = "nueva/prub.mp3"
    split_file(name, 5)

main()