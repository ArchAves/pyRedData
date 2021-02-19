from redData_extFunction import *



startupLoad()

while gameRunning:
  playerInp = str(input(">"))

  if playerInp == "help":
    help()
  elif playerInp == "ls":
    ls()
  elif playerInp == "cd":
    cd(str(input("Directory > ")))
  elif playerInp == "netls":
    netls()
  elif playerInp == "open":
    openRealOne(str(input("Name of file > ")))
  elif playerInp == "connect":
    connect(str(input("Network address > ")))
  elif playerInp == "disconnect":
    disconnect()
  elif playerInp == "dl":
    dl(str(input("File to download > ")))
  elif playerInp == "rm":
    rm(str(input("File to remove > ")))
  elif playerInp == "clock":
    clock()
  elif playerInp == "clear":
    clear()
  elif playerInp == "quickcheat":
    quickCheat()
  elif playerInp == "crack":
    crackProcess(str(input("File or Folder to crack > ")))
  else:
    print("Unknown command.")