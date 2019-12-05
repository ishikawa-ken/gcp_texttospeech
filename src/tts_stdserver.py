#!/usr/bin/env python
#-*- coding: utf-8 -*-
#[tts_stdserver.py]

import roslib
import rospy
from gcp_texttospeech.srv import TTS

from google.cloud import texttospeech

import wave
import pyaudio

Filename = 'output.wav'

class TTS_server(object):
    def __init__(self):
        rospy.init_node('gcp_texttospeech')
        self.srv = rospy.Service('/tts', TTS, self.execute)
        rospy.loginfo("Ready to gcp_texttospeech stdserver")
        rospy.spin()

    def execute(self, data):
        client = texttospeech.TextToSpeechClient()
        synthesis_input = texttospeech.types.SynthesisInput(text=data.sentence)
        voice = texttospeech.types.VoiceSelectionParams(
            language_code='en-US',
            name='en-US-Wavenet-F',
            #ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL
            )
        audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.LINEAR16)

        response = client.synthesize_speech(synthesis_input, voice, audio_config)

        with open(Filename, 'wb') as out:
            out.write(response.audio_content)
            print('Audio content written to file ' + Filename)

        self.PlayWaveFile()

    def PlayWaveFile(self):
        try:
            wf = wave.open(Filename, "rb")
            print("Time[s]:", float(wf.getnframes()) / wf.getframerate())
        except FileNotFoundError:
            print("[Error 404] No such file or directory: " + Filename)
            return

        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        chunk = 1024
        data = wf.readframes(chunk)
        while data != b'':
            stream.write(data)
            data = wf.readframes(chunk)
        stream.stop_stream()
        stream.close()
        p.terminate()


if __name__ == '__main__':
    TTS_server()
    rospy.spin()
