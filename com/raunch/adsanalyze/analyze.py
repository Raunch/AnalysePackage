#!/usr/bin/python 
# -*- coding: utf-8 -*-
'''
Created on 20190618

@author: shun
'''
import os
import subprocess
import Constants
import xml.etree.ElementTree as ET 

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
                info = str(apk) + " has ads : \n"
                for item in result:
                    info = info + item + "\n"
                info = info + "\n"    
                f.write(info)
                outputManifestInfo(outPath, f)

        f.close()
    
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
                    
def outputManifestInfo(output, f):
    manifestPath = os.path.join(output, 'AndroidManifest.xml')
    ET.register_namespace('android', "http://schemas.android.com/apk/res/android")
    tree = ET.parse(manifestPath)
    root = tree.getroot()
    packageName = root.get("package")
    print ("PackageName is : " + packageName + "\n")
    for child in root:
        if child.tag == 'application':
            info = "AndroidManifest has itmes : \n"
            print (info)
            for childItem in child:
                tag = childItem.tag
                if tag in ['activity', 'receiver', 'service']:
                    print(childItem.get('{http://schemas.android.com/apk/res/android}name'))
                    info = info + childItem.get('{http://schemas.android.com/apk/res/android}name') + '\n'
            f.write(info)               
               
    pass
    

if __name__ == '__main__':
    apkfolder = os.sys.argv[1]
    decodefolder = os.sys.argv[2]
    decodeApks(apkfolder, decodefolder)
    #foundAds(os.sys.argv[3])
    pass