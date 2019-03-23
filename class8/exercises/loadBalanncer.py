import random

class LoadBalancer:
    def __init__(self):
        # do intialization if necessary
        self.servers = [] 
        
        self.server_id_to_idx = {}

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    def add(self, server_id):
        # write your code here
        
        if server_id not in self.server_id_to_idx:
            
            self.servers.append(server_id)
            
            self.server_id_to_idx[server_id] = len(self.servers) - 1 

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, server_id):
        # write your code here
        
        if server_id in self.server_id_to_idx:
            
            last_server = self.servers[-1]
            
            cur_idx = self.server_id_to_idx[server_id]
            
            self.servers[cur_idx] = last_server
            
            self.server_id_to_idx[last_server] = cur_idx
            
            self.servers.pop()
            
            del self.server_id_to_idx[server_id]
    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        # write your code here
        
        return self.servers[random.randint(0, len(self.servers) - 1)]