# short selling: trading a good you don't have 
# flat position: 0 share 
# long position: > 0 share 
# short position: < 0 share 

# marking an order long: selling shares you currently have 
# makring an order shaort: selling shares you have borrowed 

# Create marking position monitor 

import json

class PositionMaker:
    def __init__(self):
        self.shares = 0  

    def on_event(self, event):

        data = json.loads(event)

        order_type = data['type']
        order_id = data['order_id']
        pass 
