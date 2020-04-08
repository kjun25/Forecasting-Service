from urllib.parse import urlencode, quote_plus, unquote
from urllib.request import Request, urlopen
from datetime import datetime
import json


# 기상청 API - 최신 기온(대전 유성구 온천2동)
def weather():
    now = datetime.now()
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtNcst'
    api_key = unquote('서비스 키')
    current_date = '%04d%02d%02d' % (now.year, now.month, now.day)
    current_hour = now.hour
    current_minute = now.minute
    if current_minute < 40:
        current_hour -= 1
    current_time = '%02d%02d' % (current_hour, current_minute)
    query_params = '?' + urlencode(
        {
            quote_plus('ServiceKey'): api_key,
            quote_plus('pageNo'): '1',
            quote_plus('numOfRows'): '4',
            quote_plus('dataType'): 'JSON',
            quote_plus('base_date'): current_date,
            quote_plus('base_time'): current_time,
            quote_plus('nx'): '66',
            quote_plus('ny'): '101'
        }
    )
    request = Request(url + query_params)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read().decode('utf-8')
    json_data = json.loads(response_body)
    temperature = json_data['response']['body']['items']['item'][3]['obsrValue']
    print(json_data)
    print('현재 시각 :', now, '\n동네 기온 :', temperature)


weather()



