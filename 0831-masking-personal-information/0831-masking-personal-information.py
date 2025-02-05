import re
class Solution(object):
    def maskPII(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s[0].isalpha():
            s=s.split('@')
            return( s[0][0].lower()+"*****"+s[0][-1].lower()+'@'+s[1].lower())
        else:
            corrected=re.sub(r'[^0-9]','',s)
            if len(corrected)==10:
                return "***-***-"+str(corrected[-4:])
            elif len(corrected)==11:
                return "+*-***-***-"+str(scorrected[-4:])
            elif len(corrected)==12:
                return "+**-***-***-"+str(corrected[-4:])
            elif len(corrected)==13:
                return "+***-***-***-"+str(corrected[-4:])

