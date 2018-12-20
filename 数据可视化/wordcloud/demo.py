# coding=utf-8
import jieba.analyse as analyse
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from scipy.misc import imread


def cut_words(file_path):
    word_list = []
    with open(file_path, encoding="utf-8") as f:
        text = f.read()
    for key in analyse.extract_tags(text, 50, withWeight=True):
        # print(key)
        word_list.append(key)
    return word_list


def draw_pic(image_path, file_path):
    plt.figure(figsize=(20, 10))
    # 读取图片,自定义‘沙发’形状
    pic = imread(image_path)
    w_c = WordCloud(font_path="STKAITI.TTF",
                    background_color="white",
                    mask=pic,
                    max_font_size=60,
                    margin=1)
    word_list = cut_words(file_path)
    wc = w_c.fit_words({x[0]: x[1] for x in word_list})
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()


draw_pic('shafa.png', 'words.txt')
