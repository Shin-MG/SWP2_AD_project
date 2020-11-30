from random import randrange

class SelectWord:

    def __init__(self, filename):
        self.words = []
        self.wordList = []
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        for line in lines:
            word = line.rstrip()
            # 알파벳 버튼 9X9로 구성 --> 7이하 길이의 단어만 선정
            if len(word) < 8:
                self.words.append(word)


    def selectWord(self):
         for i in range(6):
             word = randrange(len(self.words))
             self.wordList.append(self.words[word])
             del self.words[word]
         return self.wordList
