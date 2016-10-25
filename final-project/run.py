import os
from markov_python.cc_markov import MarkovChain

mc = MarkovChain()
dirname = os.path.dirname(os.path.abspath(__file__))
book = os.path.join(dirname, 'Monologo_do_Vaqueiro_Gil_Vicente.txt')

mc.add_file(book)
sentence = mc.generate_text()

print(sentence)
