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
from ahp import AHP
import numpy as np

if __name__ == '__main__':
  b5 = np.array([[1, 3, 7], [1 / 3, 1, 3], [1 / 7, 1 / 3, 1]])
  b4 = np.array([[1, 2, 5], [1 / 2, 1, 2], [1 / 5, 1 / 2, 1]])
  b3 = np.array([[1, 3, 4], [1 / 3, 1, 1], [1 / 4, 1, 1]])
  b2 = np.array([[1, 1, 3], [1, 1, 3], [1 / 3, 1 / 3, 1]])
  b1 = np.array([[1, 1, 2], [1, 1, 2], [1 / 2, 1 / 2, 1]])

  lists = [b1,b2,b3,b4,b5]
  standradlist = []
  for i in lists:
    aweight = AHP(i)
    array_weight = aweight.cal_weight__by_eigenvalue_method()
    standradlist.append(array_weight)

  standrad = np.array(standradlist)
  print(standrad)

  #            v           h            c
  # standrad = [[0.34454467, 0.10852477, 0.54693056],
  #             [0.42857143, 0.42857143, 0.14285714],
  #             [0.59537902, 0.27635046, 0.12827052],
  #             [0.63370792, 0.19192062, 0.17437146],
  #             [0.66941687, 0.24263692, 0.08794621]]
  abc = FuzzyComprehensiveEvaluation(standrad)

  scores = abc.get_scores(3)
  u = utils(scores)
  for i in range(7):
    u.plot_risk(1)