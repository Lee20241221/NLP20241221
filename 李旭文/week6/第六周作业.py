import torch
import torch.nn as nn
import numpy as np
from transformers import BertModel
'''
embedding：
[cls]
(position_embedding + segment_embedding + token_embedding) * 768 + 768 + 768
[sep]

Q、K、V
（768 * 768 + 768）* 3
linear(QKV)

feed_forward

pool_fc
'''
model = BertModel.from_pretrained(r'D:\BaiduNetdiskDownload\badou\第六周 语言模型\bert-base-chinese\bert-base-chinese',return_dict = False)
nums = 2
vocab = 21128
max_sentence_length = 512
embedding_size = 768
hidden_size = 3072
num_layers = 1  

# embedding
embedding_parameters = vocab * embedding_size + nums * embedding_size + max_sentence_length * embedding_size + embedding_size + embedding_size

# QKV
qkv_parameters = (embedding_size * embedding_size + embedding_size) * 3

# out
self_out_parameters = embedding_size * embedding_size + embedding_size + embedding_size + embedding_size

# feed_forward
feed_forward_parameters = embedding_size * hidden_size + hidden_size * embedding_parameters + embedding_size + embedding_size +embedding_size

# pool_fc
pool_fc_parameters = embedding_size * embedding_size + embedding_size

# 模型总参数 embedding + qkv_parameters + self_out_parameters + feed_forward_parameters + pool_fc
total_parameters = embedding_parameters + (qkv_parameters + self_out_parameters + feed_forward_parameters) * num_layers+pool_fc_parameters
print(total_parameters)


