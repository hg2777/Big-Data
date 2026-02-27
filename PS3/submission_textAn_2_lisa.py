'''
This is the submission template for the students
'''
# Place your imports here
import json
import pandas as pd
import numpy as np
import re
import Stemmer
# from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt


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
        # art = txt.lower().strip()
        # reexp = '[(|)|\[|\]||\n|\'|-|.|;|,|?|$|-|*|+|:]+'
        # art = re.sub(reexp, ' ', art).split()
        # sw = set(stopwords.words('english'))
        # art = [el for el in art if el not in sw]
        # stemmer = Stemmer.Stemmer('english')
        # art = stemmer.stemWords(art)
        vectorizer = CountVectorizer(stop_words='english')
        base_analyzer = vectorizer.build_analyzer()
        tokens = base_analyzer(txt)
        stemmer = Stemmer.Stemmer('english')
        tokens = stemmer.stemWords(tokens)
        return tokens
        # return 'something'
        # return art
    
    def q1a(self, filename: str):
        """
        now answer this question: 
        How many articles are there in the JSON file named "filename"?
        """

        # please make sure your return value has the same data type as the following sample return
        return 0

    def q1b(self, filename: str):
        """
        now answer this question: 
        How many of articles in the JSON file named "filename" are in English?
        """

        # please make sure your return value has the same data type as the following sample return
        return 0

    def q1c(self, filename: str):
        """
        now answer this question: 
        In the JSON file named "filename", how many English-language articles in this month mention any of the five companies: C.N, JPM.N, BAC.N, GS.N and MS.N?
        """

        # please make sure your return value has the same data type as the following sample return
        return 0

    def q1d(self):
        """
        this question is manually graded
        provide your codes for the computation here
        """

        return '''
        Please paster the headlines of the first five articles here for manual grading (any format is okay as long as it is clearly written)

        A sample answer may look like
        - headline 1
        - headline 2
        - headline 3
        - headline 4
        - headline 5

        '''

    def q2_getdata(self, data):
        '''
        (Optional)
        You may want to implement a function that loads the EM articles in the loaded JSON file to help streamline your answers for Q2
        '''
        EM_CODES = {"N2:BR", "N2:TR", "N2:MX", "N2:ZA"}
        em_items = [
            el for el in data["Items"]
            if el["data"]["language"] == "en"
            and el["data"].get("body", "") != ""
            and any(code in el["data"]["subjects"] for code in EM_CODES)
        ]
        dtm_rows = []
        for art in em_items:
            doc_id = art.get("guid", "")
            tokens = self.analyzer(art["data"].get("body", ""), stem=True)
            dtm_row = {}
            for w in tokens:
                dtm_row[w] = dtm_row.get(w, 0) + 1
            dtm_rows.extend([[doc_id, w, c] for (w, c) in dtm_row.items()])
        return dtm_rows
        # return [1, 2, 3]
    
    def q2a(self, filename: str):
        """
        now answer this question: 
        In the JSON file named "filename", how many EM articles are there in the JSON file named "filename"?
        """
        EM_CODES = {"N2:BR", "N2:TR", "N2:MX", "N2:ZA"}
        with open(filename, "r", encoding="utf-8", errors="ignore") as f:
            data = json.load(f)
        count = len([
            el for el in data["Items"]
            if el["data"]["language"] == "en"
            and any(code in el["data"]["subjects"] for code in EM_CODES)
        ])
        return count
        # return 6915
        # please make sure your return value has the same data type as the following sample return
        # return 0

    
    def q2b(self, filename: str):
        """
        this question is manually graded
        provide your codes for the computation here
        """
        with open(filename, "r", encoding="utf-8", errors="ignore") as f:
            data = json.load(f)
        dtm_rows = self.q2_getdata(data)
        total = {}
        for i, w, c in dtm_rows:
            total[w] = total.get(w, 0) + c
        top25 = [w for (w, c) in sorted(total.items(), key=lambda x: x[1], reverse=True)[:25]]

        return top25
        '''
        Please paste the the 25 most frequently occurring tokens (any format is okay as long as it is clearly written)

        A sample answer may look like
        ['reuter', 'said', 'com', 'percent', 'market', 'price', 'year', 'gold', 'sept', 'report', 'bank', 'news', 'pct', 'keyword', 'net', '10', 'south', 'messag', 'africa', 'new', 'rate', '11', 'oil', 'mexico', 'trade']
        '''

    
    def q2c(self, filename: str):
        """
        this question is manually graded
        provide your codes for the computation here
        """
        with open(filename, "r", encoding="utf-8", errors="ignore") as f:
            data = json.load(f)

        dtm_rows = self.q2_getdata(data)

        total = {}
        for i, w, c in dtm_rows:
            total[w] = total.get(w, 0) + c

        sorted_tokens = sorted(total.items(), key=lambda x: x[1], reverse=True)
        top100 = sorted_tokens[:100]
        sum_top100 = sum(c for w, c in top100)
        fractions = [c / sum_top100 for w, c in top100]
        return fractions
        # return 
        """
        Please paste the fraction of occurrences here (any format is okay as long as it is clearly written)

        A sample answer may look like
        [0.073063805940277, 0.041729245056440635, 0.032163958049795854, 0.03194299895925066, 0.02430549995997118, 0.02116724041309743, 0.01915619245857017, 0.01774717796813706, 0.017270034424785845, 0.01686334160595629, 0.015140501160835802, 0.014583299975982707, 0.014183011768473301, 0.0138595788968057, 0.013529741413817948, 0.01347530221759667, 0.01279321111200064, 0.012392922904491234, 0.012367304459210632, 0.012248819149787846, 0.01214634536866544, 0.011528300376270915, 0.010711712432951725, 0.010676487070690898, 0.010340244976382995, 0.010100072051877351, 0.010055239772636297, 0.009920742934913138, 0.009722199983988471, 0.009571691617964935, 0.00952045472740373, 0.009382755584020495, 0.009315507165158915, 0.00920342646705628, 0.008944039708590186, 0.008713473701064766, 0.008390040829397165, 0.008040989512448964, 0.008021775678488512, 0.007951324953966856, 0.007906492674725802, 0.007903290369065728, 0.00787446961812505, 0.007852053478504524, 0.00769193819550076, 0.007499799855896245, 0.00749659755023617, 0.007243615403090225, 0.007205187735169322, 0.007198783123849172, 0.007189176206868946, 0.007163557761588344, 0.00705788167480586, 0.006958610199343527, 0.006958610199343527, 0.006952205588023377, 0.00692978944840285, 0.006904171003122248, 0.006724841886158034, 0.006712032663517733, 0.006712032663517733, 0.006699223440877432, 0.00668000960691698, 0.006587142742774798, 0.0065807381314546476, 0.006539108157873669, 0.0064846689616523895, 0.006395004403170283, 0.006308542150348251, 0.006196461452245617, 0.006170843006965015, 0.006132415339044112, 0.00605235769754223, 0.006049155391882155, 0.005965895444720199, 0.005965895444720199, 0.0059626931390601235, 0.005853814746617564, 0.005837803218317188, 0.0058313986069970375, 0.0057609478824753825, 0.005732127131534705, 0.0056648787126731244, 0.005469538067408534, 0.005373468897606277, 0.005373468897606277, 0.005363861980626051, 0.005341445841005524, 0.005335041229685374, 0.005331838924025298, 0.005331838924025298, 0.005325434312705148, 0.005325434312705148, 0.00529661356176447, 0.005283804339124169, 0.005242174365543191, 0.00523576975422304, 0.005194139780642063, 0.005178128252341686, 0.005171723641021536]

        """
    
    
    def q2d(self, filename: str):
        """
        this question is manually graded
        provide your codes for the computation here
        """
        with open(filename, "r", encoding="utf-8", errors="ignore") as f:
            data = json.load(f)

        dtm_rows = self.q2_getdata(data)
        total = {}
        total_all = 0
        for i, w, c in dtm_rows:
            total[w] = total.get(w, 0) + c
            total_all += c

        top100 = sorted(total.items(), key=lambda x: x[1], reverse=True)[:100]
        x = list(range(1, 101))
        y = [c / total_all for (w, c) in top100]

        plt.figure()
        plt.plot(x, y)
        plt.xlabel("Rank among top 100 tokens")
        plt.ylabel("Fraction of all token occurrences")
        plt.savefig("q2d.png", dpi=300, bbox_inches="tight")
        plt.close()
        # return 'Nothing to return here. Remember to upload your graph'

    
    
    def q2e(self, filename: str, lm_dict_file: str):
        """
        this question is manually graded
        provide your codes for the computation here
        """
        with open(filename, "r", encoding="utf-8", errors="ignore") as f:
            data = json.load(f)
        EM_CODES = {"N2:BR", "N2:TR", "N2:MX", "N2:ZA"}
        em_items = [
            el for el in data["Items"]
            if el["data"]["language"] == "en"
            and el["data"].get("body", "") != ""
            and any(code in el["data"]["subjects"] for code in EM_CODES)
        ]
        docs = [self.analyzer(el["data"].get("body", ""), stem=True) for el in em_items]
        lm = pd.read_csv(lm_dict_file)
        pos_words_raw = lm.loc[lm["Positive"] != 0, "Word"].astype(str).tolist()
        neg_words_raw = lm.loc[lm["Negative"] != 0, "Word"].astype(str).tolist()
        pos_set = set()
        for w in pos_words_raw:
            toks = self.analyzer(w, stem=True)
            for t in toks:
                pos_set.add(t)

        neg_set = set()
        for w in neg_words_raw:
            toks = self.analyzer(w, stem=True)
            for t in toks:
                neg_set.add(t)
        p_over_t, n_over_t, s = [],[],[]
        for toks in docs:
            t_i = len(toks)
            if t_i == 0:
                continue
            p_i = 0
            n_i = 0
            for tok in toks:
                if tok in pos_set:
                    p_i += 1
                if tok in neg_set:
                    n_i += 1
            p_t = p_i / t_i
            n_t = n_i / t_i
            s_i = (p_i - n_i) / t_i
            p_over_t.append(p_t)
            n_over_t.append(n_t)
            s.append(s_i)
        p_over_t = np.array(p_over_t, dtype=float)
        n_over_t = np.array(n_over_t, dtype=float)
        s = np.array(s, dtype=float)
        var_s = np.var(s, ddof=1)
        var_p = np.var(p_over_t, ddof=1)
        var_n = np.var(n_over_t, ddof=1)
        pos_frac = var_p / var_s
        neg_frac = var_n / var_s
        return [pos_frac, neg_frac]
        # return '''
        # Please paste the fraction of total variance represented by the positive and negative words (any format is okay as long as it is clearly written)

        # A sample answer may look like
        # [0.19052703400491502, 0.9924238847965423]

        # '''

   
    
    def q2f(self, filename: str, lm_dict_file: str):
        """
        this question is manually graded
        provide your codes for the computation here
        """
        with open(filename, "r", encoding="utf-8", errors="ignore") as f:
            data = json.load(f)
        EM_CODES = {"N2:BR", "N2:TR", "N2:MX", "N2:ZA"}
        em_items = [
            el for el in data["Items"]
            if el["data"]["language"] == "en"
            and el["data"].get("body", "") != ""
            and any(code in el["data"]["subjects"] for code in EM_CODES)
        ]

        lm = pd.read_csv(lm_dict_file)
        pos_words_raw = lm.loc[lm["Positive"] != 0, "Word"].astype(str).tolist()
        neg_words_raw = lm.loc[lm["Negative"] != 0, "Word"].astype(str).tolist()
        pos_set = set()
        for w in pos_words_raw:
            toks = self.analyzer(w, stem=True)
            for t in toks:
                pos_set.add(t)

        neg_set = set()
        for w in neg_words_raw:
            toks = self.analyzer(w, stem=True)
            for t in toks:
                neg_set.add(t)
        scored = []

        for el in em_items:
            headline = el["data"].get("headline", "")
            body = el["data"].get("body", "")
            toks = self.analyzer(body, stem=True)
            t_i = len(toks)
            if t_i < 300 or t_i > 500:
                continue
            p_i = 0
            n_i = 0
            for tok in toks:
                if tok in pos_set:
                    p_i += 1
                if tok in neg_set:
                    n_i += 1

            s_i = (p_i - n_i) / t_i
            scored.append((s_i, headline))
        scored_sorted = sorted(scored, key=lambda x: x[0])
        five_most_negative = [h for (s, h) in scored_sorted[:5]]
        five_most_positive = [h for (s, h) in scored_sorted[-5:]][::-1]

        return f'''
        five most positive: 
        {five_most_positive}
        five most negative: 
        {five_most_negative}
        '''
        # return 
        '''
        Please paste the headlines of the five most negative (bottom) and most positive (top) sentiment articles (any format is okay as long as it is clearly written)

        A sample answer may look like
        five most positive: 
        ["TEXT-Moody's release on Banco Fibra SA", 'WRAPUP 1-Soccer-UEFA Cup relief for Milan and Ancelotti', 'UPDATE 2-INTERVIEW-Petra Diamonds swings to annual profit', "TEXT-Moody's release on Credito Inmobiliario notes", "TEXT-Fitch may raise Brazil's Company SA"]
        five most negative: 
        ['Mexico peso slammed by bailout fears, stocks down', 'Media-government tensions flare in Turkey', 'Media-government tensions flare in Turkey', 'INSTANT VIEW-Reaction to dismissal of case against Zuma', "FACTBOX-S.Africa's Zuma seeks dismissal of graft charges"]
        '''
    
    
    def q3_getdata(self, data):
        '''
        (Optional)
        You may want to implement a function that loads the COVID-related articles in the loaded JSON file to help streamline your answers for Q2
        '''

        return [1, 2, 3]


    def q3a(self, filename: str):
        """
        now answer this question: 
        How many articles did you locate that satisfy the search criteria in the JSON file named "filename"?
        """

        # please make sure your return value has the same data type as the following sample return
        return 0
    
    
    def q3b(self, filename: str):
        """
        this question is manually graded
        provide your codes for the computation here
        """
        
        return '''
        Please paste the 100 most and least frequently used words (any format is okay as long as it is clearly written)

        A sample answer may look like
        100 most used words:
        [word1, word2, ..., word100]
        100 least used words:
        [word1, word2, ..., word100]

        '''
    
    
    def q3c(self, filename: str):
        """
        this question is manually graded
        provide your codes for the computation here
        """
        
        return '''
        Please paste the list of the 20 words in each topic that have the highest topic-word probability in the return value (any format is okay as long as it is clearly written)

        A sample answer may look like
        top 20 words in topic 1:
        [word1, word2, ..., word20]
        top 20 words in topic 2:
        [word1, word2, ..., word20]
        ...
        top 20 words in topic 10:
        [word1, word2, ..., word20]

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
    # file_q1q2 = 'q2.json.txt'
    file_q1q2 = '/Users/linximeng/Desktop/BD/BD_homework3/News.RTRS.200809.0214.txt'
    file_q3 = 'q3.json.txt'
    file_lm = "/Users/linximeng/Desktop/BD/BD_homework3/Loughran-McDonald_MasterDictionary_1993-2024.csv"
    print('Q1 (a):')
    num1 = calc.q1a(file_q1q2)
    print('generic case:', num1)

    print('Q1 (b):')
    num1 = calc.q1b(file_q1q2)
    print('generic case:', num1)

    print('Q1 (c):')
    num1 = calc.q1c(file_q1q2)
    print('generic case:', num1)

    print('Q2 (a):')
    num1 = calc.q2a(file_q1q2)
    print('generic case:', num1)

    # top25 = calc.q2b(file_q1q2)
    # print("question2b:", top25)

    # fractions = calc.q2c(file_q1q2)
    # print("question2c:", fractions)

    # print("question2d pictures")
    # calc.q2d(file_q1q2)

    # pos_frac, neg_frac = calc.q2e(file_q1q2, file_lm)
    # print("question2e:", "pos_frac is", pos_frac, "; neg_frac is", neg_frac)

    # print("question2f")
    # answer_q2f = calc.q2f(file_q1q2, file_lm)
    # print(answer_q2f)

    print('Q3 (a):')
    num1 = calc.q3a(file_q3)
    print(num1)

