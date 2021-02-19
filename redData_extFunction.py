import time
import sys
import os
from random import randint
import signal
gameRunning = True
currentFolder = "root"
previousFolder = str()
connected = False
updatedRepo = 1
processRun = True
passCrack = False

def failScreen_missingKernel():
  os.system('clear')
  print("\033[1;37;41m FATAL ERROR.")
  print("\033[1;37;41m ONE OR MORE CORE SYSTEM FILES IS MISSING.")
  sys.exit(0)

def repoUpdate():
  global updatedRepo
  updatedRepo = 2
  netList.append("BlackHat.org")

def repoUpdate2():
  global updatedRepo
  updatedRepo = 3
  netList.append("HavocDynamics.org")

def passCrackinstall():
  global passCrack
  passCrack = True
  

def dataStreamEnd():
  os.system('clear')
  print("Welcome, ANONYMOUS!\nThe test is starting in 20 Seconds")
  time.sleep(20)
  os.system('clear')
  print("Current Sample: None\nAMSPEC Temp: 65C\nSystem Status: Stable")
  time.sleep(10)
  os.system('clear')
  print("terrencefletching.labtech: Alright Gordon, place the sample into the chamber.\nCurrent Sample: None\nAMSPEC Temp: 62C\nSystem Status: Stable")
  time.sleep(5)
  os.system('clear')
  print("Current Sample: SHTIKH3912\nAMSPEC Temp: 68C\nSystem Status: Stable")
  time.sleep(6)
  os.system('clear')
  print("jerrydavis.labtech: It seems to be stable thus far.\nCurrent Sample: SHTIKH3912\nAMSPEC Temp: 71C\nSystem Status: Stable")
  time.sleep(5)
  os.system('clear')
  print("simonhendrikkson.labtech: Wait, this can't be right. It's not supposed to arc!\nCurrent Sample: SHTIKH3912\nAMSPEC Temp: 79C\nSystem Status: Stable")
  time.sleep(3)
  os.system('clear')
  print("robertcapluund.security: It's going to go critical! Everyone needs to get the hell out of here!\nCurrent Sample: SHTIKH3912\nAMSPEC Temp: 88C\nSystem Status: WARN")
  time.sleep(4)
  os.system('clear')
  print("simonhendrikkson.labtech: My god.\nCurrent Sample: SHTIKH3912\nAMSPEC Temp: 164C\nSystem Status: MELTDOWN")
  time.sleep(2)
  os.system('clear')
  print("CONNECTION PROBLEM...")
  time.sleep(8)
  line1 = "Hello."
  line2 = "You don't know who we are, but you will soon."
  line3 = "We've had our eye on you since you first started looking into this.. Havoc Dynamics company."
  line4 = "As you've just seen, their final test went critical, and thus far, it's killed many workers."
  line5 = "We can't let you walk away with you knowing what they were doing there."
  line6 = "Havoc was meant to silently go under, but with you here, the information has the risk of going public."
  line7 = "We cannot let that happen."
  line8 = "We will arrive at your location to collect you soon."
  line9 = "Have a wonderful evening."
  for item in line1:
    sys.stdout.write(item)
    sys.stdout.flush()
    time.sleep(0.1)
  print()
  time.sleep(2)
  for item in line2:
    sys.stdout.write(item)
    sys.stdout.flush()
    time.sleep(0.1)
  print()
  time.sleep(2)
  for item in line3:
    sys.stdout.write(item)
    sys.stdout.flush()
    time.sleep(0.1)
  print()
  time.sleep(2)
  for item in line4:
    sys.stdout.write(item)
    sys.stdout.flush()
    time.sleep(0.1)
  print()
  time.sleep(2)
  for item in line5:
    sys.stdout.write(item)
    sys.stdout.flush()
    time.sleep(0.1)
  print()
  time.sleep(2)
  for item in line6:
    sys.stdout.write(item)
    sys.stdout.flush()
    time.sleep(0.1)
  print()
  time.sleep(2)
  for item in line7:
    sys.stdout.write(item)
    sys.stdout.flush()
    time.sleep(0.1)
  print()
  time.sleep(2)
  for item in line8:
    sys.stdout.write(item)
    sys.stdout.flush()
    time.sleep(0.1)
  print()
  time.sleep(2)
  for item in line9:
    sys.stdout.write(item)
    sys.stdout.flush()
    time.sleep(0.3)
  print()
  time.sleep(2)
  print("\033[1;37;41m END OF LINE.")
  sys.exit(0)


def formLoad(file):
  with open(file) as infile:
    f2 = infile.read()
    print(f2)



#Data
localfileSys = {
  "root": [
    "kernelComp.dat",
    "(Folder) Downloads"
  ],
  "Downloads": [
    "test.txt"
  ],

  "ToolsDB.net": [
    "ToolsDB.net-connectMsg.txt",
    "repoUpdate.pkg",
  ],
  "BlackHat.org": [
    "BlackHat.org-connectMsg.txt",
    "forumPost.txt",
    "(Folder) uID"
  ],
  "uID": [
    "(Folder) CSRin"
  ],
  "CSRin": [
    "repoUpdate_havoclist.pkg",
  ],
  "HavocDynamics.org": [
    "HavocDynamics.org-connectMsg.txt",
    "(Folder) Logon",
  ],
  "Logon": [
    "(Folder) Emails",
    "(Folder) Software"
  ],
  "Emails": [
    "01-15-2020.txt",
    "04-27-2020.txt",
    "05-8-2020.txt",
    "05-12-2020.txt",
    "06-13-2020.txt",
    "06-16-2020.txt"
  ],
  "Software": [
    "dataStream.pkg"
  ]
}

accessRoutelocal = {
  "root": {
    "Downloads"
  },
  "Downloads": {
  },
  "BlackHat.org": {
    "Tools",
    "uID"
  },
  "uID" : {
    "CSRin"
  },
  "CSRin" : {
  },
  "HavocDynamics.org": {
    "Logon"
  },
  "Logon": {
    "Emails",
    "Software"
  },
  "Emails": {
  },
  "Software":{
  }
}

netList = [
  "ToolsDB.net"
]
#ToolsDB.net
#BlackHat.org
#HavocDynamics.org

fileContent = {
  "test.txt":"This is a test text file.",
  "ToolsDB.net-connectMsg.txt":"Welcome to ToolsDB.net! Feel free to download any item from this page.",
  "BlackHat.org-connectMsg.txt":"Welcome to BlackHat.org! Access the forum with forumPost.txt, and download from users in the uID folder.",
  "HavocDynamics.org-connectMsg.txt":"Welcome! Havoc Dynamics is currently only accessible to staff.",
  "repoUpdate.pkg":repoUpdate,
  "repoUpdate_havoclist.pkg":repoUpdate2,
  "dataStream.pkg":dataStreamEnd
}

fileType = {
  "test.txt":"textFile",
  "ToolsDB.net-connectMsg.txt":"textFile",
  "BlackHat.org-connectMsg.txt":"textFile",
  "repoUpdate.pkg":"packageFile",
  "injectionBlocker_portable.pkg":"packageFile",
  "forumPost.txt":"fileTypeFormatted",
  "readmeStream.txt":"fileTypeFormatted",
  "01-15-2020.txt":"fileTypeFormatted",
  "04-27-2020.txt":"fileTypeFormatted",
  "05-8-2020.txt":"fileTypeFormatted",
  "05-12-2020.txt":"fileTypeFormatted",
  "06-13-2020.txt":"fileTypeFormatted",
  "06-16-2020.txt":"fileTypeFormatted",
  "repoUpdate_havoclist.pkg":"packageFile",
  "passwordCrack_install.pkg":"packageFile",
  "dataStream.pkg":"cineFile"
}

passLock = {
  "Logon":1,
  "01-15-2020.txt":1,
  "04-27-2020.txt":1,
  "05-8-2020.txt":1,
  "05-12-2020.txt":1,
  "06-13-2020.txt":1,
  "06-16-2020.txt":1,
  "Software":"hvcprivlogon1021"
}

codeList = {
  1:"sudo systemctl start passCrack",
  2:"sudo bruteForce --FAST",
  3:"sudo apt-install crashAvoidance",
  4:"T mypair<T>::getmax ()",
  5:"void mysequence<T,N>::setmember",
  6:"void Swap(t n1, T n2)",
  7:".cfi_def_cfa_register %rbp",
  8:"mov eax, offset sOutFrstByte",
  9:"cmpl %cax, %ebx"
}




def crackProcess(data):
  def timeout_error(*_):
        raise TimeoutError
  randomListint = randint(1,9)
  listPick = codeList[randomListint]
  inp = str()
  while True:
    signal.signal(signal.SIGALRM, timeout_error)
    signal.alarm(10)
    try:
      print("Input code below:")
      print(listPick)
      inp = str(input())
      if inp == listPick:
        signal.alarm(0)
        passLock[data] = 0
        break
    except TimeoutError:
      print("Ran out of time, exiting.")
      signal.alarm(0)
      break




def startupLoad():
  bootText = "Booting HybridOS"
  loadDot = "..."
  for item in bootText:
    sys.stdout.write(item)
    sys.stdout.flush()
    time.sleep(0.1)
  for item in loadDot:
    sys.stdout.write(item)
    sys.stdout.flush()
    time.sleep(0.5)
  print()
  print("Welcome to HybridOS! Type help to list commands.")



def help():
  global helpDict
  helpDict = {
    "help":"Displays this menu.",
    "ls":"Lists current accessible files.",
    "netls":"Lists currently accessible networks.",
    "connect":"Connects to network address.",
    "disconnect":"Disconnects from current network",
    "cd":"Change directory. .. to go back.",
    "open":"Open a file.",
    "dl":"Downloads a file.",
    "rm":"Deletes a file.",
    "clock":"Shows the current UTC time.",
    "clear":"Clears the screen",
    "crack":"Cracks a folder or file",
    "First Objective?":"Try connecting to a network."
  }

  
  for key, value in helpDict.items():
    print(key, ":", value)

def passCrackinstall():
  global passCrack
  passCrack = True

def quickCheat():
  repoUpdate()
  repoUpdate2()
  passCrackinstall()

def ls():
  print(localfileSys[currentFolder])

def cd(folder):
  global currentFolder
  global previousFolder
  if folder in passLock and passLock[folder] == 1:
    print("Locked")
    return
  elif folder in passLock and passLock[folder] == "hvcprivlogon1021":
    inp = str(input("Password > "))
    if inp == passLock[folder]:
      currentFolder = folder
    else:
      print("Incorrect password.")
      return
  else:
    if folder == "..":
      currentFolder = previousFolder
    elif folder in accessRoutelocal[currentFolder]:
      previousFolder = currentFolder
      currentFolder = folder
    else:
      print("Directory does not exist.")

def openRealOne(file):
  global updatedRepo
  if file in localfileSys[currentFolder]:
    if file in passLock and passLock[file] == 1:
      print("Locked")
      return
    elif fileType[file] == "textFile":
      print(fileContent[file])
    elif fileType[file] == "packageFile":
      print("Installing", file)
      fileContent[file]()
    elif fileType[file] == "fileTypeFormatted":
      formLoad(file)
    elif fileType[file] == "cineFile":
      dataStreamEnd()
  else:
    print("File does not exist.")


def netls():
  global updatedRepo
  loadDot = "..."
  print("Pinging current repo", end='')
  for item in loadDot:
    sys.stdout.write(item)
    sys.stdout.flush()
    time.sleep(0.8)
  print()
  for item in netList:
    print(item)
  print("Current available networks:", updatedRepo)


def connect(netLocation):
  global currentFolder
  global connected
  connected = True
  if netLocation in netList:
    loadDot = "..."
    print("Connecting to address", end='')
    for item in loadDot:
      sys.stdout.write(item)
      sys.stdout.flush()
      time.sleep(0.8)
    print()
    connectMsgcheck = netLocation + "-connectMsg.txt"
    print(fileContent[connectMsgcheck])
    currentFolder = netLocation
    connected = True
  else:
    print("Network does not exist.")

def disconnect():
  global currentFolder
  global connected
  if connected == True:
    connected = False
    print("Disconnected from network.")
    currentFolder = "root"
  else:
    print("Not currently connected to any network.")

def dl(file):
  if file in localfileSys[currentFolder]:
    localfileSys["Downloads"].append(file)
  
  else:
    print("File does not exist.")

def rm(file):
  if connected == False:
    global currentFolder
    if file == "(Folder) Downloads":
      print("Cannot remove, is directory")
    elif file in localfileSys[currentFolder]:
      localfileSys[currentFolder].remove(file)
      if file == "kernelComp.dat":
        failScreen_missingKernel()
    else:
      print("File does not exist")
  else:
    print("No permission to remove files.")

def clock():
  t = time.localtime()
  current_time = time.strftime("%H:%M:%S", t)
  print(current_time)

def clear():
  os.system('clear')

def crashTest():
  thread1.start()
