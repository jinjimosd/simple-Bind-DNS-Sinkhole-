import pymysql
from configparser import ConfigParser

class mysql:


    def __init__(self):

        parser = ConfigParser()
        parser.read("config/config.ini")
        host = parser.get("database_config", "host")
        user = parser.get("database_config", "user")
        passwd = parser.get("database_config", "passwd")
        dbname = parser.get("database_config", "dbname")

        self.db = pymysql.connect(host, user, passwd, dbname)
        self.cursor = self.db.cursor()

    #select max id from table
    def select_max_id(self, table_name):

        sql = "SELECT MAX(id) AS MaxId FROM " + table_name

        #if database in dnssinkhole server is empty, id = 0
        max_id = 0

        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for row in results:
                if row[0] == None:
                    max_id = 0
                else:
                    max_id = row[0]
        except Exception as e:
            print(e)

        return max_id

    #update lastest id of domain to bindDNS table
    def update_lastest_id(self, now_max_id):

        sql = "UPDATE bindDNS SET id = " + str(now_max_id)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)

    #generate id 1 to bindDNS table
    def generate_id(self):

        sql = "INSERT INTO bindDNS (id) VALUES (1)"
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)

    #select all new domain 
    #new domain have id bigger than the biggest id from previous select
    def select_new_domains(self, previous_max_id):

        sql = "SELECT * FROM domains WHERE id > " + str(previous_max_id)
        
        #create empty list
        new_domain = []
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for row in results:
                new_domain.append(row[0])
        except Exception as e:
            print(e)

        return new_domain

    #delete all row of table
    def delete_all_row(self, table_name):

        sql = "DELETE FROM bindDNS"

        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)

    #close connection
    def close_connection(self):

        self.db.close()
