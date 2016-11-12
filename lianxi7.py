# -*- coding: utf-8 -*-

import time
import datetime
import json
import MySQLdb
import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning,InsecurePlatformWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)

conn = MySQLdb.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='111111',
    db='lianxi',
    charset='utf8'
)


def fetch_data(t, start, end):

    url = "https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT"
    params = u"queryDate=" + t + u"&from_station=" + start + u"&to_station=" + end
    try:
        s = requests.get(url, params = params.encode("utf-8"), verify = False)
    except Exception, e:
        print "requests url fail.", url
        return

    datas = json.loads(s.content)

    if "datas" not in datas["data"]:
        print "no train", t, start.encode("utf-8"), end.encode("utf-8")
        return


    for data in datas["data"]["datas"]:
        # 过滤jpg file
            try:
                cursor = conn.cursor()
                # 创建sql语句
                sql = 'insert into polls_station (from_station_name,to_station_name,start_station_name,end_station_name,start_time,arrive_time,tz_num,zy_num,ze_num,lishi,station_train_code) values ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")' % (
                    data['from_station_name'],data['to_station_name'], data['start_station_name'], data['end_station_name'],data['start_time'],data['arrive_time'],data['tz_num'],data['zy_num'],data['ze_num'],data['lishi'],data['station_train_code'])
                cursor.execute(sql)
                # commit
                conn.commit()
            except Exception as e:
                print 'Error', e
                conn.rollback()
    conn.close()



if __name__ == "__main__":

        fetch_data((datetime.datetime.now() + datetime.timedelta(days = 3)).strftime("%Y-%m-%d"), "HZH", "VAP")





    



    


    















