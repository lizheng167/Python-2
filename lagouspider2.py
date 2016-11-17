#-*- coding: utf-8 -*-
import os, time, random
import requests
from multiprocessing import Pool

def scrapy(name,jobname):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    req_url = 'http://www.lagou.com/jobs/positionAjax.json?'
    headers = {
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding': 'gzip, deflate',
        'Host': 'www.lagou.com',
        'Origin': 'http://www.lagou.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'http://www.lagou.com',
        'Proxy-Connection': 'keep-alive',
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': None
    }
    maxpagenum = \
        int(requests.post(req_url, params={'first': 'false', 'pn': 1, 'kd': jobname}, headers=headers).json()[
                'content']['positionResult']['totalCount']) / 15

    flag = True
    num = 1

    filedir = jobname

    if os.path.exists(filedir) is not True or os.path.isdir(filedir) is not True:
        os.mkdir(filedir)

    while flag:
        payload = {'first': 'false', 'pn': str(num), 'kd': jobname}

        response = requests.post(req_url, params=payload, headers=headers)
        if num > maxpagenum:
            flag = False

        if response.status_code == 200:
            job_json = response.json()['content']['positionResult']['result']
            print('正在爬取第 ' + str(num) + ' 页的数据...')
            #print(job_json)

            with open(jobname + os.path.sep + str(num) + '.json', 'wt') as f:
                f.write(str(job_json))
                f.flush()
                f.close()

        else:
            print('connect error! url = ' + req_url)

        num += 1
        time.sleep(random.random() * 3)
        end = time.time()
        print 'Task %s runs %0.2f seconds.' % (name, (end - start))
        # time.sleep(2)


if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    p = Pool()
    job = ["数据挖掘", "Java", "PHP","Python","Hadoop","搜索算法","精准推荐","HTML5","iOS","计算机视觉","架构师"]
    for i in range(len(job)):
        p.apply_async(scrapy, args=(i,job[i]))
    p.close()
    p.join()
    print 'All subprocesses done.'