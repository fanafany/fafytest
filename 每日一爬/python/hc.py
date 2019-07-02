from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '16650822'
API_KEY = '5DOXosjtN8NxG5wlF0C4wIzm'
SECRET_KEY = 'oCSfGx5iKBLFzpQHoag7AfgKw0jlBnht'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

result = client.synthesis('你好百度,测试一下看看', 'zh', 1, {
    'vol': 5, 'per': 4
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)
