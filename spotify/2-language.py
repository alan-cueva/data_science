import sys
import pandas as pd
from langdetect import detect

def getLanguage(name):
    lans = {'en':1, 'de':2, 'es':3, 'it':4, 'fr':5, 'pt':6, 'nl':7, 'tl':8, 'af':9, 'id':10, 'no':11, 'ca':12, 'so':13, 'da':14, 'cy':15, 'ro':16, 'sw':17, 'fi':18, 'et':19, 'sv':20, 'tr':21, 'pl':22, 'sl':23, 'lt':24, 'hu':25, 'hr':26, 'sk':27, 'vi':28, 'ko':29, 'cs':30, 'sq':31, 'ja':32, 'number':33, 'lv':34, 'other':35, 'zh-cn':36, 'ru':37, 'th':38, 'zh-tw':39, 'he':40, 'mk':41, 'bg':42, 'ar':43, 'uk':44, 'fa':45, 'el':46, 'bn':47, 'gu':48, 'hi':49, 'kn':50, 'ml':51, 'mr':52, 'ne':53, 'pa':54, 'ta':55, 'te':56, 'ur':57}
    
    if (name.isnumeric()):
        res = "number"
    else:
        try:
            res = detect(name)
        except:
            res = "other"
    return lans[res]

if (len(sys.argv) != 2):
    exit('No')

in_file  = sys.argv[1] + '.csv'
out_file = 'data/' + sys.argv[1] + '_name_lan.csv'

# Subset
df = pd.read_csv(in_file)
df = df[['id', 'name']]

# Generate and save
df['name_lan'] = df.apply(lambda row : getLanguage(row['name']), axis = 1)
df.pop('name')
df.to_csv(out_file, index = False)


