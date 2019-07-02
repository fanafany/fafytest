def jttq():
    import requests
    import re
    from lxml import etree
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    url = 'http://www.tianqi4.com/xuzhou/'
    responses = requests.get(url,headers = headers).text
    res = re.compile(r'<p>(.*?)</p>')
    ress = res.findall(responses)
    sj_su = ','.join(ress)
    sj = sj_su[0:10]
    gw = sj_su[144:155]
    dw = sj_su[162:168]
    fx = sj_su[173:186]
    hz = sj + gw + dw + fx
    return hz



'''
今天,7月2日,周二,白天：<img src="/skins/Blue2012/icon2/101.png" width=30 height=30 /> 
多云夜间：<img src="/skins/Blue2012/icon2/101.png" width=30 height=30 /> 
多云,高温：36℃ 500hPa,低温：24℃ 65%,风向：东南风,风力：3-4 0%,
'''