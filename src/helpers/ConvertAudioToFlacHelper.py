import ffmpeg


def convertWebmToFlac(audio_buf):
    process = (ffmpeg
              .input('pipe:', format='libopus')
              .output('-', acodec='flac')
              .overwrite_output()
              .run_async(pipe_stdin=True, pipe_stdout=True)
              )
    buffer, _ = process.communicate(input=audio_buf)

    print(buffer)

