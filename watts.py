import pandas as pd
from dataClass import *
import menu
import logging

USER_PROMPT = "Please select one"
CAT = ['bass', 'guitar', 'backing', '']

##############################
def userSelectRow()->dataRow:
    # ask user for inputs and get link
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
    ## logging setup
    logging.basicConfig(filename='wattslog.log', encoding='utf-8', level=logging.DEBUG)

    # create df and load the data
    df = dataFrame()
    df.readFile()

    # main menu display
    while True:
        userSelection = menu.Disply( df.frame2List(), USER_PROMPT, custom=False, options=True)
        if userSelection == menu.OPS['Ex']:
            break   # Break from while loop
        elif userSelection == menu.OPS['new']: # new track
            temp =  userSelectRow()
            while True:
                menu.playLink(temp.link)
                correctLink = menu.Disply(['yes','no','change'], "Is this correct?", custom=False, options=False)
                if correctLink == "change":
                    temp =userSelectRow()
                elif correctLink == 'yes':
                    df.addRow(temp.row2Frame())
                    df.save2file()
                    break
                else:
                    temp.link = menu.getYouTubeLink( temp.getTitle() )
        elif userSelection == menu.OPS['bt']: # connect bluetooth speaker
            if not (blueTooth):
                blueTooth = menu.connectBlueTooth()
        else:
            # create a search function for date frame that returns link
            while True:
                # need to add check if link is null
                menu.playLink(df.search4Link(userSelection))
                userRespone =menu.Disply(['yes','no'], "Do you want to repeat?",custom=False,options=False)
                if userRespone == 'no':
                    break
