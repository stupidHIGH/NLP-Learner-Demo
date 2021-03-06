from gensim.models import word2vec
import gensim
import logging


embedding_dim=200
window=5
min_count=2

train_file_name="./text.txt"               # save_model为保存模型名
save_model_name="./my_diy_language_model"  # model_file_name为训练语料的路径

def model_train(train_file_name, save_model_name): # 模型训练，生成词向量    
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences = word2vec.Text8Corpus(train_file_name)  # 加载语料
    #训练参数说明：https://blog.csdn.net/u011748542/article/details/85880852
    model = gensim.models.Word2Vec(sentences, size=embedding_dim,window=window,min_count=min_count)  # 训练skip-gram模型; 默认window=5,忽略出现次  数小于min_count的词
    model.save(save_model_name)
    model.wv.save_word2vec_format(save_model_name + ".bin", binary=True)   # 以二进制类型保存模型以便重用
if __name__=="__main__":
    model_train(train_file_name, save_model_name)
