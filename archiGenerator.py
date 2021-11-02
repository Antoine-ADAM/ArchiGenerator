#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import urllib.request
import subprocess
import decimal

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

regex = re.compile(r"\n\s*Étape\s*(\d+)\s*\n")
getAll=re.compile(r"""<li><a href="pdf\/(.*?)\.pdf">Sujet<\/a> - <a href="pdf\/(.*?)\.pdf">Corrigé<\/a> : (.*?)<\/li>""")
while True:
    topics=getAll.findall(urllib.request.urlopen('http://www.debug-pro.com/epita/archi/s3/fr/').read().decode('utf-8'))
    idTP=-1
    max=len(topics)
    while idTP<=0 or idTP>max:
        print("Topics list:")
        for i in range(max):
            print(f"{i+1} => {topics[i][2]}")
        print()
        try:
            idTP=int(input(f"What is the number of the topic to process?(1-{max})")) or -1
        except Exception:
            pass
        if idTP <= 0 or idTP > max:
            print("Value is not valid !")
        print()

    name=topics[idTP-1][0] if (input("Topic or corrected ?(t or c)[t]") or "t") == "t" else topics[idTP-1][1]
    dirRes=input(f"Save location:[{name}/]") or name+'/'
    if dirRes[len(dirRes)-1]!='/':
        dirRes+='/'
    if not os.path.exists(dirRes):
        os.makedirs(dirRes)
    urllib.request.urlretrieve(f'http://www.debug-pro.com/epita/archi/s3/fr/pdf/{name}.pdf',f"{dirRes}{name}.pdf")
    with pdfplumber.open(f"{dirRes}{name}.pdf") as pdf:
        lastEtape=0
        subEtape=0
        for page in pdf.pages:
            datas=page.horizontal_edges
            point=None
            matches = regex.finditer(str(page.extract_text()))
            matches=[[e.start(),e.group(1)] for e in matches]
            iM=0
            for e in datas:
                if float(e["width"]) == 508.950:
                    if point and float(e["top"]) - float(point) > 50:
                        if matches:
                            while iM<len(matches) and point<page.chars[matches[iM][0]]["y0"]:
                                lastEtape=int(matches[iM][1])
                                iM+=1
                                subEtape=0
                        subEtape+=1
                        d2=(e["x0"],point, e["x0"]+decimal.Decimal(508.950),e['bottom'])
                        with open(f"{dirRes}/{name}_Etape{lastEtape}_{subEtape}.asm",'w') as f:
                            f.write(page.within_bbox(d2, relative=False).extract_text())
                        point=None
                    else:
                        point=e["top"]
    input("Press enter to redo a new backup !")