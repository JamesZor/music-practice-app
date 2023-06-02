import pandas as pd
from dataClass import *
import menu

USER_PROMPT = "Please select one"
CAT = ['bass', 'guitar', 'backing', '']

##############################
def userSelectRow()->dataRow:
        newTrack = dataRow(
            artist  = menu.Disply([],'Artist'),
            song    = menu.Disply([],'Song'),
            channel = menu.Disply([],'Channel'),
            category= menu.Disply(CAT,'Category', False)
        )
        newTrack.link=menu.getYouTubeLink( newTrack.getTitle() )
        return newTrack



##############################


if __name__ == "__main__":
    blueTooth=False
    # create df and load the data
    df = dataFrame()
    df.readFile()

    # main menu display
    userSelection = menu.Disply( df.frame2List(), USER_PROMPT, custom=False, options=True)
    if userSelection == menu.OPS['Ex']:
       x='' 
    elif userSelection == menu.OPS['new']: # new track
        df.addRow( userSelectRow().row2Frame() )
        df.save2file()
    elif userSelection == menu.OPS['bt']: # connect bluetooth speaker
        if not (blueTooth):
            blueTooth = menu.connectBlueTooth()
    else:
        menu.playLink(userSelection)

        # run youtube
        # process userSelection

