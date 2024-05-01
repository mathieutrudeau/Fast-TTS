import os
import fast_tts.tortoise.tortoise_api as tortoise
import fast_tts.rvc.rvc_api as rvc
import torch
from huggingface_hub import hf_hub_download

class FastTTS:

    def fast_tts(text, voice_dir, result_dir, delimiter='', 
                        index_rate=0.5, filter_radius=3, resample_sr=0, rms_mix_rate=0.25, protect=0.33):
        try:
            print('Fast TTS')
            print('Text: ', text)

            # Preprocessing Checks
            FastTTS.preprocessing_checks(voice_dir, result_dir)

            audio_path = tortoise.create_audio(text,voice_dir,result_dir,delimiter)
            
            rvc.clone_voice(voice_dir, audio_path)

        except Exception as e:
            print('Error in Fast TTS: ', e)


    def preprocessing_checks(voice_dir, result_dir):
        try:
            print('Preprocessing Checks')

            # Check if the autoregressive model exists
            print('Checking if the autoregressive model exists')

            if not os.path.exists(f"{os.getcwd()}/data/autoregressive.pth"):
                print('Autoregressive Model does not exist')
                print(f"{os.getcwd()}/data/autoregressive.pth")
                print('Downloading the autoregressive model')
                hf_hub_download(repo_id="Awaazo/FastTTS", repo_type="model", filename="autoregressive.pth", local_dir=f"{os.getcwd()}/data", local_dir_use_symlinks=False)
            else:
                print('Autoregressive Model exists') 

            # Check if the tokenizer JSON exists
            print('Checking if the tokenizer JSON exists')

            if not os.path.exists(f"{os.getcwd()}/data/tokenizer.json"):
                print('Tokenizer JSON does not exist')
                print(f"{os.getcwd()}/data/tokenizer.json")
                print('Downloading the tokenizer JSON')
                hf_hub_download(repo_id="Awaazo/FastTTS", repo_type="model", filename="tokenizer.json", local_dir=f"{os.getcwd()}/data", local_dir_use_symlinks=False)
            else:
                print('Tokenizer JSON exists')

            # Check if the hifi-gan decoder exists
            print('Checking if the hifi-gan decoder exists')

            if not os.path.exists(f"{os.getcwd()}/data/hifidecoder.pth"):
                print('Hifi-GAN Decoder does not exist')
                print(f"{os.getcwd()}/data/hifidecoder.pth")
                print('Downloading the hifi-gan decoder')
                hf_hub_download(repo_id="Awaazo/FastTTS", repo_type="model", filename="hifidecoder.pth", local_dir=f"{os.getcwd()}/data", local_dir_use_symlinks=False)
            else:
                print('Hifi-GAN Decoder exists')

            # Check if the mel_norms exists
            print('Checking if the mel_norms exists')

            if not os.path.exists(f"{os.getcwd()}/data/mel_norms.pth"):
                print('Mel Norms does not exist')
                print(f"{os.getcwd()}/data/mel_norms.pth")
                print('Downloading the mel norms')
                hf_hub_download(repo_id="Awaazo/FastTTS", repo_type="model", filename="mel_norms.pth", local_dir=f"{os.getcwd()}/data", local_dir_use_symlinks=False)
            else:
                print('Mel Norms exists')


            # Check if the config json files exist
            print('Checking if the config json files exist')

            if not os.path.exists(f"{os.getcwd()}/data/v1/32k.json"):
                hf_hub_download(repo_id="Awaazo/FastTTS", repo_type="model", filename="32k.json", local_dir=f"{os.getcwd()}/data/v1", local_dir_use_symlinks=False)
                hf_hub_download(repo_id="Awaazo/FastTTS", repo_type="model", filename="40k.json", local_dir=f"{os.getcwd()}/data/v1", local_dir_use_symlinks=False)
                hf_hub_download(repo_id="Awaazo/FastTTS", repo_type="model", filename="48k.json", local_dir=f"{os.getcwd()}/data/v1", local_dir_use_symlinks=False)
                hf_hub_download(repo_id="Awaazo/FastTTS", repo_type="model", filename="48k.json", local_dir=f"{os.getcwd()}/data/v2", local_dir_use_symlinks=False)
                hf_hub_download(repo_id="Awaazo/FastTTS", repo_type="model", filename="32k.json", local_dir=f"{os.getcwd()}/data/v2", local_dir_use_symlinks=False)

            # Check if CUDA is available
            if(torch.cuda.is_available()==False):
                raise Exception('CUDA is not available. Please enable CUDA to run FastTTS. Visit https://developer.nvidia.com/cuda-downloads for more information on how to install CUDA.')

            # Check if the voice directory exists
            print('Checking if the voice directory exists')
            
            if not os.path.exists(voice_dir):
                raise Exception('Voice directory does not exist')
            
            # Check if the result directory exists
            print('Checking if the result directory exists')

            if not os.path.exists(result_dir):
                print('Result directory does not exist')
                print('Creating the result directory')
                os.mkdir(result_dir)

            # Make sure that the voice directory contains the necessary files
            print('Checking if the voice directory contains the necessary files')

            speaker = voice_dir.split('\\')[-1]

            if not os.path.exists(f"{voice_dir}/{speaker}.index") or not os.path.exists(f"{voice_dir}/{speaker}.pth"):
                raise Exception('Voice directory does not contain the necessary files')


            
        except Exception as e:
            print('Error in Preprocessing Checks: ', e)