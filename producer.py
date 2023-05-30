from time import sleep
from json import dumps
from kafka import KafkaProducer
import json
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda m: json.dumps(m).encode('ascii')
)
for j in range(1000):
    print("Data baru", j)
    data = {"TLBWS":"  ","TLBSOV":"        ","TLBFP3":"\u0000","FILL1":"   ","TLBPST":0,"TLBWC1":"\u0000","TLBWC2":"\u0000","TLBJC1":"\u0000","TLBJC2":"\u0000","TLBFP1":"\u0000","TLBFP2":"—","TLBF03":"0","TLBF05":"0","TLBF06":"0","TLBF09":"0","TLBF10":"0","TLBF11":"0","TLBF12":"0","TLBF13":"0","TLBF14":"0","TLBF17":"0","TLBF18":"0","TLBF19":"0","TLBF20":"0","TLBF21":"0","TLBF22":"0","TLBF23":"0","TLBF24":"0","TLBF25":"0","TLBF26":"0","TLBF27":"0","TLBF28":"0","TLBF29":"0","TLBFP5":"\u0000","TLBFP4":"\u0000","TLBAFL":0,"TLBCIF":"0","TLBSRC":" ","TLBREN":" ","TLBIDC":" ","TLBXAT":" ","TLCUR3":"    ","TLBC01":" ","TLBC02":" ","TLBC03":" ","TLBC04":" ","TLBC05":" ","TLBC06":" ","TLBC07":" ","TLBC08":" ","TLBC09":" ","TLBC10":" ","TLBC11":" ","TLBC12":" ","TLBC13":" ","TLBC14":" ","TLBC15":" ","TLBC16":" ","TLBC17":" ","TLBC18":" ","TLBC19":" ","TLBC20":" ","TLBC21":" ","TLBC22":" ","TLBC23":" ","TLBC24":" ","TLBC25":" ","TLBC26":" ","TLBC27":" ","TLBC28":" ","TLBC29":" ","TLBC30":" ","TLXUFD":"          ","TLBPRF":"     ","RMCKC":"0","RMADD1":"                                        ","RMADD2":"                                        ","RMADD3":"                              ","RMPSTC":"          ","RMCNT":"                              ","RMPYID":"                                        ","RMPAD1":"                                        ","RMPAD2":"                                        ","RMPAD3":"                              ","RMPPSC":"          ","RMPYCN":"                    ","RMSEHS":"    ","RMSECT":"   ","TLBRES":" ","RMTTR2":"1150007242961                           ","RMCLRC":" ","TLBBLP":"                ","TLBBL2":"                                        ","TLBFIL":"                                        ","TLBTMO":101439,"TLBFRD":"N","TLBFRT":"N","TLBTRN":"N","TLBGRP":"N","TLBRBD":"N","TLBTLO":"N","TLBSVO":"N","TLBFEO":"N","TLBREL":"N","TLBNXT":" ","TLBAFT":"I6","TLBPBT":" ","TLTXSR":" ","TLBB03":0,"TLBB04":0,"TLBB05":0,"TLBB06":0,"TLBB07":0,"TLBB08":0,"TLBB09":0,"TLBB10":0,"TLBB11":0,"TLBB12":0,"TLBB13":0,"TLBB14":0,"TLBB15":0,"TLBB16":0,"TLBB17":0,"TLBB18":0,"TLBB19":0,"TLBB20":0,"TLBB21":0,"TLBB22":0,"TLBB23":0,"TLBB24":0,"TLBB25":0,"TLBB26":0,"TLBB27":0,"TLBB28":0,"TLBB29":0,"TLBB30":0,"TLBDC2":" ","TLBDC3":" ","TLBDC4":" ","TLBDC5":" ","TLBDC6":" ","TLBDC7":" ","TLBDC8":" ","TLBDC9":" ","T1BDC0":" ","T1BDC1":" ","T1BDC2":" ","T1BDC3":" ","T1BDC4":" ","T1BDC5":" ","T1BDC6":" ","T1BDC7":" ","T1BDC8":" ","T1BDC9":" ","T2BDC0":" ","T2BDC1":" ","T2BDC2":" ","T2BDC3":" ","T2BDC4":" ","T2BDC5":" ","T2BDC6":" ","T2BDC7":" ","T2BDC8":" ","T2BDC9":" ","T3BDC0":" ","TERR01":0,"TERR02":0,"TERR03":0,"TERR04":0,"TERR05":0,"TERR06":0,"TERR07":0,"TERR08":0,"TERR09":0,"TERR10":0,"TERR11":0,"TERR12":0,"TERR13":0,"TERR14":0,"TERR15":0,"TERL01":0,"TERL02":0,"TERL03":0,"TERL04":0,"TERL05":0,"TERL06":0,"TERL07":0,"TERL08":0,"TERL09":0,"TERL10":0,"TERL11":0,"TERL12":0,"TERL13":0,"TERL14":0,"TERL15":0,"TERT01":" ","TERT02":" ","TERT03":" ","TERT04":" ","TERT05":" ","TERT06":" ","TERT07":" ","TERT08":" ","TERT09":" ","TERT10":" ","TERT11":" ","TERT12":" ","TERT13":" ","TERT14":" ","TERT15":" ","TERQ01":" ","TERQ02":" ","TERQ03":" ","TERQ04":" ","TERQ05":" ","TERQ06":" ","TERQ07":" ","TERQ08":" ","TERQ09":" ","TERQ10":" ","TERQ11":" ","TERQ12":" ","TERQ13":" ","TERQ14":" ","TERQ15":" ","TLBCUD":"VE ","TLBID":9919222,"TLBTCD":9,"TLBTDT":290523,"TLBJSN":5873,"TLBF01":"1150007242961","TLBF02":"0","TLBF04":"0","TLBF07":"0","TLBF08":"0","TLBF15":"0","TLBF16":"0","TLBF30":"0","TLBCUR":"    ","TLBPRD":"          ","TLBTPN":"                                        ","TLBPNM":"                    ","TLCUR1":"    ","TLCUR2":"    ","TLBDS1":"                                                  ","TLBDS2":"                                        ","RMUSRI":"                    ","RMSRC":0,"RMAPID":"                                        ","RMNAME":"                                        ","RMPYNM":"                                        ","RMBBIC":"            ","TLBDS3":"                                        ","TLBTMI":101439,"TLBSEQ":5873,"TLBAPM":1,"TLBCOR":"N","TLBDEL":" ","TLTXOK":"Y","TLSVBR":0,"TLBB01":0,"TLBB02":0,"TLBDC1":" ","SRC_TS":"2023-05-29T10:14:39.476512000000","TGT_TS":"2023-05-29T10:14:43.195000000000","RRN":1668}
    producer.send('svrkafkatest.ref_04k.sourcedb.bmodscbsi.tllog-json', value=data)
    sleep(0)
    producer.flush()