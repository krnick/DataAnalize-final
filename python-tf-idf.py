# -*- coding:utf-8 -*-
import os.path
import math
#!/usr/bin/python3

import pymysql

db = pymysql.connect("localhost","root","krnick","DataMining",charset="utf8" )
cursor = db.cursor()









##count the idf
idf_dict={}

for dirPath, dirNames, fileNames in os.walk("./newkeyword"):
        for filename in fileNames:
                if(filename.endswith(".wrd")):
                      
                        f=open("./newkeyword/"+filename)
                        for line in f:
                                first,second=line.strip().split(" ")

##                              sum the word of idf                                
                                if first in idf_dict.keys():
                                        idf_dict[first]+=1
                                else:
                                        idf_dict[first]=1                  

for idf in idf_dict:
        print(  str(idf)    +"\t 出現次數:"+ str( idf_dict[idf])  +"\t idf:"  +str(   math.log10(     100/ idf_dict[idf] )     ))
        





##count the tf

tf_dict = {}

for dirPath, dirNames, fileNames in os.walk("./newkeyword"):
        for filename in fileNames:
                if(filename.endswith(".wrd")):


                        print("---------file:"+ filename+"-----")
                        
                        f=open("./newkeyword/"+filename)
                        for line in f:
                                first,second=line.strip().split(" ")


                                
                                tf_dict[first]=second




                        ##deal with output tf
                        maxvalue=max(tf_dict, key=tf_dict.get)

                        ##key name
                        print(maxvalue)
                        ##key value
                        the_biggest=tf_dict[maxvalue]

                        for every_word in tf_dict:
                                vle=tf_dict[every_word]
                                tf_with_idf=float(vle) / float(the_biggest) *     math.log10(100/ idf_dict[every_word] ) 

                                print(every_word+"\t value="+vle  +"\t   tf:" + str(float(vle) / float(the_biggest) ) +"\t tf*idf :" +   str( tf_with_idf )   )
			
                                f1=str(filename)
                                f2=str(every_word )
                                f3=str(vle)
                                f4=str(float(vle) / float(the_biggest))
                                f5=str( tf_with_idf )
	
                                cursor.execute('''INSERT INTO keyword(filename,key_word,value,tf, tf_idf) VALUES  (%s,%s,%s,%s,%s)''',(f1,f2,f3,f4,f5) )
                                db.commit()
				
                        print("----------------------------------")


                        tf_dict.clear()


db.close()

