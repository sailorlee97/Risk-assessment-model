# -*- coding: utf-8 -*-
"""
@Time    : 2022/12/4 11:37
@Author  : zeyi li
@Site    :
@File    : fuzzyCompreEva.py
@Software: PyCharm
"""
from utils import utils
from fuzzyCompreEva import FuzzyComprehensiveEvaluation
import matplotlib.pyplot as plt

if __name__ == '__main__':

  #            h           V           c
  standrad = [[0.34454467, 0.10852477, 0.54693056],
              [0.42857143, 0.42857143, 0.14285714],
              [0.59537902, 0.27635046, 0.12827052],
              [0.63370792, 0.19192062, 0.17437146],
              [0.66941687, 0.24263692, 0.08794621]]
  abc = FuzzyComprehensiveEvaluation(standrad)

  scores = abc.get_scores(3)
  u = utils(scores)
  for i in range(7):
    u.plot_risk(1)