import telebot
import os
import random
import webbrowser
import subprocess
import socket
from telebot import *
# from PIL import ImageGrab
from playsound import playsound
from winsound import Beep
from pytube import YouTube
from datetime import datetime
#=================================================Class
class data:
    today = datetime.now()
    nowtime = today.strftime("%H%M%S")
    runtime = nowtime
    user_want_to_restart = 0
    user_want_to_shutdown = 0

#=================================================Terminal

os.system("cls")
print("OK Amir,Bot Is Ready !\n")

#=================================================Token

TOKEN = ""
bot = telebot.TeleBot(TOKEN)

#=================================================Buttom Function
def filemanager(user):
    userchatid = user.chat.id
    Buttom = types.ReplyKeyboardMarkup(row_width=1)
    Buttom1 = types.KeyboardButton("FileList📂")
    Buttom2 = types.KeyboardButton("Download📥")
    Buttom3 = types.KeyboardButton("Home🏠")
    Buttom.add(Buttom1,Buttom2,Buttom3)
    bot.send_message(userchatid,"Ok Amir,What Do You Want?",reply_markup=Buttom)

def startcmd(user):
    userchatid = user.chat.id

    Buttom = types.ReplyKeyboardMarkup(row_width=2)
    Buttom1 = types.KeyboardButton("Take a screen shot📸")
    Buttom2 = types.KeyboardButton("Power options⚙")
    Buttom3 = types.KeyboardButton("Play Sound🔊")
    Buttom4 = types.KeyboardButton("FileManager📂")
    Buttom5 = types.KeyboardButton("Downloader⬇")
    Buttom6 = types.KeyboardButton("WiFi Detail📶")
    Buttom7 = types.KeyboardButton("Location🔎")
    Buttom.add(Buttom1, Buttom2, Buttom3, Buttom4, Buttom5, Buttom6, Buttom7)

    bot.send_message(userchatid,
                     "OK Amir,What Do You Want ?😍",
                     reply_markup=Buttom)

def poweroptions(user):
    userchatid = user.chat.id

    Buttom = types.ReplyKeyboardMarkup(row_width=2)
    Buttom1 = types.KeyboardButton("Shutdown🖲")
    Buttom2 = types.KeyboardButton("Restart🔄")
    Buttom3 = types.KeyboardButton("Home🏠")
    Buttom.add(Buttom1, Buttom2, Buttom3)
    bot.send_message(userchatid, "OK Amir,Which One ?", reply_markup=Buttom)

def playsound_(user):
    userchatid = user.chat.id
    Buttom = types.ReplyKeyboardMarkup(row_width=2)
    Buttom1 = types.KeyboardButton("🎵")
    Buttom2 = types.KeyboardButton("🎵")
    Buttom4 = types.KeyboardButton("🎵")
    Buttom5 = types.KeyboardButton("Home🏠")
    Buttom.add(Buttom1,Buttom2,Buttom4,Buttom5)
    bot.send_message(userchatid,"Which Music You Want To Play?🔊",reply_markup=Buttom)

def Downloader(user):
    userchatid = user.chat.id

    Buttom = types.ReplyKeyboardMarkup(row_width=2)
    Buttom1 = types.KeyboardButton("YouTube Downloader📽")
    Buttom2 = types.KeyboardButton("Instagram Downloader🎬")
    Buttom3 = types.KeyboardButton("Home🏠")
    Buttom.add(Buttom1, Buttom2, Buttom3)
    bot.send_message(userchatid, "Which One You Want ?", reply_markup=Buttom)
#=================================================Function
def putfile(filename, filedata):
    myfile = open(filename, "w+")
    return myfile.write(filedata)
    myfile.close()

def getfile(filename):
    myfile = open(filename, "r+")
    return myfile.read()
    myfile.close()

def instaDownloader(user):
    usertext = user.text
    userchatid = user.chat.id

    theUrl = usertext.replace("/Idownloader ", "")
    Url_Site = 'https://instadownloader.co/#url=' + theUrl
    bot.send_message(userchatid,"Opennig...✅")
    for x in range(155,156):
        Beep(10*x, 200)
    webbrowser.open(Url_Site)
    
def sendAllInforMation(user):
    userchatid = user.chat.id
    bot.send_message(userchatid,user)

def time_use_bot(user):
    userchatid = user.chat.id

    today = datetime.now()
    nowtime = today.strftime("%H%M%S")
    runningtime = int(nowtime) - int(data.runtime)

    if (runningtime > 60):
        runningtime2 = runningtime / 60
        runningtime2 = round(runningtime2)
        runningtime = str(runningtime2) + " Minutes"
        if (runningtime2 > 3600):
            runningtime2 = runningtime2 / 3600
            runningtime2 = round(runningtime2)
            runningtime = str(runningtime2) + " Hours"
    else:
        runningtime = str(runningtime) + " Seconds"
    bot.send_message(userchatid, "Running Time: " + str(runningtime))
    print("Running Time: "+str(runningtime)+"⏰")

def pcinfo(user):
    userchatid = user.chat.id

    My_user = os.getlogin()
    cpuuse = os.popen("wmic cpu get loadpercentage").read()
    cpuuse = cpuuse.replace("LoadPercentage", "")
    bot.send_message(userchatid,"👨‍💻"+str(My_user) + "\n💻CPU Usage : %" + str(eval(cpuuse)))

def youTubeDownLoader(user):
    usertext = user.text
    userchatid = user.chat.id

    theUrl = usertext.replace("/Ydownloader ", "")
    url = theUrl
    video = YouTube(url)
    bot.send_message(userchatid,"Ok Wait For Send Tag...⬇")
    for stream in video.streams:
        items = str(stream).split(' ')
        tag = items[1].split('"')[1]
        mimeType = items[2].split('"')[1].split('/')[1]
        resOrAbr = items[3].split('"')[1]
        fpsOrAcodec = items[4].split('"')[1]
        videoType = items[-1].split('"')[1]
        if videoType == 'video':
            bot.send_message(
                userchatid,
                f"◻Tag={tag}\n◻Type={videoType}\n◻Format={mimeType}\n◻Resolution={resOrAbr}\n◻Frame_Per_Second={fpsOrAcodec}\n"
            )

        else:
            bot.send_message(
                userchatid,
                f"▪Tag={tag}\n▪Type={videoType}\n▪Format={mimeType}\n▪Average_Bit_Rate={resOrAbr}\n▪Codec={fpsOrAcodec}\n"
            )

    tag = 137
    stream = video.streams.get_by_itag(tag)
    name = [
        "File1", "File2", "File3", "File4", "File5", "File6", "File7", "File8",
        "File9", "File10", "File11", "File12", "File13", "File14", "File15"
    ]
    namefile = random.choice(name) + videoType
    bot.send_message(userchatid, "Downloading...⬇")
    stream.download(filename=namefile)
    for x in range(1, 3):
        Beep(500 * x, 200)
    bot.send_message(userchatid, "Done✅")
    startcmd(user)


def wifiIPdetail(user):
    userchatid = user.chat.id

    data = subprocess.check_output(['netsh', 'wlan', 'show',
                                    'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    for i in profiles:
        results = subprocess.check_output(
            ['netsh', 'wlan', 'show', 'profile', i,
             'key=clear']).decode('utf-8', 'ignore').split('\n')
        results = [
            b.split(":")[1][1:-1] for b in results if "Key Content" in b
        ]
        try:
            wifi = ("⚪{:<30}➡ {:<}".format(i, results[0]))
            bot.send_message(userchatid, wifi)
        except IndexError:
            wifi2 = ("⚪{:<30}➡ {:<}".format(i, ""))
            bot.send_message(userchatid, wifi2)
    hostn = socket.gethostname()
    ipad = socket.gethostbyname(hostn)
    bot.send_message(userchatid, "🔴Your IP: " + str(ipad))
    startcmd(user)

def takescreenshot(user):
    userchatid = user.chat.id

    bot.send_message(userchatid, "Taking A Screen Shot...📷")
    My_Photo = ImageGrab.grab()
    My_Photo.save("ScreenShot.png")
    for x in range(1, 3):
        Beep(1000 * x, 200)
    bot.send_message(userchatid,
                     "Good,Your Screen Shot Was Taked...📸 \n\n⬛ Sending...")
    photo = open("ScreenShot.png", "rb")
    bot.send_photo(userchatid, photo)
    photo.close()
    os.remove("ScreenShot.png")
    startcmd(user)

def location(user):
    userchatid = user.chat.id
    bot.send_location(userchatid,36.368181,59.517959)

def downloadmanager(user):
    userchatid = user.chat.id
    bot.send_message(userchatid,"🔴 Help ⬇ \n If You Want To Download From Computer Use :\n◽/download [Location][FileName] ") 

def justfilelist(user):
    userchatid = user.chat.id
    bot.send_message(userchatid,"🔴 Help ⬇ \n If You Use FileManager Start With :\n◽/filemanager [Location]")

def filemanagerlist(user):
    userchatid = user.chat.id
    usertext = user.text

    directory = usertext.replace("/filemanager ","")

    if(os.path.isdir(directory)):
        bot.send_message(userchatid,"Scanning...🔎 ")

        foldercount = 0
        folderlist = ""

        filecount = 0
        filelist = ""

        for r, d, f in os.walk(directory):
            for folder in d:
                if(foldercount > 30 or foldercount == 30):
                    break
                else:
                    foldercount += 1
                    if("\\" in r):
                        folderlist = folderlist+"\n"+"👉📁 "+r+"/"+folder
                    else:
                        folderlist = folderlist+"\n"+"📁 "+r+"/"+folder
            for file in f:
                if(filecount > 30 or filecount == 30):
                    break
                else:
                    filecount += 1
                    filelist = filelist+"\n"+"🧾 "+r+"/"+file
        for x in range(155,156):
            Beep(10*x, 200)
        bot.send_message(userchatid,"🗂 30 First Folders In "+directory+" : \n"+str(folderlist))
        bot.send_message(userchatid,"🗃 30 First File In "+directory+" : \n"+str(filelist))
    else:
        bot.send_message(userchatid,"Not Found❌")
        Beep(1000, 200)      


def downloadthisfile(user):
    userchatid = user.chat.id
    usertext = user.text
    filename_or_fileadress = usertext.replace("/download ","")
    if(os.path.isdir(str(filename_or_fileadress))):
        bot.send_message(userchatid,"This Is Folder📂")
    else:
        if(os.path.isfile(str(filename_or_fileadress))):
            bot.send_message(userchatid,"Downloading...⬇\n "+"🔴Location : "+str(filename_or_fileadress))
            thefile = open(filename_or_fileadress,"rb")
            bot.send_document(userchatid,thefile)
            bot.send_message(userchatid,"Done✅")
            for x in range(1, 2):
                Beep(500 * x, 200)
        else:
            bot.send_message(userchatid,"Not Found❌")
            Beep(1000, 200)
            pass

def shutdown_btn(user):
    data.user_want_to_restart = 0
    data.user_want_to_shutdown = 1
    userchatid = user.chat.id
    bot.send_message(
        userchatid, "📍Are You Sure To ShutDown Your Computer ?\n\n⭕Send /yes to shutdown or send /no to")

def restart_btn(user):
    data.user_want_to_restart = 1
    data.user_want_to_shutdown = 0
    userchatid = user.chat.id
    bot.send_message(
        userchatid, "📍Are You Sure To Restart Your Computer ?\n\n⭕Send /yes to restart or send /no to")

def shutdown_or_restart(user):
    userchatid = user.chat.id
    if(data.user_want_to_shutdown == 1 and data.user_want_to_restart == 0):
        bot.send_message(userchatid, "Your Computer Shutting Down...✅")
        data.user_want_to_shutdown = 0
        data.user_want_to_restart = 0
        os.system("shutdown /p")
    elif(data.user_want_to_restart == 1 and data.user_want_to_shutdown == 0):
        data.user_want_to_shutdown = 0
        data.user_want_to_restart = 0
        bot.send_message(userchatid, "Your Computer Restarting...✅")
        os.system("shutdown /r /t 1")
    else:
        bot.send_message(userchatid, "Opps,An Error Occurred ❎")

def no_to_shutdown(user):
    userchatid = user.chat.id
    data.user_want_to_restart = 0
    data.user_want_to_shutdown = 0
    bot.send_message(userchatid, "Done ✅")

def hibernate(user):
    os.system("Shutdown /hybrid")

def logout(user):
    os.system("Shutdown /l")

def saveMessage(user):
    usertext = user.text
    userchatid = user.chat.id
    try:
        theMessage = usertext.replace("/save ", "")
        randomnumber = random.randint(11111, 99999)
        putfile("database/data_" + str(randomnumber) + ".txt", str(theMessage))
        bot.send_message(userchatid, "Your Message Was Save✅")
        for x in range(155,156):
            Beep(10*x, 200)
    except:
        bot.send_message(userchatid,"Error❎\nCant Save It...")

def systeminfo(user):
    userchatid = user.chat.id
    try:
        sys = os.popen("systeminfo").read()
        bot.send_message(userchatid,sys)
    except:
        bot.send_message(userchatid,"Error❎\n1=System Info Is Very Long,Telegram Cant Send!!!\n2-Your Information Was Hide.\n3-Somrthing Else...")

def taskmanager(user):
    userchatid = user.chat.id
    try:
        task = os.popen("tasklist").read()
        bot.send_message(userchatid,task)
    except:
        bot.send_message(userchatid,"Error❎\nTasklist Is Very Long,Telegram Cant Send!!!")

def ipconfig(user):
    userchatid = user.chat.id
    try:
        ip = os.popen("ipconfig").read()
        bot.send_message(userchatid,ip)
    except:
        bot.send_message(userchatid,"Error❎\nCant Find Wifi IP!!!")

def showallwifi(user):
    userchatid = user.chat.id
    try:
        wifi = os.popen("netsh wlan show networks").read()
        bot.send_message(userchatid,wifi)
    except:
        bot.send_message(userchatid,"Error❎\n1-Your Wifi Scan Was Turn Off.\n2-Your Computer/Laptop Dont Have Wireless Adaptor!!!")
    
def mac(user):
    userchatid = user.chat.id
    try:
        mac = os.popen("arp -a").read()
        bot.send_message(userchatid,mac)
    except:
        bot.send_message(userchatid,"Error❎Cant Find It...")

def UserInfo(user):
    userchatid = user.chat.id
    userusername = user.chat.username
    userfirstname = user.chat.first_name
    putfile("AllInformationAboutUser.txt",user)
    randomnumber2 = random.randint(100, 999)
    putfile(
        "database/All_UserInfo_" + str(randomnumber2) + ".txt",
        "UserName: " + str(userfirstname) + "---> User ID: " +
        str(userusername) + "---> User ID(Code): " + str(userchatid))


@bot.message_handler(content_types=['text'])
def botmain(user):
    Admin1 = "l_amr2_l"
    usertext = user.text
    userchatid = user.chat.id
    userusername = user.chat.username
    print("User ID (Code) : " + str(userchatid))
    if userusername != "l_amr2_l":
        UserInfo(user)
        bot.send_message(userchatid, "I Dont Know Who Are You !")
    else:
        print("User ID : @" + userusername)

    if (userusername == Admin1):

        if usertext == "/start" or usertext == "Home🏠":
            startcmd(user)
        
        if usertext.startswith("/shutdown"):
            shutdown_btn(user)
        
        if usertext.startswith("/restart"):
            restart_btn(user)

        if usertext == "Shutdown🖲":
            shutdown_btn(user)
        
        if usertext == "Restart🔄":
            restart_btn(user)

        if(usertext == "/yes"):
            shutdown_or_restart(user)

        if(usertext == "/no"):
            no_to_shutdown(user)

        if (usertext.startswith("/save ")):
            saveMessage(user)

        if usertext.startswith("/Idownloader "):
            instaDownloader(user)

        if usertext.startswith("/time"):
            time_use_bot(user)

        if usertext.startswith("/pcinfo"):
            pcinfo(user)

        if usertext.startswith("/Ydownloader "):
            youTubeDownLoader(user)

        if (usertext == "Power options⚙"):
            poweroptions(user)

        if usertext == "Take a screen shot📸":
            takescreenshot(user)

        if usertext == "Play Sound🔊":
            playsound_(user)
        
        if usertext.startswith('/systeminfo'):
            systeminfo(user)
        
        if usertext.startswith('/taskmanager'):
            taskmanager(user)
        
        if usertext.startswith('/showwifi'):
            showallwifi(user)
        
        if usertext.startswith('/userinfo'):
            sendAllInforMation(user)

        if usertext.startswith('/mac'):
            mac(user)

        if usertext.startswith('/ipconfig'):
            ipconfig(user)

        if usertext == "Downloader⬇":
            Downloader(user)
        
        if usertext == "FileManager📂":
            filemanager(user)
        
        if usertext == "FileList📂" or usertext == "/filelist":
        	justfilelist(user)
        
        if usertext.startswith("/filemanager "):
        	filemanagerlist(user)

        if usertext == "Location🔎":
            location(user)
        
        if usertext.startswith("/logout"):
            logout(user)
        
        if usertext.startswith("/hibernate"):
            hibernate(user)

        if usertext == "Download📥":
            downloadmanager(user)

        if usertext.startswith("/download "):
            downloadthisfile(user)

        if usertext == "Instagram Downloader🎬":
            bot.send_message(
                userchatid,
                "🔴 Help ⬇ \nIf You Want To Download From Instagram Use \n◽/Idownloader [URL] "
            )

        if usertext == "YouTube Downloader📽":
            bot.send_message(
                userchatid,
                "🔴 Help ⬇ \nIf You Want To Download From YouTube Use \n◽/Ydownloader [URL] "
            )

        if usertext == "WiFi Detail📶":
            wifiIPdetail(user)

        if usertext.startswith("/help"):
            bot.send_message(
                userchatid,
                "⭕ Help ⭕\n\n➡ /start To Start Or Back To Main Meno.\n\n➡ /userinfo To See All Information About User[User Bot].\n\n➡ /filemanager To See All Folder And File In Drive.\n\n➡ /save [Message] To Send Message And Save To Computer.\n\n➡ /time To See Time Use Bot.\n\n➡ /Idownloader [URL] To Download From Instagram App.\n\n➡ /Ydownloader [URL] To Download Video From YouTube.\n\n➡ /download [Location]+[FileName]To Download File From Computer.\n\n➡ /pcinfo To See Username And CPU Usage.\n\n➡ /systeminfo To See All Information Of System.\n\n➡ /ipconfig To See All Information About IP.\n\n➡ /mac To See Mac Address.\n\n➡ /showwifi To See All Available Wi-Fi.\n\n➡ /taskmanager To See All App[Open].\n\n➡ /shutdown To Shutdown Your Computer[You Can Use Button Too].\n\n➡ /restart To restart Your Computer[You Can Use Button Too].\n\n➡ /logout To LogOut Your System[Important:If You Click Your System Logout With No Question].\n\n➡ /hibernate To Hibernate Your System[Important:If You Click Your System Hibernate With No Question].\n\nBot Creat By Amir👨‍💻"
       
         )

    else:
        pass


bot.poling(True)