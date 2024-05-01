# Fast-TTS

Fast-TTS is a module that offers a simple api in order to generate a speech from text. 


## Requirements
- Python 3.9
- CUDA enabled GPU with [PyTorch](https://pytorch.org/get-started/locally/) installed.


## How to add Voices

The following steps show how to add voices.
- Create a folder with the speaker name '/MyVoice'. Here 'MyVoice' is the name of the speaker that you wish to add.
- Find 1-3 audio samples of the speaker, those samples should be ~1min in length and be .wav files. The clearer the voice, the better the generated audio will be.
- Add those audio sampples to the speaker folder that was previously created.
- Add the .index and .pth files for the speaker model. Name them 'MyVoice.index' and 'MyVoice.pth'.
- You can either get the .index and .pth files from trained RVC models, or you can train your own model.