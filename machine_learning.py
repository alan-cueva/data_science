import pandas

####################################################################################
# Data Exploration
####################################################################################

def explore_df(df):
    cols = df.columns
    
    uniques = []
    for col in cols:
        uniques.append( len(df[col].unique()) )
    
    mean = [float('nan')] * len(cols)
    std = [float('nan')] * len(cols)
    min = [float('nan')] * len(cols)
    p25 = [float('nan')] * len(cols)
    p50 = [float('nan')] * len(cols)
    p75 = [float('nan')] * len(cols)
    max = [float('nan')] * len(cols)
    
    i = 0
    tmp = df.describe()
    for col in cols:
        if col in tmp:
            mean[i] = tmp[col][1]
            std[i] = tmp[col][2]
            min[i] = tmp[col][3]
            p25[i] = tmp[col][4]
            p50[i] = tmp[col][5]
            p75[i] = tmp[col][6]
            max[i] = tmp[col][7]
        i = i + 1
    
    data = {
        'Cols'   : cols,
        'IsNull' : list(df.isnull().any()),
        'Count'  : list(df.count()),
        'Unique' : uniques,
        'Mean'   : mean,
        'Std'    : std,
        'Min'    : min,
        '25%'    : p25,
        '50%'    : p50,
        '75%'    : p75,
        'Max'    : max
    }
    
    res = pandas.DataFrame(data)
    return res

def get_uniques(df, col):
    tmp = df[col].unique()
    tmp.sort()
    return tmp

def get_counts(df, target, col, sortby=None):
    tmp = df[[col, target]].groupby([col, target]).size().reset_index(name='count')
    if sortby is None:
        return tmp.pivot_table('count', col, target)
    else:
        return tmp.pivot_table('count', col, target).sort_values(by=sortby)

####################################################################################
# Plots for classification
####################################################################################

####################################################################################
# Statistical Test for Classification
####################################################################################
