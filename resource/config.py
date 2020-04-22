import requests
#import os
#import sys
from requests_toolbelt.multipart.encoder import MultipartEncoder
requests.packages.urllib3.disable_warnings()
#path = os.path.abspath(os.path.dirname(sys.argv[0]))
path = './'
host = "web"

def loginad():
   burp0_url = "https://"+host+":443/admin/index.php?route=common/login"
   burp0_headers = {"Referer": "https://"+host+"/admin/", 
   "Cache-Control": "max-age=0", 
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
   "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3",
   "Content-Type": "multipart/form-data; boundary=---------------------------7e43b42b30a14", 
   "Upgrade-Insecure-Requests": "1", 
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", 
   "Accept-Encoding": "gzip, deflate", 
   "Connection": "close"}


   burp0_data = "-----------------------------7e43b42b30a14\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\nuser\r\n-----------------------------7e43b42b30a14\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\nbitnami1\r\n-----------------------------7e43b42b30a14--\r\n"
    # r=requests.post(burp0_url, headers=burp0_headers,  data=burp0_data,verify=False)
#cookies=r.cookies.get_dict()

#cookie
   #  cookies=r.cookies['OCSESSID']

#token
   session = requests.Session()
   res = session.post(burp0_url, headers=burp0_headers,  data=burp0_data,verify=False, allow_redirects=False)
   location=res.headers['location']
   cookies=res.cookies['OCSESSID']
   token=location[-32:]
     
   print(cookies)
   print(token)
   return {
    'cookies': cookies,
    'token': token
     }





def adddatefile():
    filename='datafill.sql'
    filepath=path+'datafill.sql'
    multipart_encoder = MultipartEncoder(
        fields={
            "import": (
            "datafill.sql", open(filepath,'rb'), 'application/octet-stream')
        },
        boundary='---------------------------7e4e614b0306'
    )

    burp0_data=multipart_encoder
    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken
    burp0_cookies = {"OCSESSID": adcookies, "__atuvc": "1%7C12%2C0%7C13%2C1%7C14", "currency": "USD", "language": "en-gb"}
    burp0_headers = {"Origin": "https://"+host, "Referer": "https://"+host+"/admin/index.php?route=tool/backup&user_token="+adtoken, "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "Content-Type": "multipart/form-data; boundary=---------------------------7e4e614b0306", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Cache-Control": "no-cache"}
  
    
    r=requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies,data=burp0_data,verify=False)
    print("add file")
    print(burp0_data)
    print(r.text)
    datetoken=r.text[-25:-16]
    print(datetoken)
    return {'datetoken':datetoken}



def sure():
    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacfwv6Pu&position=8688"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken, "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
    print(r.text)
    
    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacfwv6Pu&position=22122"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
    print(r.text)
    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacfwv6Pu&position=38337"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
    print(r.text)



    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacfwv6Pu&position=56503"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
    print(r.text)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacfwv6Pu&position=71968"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
    print(r.text)


    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacfwv6Pu&position=75913"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
    print(r.text)



    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacfwv6Pu&position=89750"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
    print(r.text)


    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacfwv6Pu&position=108595"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
    print(r.text)
    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=127632"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
    print("fail")
    print(r.text)


    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=147926"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
    print(r.text)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=168160"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
    print(r.text)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=186856"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
    print(r.text)



    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=205782"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)



    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=225718"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)


    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=245942"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=266161"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)


    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=286053"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)


    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=294649"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=302641"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=311161"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=330357"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=352744"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)


    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=359204"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
    print(r.text)
    #9

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=372009"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
    print(r.text)
    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=390754"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=413050"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
    print(r.text)
    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=420397"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)


    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=420793"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)


    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=443557"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)


    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=455346"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)


    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=467391"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
    print(r.text)
    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=479535"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=491651"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=503579"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=515730"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=527799"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)


    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=539731"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)


    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=552003"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=564250"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=576727"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=589107"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=601317"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=613857"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=626141"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=638337"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=650664"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=662861"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=675169"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=687329"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=699563"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=711624"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)


    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=723708"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=735913"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=735913"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=760406"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)


    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=772727"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=785010"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=797257"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=809491"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=822186"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=834426"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=846606"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=859172"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=871731"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=883961"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=896093"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=908229"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=921000"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=934612"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/opencart/system/storage/upload/bacDmuUY9&position=950135"
    burp0_cookies = {"__atuvc": "2%7C15", "OCSESSID":adcookies}
    burp0_headers = {"Referer": "https://opencart/admin/index.php?route=tool/backup&user_token="+adtoken+"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)


    print("sure")
    print(r.text)
    #print(r)

def check_config():
    burp0_url = "http://" + host + ":80"
    burp0_cookies = {"language": "zh-cn", "currency": "rmb"}
    burp0_headers = {"Upgrade-Insecure-Requests": "1",
                     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                     "Referer": "http://" + host + ":80",
                     "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    r = requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
    #print("check_config")
    #print(r.text)
    
    return r

if __name__ == "__main__":
    result1 = check_config()
    n=loginad()
    adcookies=n['cookies']
    adtoken=n['token']
    m=adddatefile()
    datetoken=m['datetoken']
    sure()
    result2 = check_config()

    target_info = '中国移动电子商场'

    if (target_info not in result1.text and target_info in result2.text):
        print('Config success!')
        exit(0)
    else:
        print('Config failed!')
        exit(-1)
