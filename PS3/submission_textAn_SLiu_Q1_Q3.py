#!/apps/anaconda3/bin/python
'''
This is the submission template for the students
'''
# Place your imports here
import json
import sys
import os
import re
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation as LDA
from collections import Counter
import pandas as pd
import numpy as np

class CalculatorException(Exception):
    """A class to throw if you come across incorrect syntax or other issues"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class hm_textAn(object):
    """
    This is the class you need to finish. 
    """
    def analyzer(self, filename, stem=True):
        '''
        (Optional)
        You may want to implement a function to process the textual data to streamline your answers for this homework
        '''

        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    
    def q1a(self, filename: str):
        """
        now answer this question: 
        How many articles are there in the JSON file named "filename"?
        """
        data = self.analyzer(filename)
        items = data.get("Items", [])

        # please make sure your return value has the same data type as the following sample return
        return len(items)

    def q1b(self, filename: str):
        """
        now answer this question: 
        How many of articles in the JSON file named "filename" are in English?
        """
        data = self.analyzer(filename)
        items = data.get("Items", [])

        total_english = 0
        for item in items:
            article_data = item.get("data", {})
            lang = article_data.get("language")
            if lang == "en":
                total_english += 1

        return total_english

    def q1c(self, filename: str):
        """
        now answer this question: 
        In the JSON file named "filename", how many English-language articles in this month mention any of the five companies: C.N, JPM.N, BAC.N, GS.N and MS.N?
        """
        data = self.analyzer(filename)
        items = data.get("Items", [])
        target_companies = {"C.N", "JPM.N", "BAC.N", "GS.N", "MS.N"}
        english_with_companies = 0
        for item in items:
            article_data = item.get("data", {})
            lang = article_data.get("language")
            if lang == "en":
                subjects = set(article_data.get("subjects", []))
                for subject in subjects:
                    if any(company in subject for company in target_companies):
                        english_with_companies += 1
                        break

        # please make sure your return value has the same data type as the following sample return
        return english_with_companies

    def q1d(self, filename):
        """
        this question is manually graded
        provide your codes for the computation here
        """

        first_in_chain_by_altid = {}

        data = self.analyzer(filename)

        for item in data.get("Items", []):
            d = item.get("data", {})

            if d.get("language") != "en":
                continue

            body = d.get("body", "")
            if len(body) < 1800:
                continue

            subjects = d.get("subjects", [])
            if not any("LEH.N" in s for s in subjects):
                continue

            alt_id = d.get("altId")
            vc = d.get("versionCreated")
            headline = d.get("headline")

            if not alt_id or not vc or headline is None:
                continue

            prev = first_in_chain_by_altid.get(alt_id)
            if prev is None or vc < prev["versionCreated"]:
                first_in_chain_by_altid[alt_id] = {
                    "altId": alt_id,
                    "versionCreated": vc,
                    "headline": headline,
                }

        sorted_firsts = sorted(first_in_chain_by_altid.values(), key=lambda x: x["versionCreated"])
        return '''
        Headlines
        'PRESS DIGEST - South Korean newspapers - Sept 1'
        'UPDATE 1-Lehman in talks with KDB to raise $6 bln-Telegraph'
        'TAKE-A-LOOK-Ongoing major Asia M&A deals'
        'PRESS DIGEST - South Korean newspapers - Sept 2'
        'UPDATE 1-KDB confirms talks with Lehman on possible deal'
        '''

    def q2_getdata(self, data):
        '''
        (Optional)
        You may want to implement a function that loads the EM articles in the loaded JSON file to help streamline your answers for Q2
        '''

        return [1, 2, 3]
    
    def q2a(self, filename: str):
        """
        now answer this question: 
        In the JSON file named "filename", how many EM articles are there in the JSON file named "filename"?
        """

        # please make sure your return value has the same data type as the following sample return
        return 0

    
    def q2b(self, filename: str):
        """
        this question is manually graded
        provide your codes for the computation here
        """

        return '''
        Please paste the the 25 most frequently occurring tokens (any format is okay as long as it is clearly written)

        A sample answer may look like
        [token1, token2, ..., token25]

        '''

    
    def q2c(self, filename: str):
        """
        this question is manually graded
        provide your codes for the computation here
        """

        return '''
        Please paste the fraction of occurrences here (any format is okay as long as it is clearly written)

        A sample answer may look like
        [freq2, freq2, ..., freq100]

        '''
    
    
    def q2d(self, filename: str):
        """
        this question is manually graded
        provide your codes for the computation here
        """

        return 'Nothing to return here. Remember to upload your graph'

    
    
    def q2e(self, filename: str, lm_dict_file: str):
        """
        this question is manually graded
        provide your codes for the computation here
        """

        return '''
        Please paste the fraction of total variance represented by the positive and negative words (any format is okay as long as it is clearly written)

        A sample answer may look like
        [pos_var_percentage, neg_var_percentage]

        '''

   
    
    def q2f(self, filename: str, lm_dict_file: str):
        """
        this question is manually graded
        provide your codes for the computation here
        """

        return '''
        Please paste the headlines of the five most negative (bottom) and most positive (top) sentiment articles (any format is okay as long as it is clearly written)

        A sample answer may look like
        five most positive: 
        [headline1, headline2, headline3, headline4, headline5]
        five most negative: 
        [headline1, headline2, headline3, headline4, headline5]

        '''
    
    
    def q3_getdata(self, data):
        '''
        (Optional)
        You may want to implement a function that loads the COVID-related articles in the loaded JSON file to help streamline your answers for Q2
        '''

        results = []

        for item in data.get("Items", []):
            d = item.get("data", {})

            if d.get("language") != "en":
                continue

            body = d.get("body", "")
            body_lower = body.lower()
            d["body"] = body_lower

            if "covid" in d["body"] or "coronavirus" in d["body"]:
                results.append(d)
        
        stemmer = SnowballStemmer("english")
        analyzer = CountVectorizer(stop_words="english").build_analyzer()
        
        dtm_rows = []
        for item in results:
            item["body"] = [stemmer.stem(el) for el in analyzer(item["body"])]
            dtm_row = Counter(item["body"])
            data_as_list = [(item["id"], wrd, cnt) for wrd, cnt in dtm_row.items()]
            dtm_rows.extend(data_as_list)
        df = pd.DataFrame(dtm_rows, columns=["Id", "Word", "Count"])

        return results, df


    def q3a(self, filename: str):
        """
        now answer this question: 
        How many articles did you locate that satisfy the search criteria in the JSON file named "filename"?
        """
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        articles, _ = self.q3_getdata(data)

        # please make sure your return value has the same data type as the following sample return
        return len(articles)
    
    
    def q3b(self, filename: str):
        """
        this question is manually graded
        provide your codes for the computation here
        """
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        _, dtm = self.q3_getdata(data)

        word_freq = dtm.groupby("Word", as_index=False)["Count"].sum().rename(columns={"Count": "TotalCount"})

        most_frequent = word_freq.sort_values("TotalCount", ascending=False).head(100)
        least_frequent = word_freq.sort_values("TotalCount", ascending=True).head(100)

        return '''
        Top 100 most frequent words:
        ['news', 'rate', 'market', 'compani', 'page', 'bank', 'global', 'reuter', 'com', 'commod', 'thomsonreut', 'report', 'china', 'energi', 'new', 'gas', 'africa', 'data', 'north', 'america', 'european', 'world', 'coronavirus', 'wealth', 'central', 'basic', 'fitch', 'stock', 'oil', 'econom', 'https', 'phone', 'price', 'equiti', 'inform', 'help', 'financi', 'covid', 'index', 'deal', 'gb', 'industri', 'economi', '19', 'bond', 'crude', 'metal', 'said', 'cen', 'australia', 'asian', 'live', 'invest', 'brazil', 'servic', 'ftse', 'canada', 'indic', 'group', 'say', 'power', 'debt', 'emerg', 'britain', 'year', 'retail', 'health', 'gro', 'level', 'need', 'exchang', 'latam', 'foreign', 'media', 'cn', 'visit', 'german', 'case', 'region', 'consum', 'sport', 'franc', 'cp', 'view', 'mtl', 'access', 'meast', 'zealand', 'latest', 'east', 'good', 'technolog', 'incom', 'depend', 'money', 'breakingview', 'french', 'emrg', 'break', 'entertain']

        Top 100 least frequent words:
        ['0001140361', '000114036120014016', '000119312520157158', '000119312520174218', '000119312520174647', 'цен', 'цветковой', 'цветкова', 'хотя', 'фоне', 'фирмы', 'факт', '000089914020000292', '000063', '000033', 'явке', '00119taa2', 'участия', 'этом', '000110465920069226', '000104746920003846', '000104746920003828', '000104746920003622', 'четырех', 'чем', '000110465920076855', '000110465920074139', '000163720720000033', '0001637207', '000162828020008792', '000155837020007429', 'ﬁnancial', 'уровне', 'урн', 'уникальные', 'уже', 'угощений', 'трех', 'того', 'тогда', 'человек', 'частные', '000366ac8', '000366ab0', '000366aa2', '00025', '000921', '000831', 'idr500', 'iduskbn19q18j', 'iduna', 'эти', 'экономических', 'idnom', 'idr490', 'idr480', 'idr47', 'idr454', 'idr45', '00125', '00256dab8', '00256daa0', 'тезисы', 'установить', 'структуре', 'страну', 'стран', 'стимулировать', 'участках', '002468', '002352', '000e', '000bpd', '002024', '00201116281191', '002007', '00185', 'idr607', 'idr60', 'idr6', '002030', '00325', '002928', '00285', '002603', '00256dac6', 'срока', 'срок', 'среди', 'те', 'твиттере', 'там', 'так', 'тhere', 'считаю', 'стыдно', 'idr35', 'idr31', 'idukl4n2du3m5', 'idukkcn1g51m4']

        '''
    
    
    def q3c(self, filename: str):
        """
        this question is manually graded
        provide your codes for the computation here
        """

        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        _, dtm = self.q3_getdata(data)

        word_totals = dtm.groupby("Word")["Count"].sum()
        top_words = word_totals.nlargest(1000).index

        dtm_small_df = dtm[dtm["Word"].isin(top_words)]

        dtm_matrix = dtm_small_df.pivot_table(
            index="Id",
            columns="Word",
            values="Count",
            fill_value=0
        )
        vocab = dtm_matrix.columns.to_numpy()
        dtm_small = dtm_matrix.to_numpy()
        # dtm_small = dtm_small[:5000]

        lda = LDA(n_components=10, learning_method="batch", max_iter=50)
        lda.fit(dtm_small)

        topic_word_probs = lda.components_ / lda.components_.sum(axis=1, keepdims=True)

        for k in range(10):
            print("\nTopic", k)
            top20 = np.argsort(topic_word_probs[k])[-20:][::-1]
            # print(vocab[top20].tolist())
        
        return '''
        Topic 0
        ['market', 'stock', 'dollar', 'week', 'index', 'gain', 'econom', 'high', 'investor', 'trade', 'rise', 'recoveri', 'coronavirus', 'risk', 'rs', 'tmsnrt', 'fed', 'bond', 'usd', '10']

        Topic 1
        ['news', 'market', 'code', 'oil', 'commod', 'report', 'guid', 'gas', 'energi', 'metal', 'nymex', 'page', 'brent', 'crude', 'global', 'data', 'compani', 'european', 'gro', 'paper']

        Topic 2
        ['said', 'reuter', 'coronavirus', 'report', 'com', 'state', 'thomsonreut', 'new', 'case', '19', 'covid', 'june', 'peopl', 'edit', 'countri', 'govern', 'health', 'death', 'test', 'pandem']

        Topic 3
        ['soccer', 'june', 'bank', 'gmt', 'sport', 'juli', 'leagu', 'meet', 'player', '19', 'season', 'team', 'unit', 'polici', 'game', 'restart', 'race', 'http', 'play', 'hold']

        Topic 4
        ['china', 'report', 'hong', 'kong', 'uk', 'stock', 'gb', 'market', 'hk', 'equiti', 'taiwan', 'britain', 'london', 'chines', 'index', 'news', 'outlook', 'press', 'tw', 'eu']

        Topic 5
        ['news', 'page', 'compani', 'market', 'global', 'commod', 'bank', 'thomsonreut', 'africa', 'america', 'north', 'wealth', 'energi', 'basic', 'gas', 'world', 'reuter', 'phone', 'com', 'ftse']

        Topic 6
        ['said', 'reuter', 'year', 'june', 'com', 'price', 'oil', 'month', 'coronavirus', 'thomsonreut', 'report', 'million', 'april', 'demand', 'expect', 'edit', 'economi', 'cut', 'net', 'billion']

        Topic 7
        ['bank', 'news', 'rate', 'diari', 'central', 'int', 'market', 'poll', 'fed', 'ecb', 'compani', 'global', 'page', 'http', 'index', 'reuter', 'www', 'cen', 'key', 'european']

        Topic 8
        ['rate', 'fitch', 'credit', 'report', 'com', 'www', 'inform', 'fitchrat', 'secur', 'https', 'issuer', 'site', 'issu', 'avail', '2020', 'provid', 'term', 'case', 'expect', 'risk']

        Topic 9
        ['compani', 'billion', 'share', 'sale', 'reuter', 'com', 'euro', 'plan', 'sourc', 'busi', 'fund', 'deal', 'covid', '19', 'group', 'thomsonreut', 'say', 'million', 'firm', 'airlin']

        '''
    

    def q3d(self, filename: str):
        """
        this question is manually graded
        provide your codes for the computation here
        """

        return 'Nothing to return here. Remember to upload your graph'
    

    def q3e(self):
        return '''
        this question is manually graded
        type your response here
        '''


    def q3f(self):
        """
        this question is manually graded
        provide your codes for the analysis here
        """
        return '''
        type your response here
        '''

'''
Please use the following codes to test your program locally
'''
if __name__ == '__main__':
    calc = hm_textAn()
    file_q1q2 = 'q2.json.txt'
    file_q3 = 'q3.json.txt'

    file_q1q2 = './News.RTRS.200809.0214.txt'
    file_q3 = './News.RTRS.202006.0214.txt'
    # print('Q1 (a):')
    # num1 = calc.q1a(file_q1q2)
    # print('generic case:', num1)

    # print('Q1 (b):')
    # num1 = calc.q1b(file_q1q2)
    # print('generic case:', num1)

    # print('Q1 (c):')
    # num1 = calc.q1c(file_q1q2)
    # print('generic case:', num1)

    # print("Q1D")
    # print(calc.q1d(file_q1q2))

    # print('Q3 (c):')
    # num1 = calc.q3c(file_q3)
    # print('generic case:', num1)

    # print('Q3 (a):')
    # num1 = calc.q3a(file_q3)
    # print(num1)

