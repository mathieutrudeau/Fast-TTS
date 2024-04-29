import os
import tortoise.tortoise_api as tortoise

class FastTTS:

    def fast_tts(text, delimiter='', speaker='Default', language='en', use_tortoise=True, 
                        index_rate=0.5, filter_radius=3, resample_sr=0, rms_mix_rate=0.25, protect=0.33):
        try:
            print('Fast TTS')

            print('Text: ', text)

            if use_tortoise:
                tortoise.create_audio(text,"C:\\backend_server\\ServerFiles\\Speakers\\Drinker","C:\\Users\\Mathieu\\Desktop",delimiter)


        except Exception as e:
            print('Error in Fast TTS: ', e)







FastTTS.fast_tts('Hello World! This is the ultimate test of the Fast TTS! I hope it works! Thank you!')