from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    description = f.read()

setup(
    name='fast_tts',
    version='0.0.2',
    long_description=description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'tbb',
        'mpmath',
        'MarkupSafe', 
        'intel-openmp', 
        'typing-extensions', 
        'sympy', 
        'networkx', 
        'mkl', 
        'jinja2', 
        'fsspec', 
        'filelock', 
        'torch', 
        'pillow', 
        'numpy', 
        'torchvision', 
        'torchaudio',
        'einops',
        'transformers<=4.19.0',
        'librosa',
        'inflect',
        'unidecode',
        'psutil',
        'av',
        'faiss-cpu',
        'praat-parselmouth>=0.4.2',
        'pyworld',
        'torchcrepe',
        'fairseq',
        'tensorboardX',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
)