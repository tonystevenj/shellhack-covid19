import json
import os
import tf

def data_reader():
    dic = {}
    filePath = 'data/'
    count = 0
    # filePath = 'F:\pycharm-workspace\shellhack-covid-19\data'
    list = os.listdir(filePath)
    # print("哈哈",len(list))
    for name in list:
        day = name.split(" ")[0]
        with open(filePath + name, 'r') as f:
            data = json.load(f)
            if day not in dic:
                dic[day] = ""
            # print(len(data),count)
            count += 1
            for i in range(len(data)):
                dic[day] = dic[day] + data[i]['CONTENT']
    return dic
    # print(dic["2020-01-20"])
    # print(len(dic))
    # for key in dic:
    #     print(key)

def return_tf():
    dic_op =  {}
    day_review = data_reader()
    for day in day_review:
        dic_op[day]=tf.count_words(day_review[day],10)
    return dic_op
# main：
if __name__ == '__main__':
    day_review = data_reader()
    for day in day_review:
        print(day,tf.count_words(day_review[day],10))