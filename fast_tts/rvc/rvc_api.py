from rvc.configs.config import Config
from rvc.infer.modules.vc.modules import VC
from scipy.io import wavfile
import os
from huggingface_hub import hf_hub_download


def clone_voice(voice_dir, audio_path,
                index_rate=0.5,filter_radius=3,resample_sr=0,rms_mix_rate=0.25,protect=0.33):
    try:

        preprocessing_checks()

        print('Cloning Voice')
        print('Voice Directory: ', voice_dir)
        print('Audio Path: ', audio_path)

        speaker = voice_dir.split('\\')[-1]

        model_path = f"{voice_dir}\\{speaker}.pth"
        index_path = f"{voice_dir}\\{speaker}.index"

        temp_audio_path = f"{audio_path.split('.')[0]}_temp.wav"

        print('Model Path: ', model_path)
        print('Index Path: ', index_path)
        print('Temp Audio Path: ', temp_audio_path)

        # Load the configuration
        config = Config()

        print('Configuration Loaded')

        # Initialize Voice Cloning
        vc = VC(config)

        print('Voice Cloning Initialized')

        vc.get_vc(model_path, protect,protect)

        print('Voice Cloning Model Loaded')

        _, wav_opt = vc.vc_single(
            sid=0,
            input_audio_path=audio_path,
            f0_up_key=0,
            f0_file=None,
            f0_method="rmvpe",
            file_index=index_path,
            file_index2=None,
            index_rate=index_rate,
            filter_radius=filter_radius,
            resample_sr=resample_sr,
            rms_mix_rate=rms_mix_rate,
            protect=protect,
        )

        print(f"_: {_}\n")

        wavfile.write(temp_audio_path, wav_opt[0], wav_opt[1])

        os.remove(audio_path)
        os.rename(temp_audio_path, audio_path)


    except Exception as e:
        print('Error in Cloning Voice: ', e)


def preprocessing_checks():
    try:
        print('Preprocessing Checks')

        # Check if the rmvpe model exists
        print('Checking if the rmvpe model exists')

        if not os.path.exists(f"{os.getcwd()}/data/rmvpe.pt"):
            print('RMVPE Model does not exist')
            print(f"{os.getcwd()}/data/rmvpe.pt")
            print('Downloading the rmvpe model')
            hf_hub_download(repo_id="Awaazo/FastTTS", repo_type="model", filename="rmvpe.pt", local_dir=f"{os.getcwd()}/data", local_dir_use_symlinks=False)

        # Check if the hubert base model exists
        print('Checking if the hubert base model exists')

        if not os.path.exists(f"{os.getcwd()}/data/hubert_base.pt"):
            print('Hubert Base Model does not exist')
            print(f"{os.getcwd()}/data/hubert_base.pt")
            print('Downloading the hubert base model')
            hf_hub_download(repo_id="Awaazo/FastTTS", repo_type="model", filename="hubert_base.pt", local_dir=f"{os.getcwd()}/data", local_dir_use_symlinks=False)


    except Exception as e:
        print('Error in Preprocessing Checks: ', e)