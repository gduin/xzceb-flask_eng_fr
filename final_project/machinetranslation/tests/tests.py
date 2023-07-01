import unittest
import translator

class translator_test(unittest.TestCase):

    english_text = 'Hello'
    french_text = 'Bonjour'

    def test_e2f(self):
    
        self.assertEqual( translator.translate_english_to_french(self.english_text), self.french_text)

    def test_f2e(self):
        
        self.assertEqual( translator.translate_french_to_english(self.french_text), self.english_text)

if __name__ == '__main__':
    unittest.main()