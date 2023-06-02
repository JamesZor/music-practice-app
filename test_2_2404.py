import subprocess as sp
import pandas as pd

#################### Class
class dataCell:
    def __init__(self, artist, song, channel='', youtubelink=''):
        self.artist=artist
        self.song=song
        self.channel=channel
        self.yt= youtubelink

    def getDataFrame(self):
        return  pd.DataFrame.from_records([{'artist':self.artist,
                 'song':self.song,
                 'channel':self.channel,
                 'youtube_link':self.yt}])

    def getTitle(self):
        return "%s %s %s"%(self.artist, self.song, self.channel)

class dataFrame:
    COLUMNS_LIST=['artist','song','channel', 'youtube_link',]
    def __init__(self):
        self.frame= pd.DataFrame(columns=self.COLUMNS_LIST)

    def addRow(self, dataframe):
        self.frame= pd.concat([self.frame, dataframe], ignore_index=True)

    def displayFrame(self):
        print(self.frame)

    def extractList(self):
        return_list=[]
        for index, row in self.frame.iterrows():
            text = '%s - %s :%s'%(self.frame['artist'].values[index],self.frame['song'].values[index],self.frame['channel'].values[index]  )
            return_list.append(text) 
        return return_list

    def addNewTrack(self):
        newTrack = dataCell(menu([],"Artist"),menu([],"Song"),menu([],"channel"))
        newTrack.yt=getYouTubeLink(newTrack.getTitle() )
        self.addRow( newTrack.getDataFrame() )
        return

######################### functions
def menu( display_list, menu_prompt, custom=False ):
    custom_str=''
    if custom:
        custom_str='-no-custom'
    disply_str=""

    [disply_str:=disply_str+x+'\n' for x in display_list]
    process_one= sp.Popen(["echo", disply_str], stdout=sp.PIPE)
    process_two= sp.Popen(["rofi", "-dmenu",custom_str, '-i','-p', menu_prompt], stdin=process_one.stdout, stdout=sp.PIPE, text=True)
    process_one.stdout.close()
    return  process_two.communicate()[0].strip('\n')

def getYouTubeLink(dataCell ):
    # change me data type..,
    cmd_out =''
    i=0
    while ("http" not in cmd_out)&(i<2) :
        process_one = sp.Popen(['ytfzf','-DL', dataCell ],stdout=sp.PIPE, text=True)
        cmd_out = process_one.communicate()[0].strip('\n')
        i+=1
    return  cmd_out


#########################
# start main


main = dataFrame()
trackone = dataCell( 'beachtape', 'maybe')
tracktwo= dataCell( 'strokes', 'you only live once')
#lines =getYouTubeLink(trackone)
main.addRow( trackone.getDataFrame())
main.addRow( tracktwo.getDataFrame())
main.addNewTrack()
main.displayFrame()


