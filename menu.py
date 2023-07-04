import subprocess as sp

OPTIONS = ['Add New Track', 'Connect Speaker','Exit']
OPS = {'new':OPTIONS[0], 'bt':OPTIONS[1], 'Ex':OPTIONS[2]}


def Disply(display_list:[str], menu_prompt:str, custom=False ,options=False)->str:
    # display a menu with a custom list
    custom_str=''
    if custom:
        custom_str='-no-custom'

    if options:
        display_list = OPTIONS + display_list
    disply_str=""

    [disply_str:=disply_str+x+'\n' for x in display_list]
    process_one= sp.Popen(["echo", disply_str], stdout=sp.PIPE)
    process_two= sp.Popen(["rofi", "-dmenu",custom_str, '-i','-p', menu_prompt], stdin=process_one.stdout, stdout=sp.PIPE, text=True)
    process_one.stdout.close()
    return  process_two.communicate()[0].strip('\n')

def connectBlueTooth()->bool:
    process = sp.Popen(['bluetoothctl', 'connect', '08:EB:ED:FE:97:67'], stdout=sp.PIPE, text=True)
    temp = process.communicate()[0].split('\n')[1].split()[0]
    if temp == "Failed":
        return False
    else:
        return True

def playLink(link:str):
    process =sp.Popen(['ytfzf','-a', link])
    process.wait()
    return


def getYouTubeLink(searchTerm)->str:
    # change me data type..,
    MAX_SEARCH_LIMIT:int=2
    LINK_HEADER:str="http"

    linkOut =''
    i=0
    while (LINK_HEADER not in linkOut)&(i<MAX_SEARCH_LIMIT) :
        process_one = sp.Popen(['ytfzf','-DL', searchTerm ],stdout=sp.PIPE, text=True)
        linkOut = process_one.communicate()[0].strip('\n')
        i+=1
    return  linkOut




