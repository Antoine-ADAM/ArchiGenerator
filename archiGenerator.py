#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import urllib.request
import subprocess

VERSION="1.0"
HEADER="https://github.com/Antoine-ADAM/ArchiGenerator "+VERSION

print("""                                                                                                                                                
                                                                                                                                                
   ,---,                          ,---,               ,----..                                                         ___                       
  '  .' \                       ,--.' |      ,--,    /   /   \                                                      ,--.'|_                     
 /  ;    '.      __  ,-.        |  |  :    ,--.'|   |   :     :                ,---,             __  ,-.            |  | :,'   ,---.    __  ,-. 
:  :       \   ,' ,'/ /|        :  :  :    |  |,    .   |  ;. /            ,-+-. /  |          ,' ,'/ /|            :  : ' :  '   ,'\ ,' ,'/ /| 
:  |   /\   \  '  | |' | ,---.  :  |  |,--.`--'_    .   ; /--`     ,---.  ,--.'|'   |   ,---.  '  | |' | ,--.--.  .;__,'  /  /   /   |'  | |' | 
|  :  ' ;.   : |  |   ,'/     \ |  :  '   |,' ,'|   ;   | ;  __   /     \|   |  ,"' |  /     \ |  |   ,'/       \ |  |   |  .   ; ,. :|  |   ,' 
|  |  ;/  \   \'  :  / /    / ' |  |   /' :'  | |   |   : |.' .' /    /  |   | /  | | /    /  |'  :  / .--.  .-. |:__,'| :  '   | |: :'  :  /   
'  :  | \  \ ,'|  | ' .    ' /  '  :  | | ||  | :   .   | '_.' :.    ' / |   | |  | |.    ' / ||  | '   \__\/: . .  '  : |__'   | .; :|  | '    
|  |  '  '--'  ;  : | '   ; :__ |  |  ' | :'  : |__ '   ; : \  |'   ;   /|   | |  |/ '   ;   /|;  : |   ," .--.; |  |  | '.'|   :    |;  : |    
|  :  :        |  , ; '   | '.'||  :  :_:,'|  | '.'|'   | '/  .''   |  / |   | |--'  '   |  / ||  , ;  /  /  ,.  |  ;  :    ;\   \  / |  , ;    
|  | ,'         ---'  |   :    :|  | ,'    ;  :    ;|   :    /  |   :    |   |/      |   :    | ---'  ;  :   .'   \ |  ,   /  `----'   ---'     
`--''                  \   \  / `--''      |  ,   /  \   \ .'    \   \  /'---'        \   \  /        |  ,     .-./  ---`-'                     
                        `----'              ---`-'    `---`       `----'               `----'          `--`---'                                 
                                                                                                                                                
""")
print()
print("Version:",VERSION)
print("Author: antoine.adam@epita.fr")
print("Description: This program allows to automatically generate the structure, to make a git and push clone.")
print()#print("___________________________________________________________________________________________________________________")
print()

print("ArchiGenerator update check ...")
lastVersion=urllib.request.urlopen('https://raw.githubusercontent.com/Antoine-ADAM/ArchiGenerator/main/VERSION').read().decode('utf-8').strip()
if lastVersion != VERSION:
    print("Version installed => Latest version available")
    print(VERSION,"=>",lastVersion)
    print("This code is made of critical actions, it is very important to carry out the update.")
    print("Update link: https://github.com/Antoine-ADAM/ArchiGenerator")
    raise Exception("Please update ArchiGenerator !")

try:
    import pdfplumber
except:
    subprocess.run(["pip3","install","pdfplumber"])
    import pdfplumber

getAll=re.compile(r"""<li><a href="pdf\/(.*?)\.pdf">Sujet<\/a> - <a href="pdf\/(.*?)\.pdf">Corrigé<\/a> : (.*?)<\/li>""")
while True:
    for e in getAll.findall(urllib.request.urlopen('https://www.debug-pro.com/epita/archi/s3/fr/').read().decode('utf-8')):
        print(e)

