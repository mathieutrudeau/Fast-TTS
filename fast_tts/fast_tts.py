import os
import fast_tts.tortoise.tortoise_api as tortoise
import fast_tts.rvc.rvc_api as rvc

class FastTTS:

    def fast_tts(text, voice_dir, result_dir, delimiter='', 
                        index_rate=0.5, filter_radius=3, resample_sr=0, rms_mix_rate=0.25, protect=0.33):
        try:
            print('Fast TTS')

            print('Text: ', text)

#            voice_dir = f"C:\\backend_server\\ServerFiles\\Speakers\\Drinker"

#            result_dir = f"C:\\Users\\Mathieu\\Desktop"

            audio_path = tortoise.create_audio(text,voice_dir,result_dir,delimiter)
            
            rvc.clone_voice(voice_dir, audio_path)

        except Exception as e:
            print('Error in Fast TTS: ', e)


#FastTTS.fast_tts('Hello World! This is the ultimate test of the Fast TTS! I hope it works! Thank you!')