import jieba
text = '我來到北京清華大學'
print('預設:', '|'.join(jieba.cut(text, cut_all=False, HMM=True)))
print('全關閉:', '|'.join(jieba.cut(text, cut_all=False, HMM=False)))
print('全關閉:', '|'.join(jieba.cut(text, cut_all=True, HMM=True)))