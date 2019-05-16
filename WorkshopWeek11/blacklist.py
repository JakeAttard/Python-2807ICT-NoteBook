from DNS import*

class Blacklist(DNS):
    """ Domain Name Server System """
    def __init__(self):
        self._domainsblacklist = set()
        DNS.__init__(self)

    def newblacklist(self, IPA):
        self._domainsblacklist.add(IPA)

    def  domainlookup(self, domain):
      #  print(domain,self._IPAdict[domain],self._domainsblacklist)
        if domain in self._IPAdict and self._IPAdict[domain] not in self._domainsblacklist:
            return (self._IPAdict[domain])
        else:
            return ("None")