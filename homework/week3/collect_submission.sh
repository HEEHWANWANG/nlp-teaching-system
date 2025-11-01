conda config --add channels conda-forge
conda install zip
rm -f 2000_00000_coding.zip #change here to your student id
zip -r 2000_00000_coding.zip ./q3/*.py ./q3/model.bin ./q3/model.bin.optim ./q3/outputs/test_outputs*.txt
#change above to your student id