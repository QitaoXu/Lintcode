class UnionFind:
    
    def __init__(self, n):
        
        self.father = {i : i for i in range(n)} 
        self.count = n
        
    def union(self, a, b):
        
        a_root = self.find(a)
        b_root = self.find(b)
        
        if a_root == b_root:
            
            return 
        
        self.father[b_root] = a_root
        
        self.count -= 1 
        
    def find(self, point):
        
        path = [] 
        
        while point != self.father[point]:
            
            path.append(point)
            
            point = self.father[point]
            
        for p in path:
            
            self.father[p] = point 
            
        return point 
        


class Solution:
    """
    @param accounts: List[List[str]]
    @return: return a List[List[str]]
    """
    def accountsMerge(self, accounts):
        # write your code here
        
        self.uf = UnionFind(len(accounts))
        
        email_to_ids = self.get_email_to_ids(accounts)
        
        for _, ids in email_to_ids.items():
            
            root_id = ids[0]
            
            for user_id in ids[1:]:
            
                self.uf.union(root_id, user_id)
                
                
                
        id_to_email_set = self.get_id_to_emails_set(accounts)
        
        merged_accounts = []
        
        for user_id, email_set in id_to_email_set.items():
            
            merged_accounts.append( [accounts[user_id][0]] + sorted(email_set) )
            
        return merged_accounts
            
            
        
    def get_email_to_ids(self, accounts):
        
        email_to_ids = {}
        
        for uesr_id, account in enumerate(accounts):
            
            for email in account[1:]:
                
                email_to_ids[email] = email_to_ids.get(email, [])
                
                email_to_ids[email].append(uesr_id)
                
        return email_to_ids
        
        
        
    def get_id_to_emails_set(self, accounts):
        
        id_to_email_set = {} 
        
        for user_id, account in enumerate(accounts):
            
            root_user_id = self.uf.find(user_id)
            
            email_set = id_to_email_set.get(root_user_id, set())
            
            for email in account[1:]:
                
                email_set.add(email)
                
            id_to_email_set[root_user_id] = email_set
            
        return id_to_email_set