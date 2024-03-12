
from random import randint

class WordFinder:
    """Word Finder: finds random words from a dictionary.
        
    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    
    """

    def __init__(self, path):
        self.words = []
        self.getWordsList(path)

    def getWordsList(self, path):
        file = open(path, 'r')
        self.words = [word.strip() for word in file]
        file.close()
        print(f"{len(self.words)} words read") 
       

    def random(self):
        randomIdx = randint(0, len(self.words)-1)
        return self.words[randomIdx]
    

class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.

    >>> swf = SpecialWordFinder("complex.txt")
    4 words read

    >>> swf.random() in ["apple", "mango", "kale", "parsnips"]
    True

    >>> swf.random() in ["apple", "mango", "kale", "parsnips"]
    True

    >>> swf.random() in ["apple", "mango", "kale", "parsnips"]
    True
    """


    def getWordsList(self, path):
        file = open(path, 'r')
        self.words = [word.strip() for word in file if (not word.startswith('#')) and (not word.isspace())]
        file.close()
        print(f"{len(self.words)} words read") 


