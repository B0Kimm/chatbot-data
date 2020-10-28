from data.utils import DoublespaceLineCorpus
from data.noun import LRNounExtractor_v2


corpus_fname = 'corpus.txt'
sents = DoublespaceLineCorpus(corpus_fname, iter_sent=True)

noun_extractor = LRNounExtractor_v2(verbose=True)
nouns = noun_extractor.train_extract(sents)

print(nouns['배달'])