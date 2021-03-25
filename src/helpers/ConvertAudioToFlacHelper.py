import os

import ffmpeg

from definitions import ROOT_DIR


def convertWebmToFlac(audio_buf):
    """
    Converts an audio buffer in audio/webm format into a bytes array using the flac format.
    """

    # Setup conversion process
    process = (ffmpeg
               .input("pipe:", acodec='opus')  # Input from stdin using pipe
               .output("pipe:", acodec='flac', format='flac')  # Output via stdout using pipe
               .run_async(pipe_stdin=True, pipe_stdout=True, pipe_stderr=True,
                          cmd=os.path.join(ROOT_DIR, "src/modules/ffmpeg/ffmpeg.exe"))  # set correct flags
               )

    # Insert audio buffer
    process.communicate(input=audio_buf.read())

    # Wait for process to finish
    process.wait()

    # Get results
    buffer, err = process.communicate()

    # Return buffer
    return buffer
