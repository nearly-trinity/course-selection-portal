import pandas as pd
import re
# from genschedule.models import ClassData

def bigPrint(df):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(df)

pat = re.compile('CSCI.\d{4}')
def cleanPrerequisites(courses):
    if '21 hours' in courses:
        return ",".join(['CSCI-9999'])

    classes = []
    space_idx = courses.index(' ')
    courses = courses[space_idx+1:]
    
    # different courses are delimited with ','
    # within each their description is separated with ';'
    parts = courses.split(',')

    for part in parts:
        matches = re.findall(pat,part)
        matches = list(map(lambda x: x.replace(' ', '-'), matches))
        classes.extend(matches)

    return ",".join(classes)

def getRows(filename):
    df = pd.read_excel(filename)
    
    # isolate cols relevant to project and remove redundancies
    relevant_cols = ['course','title', 'credits', 'printed specs']
    df = df[relevant_cols]
    df.rename(columns={'printed specs':'prereqs'}, inplace=True)

    
    # only retain CSCI courses
    df = df[df.apply(lambda x: x['course'].split('-')[0] == 'CSCI', axis=1)]

    # clean the prerequisite values and store in the df
    for dict in df.itertuples():
        idx = dict.Index
        str = ""
        if not pd.isnull(df.at[idx,'prereqs']):
            str = cleanPrerequisites(dict.prereqs)
        df.at[idx,'prereqs'] = str
    
    return df

def loadData(df):
    return

