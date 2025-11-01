conda install -y pytorch pytorch-cuda=11.8 -c pytorch -c nvidia
conda install -y -c pytorch torchtext

conda install -y numpy scipy nltk pillow tqdm docopt mkl

pip install -U pip setuptools wheel
pip install -U spacy sentencepiece sacrebleu tensorboard
python -m spacy download en_core_web_sm