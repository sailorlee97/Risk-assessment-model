# -*- coding: utf-8 -*-
"""
@Time    : 2022/12/4 11:44
@Author  : zeyi li
@Site    : 
@File    : utils.py
@Software: PyCharm
"""
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class utils():
    def __init__(self,socres):
        self.scores = socres

    def plot_risk(self,day):
        fig, ax = plt.subplots()
        im = ax.imshow(self.scores)
        ax.set_title("risk day %s"%day)
        fig.tight_layout()
        plt.colorbar(im)
        plt.show()