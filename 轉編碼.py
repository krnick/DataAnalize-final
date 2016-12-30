#to support encodings
import codecs
import os


for dirPath, dirNames, fileNames in os.walk("./word"):
        for filename in fileNames:
                        with codecs.open("./word/"+filename, 'r') as file:
                                with codecs.open("./newkeyword/"+filename, 'w', encoding = 'utf8') as newfile:
                                        for line in file:
                                                #write output file
                                                print(line)
                                                newfile.write(line)
            


