"""This function runs unit tests on the emotion_detector function"""

import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        self.assertEqual(emotion_detector('I am glad this happened').get('dominant_emotion', 0), 'joy')
        self.assertEqual(emotion_detector('I am really mad about this').get('dominant_emotion', 0), 'anger')
        self.assertEqual(emotion_detector('I feel disgusted just hearing about this').get('dominant_emotion', 0), 'disgust')
        self.assertEqual(emotion_detector('I am so sad about this').get('dominant_emotion', 0), 'sadness')
        self.assertEqual(emotion_detector('I am really afraid that this will happen').get('dominant_emotion', 0), 'fear')
unittest.main()