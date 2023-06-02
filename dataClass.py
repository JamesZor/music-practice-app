import pandas as pd
import subprocess as sp
COLS =['artist','song','channel','link','category']
SAVE_PATH='/home/james/projects/watts/'
DATA_FILE='data.csv'
###############################
class cat:
    CAT = ['bass', 'guitar', 'backing', '']
    def __init__(self, object):
        if object not in self.CAT:
            raise("User error: object is not in define category list.")
        self.c = object
###############################

class dataRow:
    def __init__(self, artist:str='',
                 song:str='',channel:str='',link:str='', category='' ):
        self.artist:str  = artist
        self.song:str    = song
        self.channel:str = channel
        self.link:str    = link
        self.category    = category

    def row2Frame(self):
        return  pd.DataFrame.from_records([{'artist':self.artist,
                 'song':self.song,
                 'channel':self.channel,
                 'link':self.link,
                  'category':self.category}])
    def getTitle(self):
        return "%s %s %s -- %s "%(self.artist, self.song, self.channel, self.link)
    ### testing
    def printALL(self):
        attrs = vars(self)
        print(' ,'.join("%s: %s" % item for item in attrs.items()))


class dataFrame:
    COLUMNS_LIST = ['artist','song','channel','link','category']
    def __init__(self):
        self.frame= pd.DataFrame(columns=self.COLUMNS_LIST)

    def addRow(self, newRow:dataRow ):
        self.frame = pd.concat([self.frame, newRow], ignore_index=True)

    def displayFrame(self):
        print(self.frame)

    def frame2List(self):
        return_list=[]
        for index, row in self.frame.iterrows():
            text = '%s  %s  %s'%(self.frame['artist'].values[index],self.frame['song'].values[index],self.frame['channel'].values[index]  )
            return_list.append(text)
        return return_list
    def save2file(self):
        self.frame.to_csv(SAVE_PATH+DATA_FILE)
    def readFile(self):
        temp = pd.read_csv(SAVE_PATH+DATA_FILE)
        self.frame = pd.concat([self.frame, temp], ignore_index=True)

##############################

