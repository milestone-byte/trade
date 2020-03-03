import requests
import json
import pymysql
 
code_list = []
 
dbconf = {'host':'127.0.0.1',
                'port':3306,
                'user':'root',
                'password':'root',
                'db':'shares',
                'charset':'utf8mb4',
                'cursorclass':pymysql.cursors.DictCursor}
 
def execsql(sql, databaseconf):
    '''connect mysql return result'''
    try:
        conn = pymysql.connect(**databaseconf)
        with conn.cursor() as cursor:
            try:
                cursor.execute(sql)
                conn.commit()
            except Exception as e:
                print(e)
                cursor.close()
        conn.close()
 
    except Exception as e:
        print(e)
 
 
def share_code():
   print('abc')
     
    with open('sh_info.txt', 'rU') as file:
        for code in file.readlines():
            code_list.append(code.strip())
 
    print(code_list)
 
 
def insert_db(url):
    response = requests.get(url)
    shares = response.text
    share = json.loads(shares[9:-1])
    data = share["Value"]
    date = data[49][:-9]
    sql = 'insert into share(name,code,now,rise,changehands,amplitude,priceearnings,marketrate,date) values("{name}","{code}","{now}","{rise}","{changehands}","{amplitude}","{priceearnings}","{marketrate}","{date}")'.format(name=data[2],code=data[1],now=data[25],rise=data[29],changehands=data[37],amplitude=data[50],priceearnings=data[38],marketrate=data[43],date=date)
 
    execsql(sql,dbconf)
    print(sql)
 
def main():
    share_code()
    # for code in code_list:
    #     if code[:2] == '60':
    #         sh_url = 'http://nuff.eastmoney.com/EM_Finance2015TradeInterface/JS.ashx?id={code}1'.format(code=code)
    #         try:
    #             insert_db(sh_url)
    #         except Exception as e:
    #             print(e)
    #     else:
    #         sz_url = 'http://nuff.eastmoney.com/EM_Finance2015TradeInterface/JS.ashx?id={code}2'.format(code=code)
    #         try:
    #             insert_db(sz_url)
    #         except Exception as e:
    #             print(e)
 
if __name__=="__main__":
    main()