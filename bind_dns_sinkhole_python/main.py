from method.bind_dns import bind_dns
from method.mysql import mysql
from method.util import util


def main():
    
    mysql_ob = mysql()
    bind_dns_ob = bind_dns()
    util_ob = util()

    previous_max_id = mysql_ob.select_max_id("bindDNS")
    now_max_id = mysql_ob.select_max_id("domains")
    print(previous_max_id)

    #
    if(previous_max_id == 0):
        mysql_ob.generate_id()
        blacklists = mysql_ob.select_new_domains(previous_max_id)
        bind_dns_ob.update_blacklists(blacklists)
        mysql_ob.update_lastest_id(now_max_id)
        util_ob.save_datetime_update()
        mysql_ob.close_connection()
    elif(previous_max_id < now_max_id):
        blacklists = mysql_ob.select_new_domains(previous_max_id)
        bind_dns_ob.update_blacklists(blacklists)
        mysql_ob.update_lastest_id(now_max_id)
        util_ob.save_datetime_update()
        mysql_ob.close_connection()
    else:
        exit(0)

if __name__ == "__main__":
    main()
