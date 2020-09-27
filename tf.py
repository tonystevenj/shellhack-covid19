from collections import Counter
def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    # TODO: Count the number of occurences of each word in s
    from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS as esw
    myStopWords = ['00', '00a', '00am', '00pm', '01', '04', '050d_xior1npcuwkbivaq', '0530', '06', '0600', '0630',
                   '07','','#coronavirus','case',
                   '09', '10', '100', '1000', '105', '10a', '10am', '11', '110', '115', '11am', '11dollars', '11pm',
                   '12',
                   '120', '1230', '12oz', '12p', '12pm', '13', '15', '15a', '15ish', '16', '17', '18', '19', '1950',
                   '1hour', '1hr', '1hr1', '1ish', '1pm', '1st', '20', '200', '2007', '2008', '2009', '2010',
                   '2011',
                   '20min', '21', '22', '24', '25', '26', '27', '28', '2hr', '2nd', '2oz', '2pm', '2x', '30', '300',
                   '300th', '30am', '30ish', '30mins', '30p', '30pm', '30s', '31', '35', '35mins', '37', '38', '3d',
                   '3oz',
                   '3rd', '3secs', '40', '40a', '40mins', '45', '45a', '45am', '45min', '47', '48', '480', '4oz',
                   '4pm',
                   '4star', '4x', '50', '500', '50s', '51cents', '51st', '53', '55am', '5hrs', '5jzlbw7os2kcja',
                   '5th',
                   '60', '600', '630', '645am', '6am', '6oz', '6zwwyxzvspp83yplkggr5g', '730', '745', '75', '7am',
                   '7items',
                   '7th', '801', '815', '85', '8am', '90', '930', '945', '95', '97', '98', '99', '9am',
                   '_shdjvyidwqmo9lphwsrcg', 'aaaahing', 'aah']
    myStopWords2 = ['05', '101', '10min', '128', '14', '15min', '15pm', '16th', '1800s', '1980', '1985', '1988',
                    '1red',
                    '2006', '2014', '2015', '2017', '2018', '23', '23rd', '29', '32', '3pm', '3x', '3year', '40th',
                    '42',
                    '44', '44oz', '44th', '45mins', '45pm', '49', '4b', '4th', '50pm', '55', '56th', '59', '5and',
                    '5pm',
                    '63', '65', '69', '72', '77', '80', '80s', '83', '845', '8pm', '8th', '90s', '9pm', '9th',
                    '_____',
                    'a1']
    stopWords = myStopWords + list(myStopWords2) + list(esw)
    stopset = set(stopWords)

    ws=s.split(' ')
    dt={}
    total = 0
    for w in ws:
        # dt[w]=dt.setdefault(w,0)+1
        # total+=1
        w=w.lower()
        if w not in stopset:
            dt[w]=dt.setdefault(w,0)+1
            total+=1
    # 处理权重为占比，而不是单词个数
    for w in dt:
        # print(w)
        dt[w] = dt[w]/total
    sort_s = sorted(Counter(dt).most_common(), key=lambda x: (-x[1], x[0]))
    top_n=[]

    for i in range(n):
        if i==len(sort_s):
            break
        else:
            top_n.append(sort_s[i])
    return top_n


# print (count_words("cat bat mat cat bat cat", 10))
# print (count_words("betty bought a bit of butter but the butter was bitter", 10))
#
