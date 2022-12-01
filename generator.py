import os, random
from pylatex import Document, Section, Subsection, Command, Package
from pylatex.utils import italic, NoEscape

if __name__ == '__main__':
    print('Enter seed: ', end='')
    seed = input()
    random.seed(seed)

    doc = Document(documentclass='exam')
    doc.packages.append(Package('minted'))

    doc.preamble.append(Command('title', 'Generated Exam'))
    doc.preamble.append(Command('author', 'Seed: ' + seed))
    doc.preamble.append(Command('date', NoEscape(r'\today')))
    doc.append(NoEscape(r'\maketitle'))

    with doc.create(Section('Programming Comprehension')):
        files = []
        for x in os.listdir("exam1/problem1"):
            if x.endswith(".tex"):
                files.append(x)

        doc.append(Command('input', 'exam1/problem1/' + random.choice(files)))

    doc.generate_pdf('exam-' + str(seed), compiler_args=["-shell-escape"], clean_tex=False)
