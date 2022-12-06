# -*- coding: utf-8 -*-
"""
@Time    : 2022/12/6 11:19
@Author  : zeyi li
@Site    : 
@File    : preprocess.py
@Software: PyCharm
"""
import scipy.io as scio
from scipy import interpolate
import numpy as np
import copy

class datapreprocess():
  def __init__(self):
    self.name = "data_propress"


  def fix_three_dim(self,data):
    """
    Dr. wenhong:
      3d linear interpolation

    :param data: array of v and tems with nan
    :return: array finished interpolate
    """

    data = copy.deepcopy(data)
    for index in range(0, len(data)):
      list_lost = []
      list_true = []
      true_content = []
      #    0天
      for sub_index in range(0, len(data[index, :, 0])):
        if np.isnan(data[index, sub_index, 0]):
          list_lost.append(sub_index)
        else:
          list_true.append(sub_index)
          true_content.append(data[index, sub_index, 0])

      if len(list_lost) > 50 or len(list_lost) == 0:
        pass
      else:
        #  竖直方向上用线性插值
        f = interpolate.interp1d(np.array(list_true), np.array(true_content), kind='linear', fill_value="extrapolate")
        predict = f(np.array(list_lost))
        data[index, np.array(list_lost), 0] = predict

      list_lost = []
      list_true = []
      true_content = []

      #    1天
      for sub_index in range(0, len(data[index, :, 1])):
        if np.isnan(data[index, sub_index, 1]):
          list_lost.append(sub_index)
        else:
          list_true.append(sub_index)
          true_content.append(data[index, sub_index, 1])

      if len(list_lost) > 50 or len(list_lost) == 0:
        pass
      else:
        #  竖直方向上用线性插值
        f = interpolate.interp1d(np.array(list_true), np.array(true_content), kind='linear',
                                 fill_value="extrapolate")
        predict = f(np.array(list_lost))
        data[index, np.array(list_lost), 1] = predict

      list_lost = []
      list_true = []
      true_content = []

      #    2天
      for sub_index in range(0, len(data[index, :, 2])):
        if np.isnan(data[index, sub_index, 2]):
          list_lost.append(sub_index)
        else:
          list_true.append(sub_index)
          true_content.append(data[index, sub_index, 2])

      if len(list_lost) > 50 or len(list_lost) == 0:
        pass
      else:
        #  竖直方向上用线性插值
        f = interpolate.interp1d(np.array(list_true), np.array(true_content), kind='linear',
                                 fill_value="extrapolate")
        predict = f(np.array(list_lost))
        data[index, np.array(list_lost), 2] = predict

      list_lost = []
      list_true = []
      true_content = []

      #    3天
      for sub_index in range(0, len(data[index, :, 3])):
        if np.isnan(data[index, sub_index, 3]):
          list_lost.append(sub_index)
        else:
          list_true.append(sub_index)
          true_content.append(data[index, sub_index, 3])

      if len(list_lost) > 50 or len(list_lost) == 0:
        pass
      else:
        #  竖直方向上用线性插值
        f = interpolate.interp1d(np.array(list_true), np.array(true_content), kind='linear',
                                 fill_value="extrapolate")
        predict = f(np.array(list_lost))
        data[index, np.array(list_lost), 3] = predict

      list_lost = []
      list_true = []
      true_content = []

      #    4天
      for sub_index in range(0, len(data[index, :, 4])):
        if np.isnan(data[index, sub_index, 4]):
          list_lost.append(sub_index)
        else:
          list_true.append(sub_index)
          true_content.append(data[index, sub_index, 4])

      if len(list_lost) > 50 or len(list_lost) == 0:
        pass
      else:
        #  竖直方向上用线性插值
        f = interpolate.interp1d(np.array(list_true), np.array(true_content), kind='linear',
                                 fill_value="extrapolate")
        predict = f(np.array(list_lost))
        data[index, np.array(list_lost), 4] = predict

      list_lost = []
      list_true = []
      true_content = []

      #    5天
      for sub_index in range(0, len(data[index, :, 5])):
        if np.isnan(data[index, sub_index, 5]):
          list_lost.append(sub_index)
        else:
          list_true.append(sub_index)
          true_content.append(data[index, sub_index, 5])

      if len(list_lost) > 50 or len(list_lost) == 0:
        pass
      else:
        #  竖直方向上用线性插值
        f = interpolate.interp1d(np.array(list_true), np.array(true_content), kind='linear',
                                 fill_value="extrapolate")
        predict = f(np.array(list_lost))
        data[index, np.array(list_lost), 5] = predict

      list_lost = []
      list_true = []
      true_content = []

      #    6天
      for sub_index in range(0, len(data[index, :, 6])):
        if np.isnan(data[index, sub_index, 6]):
          list_lost.append(sub_index)
        else:
          list_true.append(sub_index)
          true_content.append(data[index, sub_index, 6])

      if len(list_lost) > 50 or len(list_lost) == 0:
        pass
      else:
        #  竖直方向上用线性插值
        f = interpolate.interp1d(np.array(list_true), np.array(true_content), kind='linear',
                                 fill_value="extrapolate")
        predict = f(np.array(list_lost))
        data[index, np.array(list_lost), 6] = predict

    return data

  def fix_four_dim(self,data):
    """
    Dr. wenhong:
      3d linear interpolation

    :param data:  array of h with nan
    :return: array finished interpolate
    """

    #  转化以天数带队
    data = copy.deepcopy(data)
    data = data.transpose(0, 1, 3, 2)
    print(data.shape)

    new_data = np.zeros((133, 121, 7))

    for i in range(0, len(data)):
      for j in range(0, len(data[0])):
        for m in range(0, len(data[0][0])):
          group_avg = []
          for n in range(0, len(data[0][0][0])):
            # 查看NAN
            if not np.isnan(data[i][j][m][n]):
              group_avg.append(data[i][j][m][n])

          if len(group_avg) != 0:
            new_data[i][j][m] = np.mean(np.array(group_avg))
          else:
            new_data[i][j][m] = np.nan

    # print(count_nan_3(new_data))
    return self.fix_three_dim(new_data)