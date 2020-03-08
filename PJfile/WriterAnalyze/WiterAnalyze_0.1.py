# %%
import torch

torch.cuda.is_available()

# %%
import os
import glob
import codecs
import logging
import re
import random
from itertools import chain

# 形態素解析用の外部モジュール
from janome.tokenizer import Tokenizer
from gensim.models import Word2Vec

# LSTM用のモジュール
import copy
import numpy as np
from numpy.random import rand  # ランダムなベクトルを作るための関数
from tqdm import tqdm  # ループの進捗を示すモジュール
import torch  # 深層学習用のモジュール
import torch.nn as nn  # ニューラルネットワーク用のモジュール
import torch.nn.functional as F  # 活性化関数用のモジュール
import torch.optim as optim  # Pytorchのオプティマイザー
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

#　文章データの読み込み

