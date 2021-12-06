import pymysql

loginInfo = {
    'host':'localhost',
    'port':3306,
    'user':'root',
    'passwd':'Sss06250721',
    'db':'azuredata',
    'charset':'utf8mb4'
}

conn= pymysql.connect(**loginInfo)
cursor = conn.cursor()

sql ="""SELECT a.cname, a.cost,a.datatime,b.fullname,b.tel
from userdata a natural join userprofile b
where a.CUSTOMERNO=1;
"""

cursor.execute(sql)

data = cursor.fetchall()
#print(data)

cursor.close()
conn.close()