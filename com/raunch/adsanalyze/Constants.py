#!/usr/bin/python 
# -*- coding: utf-8 -*-
'''
Created on 20190618

@author: shun
'''

APKTOOL_COMMAND = "apktool d %s -o %s -f"

ADS_FILTER = {"com.adcolony" : "AdColony",
              "com.google.android.gms.ads" : "AdMob",
              "com.amazon.device.ads" : "Amazon",
              "com.applovin" : "AppLovin",
              "com.appnext" : "AppNext",
              "com.batmobi" : "Batmobi",
              "com.chartboost.sdk" : "Chartboost",
              "io.display.sdk" : "DisplayIO",
              "com.duapps.ad" : "DAP",
              "com.facebook.ads" : "Facebook",
              "com.flurry.android.ads" : "Flurry",
              "com.fyber.inneractive.sdk" : "Fyber",
              "com.inmobi.ads" : "InMobi",
              "com.ironsource" : "IronSource",
              "com.mopub" : "MoPub",
              "com.tapjoy" : "Tapjoy",
              "com.unity3d" : "Unity",
              "com.vungle.warren" : "Vungle",
              "com.ad_stir" : "Ad_Stir",
              "com.socdm.d.adgeneration" : "ADGeneration",
              "net.nend.android" : "Nend",  
              "jp.maio.sdk.android" : "Maio"            
              }