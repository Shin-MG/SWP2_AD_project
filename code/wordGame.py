from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel
from PyQt5.QtWidgets import QLayout, QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt


from selectWord import SelectWord
from shuffleWord import ShuffleWord


class WordGame(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # 단어 랜덤으로 선정 및 위치 배정
        self.w = SelectWord('word.txt')
        self.word = ['']

        self.alphabet = [['' for i in range(9)] for i in range(9)]
        self.positions = [(i, j) for i in range(9) for j in range(9)]
        self.wordLocation = [(0, 0) for i in range(9) for j in range(9)]


        # 알파벳 버튼 생성 및 배치
        wordLayout = QGridLayout()
        self.allButton = []


        a = [alp for alpha in self.alphabet for alp in alpha]
        for position, alphabet in zip(self.positions, a):
            button = QPushButton(alphabet)
            button.setStyleSheet('background-color:white')
            wordLayout.addWidget(button, *position)
            button.clicked.connect(self.buttonClicked)
            self.allButton.append(button)


        # 게임에 필요한 도구 버튼 (STRAT, ANSWER, CLAER) 생성 및 배치
        tool = QHBoxLayout()

        toolButtons = [{'NEW':self.newButtonClicked},
                       {'ANSWER':self.answerButtonClicked},
                       {'CLEAR':self.clearButtonClicked}]

        for t in toolButtons:
            for name, connect in t.items():
                toolButton = QPushButton(name)
                toolButton.setStyleSheet('background-color:white')
                tool.addWidget(toolButton)
                toolButton.clicked.connect(connect)



        # 맞춰야 할 Word List 표시
        display = QVBoxLayout()

        wordList = QLabel('Word List')
        wordList.setAlignment(Qt.AlignCenter)
        display.addWidget(wordList)

        self.displayWord = QLineEdit()
        self.displayWord.setReadOnly(True)
        self.displayWord.setAlignment(Qt.AlignCenter)
        display.addWidget(self.displayWord)

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addLayout(wordLayout, 0, 0)
        mainLayout.addLayout(tool, 1, 0)
        mainLayout.addLayout(display, 2, 0)
        self.setLayout(mainLayout)
        self.setWindowTitle("Word Game")

        self.newButtonClicked()


    # 게임 시작 버튼
    def newButtonClicked(self):
        self.word.clear()
        self.answerLocation = []
        self.answer = ''
        self.buttonGroup = []
        self.displayWord.clear()
        self.changeColor(self.allButton, False)
        for i in self.allButton:
            i.setEnabled(True)


        self.word = self.w.selectWord()
        a = ShuffleWord(self.word)
        self.alphabet, self.positions, self.wordLocation = a.shuffleWord()


        i = 0
        a = [alp for alpha in self.alphabet for alp in alpha]
        for position, alphabet in zip(self.positions, a):
            self.allButton[i].setText(alphabet)
            if position in self.wordLocation:
                self.answerLocation.append(self.allButton[i])
            i += 1

        self.displayWordList(self.word)

        # 선택된 단어 중 가장 긴 단어의 길이 확인
        length = []
        for i in self.word:
            length.append(len(i))
        self.maxLengthWord = max(length)



    # 모든 단어 위치 표시 및 게임 종료
    def answerButtonClicked(self):
        for b in self.allButton:
            b.setDisabled(True)
        self.changeColor(self.answerLocation, True)


    # 선택된 버튼 원래 색상으로 (하얀색)
    def clearButtonClicked(self):
        self.answer = ''
        self.changeColor(self.buttonGroup, False)
        self.buttonGroup.clear()


    def buttonClicked(self):
        sender = self.sender()
        self.buttonGroup.append(sender)
        self.changeColor(self.buttonGroup, True)
        self.answer += sender.text()


        # 클릭한 단어 길이가 wordList의 최장 단어의 길이보다 길 때 --> clear 버튼 눌렀을 때와 같은 효과
        if len(self.answer) > self.maxLengthWord:
             self.clearButtonClicked()


        # 단어 맞췄을 때 --> Word List에서 해당 단어 삭제(안보이도록), 맞춘 단어 버튼 클릭 색상으로 유지 (하늘색)
        if self.answer in self.word:
            self.word.remove(self.answer)
            self.displayWordList(self.word)
            self.answer = ''
            self.changeColor(self.buttonGroup, True)
            self.buttonGroup.clear()


        # 단어 다 맞췄을 때 --> 성공 메시지 출력 및 게임 종료
        if not self.word:
            self.displayWordList(['S u c c e s s !'])
            self.answerButtonClicked()


    # Word List에 맞추어야 하는 단어 표시
    def displayWordList(self, wordList):
        self.displayWord.clear()
        for word in wordList:
           self.displayWord.insert(word + '         ')


    # 상황에 따라 버튼 색상 변경 (알파벳 버튼 클릭, 맞추었을 때 --> 하늘색 / CLEAR 버튼 클릭, 틀렸을 때 --> 하얀색)
    def changeColor(self, buttonGroup, state):
        for button in buttonGroup:
            button.setStyleSheet("background-color: %s" %({True: "skyblue", False: "white"}[state]))




if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    game = WordGame()
    game.show()
    sys.exit(app.exec_())
