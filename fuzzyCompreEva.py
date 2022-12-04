# -*- coding: utf-8 -*-
"""
@Time    : 2022/12/4 11:37
@Author  : zeyi li
@Site    : 
@File    : fuzzyCompreEva.py
@Software: PyCharm
"""
from scipy.io import loadmat
import numpy as np

class FuzzyComprehensiveEvaluation():

  def __init__(self,standrad):

    self.standrad = standrad

  def _fullnan(self,data):
    return np.nan_to_num(data)


  def _avg(self,data,axises):
    array = np.average(data, axis=axises)
    return array

  def _load_mat(self):
    data1 = loadmat('matlabdata/date_1.mat')
    data2 = loadmat('matlabdata/wave_1.mat')

    h = data2['H']
    v = data1['v']
    tems = data1['tems']

    return h,v,tems

  def _list_add(self,v,h,tems):
    """
    Addition of corresponding elements

    :param v:speed
    :param h:height of waves
    :param tems: temperature
    :return: scores list
    """
    scores = []
    for i in range(len(v)):
      scores.append(v[i]+h[i]+tems[i])
    return scores


  def _compute_one_data(self,day):
    """

    :param day:
    :return:
    """
    h, v, tems = self._load_mat()
    temph = self._avg(h,axises=2)

    newh = temph[:,:,day]
    v = v[:,:,day]
    tems = tems[:,:,day]

    anewh = self._fullnan(newh)
    av = self._fullnan(v)
    atems = self._fullnan(tems)

    return anewh,av,atems

  def _list_to_array(self,clist):
    """
      list transform array

    :param clist:
    :return: array
    """
    array = np.array(clist)
    narray = array.reshape(133,-1)

    return narray


  def judge_waves_standard(self,i):
    """
    judge height of waves

    :param i: height
    :return: risk factor of h
    """
    test = 0
    if (i >= 7.0):
      test = self.standrad[0][0] * i
    elif (i >= 5.0 and i < 7.0):
      test = self.standrad[1][0] * i
    elif i >= 3.0 and i < 5.0:
      test = self.standrad[2][0] * i
    elif i >= 1.0 and i < 3.0:
      test = self.standrad[3][0] * i
    elif i >= 0.0 and i < 1.0:
      test = self.standrad[4][0] * i
    return test

  def judge_stream(self,j):
    """
        judge height of stream

    :param j: speed of stream
    :return:risk factor of v
    """
    vtest = 0
    if j >= 2:
      vtest = self.standrad[0][1] * j
    elif j >= 1.5 and j < 2:
      vtest = self.standrad[1][1] * j
    elif j >= 1 and j < 1.5:
      vtest = self.standrad[2][1] * j
    elif j >= 0.5 and j < 1:
      vtest = self.standrad[3][1] * j
    elif j >= 0 and j < 0.5:
      vtest = self.standrad[4][1] * j
    return vtest

  def judge_tems(self,z):
    """
        judge temperature

    :param z:temperature
    :return: risk factor of temperature
    """
    temstest = 0
    if z <12 or z >31:
      temstest = self.standrad[0][2]*z
    elif (z<14 and z>=12) or (z<=31 and z>29):
      temstest = self.standrad[1][2] * z
    elif (z<16 and z>=14) or (z<=29 and z>27):
      temstest = self.standrad[2][2] * z
    elif (z<18 and z>=16) or (z<=27 and z>25):
      temstest = self.standrad[3][2] * z
    elif z>=18 and z<=25:
      temstest = self.standrad[4][2] * z

    return temstest

  def get_scores(self,dayth):
    """
    Obtain the risk assessment factor for a given day

    :param dayth:One of seven days
    :return:Matrix of risk
    """
    test = []
    vtest = []
    temstest = []

    h, v, tems = self._compute_one_data(dayth)

    for i in np.nditer(h):
      test.append(self.judge_waves_standard(i))

    for j in np.nditer(v):
      vtest.append(self.judge_stream(j))

    for z in np.nditer(tems):
      temstest.append(self.judge_tems(z))

    scores = self._list_add(vtest,test,temstest)
    newscores = self._list_to_array(scores)

    return newscores

# unit test
if __name__ == '__main__':

  #            h           V           c
  standrad = [[0.59537902, 0.27635046, 0.12827052],
              [0.42857143, 0.42857143, 0.14285714],
              [0.63370792, 0.19192062, 0.17437146],
              [0.66941687, 0.24263692, 0.08794621],
              [0.34454467, 0.10852477, 0.54693056]]
  abc = FuzzyComprehensiveEvaluation(standrad)
  scores = abc.get_scores(1)
  print(scores)