class Solution:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    """
    def restoreIpAddresses(self, s):
        # write your code here
        results = []
        
        if not s:
            return results
            
        ip = [] 
        
        self.restoreIpAddressesHelper(s, 0, [], results)
        
        return results
    
    def restoreIpAddressesHelper(self, s, sub, ip, results):
        
        if sub == 4:
            if s == '':
                results.append('.'.join(ip))
            return
                
        for i in range(1, 4):
            
            if i <= len(s):
                
                prefix = s[:i]
                
                if int(prefix) <= 255:
                    
                    ip.append(prefix)
                    
                    self.restoreIpAddressesHelper(s[i:], sub + 1, ip, results)
                    
                    ip.pop()
                
                if s[0] == '0':
                    break