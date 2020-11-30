from random import choice, shuffle, randint
from string import ascii_lowercase

class ShuffleWord:

    def __init__(self, wordList):
        self.word = wordList
        self.word_reverse = [self.word[i] for i in range(3)]
        for i in range(3, 6):
            self.word_reverse.append(self.word[i][::-1])
        shuffle(self.word_reverse)


    def shuffleWord(self):
        alphabet = [[choice(ascii_lowercase) for i in range(9)] for i in range(9)]
        positions = [(i, j) for i in range(9) for j in range(9)]

        location = [] # 현재 단어의 위치 선정에 사용
        wordLocation = [] # 모든 단어 위치 저장
        counter = 0

        while(counter < 6):
            word = self.word_reverse[counter]
            location.clear()
            ranNumCol = randint(0, 8)
            ranNumRow = randint(0, 9 - len(word))

            # 가로로 단어 배치
            if counter < 3:
                for i in range(len(word)):
                    location.append((ranNumCol, ranNumRow))
                    ranNumRow += 1

            # 세로로 단어 배치
            else:
                for i in range(len(word)):
                    location.append((ranNumRow, ranNumCol))
                    ranNumRow += 1

            # 선정된 위치에 다른 단어가 존재하면, 현재 단어 위치 다시 선정
            if list(set(location).intersection(wordLocation)):
                continue

            # 선정 위치에 다른 단어 없으면, 현재 단어 위치로 확정
            w = 0
            for l in location:
                wordLocation.append(l)
                alphabet[l[0]][l[1]] = word[w]
                w += 1
            counter += 1

        return alphabet, positions, wordLocation