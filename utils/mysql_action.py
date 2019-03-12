import pymysql

class mysqlclass():
    def __init__(self,host,port,user,password,db,charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset

    def connect(self):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.password,
            db=self.db,
            charset=self.charset
        )
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()


    def select_one(self,sql,params=()):
        result = None
        try:
            self.connect()
            self.cursor.execute(sql,params)
            result = self.cursor.fetchone()
            self.close()
        except Exception as e:
            print('发生异常：',e)
        return result

    def select_all(self,sql,params=()):
        list = []
        try:
            self.connect()
            self.cursor.execute(sql,params)
            list = self.cursor.fetchall()
            self.close()
        except Exception as e:
            print('发生异常：',e)

    def insert(self,sql,params=()):
        return self.__edit(sql,params)

    def update(self,sql,params=()):
        return self.__edit(sql,params)

    def delete(self,sql,params=()):
        return  self.__edit(sql,params)

    def __edit(self,sql,params):
        count=0
        try:
            self.connect()
            count = self.cursor.execute(sql,params)
            self.conn.commit()
            self.close()
        except Exception as e:
            print('发生异常：',e)
        return count








