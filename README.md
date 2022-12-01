# Exam Generator
Testing with random seeded LaTeX exam generation. Depending on a seed given, an exam may be generated with different questions.

Existing examples of generated exams can be found in the [exam-123.pdf](https://github.com/ezrichards/exam-generator/blob/master/exam-123.pdf) and [exam-3053.pdf](https://github.com/ezrichards/exam-generator/blob/master/exam-3053.pdf) files.

# Local Setup (Linux)
Note that if you don't have a LaTeX processor installed, you'll need to run the following command:

`sudo apt-get install texlive-pictures texlive-science texlive-latex-extra latexmk`
(`latexmk` is just one LaTeX processor, but any could be used.)

After installing a LaTeX processor, we can run the following:
```git clone https://github.com/ezrichards/exam-generator.git
cd exam-generator
pip install -r requirements.txt
python3 generator.py
```
After running the generator, it will ask for a seed. Depending on the result of the seed and its randoms, it will select a problem from the `exam1/problem1` folder.

The generated exam will be created in the root directory with name `exam-seed.pdf` and a corresponding `.tex` file.

## Caveats
Randoms may not necessarily use all files from the random folder; although random seeds will reproduce the same questions each time,
all combinations of questions may not be used.
