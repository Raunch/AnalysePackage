#!/usr/bin/python 
# -*- coding: utf-8 -*-
'''
Created on 20190618

@author: shun
'''
import os
import subprocess
import Constants

def decodeApks(apkfolder, decodefolder): 
    outFile = os.path.join(decodefolder, "result.txt")
    with open(outFile, "a", encoding="utf-8") as f:
        for apk in os.listdir(apkfolder):
            index = str(apk).index("apk")        
            apkName = str(apk)[:index-1]
            apkPath = os.path.join(apkfolder, apk)
            outPath = os.path.join(decodefolder, apkName)
            if not os.path.exists(outPath):
                os.makedirs(outPath)
            print (Constants.APKTOOL_COMMAND % (apkPath, outPath))
            command = (Constants.APKTOOL_COMMAND % (apkPath, outPath))
            result = subprocess.call(command, shell=True)
            if result != 0:
                print (str(apk) + "can not be decoded")
            result = foundAds(outPath)
            if result:
                info = str(apk) + ":"
                for item in result:
                    info = info + " " + item + " "
                info = info + "\n"    
                f.write(info)                
        f.close()
    
    
        '''
        found = False
        for root,dirs,files in os.walk(outPath):
            if found:
                continue
            for dir in dirs:
                if found:
                    continue
                foldPath = os.path.join(root,dir)
                for key in Constants.ADS_FILTER.keys():
                    keyfolder = str(key).replace(".", os.sep)
                    if str(foldPath).__contains__(keyfolder):
                        print (Constants.ADS_FILTER[key] + "has found")
                        found = True
                        continue


        pass
        '''
    pass

def foundAds(outPath):
    result = []
    for root,dirs,files in os.walk(outPath):
        for dir in dirs:
            foldPath = os.path.join(root,dir)
            for key in Constants.ADS_FILTER.keys():                
                keyfolder = str(key).replace(".", os.sep)
                if str(foldPath).__contains__(keyfolder):
                    if not result.__contains__(Constants.ADS_FILTER[key]):
                        result.append(Constants.ADS_FILTER[key])
                        print (Constants.ADS_FILTER[key] + " has found")                                                
                    continue
    return result                    
                    
                    
    

if __name__ == '__main__':
    apkfolder = os.sys.argv[1]
    decodefolder = os.sys.argv[2]
    decodeApks(apkfolder, decodefolder)
    #foundAds(os.sys.argv[3])
    pass