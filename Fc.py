import os, platform, time, sys
os.system('xdg-open https://wa.me/923065893752')
try:
 import requests
except:os.system("pip uninstall requests -y;pip install requests")

print('\033[1;91m[\033[1;97m-\033[1;91m] \033[1;97mChecking For Update...')
os.system('git pull --quiet 2>/dev/null')
bit = platform.architecture()[0]
if bit == '64bit':                                                                                    print('\033[1;91m[\033[1;97m✓\033[1;91m] \033[1;97m64Bit Found')
 import jutt
elif bit == '32bit':
 print('\033[1;91m[\033[1;97m✓\033[1;91m] \033[1;97m32Bit Found')
 import jutt
