# -*- coding:utf-8 -*-
import os.path
#!/usr/bin/python3

import pymysql

db = pymysql.connect("localhost","root","krnick","DataMining",charset="utf8" )
cursor = db.cursor()

for dirPath, dirNames, fileNames in os.walk("./newkeyword"):
        for filename in fileNames:
                if(filename.endswith(".txt")and filename!="words.txt"):
                        f=open("./newkeyword/"+filename,'r')
                        filecontent=str(f.read())
                        f.close()
                        print(filename)
                        print(filecontent)

                        cursor.execute('''INSERT INTO file(filename,content) VALUES  (%s,%s)''',(filename,filecontent) )
                        db.commit()
			
