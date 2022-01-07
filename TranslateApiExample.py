#! python3

### USAGE: Write your localization sql in a specific file for english
## then your sql will call the google translate api and create the translated text
## from there you can grab your translated sql from each file.
## Each file will overwrite the last

### NOTE: It is best to write just the lines you need,
## the API charges per charaters translated, to reduce cost, let's only translate what we need.

### COST:  $20 per million charaters

## Automating this will reduce the amount of time it takes for localization sql, Instead of having to open multiple tabs and copy paste each part of the SQL we need to translate
## We can write one sql file in english and have the rest in seconds vs 30+ minutes to potentially hours

## I recommend we use python's venv, but we don't have to. The setup guide will go over this. Python was the language of choice, due to simplicity, but there are multiple options. 

### You will be able to run Python scripts from IDLE without the shebang line, but the line is needed to run them from the command line.
### BE SURE TO GIVE THE FILE PREMISSIONS (ex chmod 700 filename.py on mac) then you will be able to run ./filename.py from your terminal/command line

### ADDITIONAL SETUP WINDOWS FOR DOUBLE CLICK RUN:
## 1- Right Click the script file and go to properties.

## 2- Select the option ‘Opens with:’ in General tab, and select the python from list, if its not available then browse to the installation directory of python and select the python.exe from there.

## 3- Now when you double click on the file it will run automatically.

### SHBANG LINE PER OS:
## On Windows, the shebang line is #! python3.

## On OS X, the shebang line is #! /usr/bin/env python3.

## On Linux, the shebang line is #! /usr/bin/python3.

### OTHER OPTIONS:
## python filename.py in terminal (or python3 if you have python 2 installed as well)


### LINKS BELOW
###
### SETUP GUIDE: https://cloud.google.com/python/setup
### REFERENCE: https://cloud.google.com/translate/docs/reference/libraries/v2/python#usage
### DOCUMENTATION: https://cloud.google.com/translate/docs/
### RESOURCES: https://cloud.google.com/translate/docs/resources (pricing, FAQ etc.) For Attribution under the FAQ Section We should fall under post-editing due to the nature of this program.

### END OF MAIN NOTES

## (Developer) UNCOMMENT the lines below with only one # once setup is complete

import os
from google.oauth2 import service_account
from google.cloud import translate_v2 as translate
credentials = service_account.Credentials.from_service_account_file('/Users/your-user/path-to-creds/Project-Creds.json')

translate_client= translate.Client(credentials=credentials)

## We setup the global variable for GCP service account credentials which we can save to a json file [ex r'C:\\folder\\as.jpg' |or| r'C:\folder\as' |or even| os.path.join( 'C:\\', 'folder', 'as' )]

#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r

try:
    ## This .sql file could and should be a general sql on your filesystem and idealily in it's own folder with this program. to see this in action without the api write a file with 3 insert statements
    f = open('examplesql.sql',mode = 'r',encoding = 'utf-8')
    ## Grab all lines from the sql file
    lines = f.readlines()
    ## words will just store the last word in the sql statement that will be translated
    words = []
    ## Using this for example only
    twords = ['Tthis','Tword 2', 'Tspaced test']
    ## print(lines)
    
    ## To account for newline charaters within the lines list
    ## This will not account for errors like a missing ; or \t for example
    while '\n' in lines:
        lines.remove('\n')
    ## print(lines)

    ## This will grab the word(s) from each line to be translated and put them in the words list
    for l in lines:
        words.append(l.split(",")[-1].split("'")[-2])

    i = 0

    for l in range(len(lines)):
        ## So we don't have a million clones of our sql translations,
        ## We will overwrite the existing sql file in our filesystem if it exists
        ## or create it if it doesn't exist.
        ## to get each line we need, we change the char to append ('a')
        ## This avoids overriding the last line we've already translated
        if i > 0:
            char = 'a'
        else:
            char = 'w'
        # print(i)
        i = i + 1

        ## GERMAN
        lde = lines[l].replace("'en'", "'de'")
        #lde = lde.replace(words[l], twords[words.index(words[l])])
        ### IMPORTANT:  Comment out the line ABOVE that is using twords and uncomment the one BELOW to use the api once setup is compelete, there will be a similar line in each section.
        lde = lde.replace(words[l], translate_client.translate(words[l], target_language='de')['translatedText'])
        lde += "\n"
        # print("LDE", lde)
        with open("detest.sql",char,encoding = 'utf-8') as de:
            de.write(lde)
        ## FRENCH
        lfr = lines[l].replace("'en'", "'fr'")
        #lfr = lfr.replace(words[l], twords[words.index(words[l])])
        lfr = lfr.replace(words[l], translate_client.translate(words[l], target_language='fr')['translatedText'])
        lfr += "\n"
        # print("LFR", lfr)
        with open("frtest.sql",char,encoding = 'utf-8') as fr:
            fr.write(lfr)
        ## DUTCH
        lnl = lines[l].replace("'en'", "'nl'")
        #lnl = lnl.replace(words[l], twords[words.index(words[l])])
        lnl = lnl.replace(words[l], translate_client.translate(words[l], target_language='nl')['translatedText'])
        lnl += "\n"
        ## print("LNL",lnl)
        with open("nltest.sql",char,encoding = 'utf-8') as nl:
            nl.write(lnl)
        ## SPANISH
        les = lines[l].replace("'en'", "'es'")
        #les = les.replace(words[l], twords[words.index(words[l])])
        les = les.replace(words[l], translate_client.translate(words[l], target_language='es')['translatedText'])
        les += "\n"
        ## print("LES", les)
        with open("estest.sql",char,encoding = 'utf-8') as es:
            es.write(les)
        ## PORTUGESE
        lpt = lines[l].replace("'en'", "'pt'")
        lpt = lpt.replace(words[l], twords[words.index(words[l])])
        # lpt = lpt.replace(words[l], translate_client.translate(words[l], target_language='pt')['translatedText'])
        lpt += "\n"
        ## print("LPT", lpt)
        with open("pttest.sql",char,encoding = 'utf-8') as pt:
            pt.write(lpt)
        ## CHINESE (simplified)
        lzh = lines[l].replace("'en'", "'zh'")
        #lzh = lzh.replace(words[l], twords[words.index(words[l])])
        lzh = lzh.replace(words[l], translate_client.translate(words[l], target_language='zh')['translatedText'])
        lzh += "\n"
        ## print("LZH", lzh)
        with open("zhtest.sql",char,encoding = 'utf-8') as zh:
            zh.write(lzh)
        ## ARABIC
        lar = lines[l].replace("'en'", "'ar'")
        #slar = lar.replace(words[l], twords[words.index(words[l])])
        lar = lar.replace(words[l], translate_client.translate(words[l], target_language='ar')['translatedText'])
        lar += "\n"
        ## print("LAR", lar)
        with open("artest.sql",char,encoding = 'utf-8') as ar:
            ar.write(lar)
                       
finally:
    f.close()
    ## Making sure to close the file in case the code exits for any reason before finishing
