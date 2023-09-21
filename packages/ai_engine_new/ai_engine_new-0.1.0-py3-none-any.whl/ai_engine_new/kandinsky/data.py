
headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryrlQE4GkVXTOCFaq3',
            'Origin': 'https://editor.fusionbrain.ai',
            'Pragma': 'no-cache',
            'Referer': 'https://editor.fusionbrain.ai/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
        }

data = "------WebKitFormBoundaryrlQE4GkVXTOCFaq3\r\nContent-Disposition: form-data; name=\"params\"; filename=\"blob\"\r\nContent-Type: application/json\r\n\r\n{{\"type\":\"GENERATE\",\"style\":\"{style}\",\"width\":{width},\"height\":{height},\"generateParams\":{{\"query\":\"{prompt}\"}}}}\r\n------WebKitFormBoundaryrlQE4GkVXTOCFaq3--\r\n"

urls = {
    "ask": "https://api.fusionbrain.ai/web/api/v1/text2image/run?model_id=1",
    "check": "https://api.fusionbrain.ai/web/api/v1/text2image/status/{id}",
    "styles": "https://api.fusionbrain.ai/web/api/v1/text2image/styles"
}

ratios = {
        "1:1" : ["512", "512"],
        "16:9": ["1024", "576"],
        "9:16": ["576", "1024"],
        "3:2": ["960", "640"],
        "2:3": ["640", "960"]
    }