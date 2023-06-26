import subprocess as sp

FFMPEG_BIN = "ffmpeg"



pipe = sp.Popen([ FFMPEG_BIN,
       '-y', # (optional) means overwrite the output file if it already exists.
       "-f", 'alsa', # means 16bit input
       "-acodec", "pcm_s16le", # means raw 16bit input
       '-r', "44100", # the input will have 44100 Hz
       '-ac','2', # the input will have 2 channels (stereo)
       '-i', 'hw:1,0', # means that the input will arrive from the pipe
       '-vn', # means "don't expect any video input"
       '-acodec', "libfdk_aac" # output audio codec
       '-b', "3000k", # output bitrate (=quality). He                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           re, 3000kb/second
       'my_awesome_output_audio_file.mp3'],
            stdin=sp.PIPE,stdout=sp.PIPE, stderr=sp.PIPE)

# audio_array.astype("int16").tofile(self.proc.stdin)
                                                                           
