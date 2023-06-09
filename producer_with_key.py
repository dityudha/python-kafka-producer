from time import sleep
from json import dumps
from kafka import KafkaProducer
import json
#Envi Dev
producer = KafkaProducer(bootstrap_servers='10.243.215.122:9092')
#Envi Test
#producer = KafkaProducer(bootstrap_servers='10.243.215.138:9092')
for j in range(10):
    print("Data baru", j)
    producer.send(topic='acul-topic',partition=0, key=b'{"TLBID":2516136,"TLBTDT":90623,"TLBJSN":9004909,"TLBTPN":"UBP60112399001FFFFFF8888801891512483","TLBTMI":112337,"TLBSEQ":9004909,"TLBAPM":1,"TLBCOR":"N","TLTXOK":"Y","RRN":2928}', value=b'{"TLBWS":"  ","TLBSOV":"        ","TLBFP3":"%","FILL1":"   ","TLBPST":0,"TLBWC1":"u0000","TLBWC2":"u0000","TLBJC1":"u0000","TLBJC2":"u0000","TLBFP1":"","TLBFP2":"u0018","TLBF03":"0","TLBF05":"0","TLBF06":"0","TLBF09":"0","TLBF10":"0","TLBF11":"1220098030300","TLBF12":"0","TLBF13":"0","TLBF14":"0","TLBF17":"0","TLBF18":"0","TLBF19":"90623","TLBF20":"0","TLBF21":"150000","TLBF22":"1220098030300","TLBF23":"150000","TLBF24":"0","TLBF25":"0","TLBF26":"0","TLBF27":"0","TLBF28":"0","TLBF29":"7000260060900000000","TLBFP5":"","TLBFP4":"","TLBAFL":0,"TLBCIF":"1123330000000000000","TLBSRC":" ","TLBREN":" ","TLBIDC":" ","TLBXAT":" ","TLCUR3":"    ","TLBC01":" ","TLBC02":" ","TLBC03":" ","TLBC04":" ","TLBC05":" ","TLBC06":" ","TLBC07":" ","TLBC08":" ","TLBC09":" ","TLBC10":" ","TLBC11":" ","TLBC12":" ","TLBC13":" ","TLBC14":" ","TLBC15":" ","TLBC16":" ","TLBC17":" ","TLBC18":" ","TLBC19":" ","TLBC20":" ","TLBC21":" ","TLBC22":" ","TLBC23":" ","TLBC24":" ","TLBC25":" ","TLBC26":" ","TLBC27":" ","TLBC28":" ","TLBC29":" ","TLBC30":" ","TLXUFD":"260       ","TLBPRF":"     ","RMCKC":"0","RMADD1":"6575260609054439112333                  ","RMADD2":"                                        ","RMADD3":"                              ","RMPSTC":"          ","RMCNT":"0609054439657526              ","RMPYID":"                                        ","RMPAD1":"                                        ","RMPAD2":"                                        ","RMPAD3":"                              ","RMPPSC":"          ","RMPYCN":"                    ","RMSEHS":"    ","RMSECT":"   ","TLBRES":" ","RMTTR2":"                                        ","RMCLRC":" ","TLBBLP":"                ","TLBBL2":"                                        ","TLBFIL":"                                        ","TLBTMO":112337,"TLBFRD":"N","TLBFRT":"N","TLBTRN":"N","TLBGRP":"N","TLBRBD":"N","TLBTLO":"N","TLBSVO":"N","TLBFEO":"N","TLBREL":"N","TLBNXT":" ","TLBAFT":"A1","TLBPBT":"N","TLTXSR":"T","TLBB03":11500,"TLBB04":26000,"TLBB05":0,"TLBB06":11500,"TLBB07":0,"TLBB08":0,"TLBB09":0,"TLBB10":0,"TLBB11":0,"TLBB12":0,"TLBB13":0,"TLBB14":0,"TLBB15":0,"TLBB16":0,"TLBB17":0,"TLBB18":0,"TLBB19":0,"TLBB20":0,"TLBB21":0,"TLBB22":0,"TLBB23":0,"TLBB24":0,"TLBB25":0,"TLBB26":0,"TLBB27":0,"TLBB28":0,"TLBB29":0,"TLBB30":0,"TLBDC2":"C","TLBDC3":"C","TLBDC4":"D","TLBDC5":"D","TLBDC6":"C","TLBDC7":" ","TLBDC8":" ","TLBDC9":" ","T1BDC0":" ","T1BDC1":" ","T1BDC2":" ","T1BDC3":" ","T1BDC4":" ","T1BDC5":" ","T1BDC6":" ","T1BDC7":" ","T1BDC8":" ","T1BDC9":" ","T2BDC0":" ","T2BDC1":" ","T2BDC2":" ","T2BDC3":" ","T2BDC4":" ","T2BDC5":" ","T2BDC6":" ","T2BDC7":" ","T2BDC8":" ","T2BDC9":" ","T3BDC0":" ","TERR01":0,"TERR02":0,"TERR03":0,"TERR04":0,"TERR05":0,"TERR06":0,"TERR07":0,"TERR08":0,"TERR09":0,"TERR10":0,"TERR11":0,"TERR12":0,"TERR13":0,"TERR14":0,"TERR15":0,"TERL01":0,"TERL02":0,"TERL03":0,"TERL04":0,"TERL05":0,"TERL06":0,"TERL07":0,"TERL08":0,"TERL09":0,"TERL10":0,"TERL11":0,"TERL12":0,"TERL13":0,"TERL14":0,"TERL15":0,"TERT01":" ","TERT02":" ","TERT03":" ","TERT04":" ","TERT05":" ","TERT06":" ","TERT07":" ","TERT08":" ","TERT09":" ","TERT10":" ","TERT11":" ","TERT12":" ","TERT13":" ","TERT14":" ","TERT15":" ","TERQ01":" ","TERQ02":" ","TERQ03":" ","TERQ04":" ","TERQ05":" ","TERQ06":" ","TERQ07":" ","TERQ08":" ","TERQ09":" ","TERQ10":" ","TERQ11":" ","TERQ12":" ","TERQ13":" ","TERQ14":" ","TERQ15":" ","TLBCUD":"ATM","TLBID":2516136,"TLBTCD":4541,"TLBTDT":90623,"TLBJSN":9004909,"TLBF01":"2600000203310","TLBF02":"3200000","TLBF04":"0","TLBF07":"0","TLBF08":"0","TLBF15":"1220098030300","TLBF16":"3200000","TLBF30":"0","TLBCUR":"IDR ","TLBPRD":"          ","TLBTPN":"UBP60112399001FFFFFF8888801891512483    ","TLBPNM":"0006032988900160149 ","TLCUR1":"    ","TLCUR2":"    ","TLBDS1":"2                                                 ","TLBDS2":"T0800008  0000012134ATM-Menara Dea    ","RMUSRI":"                    ","RMSRC":0,"RMAPID":"                                        ","RMNAME":"0210782000T0800008        000000012134  ","RMPYNM":"                                        ","RMBBIC":"            ","TLBDS3":"P8888801891512483                       ","TLBTMI":112337,"TLBSEQ":9004909,"TLBAPM":1,"TLBCOR":"N","TLBDEL":" ","TLTXOK":"Y","TLSVBR":99105,"TLBB01":26000,"TLBB02":0,"TLBDC1":"D","SRC_TS":"2023-06-09T11:23:37.778064000000","TGT_TS":"2023-06-09T11:23:40.809000000000","RRN":2928}')
    sleep(0)
    producer.flush()