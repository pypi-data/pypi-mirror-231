from typing import Dict

urls = {
    "js_filename": "https://dream.ai/create",
    "auth_key": "https://identitytoolkit.googleapis.com/v1/accounts:signUp",
    "draw_url": "https://paint.api.wombo.ai/api/v2/tasks",
    "styles": "https://paint.api.wombo.ai/api/styles"
}

auth_key_headers = {
    "authority": "identitytoolkit.googleapis.com",
    "accept": "*/*",
    "accept-language": "ru,en;q=0.9",
    "content-type": "application/json",
    "origin": "https://dream.ai",
    "sec-ch-ua": '"Chromium";v="110", "Not A(Brand";v="24", "YaBrowser";v="23"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "x-client-version": "Chrome/JsCore/9.1.2/FirebaseCore-web",
}

def headers_gen(auth_key: str) -> Dict:
    return {
        "authority": "paint.api.wombo.ai",
        "accept": "*/*",
        "accept-language": "ru,en;q=0.9",
        "authorization": f"bearer {auth_key}",
        "content-type": "text/plain;charset=UTF-8",
        "origin": "https://dream.ai",
        "referer": "https://dream.ai/",
        "sec-ch-ua": '"Chromium";v="110", "Not A(Brand";v="24", "YaBrowser";v="23"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaBrowser/23.3.1.895 Yowser/2.5 Safari/537.36",
        "x-app-version": "WEB-2.0.0",
    }