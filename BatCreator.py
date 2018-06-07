import os
# minerprog = input("Miner .exe name(sgminer, z-enemy, ccminer): ")#Unfinished, eventually want to have user choose miner software.
coinName = input("1. Enter coin name: ")
algoType = input("2. Enter the algorithm: ")
mainPool = input("3. Enter the main pool and port (stratum+tcp://site.com:port): ")
failoverPool = input("4. Enter the failover pool and port: ")
walletAddress = input("5. Enter the wallet receiving address: ")
coinSymbol = input("6. Enter the coin symbol: ")
rigname = input("7. Enter rig identifier name: ")
intesity = input("8. Enter intesity(Choose a number between 16-21): ")
userPass = " -p c=" + coinSymbol +","

stringToSavesgminer = "sgminer -k " + algoType + " -o " + mainPool + " -u " + walletAddress + userPass + rigname +" --failover-only -o " + failoverPool + " -u " + walletAddress + userPass + rigname +" -i " + intesity + " -L log.txt"
stringToSavezenemy = "z-enemy -a " + algoType + " -o " + mainPool + " -u " + walletAddress + userPass + rigname +" -i " + intesity + " -L log.txt -o " + failoverPool + " -u " + walletAddress + userPass + rigname +" -i 21 -L log.txt"
stringToSaveccminer = "ccminer -a " + algoType + " -o " + mainPool + " -u " + walletAddress + userPass + rigname +" -i " + intesity + " -L log.txt -o " + failoverPool + " -u " + walletAddress + userPass + rigname +" -i 21 -L log.txt"

fileName1 = coinName + algoType + rigname + "sgminer.bat"
batFile = open(fileName1, 'w')
batFile.write("timeout /t 15 \n")
batFile.write(stringToSavesgminer)
batFile.write("\nclose")
batFile.close()

fileName2 = coinName + algoType + rigname + "zenemy.bat"
batFile = open(fileName2, 'w')
batFile.write("timeout /t 15 \n")
batFile.write(stringToSavezenemy)
batFile.write("\nclose")
batFile.close()

fileName3 = coinName + algoType + rigname + "ccminer.bat"
batFile = open(fileName3, 'w')
batFile.write("timeout /t 15 \n")
batFile.write(stringToSaveccminer)
batFile.write("\nclose")
batFile.close()

autoStart1 = "restartsgminer" + fileName1
errorCheck = "if errorlevel 1  (start \"\" %~dp0" + fileName1 + " -e -m -v)\ntimeout /t 30\n"
#fileName = "test.bat" #commented out depricated in main file, uncomment for debugging in standalone py file
autoStartFile = open(autoStart1, 'w')
autoStartFile.write("@echo on\ntimeout /t 3600\n:eof\nTASKKILL /F /IM \"sgminer.exe\"\ntimeout /t 5\n")
autoStartFile.write("tasklist|find /i \"sgminer.exe\" >NUL\n")
autoStartFile.write(errorCheck)
autoStartFile.write("tasklist|find /i \"sgminer.exe\" >NUL\n")
autoStartFile.write(errorCheck)
autoStartFile.write("tasklist|find /i \"sgminer.exe\" >NUL\n")
autoStartFile.write(errorCheck)
autoStartFile.write("timeout /t 7200\n")
autoStartFile.write(errorCheck)
autoStartFile.write("goto eof\n")
autoStartFile.write(errorCheck)
autoStartFile.close()

# os.startfile(fileName) #commented to not autorun file
