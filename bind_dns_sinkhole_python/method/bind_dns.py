
class bind_dns:


    def __init__(self):

        self.f = open("/etc/bind/named.conf.blacklists","a+")

    def update_blacklists(self, blacklists):

        for domain in blacklists:
            blackdomain = "zone \"" + str(domain) + "\" {type master; file \"/etc/bind/client.nowhere\"; }; \r\n"
            self.f.write(blackdomain)
        self.f.close()


