conda install pytorch pytorch-cuda=11.8 -c pytorch -c nvidia -y
conda install -c pytorch torchtext -y
pip install -U pip setuptools wheel
pip install -U spacy
conda install mkl -y
python -m spacy download en_core_web_sm
conda install pillow -y
conda install nomkl numpy scipy tqdm docopt nltk -y
pip install sentencepiece sacrebleu tensorboard