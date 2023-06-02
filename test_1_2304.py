####  Test 1 ### 
# Details
# This script is made to test the technologies and improve skills needed for this project.
# In which it aims to achieve the following:
#      1)  python to cmd ( using youtube downloader )
#      2)  python pip list into rofi and use selection 
#      3)  logic menu 
#      4)  data base


###### Code Section ######
#1)
#import os
#cmd_code ='ytfzf -D cats'
#os.system(cmd_code)

#2)
import subprocess as sp
#cmd_code='echo "%s" | rofi -dmenu -i -p " Select an option"'
#SELECTION_OPTIONS=['OK.', 'No.']
#selection_list=""
#[ selection_list:=selection_list+x+'\n' for x in SELECTION_OPTIONS ]
#process_one= sp.Popen(["echo", selection_list], stdout=sp.PIPE)
#process_two= sp.Popen(["rofi", "-dmenu", "-i"], stdin=process_one.stdout, stdout=sp.PIPE,
#                      text=True)
#process_one.stdout.close()
#user_selection = process_two.communicate()[0]
#
##3) logic on menu
#
#if "OK." in user_selection :
#    print("the user has selected %s"%(SELECTION_OPTIONS[0]))
#elif SELECTION_OPTIONS[1] in user_selection:
#    print("the user has said this man: %s"%(SELECTION_OPTIONS[1]))
#else:
#    print("fail.")
#

## 2.1)
def menu( display_list, menu_prompt ):
    disply_str=""
    [disply_str:=disply_str+x+'\n' for x in display_list]
    process_one= sp.Popen(["echo", disply_str], stdout=sp.PIPE)
    process_two= sp.Popen(["rofi", "-dmenu", "-i",'-p', menu_prompt], stdin=process_one.stdout, stdout=sp.PIPE, text=True)
    process_one.stdout.close()
    return  process_two.communicate()[0].strip('\n')

#menu(['tea','coffee'], 'drink')

# 3.9) database
import pandas as pd
class drinker:
    def __init__(self, name, drink):
        self.name=name
        self.drink=drink

    def getDF(self):
        return pd.DataFrame.from_records([{'Name':self.name,'Drink':self.drink}])
class drinks:
    COLS=['Name', 'Drink']
    def __init__(self):
        self.frame=pd.DataFrame(columns=self.COLS)

    def addRow(self, dataframe):
        self.frame= pd.concat([self.frame, dataframe])


dataDrinks = drinks()
print(dataDrinks.frame )
for i in range(1,5):
    a = drinker(menu('', 'Name'),menu(['tea','coffee'], 'drink'))
    dataDrinks.addRow(a.getDF() )
print(dataDrinks.frame )


# 4) database.
class dataCell:
    def __init__(self, artist, song, channel=None, youtubelink=None):
        self.artist=artist
        self.song=song
        self.channel=channel
        self.yt= youtubelink

    def getDataFrame(self):
        return  pd.DataFrame.from_records([{'artist':self.artist,
                 'song':self.song,
                 'channel':self.channel,
                 'youtube_link':self.yt}])

line_one = dataCell("king kule", "easy easy")

class dataFrame:
    COLUMNS_LIST=['artist','song','channel', 'youtube_link']
    DATA = {'artist':['beachtape'],'song':['maybe'],
                 'channel':['something'],
                 'youtube_link':['wwww']}

    def __init__(self):
        self.frame= pd.DataFrame(self.DATA)

    def addRow(self, dataframe):
        self.frame= pd.concat([self.frame, dataframe])

    def displayFrame(self):
        print(self.frame)


