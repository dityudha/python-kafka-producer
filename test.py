from time import sleep
from json import dumps
from kafka import KafkaProducer
import json
producer = KafkaProducer(
    bootstrap_servers=['10.243.215.122:9092'],
    value_serializer=lambda m: json.dumps(m).encode('ascii')
)
for j in range(5):
    print("Data baru", j)
    key = {"RMADD1":"Testing","RMADD2":"Testing","TLBCUD":"DII","TLBID":j}
    data = {"RMADD1":"Testing","RMADD2":"Testing","RMADD3":"Testing","RMAPID":"Testing","RMBBIC":"Testing","RMCKC":1250000,"RMCLRC":"Y","RMCNT":"Testing","RMNAME":"Testing","RMPAD1":"Testing","RMPAD2":"Testing","RMPAD3":"Testing","RMPPSC":"Testing","RMPSTC":"Testing","RMPYCN":"Testing","RMPYID":"Testing","RMPYNM":"Testing","RMSECT":"Tes","RMSEHS":"Test","RMSRC":12,"RMTTR2":"Testing","RMUSRI":"Testing","TERR01":129,"TLBAFT":"MO","TLBAPM":1,"TLBB01":11500,"TLBB02":0,"TLBBL2":"Y","TLBCIF":1250000,"TLBCOR":"N","TLBCUD":"DII","TLBCUR":"IDR ","TLBDC1":"D","TLBDC2":"D","TLBDC3":"C","TLBDEL":"Y","TLBDS1":"XMCM001","TLBDS2":"99129BTS Medan01","TLBDS3":"May-23","TLBF01":600991565,"TLBF02":1000000000,"TLBF03":1250000,"TLBF04":1250000,"TLBF05":1000000000,"TLBF06":1000000000,"TLBF07":100000000,"TLBF08":100000000,"TLBF09":1250000,"TLBF10":1250000,"TLBF11":1250000,"TLBF12":1250000,"TLBF13":1250000,"TLBF14":1250000,"TLBF15":11011108,"TLBF16":1000000000,"TLBF17":1250000,"TLBF18":1250000,"TLBF19":1250000,"TLBF20":1250000,"TLBF21":1250000,"TLBF22":1250000,"TLBF23":1250000,"TLBF24":1250000,"TLBF25":1250000,"TLBF26":1250000,"TLBF27":1250000,"TLBF28":1250000,"TLBF29":1250000,"TLBF30":1250000,"TLBFP3":"\f","TLBID":j,"TLBJSN":13,"TLBPNM":"Testing","TLBPRD":"Testing","TLBPRF":"Test","TLBRES":"Y","TLBSEQ":13,"TLBSRC":"Y","TLBTCD":9417,"TLBTDT":110523,"TLBTMI":154102,"TLBTMO":154102,"TLBTPN":"DB23051115182802764TRXCD","TLBWS":"id","TLCUR1":"IDR","TLCUR2":"IDR","TLCUR3":"IDR","TLSVBR":99129,"TLTXOK":"Y","TLXUFD":"Testing"}
    producer.send('abcs-topic', key=key, value=data)
    sleep(0.0)
    producer.flush()