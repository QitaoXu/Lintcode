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
        self.symbol_to_shares = {} 
        self.order_id_to_info = {} 

    def on_event(self, event):

        data = json.loads(event)

        order_type = data['type']
        order_id = data['order_id']
        pass 

    def on_new(self, data, order_id):

        side = data["side"] 
        symbol = data["symbol"]
        quantity = data["quantity"] 

        if side == "BUY":

            self.symbol_to_shares[symbol] = self.symbol_to_shares.get(symbol, 0)
            self.order_id_to_info[order_id] = [symbol, side, quantity]
        
        if side == "SELL":

            self.symbol_to_shares[symbol] = self.symbol_to_shares.get(symbol, 0) - quantity
            self.order_id_to_info[order_id] = [symbol, side, quantity]

        return self.symbol_to_shares[symbol]

    def on_order_ack(self, data, order_id):

        symbol, side, quantity = self.order_id_to_info[order_id] 

        if side == "BUY":
            pass 

        if side == "SELL":
            pass 

        return self.symbol_to_shares.setdefault(symbol, 0) 

    def on_order_rej(self, data, order_id):

        symbol, side, quantity = self.order_id_to_info[order_id]

        if side == "BUY":
            del self.order_id_to_info[order_id] 

        if side == "SELL":
            self.symbol_to_shares[symbol] += quantity 
            del self.order_id_to_info[order_id]

        return self.symbol_to_shares.setdefault(symbol, 0)  

    def on_cancel(self, data, order_id):

        symbol, side, quantity = self.order_id_to_info[order_id]

        return self.symbol_to_shares.setdefault(symbol, 0) 

    def on_cancel_ack(self, data, order_id):

        
        symbol, side, quantity = self.order_id_to_info[order_id] 

        if side == "BUY":

            del self.order_id_to_info[order_id] 

        if side == "SELL":

            self.symbol_to_shares.get(symbol, 0) + quantity 

            del self.order_id_to_info[order_id] 

        return self.symbol_to_shares.setdefault(symbol, 0) 

    def on_cancel_rej(self, data, order_id):

        pass 

    def fill(self, data, order_id):

        symbol, side, quantity = self.order_id_to_info[order_id] 

        filled_quantity, remaining_quantity = data["filled_quantity"], data["remaining_quantity"]

        self.symbol_to_shares[symbol] = self.symbol_to_shares.get(symbol, 0) + filled_quantity

        if remaining_quantity == 0:

            del self.order_id_to_info[order_id]

        else:
            self.order_id_to_info[order_id] = [symbol, side, remaining_quantity] 

        return self.symbol_to_shares.setdefault(symbol, 0) 