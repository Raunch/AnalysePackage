#!/usr/bin/python 
# -*- coding: utf-8 -*-
'''
专门用来处理xml文件
'''
import xml.etree.ElementTree as ET 

class ETXml () :
    def __init__(self, file_path):
        self.file_path = file_path
        ET.register_namespace('android', "http://schemas.android.com/apk/res/android")
        tree = ET.parse(self.file_path)
        self._root = tree.getroot()
        self._package_name = self._root.get("package")

    def getElements(self):
        self._root.get
        pass