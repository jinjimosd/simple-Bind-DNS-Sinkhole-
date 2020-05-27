
class bind_dns:


    def __init__(self):

        self.f = open("/etc/bind/Bind_DNS_Sinkhole_Config/named.conf.blacklists","a+")

    def update_blacklists(self, blacklists):

        for domain in blacklists:
            blackdomain = "zone \"" + str(domain) + "\" {type master; file \"/etc/bind/Bind_DNS_Sinkhole_Config/client.nowhere\"; }; \r\n"
            self.f.write(blackdomain)
        self.f.close()


