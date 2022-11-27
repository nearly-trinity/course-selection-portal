from genschedule.models import ClassData
from .datamanagement import *

def loadData(df):
    for dict in df.itertuples(index=False):
        entry = ClassData()
        entry.course = dict.course
        entry.title = dict.title
        entry.credits = int(dict.credits)
        entry.prereqs = dict.prereqs
        entry.save()

def run():
    _filename = r'C:\Users\early\OneDrive\Desktop\sideproject\tigerPaws\genschedule\scripts\courses.xlsx'
    df = getRows(_filename)
    loadData(df)