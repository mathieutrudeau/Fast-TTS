from tortoise.api_fast import TextToSpeech as Tortoise_TTS_Hifi
from tortoise.utils.text import split_and_recombine_text
from tortoise.utils.audio import load_audio,load_voice


def create_audio(text, autoregressive_model, diffusion_model, tokenizer_json, voice_dir, result_dir, delimiter='', temperature=0.2, top_p=0.8, diffusion_temperature=1, length_penalty=1, repetition_penalty=2, cond_free_k=2, 
                 num_autoregressive_samples=16, sample_batch_size=1, diffusion_iterations=30, voice_samples=None, conditioning_latents=None, use_deterministic_seed=None, 
                 returns_deterministic_state=True, k=1,diffusion_sampler='DDIM', breathing_room=8,half_p=False, cond_free=True, cvvp_amount=0):
    try:
        print('----------- Tortoise TTS -----------')
        print('Parameters: ')
        print('\tText: ', text)
        print('\tAutoregressive Model: ', autoregressive_model)
        print('\tDiffusion Model: ', diffusion_model)
        print('\tTokenizer JSON: ', tokenizer_json)
        print('\tVoice Directory: ', voice_dir)
        print('\tResult Directory: ', result_dir)




    except Exception as e:
        print('Error in Tortoise TTS: ', e)