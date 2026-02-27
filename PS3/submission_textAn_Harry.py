'''
This is the submission template for the students
'''
# Place your imports here
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation as LDA


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
    def analyzer(self, txt, stem=True):
        '''
        (Optional)
        You may want to implement a function to process the textual data to streamline your answers for this homework
        '''
        analyzer = CountVectorizer(stop_words = 'english').build_analyzer()
        tokens = analyzer(txt)

        if stem:
            stemmer = SnowballStemmer('english')
            return [stemmer.stem(wrd) for wrd in tokens]    
            
        return tokens
    
    def q1a(self, filename: str):
        """
        now answer this question: 
        How many articles are there in the JSON file named "filename"?
        """

        fp = open(filename, 'r', encoding = 'utf-8')
        self.q1_data = json.load(fp)

        # please make sure your return value has the same data type as the following sample return
        return len(self.q1_data['Items'])

    def q1b(self, filename: str):
        """
        now answer this question: 
        How many of articles in the JSON file named "filename" are in English?
        """

        # please make sure your return value has the same data type as the following sample return
        enCount = 0
        for el in self.q1_data['Items']:
            if el['data']['language'] == 'en':
                enCount += 1
        return enCount

    def q1c(self, filename: str):
        """
        now answer this question: 
        In the JSON file named "filename", how many English-language articles in this month mention any of the five companies: C.N, JPM.N, BAC.N, GS.N and MS.N?
        """

        # please make sure your return value has the same data type as the following sample return
        return len([el['data']['headline'] for el in self.q1_data['Items'] if el['data']['language'] == 'en' and \
                 any(cd in el['data']['subjects'] for cd in ['R:C.N', 'R:JPM.N', 'R:BAC.N', 'R:GS.N', 'R:MS.N'])])

    def q1d(self, filename: str):
        """
        this question is manually graded
        provide your codes for the computation here
        """
        data = [el['data'] for el in self.q1_data['Items'] if el['data']['language'] == 'en' and \
                 'R:LEH.N' in el['data']['subjects'] and len(el['data']['body']) > 1800]
        
        usedAltIds = set()
        articles = list()
        for el in data:
            altid = el['altId']

            if altid not in usedAltIds:
                articles.append(el)
                usedAltIds.add(altid)

        sorted_articles = sorted(articles, key=lambda x: x['versionCreated'])
        
        return [article['headline'] for article in sorted_articles[:5]]
    '''
        Please paster the headlines of the first five articles here for manual grading (any format is okay as long as it is clearly written)

        Answer:
        - 'PRESS DIGEST - South Korean newspapers - Sept 1'
        - 'UPDATE 1-Lehman in talks with KDB to raise $6 bln-Telegraph'
        - 'TAKE-A-LOOK-Ongoing major Asia M&A deals'
        - 'PRESS DIGEST - South Korean newspapers - Sept 2'
        - 'UPDATE 1-KDB confirms talks with Lehman on possible deal'

        '''
    def q2a(self, filename: str):
        """
        now answer this question: 
        In the JSON file named "filename", how many EM articles are there in the JSON file named "filename"?
        """

        fp = open(filename, 'r', encoding = 'utf-8')
        data = json.load(fp)

        filtered_data = [el['data'] for el in data['Items'] if el['data']['language'] == 'en' and \
                 any(cd in el['data']['subjects'] for cd in ['N2:BR', 'N2:TR', 'N2:MX', 'N2:ZA'])]
        
        self._em_data = filtered_data

        # please make sure your return value has the same data type as the following sample return
        return len(self._em_data)

    
    def q2b(self, filename: str):
        """
        this question is manually graded
        provide your codes for the computation here
        """
        cv = CountVectorizer(analyzer=self.analyzer)
        dtm_raw = cv.fit_transform([el['body'] for el in self._em_data])

        self._dtm_raw = dtm_raw
        self.cv = cv

        freq = dtm_raw.sum(axis=0)
        named_freq = [(wrd, freq[0,idx]) for wrd, idx in self.cv.vocabulary_.items()]
        named_freq = sorted(named_freq, key = lambda xx: xx[1], reverse=True)

        self._tokenized_freq = named_freq

        return [wrd[0] for wrd in self._tokenized_freq[:25]]
        '''
        Please paste the the 25 most frequently occurring tokens (any format is okay as long as it is clearly written)

        Answer:
        ['reuter', 'said', 'com', 'percent', 'market', 'price', 'year', 'gold', 'sept', 'report', 'bank', 'news', 'pct', 'keyword', 
        'net', '10', 'south', 'messag', 'africa', 'new', 'rate', '11', 'oil', 'mexico', 'trade']
        '''

    
    def q2c(self, filename: str):
        """
        this question is manually graded
        provide your codes for the computation here
        """
        top_100_token_vals = [wrd[1] for wrd in self._tokenized_freq[:100]]

        return top_100_token_vals/np.sum(top_100_token_vals)
    '''
        Please paste the fraction of occurrences here (any format is okay as long as it is clearly written)

        Answer:
        [0.07316573 0.04178746 0.03220883 0.03198756 0.0243394  0.02119677
 0.01918291 0.01777193 0.01729413 0.01688687 0.01516162 0.01460364
 0.0142028  0.01387891 0.01354861 0.0134941  0.01281106 0.01241021
 0.01238456 0.01226591 0.01216329 0.01154438 0.01072665 0.01069138
 0.01035467 0.01011416 0.01006927 0.00993458 0.00973576 0.00958504
 0.00953374 0.00939584 0.0093285  0.00921626 0.00895652 0.00872563
 0.00840174 0.00805221 0.00803297 0.00796242 0.00791752 0.00791432
 0.00788545 0.00786301 0.00770267 0.00751026 0.00750705 0.00725372
 0.00721524 0.00720883 0.0071992  0.00717355 0.00706773 0.00696832
 0.00696832 0.0069619  0.00693946 0.0069138  0.00673422 0.0067214
 0.0067214  0.00670857 0.00668933 0.00659633 0.00658992 0.00649371
 0.00640393 0.00631734 0.00620511 0.00617945 0.00614097 0.0060608
 0.00605759 0.00597422 0.00597422 0.00597101 0.00586198 0.00584595
 0.00583953 0.00576898 0.00574012 0.00567278 0.00547717 0.00538096
 0.00538096 0.00537134 0.0053489  0.00534248 0.00533928 0.00533928
 0.00533286 0.00533286 0.005304   0.00529117 0.00524949 0.00524307
 0.00520139 0.00518535 0.00517894 0.00515328]

        '''
    
    
    def q2d(self, filename: str):
        """
        this question is manually graded
        provide your codes for the computation here
        """
        freqser = pd.Series([wrd[1] for wrd in self._tokenized_freq])

        fig, axs = plt.subplots()
        (freqser / freqser.sum()).plot(ax = axs, title='Word frequency')
        plt.savefig('q2d.png', bbox_inches='tight')

        return 'Nothing to return here. Remember to upload your graph'

    def q2_get_percentages(self, data, lm_dict_file: str, low_limit = 1, high_limit = 1E12):
        wordfile = pd.read_csv(lm_dict_file)
        wordfile.Word = wordfile.Word.str.lower()
        negative_words = wordfile.loc[wordfile['Negative'] > 0, 'Word'].tolist()
        positive_words = wordfile.loc[wordfile['Positive'] > 0, 'Word'].tolist()

        stemmer = SnowballStemmer('english')
        neg_stems = set([stemmer.stem(word) for word in negative_words])
        pos_stems = set([stemmer.stem(word) for word in positive_words])

        headline_list = list()
        pos_perc = list()
        neg_perc = list()

        for el in data:
            tokens = self.analyzer(el['body'])
            t_i = len(tokens)

            if t_i == 0:
                continue
            if not (low_limit <= t_i <= high_limit):
                continue

            p_i = 0
            n_i = 0
            for word in tokens:
                if word in pos_stems:
                    p_i += 1

                if word in neg_stems:
                    n_i += 1
            headline_list.append(el['headline'])
            pos_perc.append(p_i / t_i)
            neg_perc.append(n_i / t_i)
        d = {'headline': headline_list, 'pos_perc': pos_perc, 'neg_perc': neg_perc}
        df = pd.DataFrame(data = d)
        self.df = df
        return self.df
    
    def q2e(self, filename: str, lm_dict_file: str):
        """
        this question is manually graded
        provide your codes for the computation here
        """
        df = self.q2_get_percentages(self._em_data, lm_dict_file)
        pos_perc = df['pos_perc']
        neg_perc = df['neg_perc'] 
        var_p = np.var(pos_perc, ddof = 1)
        var_n = np.var(neg_perc, ddof = 1)
        cov_pn = np.cov(pos_perc, neg_perc)[0, 1]

        var_s = var_p + var_n - 2 * cov_pn

        pos_var_frac = var_p / var_s
        neg_var_frac = var_n / var_s


        return pos_var_frac, neg_var_frac
        '''
        Please paste the fraction of total variance represented by the positive and negative words (any format is okay as long as it is clearly written)

        0.18794262994644081, 0.999055837376546

        '''
   
    
    def q2f(self, filename: str, lm_dict_file: str):
        """
        this question is manually graded
        provide your codes for the computation here
        """
        df = self.q2_get_percentages(self._em_data, lm_dict_file, low_limit = 300, high_limit = 500)

        top_5_pos = df.sort_values(by='pos_perc', ascending=False).head(5)['headline'].tolist()
        top_5_neg = df.sort_values(by='neg_perc', ascending=False).head(5)['headline'].tolist()

        return top_5_pos, top_5_neg
        '''
        Please paste the headlines of the five most negative (bottom) and most positive (top) sentiment articles (any format is okay as long as it is clearly written)

        Answer:
        five most positive: 
        ['WRAPUP 1-Soccer-UEFA Cup relief for Milan and Ancelotti', "TEXT-S&P: Banco BAC San Jose 'BB/B' rtgs affirmed; outlk stble", 
        "TEXT-S&P release on Brazil's Magnesita Refratarios", "FUND VIEW-Templeton's Mobius sees S.Africa growth", 'Motor racing-Hamilton punishment whips up another F1 storm'], 
        ["FACTBOX-S.Africa's Zuma seeks dismissal of graft charges", 'UPDATE 2-Lula suspends Brazil spy chiefs over phone taps', 'INSTANT VIEW-Reaction to dismissal of case against Zuma', 
        'Media-government tensions flare in Turkey', 'Media-government tensions flare in Turkey']  '''

    def q3a(self, filename: str):
        """
        now answer this question: 
        How many articles did you locate that satisfy the search criteria in the JSON file named "filename"?
        """
        fp = open(filename, 'r', encoding = 'utf-8')
        data = json.load(fp)

        filtered_data = [el['data'] for el in data['Items'] if el['data']['language'] == 'en' and \
                 any(cd in el['data']['body'].lower() for cd in ['covid', 'coronavirus'])]
        
        self._covid_data = filtered_data
        return len(self._covid_data)
    
    
    def q3b(self, filename: str):
        """
        this question is manually graded
        provide your codes for the computation here
        """
        cv = CountVectorizer(analyzer=self.analyzer)
        dtm_raw = cv.fit_transform([el['body'] for el in self._covid_data])

        self._dtm_raw_q3 = dtm_raw
        self.cv_q3 = cv

        freq = self._dtm_raw_q3.sum(axis=0)
        named_freq = [(wrd, freq[0,idx]) for wrd, idx in self.cv_q3.vocabulary_.items()]
        named_freq = sorted(named_freq, key = lambda xx: xx[1], reverse=True)

        self._tokenized_freq_q3 = named_freq

        top_100_words = [wrd[0] for wrd in self._tokenized_freq_q3[:100]]
        btm_100_words = [wrd[0] for wrd in self._tokenized_freq_q3[-100:]]

        
        return top_100_words, btm_100_words
    '''
        Please paste the 100 most and least frequently used words (any format is okay as long as it is clearly written)

        A sample answer may look like
        100 most used words:
        ['news', 'rate', 'market', 'compani', 'page', 'bank', 'global', 'reuter', 'com', 'commod', 'thomsonreut', 'report', 'china', 
        'energi', 'new', 'gas', 'africa', 'data', 'north', 'america', 'european', 'world', 'coronavirus', 'wealth', 'central', 'basic', 
        'fitch', 'stock', 'oil', 'econom', 'https', 'phone', 'price', 'equiti', 'inform', 'help', 'financi', 'covid', 'index', 'deal', 
        'gb', 'industri', 'economi', '19', 'bond', 'crude', 'metal', 'said', 'cen', 'australia', 'asian', 'live', 'invest', 'brazil', 
        'servic', 'ftse', 'canada', 'indic', 'group', 'say', 'power', 'debt', 'emerg', 'britain', 'year', 'retail', 'health', 'gro', 
        'level', 'need', 'exchang', 'latam', 'foreign', 'media', 'cn', 'visit', 'german', 'case', 'region', 'consum', 'sport', 'franc', 
        'cp', 'view', 'mtl', 'access', 'meast', 'zealand', 'latest', 'east', 'good', 'technolog', 'incom', 'depend', 'money', 
        'breakingview', 'french', 'emrg', 'break', 'entertain'] 
        ['9936', '3754', 'apocalypt', 'congratulatori', 'downright', 'waitr', 'wtrh', 'boatload', '301084840', '10126762', 'autofin', 
        'lucian', 'nl1n2e61z0', '65474vas0', '65474vap6', '65474vaq4', '10114200', '10099430', '963961', '2vxsjcq', 'nfit4fyf8c', 'agf', '3577', 
        '3566', '30293wae2', '30293wag7', '30293waa0', '6577', '68985', '00325', '3089', 'etruenorth', '1ub', 'australianz', '1906456', 'rainmak', 
        'nl4n24a0rl', 'vanderzeil', 'jarden', 'nl8n2410i4', 'ngnxbvcxm9', '38fwgth', '5860070', '2398', 'nl8n2e77sn', 'valetodo', 'belaluh', 'sequin', 
        'npnv9nwba', 'midmarket', 'broadsoft', 'intrado', 'polycom', 'ngnxc5drn', '2vvmkxs', 'np6n2di006', 'abrade', 'smartpost', 'segement', 'nbwb2vylja', 
        '38fyvs3', 'nl1n2e71z', 'nl1n2du2t4', 'unhind', 'hov3', 'mmra', 'rctc', 'chokepoint', '10127186', 'neq9cclmsa', '38ei1ya', '8067490824', 'nl8n2e7859', 
        'sekin', 'nl8n2cw44n', 'nl4n2c92rd', 'nl8n2d8360', '8091', 'ns0n2d102e', 'nl8n2e7508', '2258', '453m', '38dwomg', 'transferwis', 'nl1n2e72yz', 'calio', 
        'nl1n2e733r', 'ede', 'brie', 'cu0', '1779', '3gdauhh', 'nl1n2e734w', 'horen', 'dransfield', 'nasxbg91l', 'nl4n2e759x', 'nl1n2e732z', 'joust', 'franziska']
        '''
    
    
    def q3c(self, filename: str):
        """
        this question is manually graded
        provide your codes for the computation here
        """

        Nwrds = 1000
        freq = self._dtm_raw_q3.sum(axis=0)
        top_words = [(wrd, idx, freq[0,idx]) for wrd, idx in self.cv_q3.vocabulary_.items()]
        top_words = sorted(top_words, key = lambda xx: xx[2], reverse=True)[:Nwrds]
        top_idx = [el[1] for el in top_words]
        words_ordered = [wrd for wrd,_,_ in top_words]
        lda = LDA(n_components=10, learning_method='batch', max_iter=50)
        dtm_small = self._dtm_raw_q3[:, top_idx]
        lda.fit(dtm_small)
        topics = []
        for ii in range(len(lda.components_)):
            tot_refs = sum(lda.components_[ii])
            topic =[(wrd, refs/tot_refs) for wrd, refs in zip(words_ordered, lda.components_[ii])]
            topic = sorted(topic, key = lambda xx: xx[1], reverse=True)
            top_20_words = [t[0] for t in topic[:20]]
            print(f"top 20 words in topic {ii}:\n {top_20_words}\n\n")
        
        return topics
    '''
        Please paste the list of the 20 words in each topic that have the highest topic-word probability in the return value (any format is okay as long as it is clearly written)
top 20 words in topic 0:
 ['said', 'reuter', 'coronavirus', 'report', 'june', 'state', 'com', 'new', 'edit', 'thomsonreut', 'case', 'countri', 'peopl', 'govern', 'year', 'unit', 'presid', 'death', 'pandem', 'citi']


top 20 words in topic 1:
 ['news', 'market', 'oil', 'code', 'commod', 'report', 'guid', 'gas', 'energi', 'nymex', 'metal', 'page', 'brent', 'crude', 'global', 'data', 'compani', 'european', 'gro', 'paper']


top 20 words in topic 2:
 ['market', 'price', 'stock', 'week', 'year', 'reuter', 'dollar', 'month', 'coronavirus', 'june', 'oil', 'report', 'trade', 'econom', 'index', 'said', 'rise', 'gain', 'high', 'data']


top 20 words in topic 3:
 ['news', 'page', 'market', 'compani', 'global', 'commod', 'bank', 'africa', 'north', 'america', 'wealth', 'basic', 'energi', 'world', 'gas', 'phone', 'reuter', 'rate', 'thomsonreut', 'ftse']


top 20 words in topic 4:
 ['covid', '19', 'reuter', 'com', 'test', 'vaccin', 'link', 'https', 'thomsonreut', 'drug', 'patient', 'sport', 'trial', 'leagu', 'player', 'season', 'team', 'http', 'studi', 'game']


top 20 words in topic 5:
 ['bank', 'rate', 'news', 'diari', 'central', 'int', 'market', 'fed', 'poll', 'ecb', 'http', 'global', 'compani', 'www', 'index', 'cen', 'reuter', 'event', 'page', 'key']


top 20 words in topic 6:
 ['rate', 'fitch', 'report', 'credit', 'com', 'www', 'inform', 'fitchrat', 'secur', 'https', 'issuer', 'site', 'issu', 'avail', '2020', 'provid', 'term', 'case', 'expect', 'risk']


top 20 words in topic 7:
 ['news', 'compani', 'page', 'market', 'global', 'thomsonreut', 'bank', 'commod', 'econom', 'crude', 'european', 'data', 'asian', 'live', 'equiti', 'cen', 'central', 'help', 'indic', 'ftse']


top 20 words in topic 8:
 ['news', 'china', 'market', 'report', 'page', 'uk', 'hong', 'kong', 'gb', 'stock', 'equiti', 'cn', 'compani', 'global', 'commod', 'index', 'bank', 'britain', 'diari', 'hk']


top 20 words in topic 9:
 ['compani', 'billion', 'bank', 'sale', 'year', 'share', 'reuter', 'million', 'com', 'euro', 'busi', 'expect', 'plan', 'june', 'fund', 'thomsonreut', 'sourc', 'european', 'pandem', 'group']
    '''
'''
Please use the following codes to test your program locally
'''
if __name__ == '__main__':
    file_q1q2 = 'News.RTRS.200809.0214.txt'
    file_q3 = 'News.RTRS.202006.0214.txt'
    lm_dict_file = 'Loughran-McDonald_MasterDictionary_1993-2024.csv'
    
    calc = hm_textAn()
    print('Q1 (a):')
    num1 = calc.q1a(file_q1q2)
    print('generic case:', num1)

    print('Q1 (b):')
    num1 = calc.q1b(file_q1q2)
    print('generic case:', num1)

    print('Q1 (c):')
    num1 = calc.q1c(file_q1q2)
    print('generic case:', num1)

    print('Q1 (d):')
    num1 = calc.q1d(file_q1q2)
    print('generic case:', num1)

    print('Q2 (a):')
    num1 = calc.q2a(file_q1q2)
    print('generic case:', num1)
    
    print('Q2 (b):')
    num1 = calc.q2b(file_q1q2)
    print('generic case:', num1)

    print('Q2 (c):')
    num1 = calc.q2c(file_q1q2)
    print('generic case:', num1)

    print('Q2 (d):')
    num1 = calc.q2d(file_q1q2)
    print('generic case:', num1)

    print('Q2 (e):')
    num1 = calc.q2e(file_q1q2, lm_dict_file)
    print('generic case:', num1)

    print('Q2 (f):')
    num1 = calc.q2f(file_q1q2, lm_dict_file)
    print('generic case:', num1)

    print('Q3 (a):')
    num1 = calc.q3a(file_q3)
    print(num1)

    print('Q3 (b):')
    num1 = calc.q3b(file_q3)
    print(num1)

    print('Q3 (c):')
    num1 = calc.q3c(file_q3)
    print(num1)

