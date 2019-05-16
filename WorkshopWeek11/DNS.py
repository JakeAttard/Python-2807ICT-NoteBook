class DNS:
    def __init__(self):
        """First Domain name and IPA"""
        self._IPAdict = dict()

    def domainlookup(self,domainName):
        """Retrieve a domain name for a IPA"""
        if domainName in self._IPAdict:
            return ("IPA for domain name " + domainName + " is: ", self._IPAdict[domainName])
        else:
            return ("None")

    def change(self,changeDomain,changeIPA):
        """Change the domain name for an IPA"""
        if changeDomain in self._IPAdict:
            self._IPAdict[changeDomain] = changeIPA
            return ("Domain " +changeDomain+ " IPA has been changed to ", changeIPA)
        elif changeDomain not in self._IPAdict:
            self._IPAdict[changeDomain] = changeIPA
            return ("New domain " +changeDomain+ " has been added to IPA ", changeIPA)

    def upDateDomain(self, oldDomain,newDomain):
        return ("Domain name " +oldDomain+ " for IPA " + self._IPAdict[oldDomain] +" has been changed to ", newDomain)
        self._IPAdict[newDomain] = self._IPAdict[oldDomain]
        del self._IPAdict[oldDomain]

