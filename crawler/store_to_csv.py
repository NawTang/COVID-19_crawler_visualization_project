import time
import pandas as pd


def to_csv(dlist, file_name):
    df = pd.DataFrame(dlist)
    df.to_csv('../data/'+file_name+'_'+time.strftime('%m%d', time.localtime())+'.csv', index=False)
