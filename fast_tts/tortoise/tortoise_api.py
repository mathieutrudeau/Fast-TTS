from fast_tts.tortoise.api_fast import TextToSpeech as Tortoise_TTS_Hifi
from fast_tts.tortoise.utils.text import split_and_recombine_text
from fast_tts.tortoise.utils.audio import load_audio,load_voice

import os
import torchaudio
import torch
from datetime import datetime

def create_audio(text, voice_dir, result_dir, delimiter='', temperature=0.2, top_p=0.8, diffusion_temperature=1, length_penalty=1, repetition_penalty=2, cond_free_k=2, 
                 num_autoregressive_samples=16, sample_batch_size=1, diffusion_iterations=30, voice_samples=None, conditioning_latents=None, use_deterministic_seed=None, 
                 returns_deterministic_state=True, k=1,diffusion_sampler='DDIM', breathing_room=8,half_p=False, cond_free=True, cvvp_amount=0, output_volume=1, use_deepspeed=False):
    try:
        print('----------- Tortoise TTS -----------')
        print('Parameters: ')
        print('\tText: ', text)
        print('\tVoice Directory: ', voice_dir)
        print('\tResult Directory: ', result_dir)

        speaker = voice_dir.split('\\')[-1]
        speaker_dir = voice_dir.split('\\')[0:-1]
        speaker_dir = '\\'.join(speaker_dir)
        
        filename = f"{result_dir}/{speaker}_{str(datetime.now().timestamp()).replace('.','')}"

        # Loading the TTS model
        print('Loading the TTS model')

        tts = Tortoise_TTS_Hifi(autoregressive_model_path=f"{os.getcwd()}/data/autoregressive.pth", 
                                tokenizer_json=f"{os.getcwd()}/data/tokenizer.json",
                                use_deepspeed=use_deepspeed)

        print('TTS Model Loaded')

        # Split the text into sections of 200-300 characters
        print('Splitting the text into sections of 200-300 characters')

        if delimiter == '':
            text_sections = split_and_recombine_text(text)
        else:
            text_sections = text.split(delimiter)

        print('Text Sections: ', text_sections)

        # Make sure the volume adjustment is correct
        volume_adjustment = torchaudio.transforms.Vol(gain=output_volume, gain_type='amplitude') if output_volume != 1 else None

        settings = {
            'temperature': temperature,
            'top_p': top_p,
            'diffusion_temperature': diffusion_temperature,
            'length_penalty': length_penalty,
            'repetition_penalty': repetition_penalty,
            'cond_free_k': cond_free_k,
            'num_autoregressive_samples': num_autoregressive_samples,
            'sample_batch_size': sample_batch_size,
            'diffusion_iterations': diffusion_iterations,
            'voice_samples': voice_samples,
            'conditioning_latents': conditioning_latents,
            'use_deterministic_seed': use_deterministic_seed,
            'returns_deterministic_state': returns_deterministic_state,
            'k': k,
            'diffusion_sampler': diffusion_sampler,
            'breathing_room': breathing_room,
            'half_p': half_p,
            'cond_free': cond_free,
            'cvvp_amount': cvvp_amount
        }

        # Load the voice samples and create the conditioning latents
        print('Loading the voice samples and creating the conditioning latents')


        voice_samples, confitioning_latents = load_voice(voice=speaker, extra_voice_dirs=[speaker_dir], model_hash=tts.autoregressive_model_hash)

        settings['voice_samples'] = voice_samples
        settings['conditioning_latents'] = conditioning_latents


        # Generate the audio
        print('Generating the audio')

        for i, cut_text in enumerate(text_sections):
            print(f"Generating audio for section {i+1}/{len(text_sections)}")

            gen = tts.tts(cut_text, **settings)

            if not isinstance(gen, list):
                gen = [gen]

            for j, g in enumerate(gen):
                audio = g.squeeze(0).cpu()
                name = f"{filename}_{i}.wav"

                torchaudio.save(name, audio, tts.output_sample_rate)

        # Combine the audio sections into a single audio file
        print('Combining the audio sections into a single audio file')

        combined_audio = None

        for i, cut_text in enumerate(text_sections):
            name = f"{filename}_{i}.wav"
            audio = load_audio(name, tts.output_sample_rate)

            if volume_adjustment is not None:
                audio = volume_adjustment(audio)
            
            if combined_audio is None:
                combined_audio = audio
            else:
                combined_audio = torch.cat([combined_audio, audio], dim=1)

        torchaudio.save(f"{filename}.wav", combined_audio, tts.output_sample_rate)

        print("Cleaning up...")
        for i, cut_text in enumerate(text_sections):
            name = f"{filename}_{i}.wav"
            os.remove(name)    

        return f"{filename}.wav"

    except Exception as e:
        print('Error in Tortoise TTS: ', e)

