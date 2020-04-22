import os
import time

name = input("Whats your PCs name? eg, Dan. This is found by going to C:/Users/ - If youre Users file isnt there, you must manually edit run_demos.bat: ")

f=open("run_demos.txt", "w+")
cwd = os.getcwd() + "\demo-remover.pyw"

content = '"C:\\Users\\'+ name +'\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe" "' + cwd +'"'
f.write(content)
#f.write("\npause\nexit")
f.close()
time.sleep(1)
os.rename(r'run_demos.txt', r'run_demos.bat')