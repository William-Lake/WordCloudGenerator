# -*- coding: utf-8 -*-

import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from primary_ui import PrimaryUI
import stop_words

"""Main module."""

class WordCloudGenerator(object):

    def generate_wordcloud(self, input_text):

        input_text = self.sanitize(input_text)

        wordcloud = WordCloud(width=480, height=480, margin=0).generate(input_text)

        plt.imshow(wordcloud, interpolation='bilinear')

        plt.axis('off')

        plt.margins(x=0, y=0)

        plt.show()
    
    def sanitize(self, input_text):

        input_text = re.sub(r'[^A-Za-z0-9 ]','',input_text.strip())

        words = input_text.split(' ')

        words = [word for word in words if word not in stop_words.words]

        input_text = ' '.join(words)

        return input_text

def main():

    wordcloud_generator = WordCloudGenerator()

    primary_ui = PrimaryUI()

    primary_ui.start(wordcloud_generator.generate_wordcloud)