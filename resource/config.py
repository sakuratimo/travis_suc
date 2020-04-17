import requests
#import os
#import sys
from requests_toolbelt.multipart.encoder import MultipartEncoder
requests.packages.urllib3.disable_warnings()
#path = os.path.abspath(os.path.dirname(sys.argv[0]))
path = './/'
host = "opencart"

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
     
   #print(cookies)
   #print(token)
   return {
    'cookies': cookies,
    'token': token
     }





def adddatefile():
    filename='datafill.sql'
    filepath=path+'//datafill.sql'
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
    burp0_headers = {"Origin": "https://"+host+"", "Referer": "https://"+host+"/admin/index.php?route=tool/backup&user_token="+adtoken, "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "Content-Type": "multipart/form-data; boundary=---------------------------7e4e614b0306", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Cache-Control": "no-cache"}
  
    
    r=requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies,data=burp0_data,verify=False)
    #print(r.text)
    datetoken=r.text[-25:-16]
    return {'datetoken':datetoken}






def sure():
    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=8688"
    burp0_cookies = {"__atuvc": "1%7C12%2C0%7C13%2C1%7C14", "currency": "USD", "language": "zh-cn", "OCSESSID": adcookies}
    burp0_headers = {"Referer": "https://"+host+"/admin/index.php?route=tool/backup&user_token="+adtoken, "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)



    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=22122"
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)



    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=38337"
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)



    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=56503"
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)


    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=71968"
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)



    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=75913"
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)



    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=89750"
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=108595"
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=127632" 
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=147926"
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=168160"
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=186856"
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=205782"
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=225718"
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=245942"
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)


    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=266161"
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=286053"
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=294649"
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=302641"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=311161"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=330357"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=352744"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=359204"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=372009"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=390754"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)


    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=413050"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=420397"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=420793"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=443557"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=455346"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=467391"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=479535"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=491651"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=503579"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=515730"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=527799"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)


    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=539731"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=552003"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=564250"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=576727"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=589107"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=601317"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=613857"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=626141"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=638337"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=650664"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=662861"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=675169"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=687329"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)


    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=699563"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=711624"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=723708"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=735913"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=748260"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=760406"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=772727"
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)



    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=785010"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=797257"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=809491"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=822186"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=834426"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=846606"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=859172"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=871731"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=883961"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=896093"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=908229"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=921000"

    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=934612"

    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
    #print(r.text)


    burp0_url = "https://"+host+":443/admin/index.php?route=tool/backup/import&user_token="+adtoken+"&import=/bitnami/"+host+"/system/storage/upload/"+datetoken+"&position=950135"
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
    #print(r.text)
    #print(r)

def check_config():
    burp0_url = "http://" + host + ":80"
    burp0_cookies = {"language": "zh-cn", "currency": "rmb"}
    burp0_headers = {"Upgrade-Insecure-Requests": "1",
                     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                     "Referer": "http://" + host + ":80",
                     "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    r = requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
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
