import sys
import unittest

from wordGame import WordGame

from PyQt5.QtWidgets import QApplication

app= QApplication( sys.argv )



class TestWordGame(unittest.TestCase):

    def setUp(self):
        # Word Game 내의 changeColor() 모두 제거 후 테스트 진행
        self.game = WordGame()


    def tearDown(self):
        pass


    def testInit(self):
        self.assertEqual(len(self.game.allButton), 81)
        self.assertTrue(self.game.displayWord.isReadOnly())
        self.assertEqual(self.game.windowTitle(), "Word Game")


    def testNewButtonClicked(self):
        self.game.newButtonClicked()
        self.assertTrue(self.game.button.isEnabled())
        self.assertEqual(len(self.game.word), 6)

        length = 0
        for i in self.game.word:
            length += len(i)

        self.assertEqual(len(self.game.wordLocation), length)
        self.assertEqual(len(self.game.wordLocation), len(self.game.answerLocation))


    def testAnswerButtonClicked(self):
        self.game.answerButtonClicked()
        self.assertFalse(self.game.button.isEnabled())


    def testClearButtonClicked(self):
        self.game.answer = 'candy'
        self.game.clearButtonClicked()
        self.assertEqual(self.game.answer, '')


    def testButtonClicked(self):
        # set up for testButtonClicked
        self.game.word = ['candy', 'coffee', 'trade', 'egg', 'bank', 'sticker']
        self.game.answer = 'candy'

        # test
        self.game.buttonClicked()
        self.assertEqual(self.game.word, ['coffee', 'trade', 'egg', 'bank', 'sticker'])
        self.game.answer = 'eightword'
        self.game.buttonClicked()
        self.assertEqual(self.game.answer, '')
        self.assertEqual(self.game.displayWord.text(), 'coffee         trade         egg         bank         sticker         ')
        self.game.word.clear()
        self.game.buttonClicked()
        self.assertEqual(self.game.displayWord.text(), 'S u c c e s s !         ')
        self.assertFalse(self.game.button.isEnabled())




if __name__ == '__main__':
    unittest.main()