# Implement the class below, keeping the constructor's signature unchanged; it should take no arguments.
import json
class MarkingPositionMonitor:
    def __init__(self):
        self.orders = {} # {order_id: {order info}}
        self.marking_pos = {} # {symbol: marking position}
     
    def on_event(self, message):        
        data = json.loads(message)
        type = data["type"]
        if type == "NEW":
            return self.place_order(data)
        elif type == "ORDER_ACK":
            return self.order_ack(data)
        elif type == "ORDER_REJECT":
            return self.order_rej(data)
        elif type == "CANCEL":
            return self.cancel(data)
        elif type == "CANCEL_ACK":
            return self.cancel_ack(data)
        elif type == "CANCEL_REJECT":
            return self.cancel_rej(data)
        elif type == "FILL":
            return self.fill(data)
     
    def place_order(self, data):
        order_id = data["order_id"]
        symbol = data["symbol"]
        quantity = data["quantity"]
        if data["side"] == "SELL":
            # add order to market
            self.orders[order_id] = {"symbol": symbol, "side": "SELL", "quantity": quantity}
            # update marking position
            self.marking_pos[symbol] = self.marking_pos.get(symbol, 0) - quantity
        elif data["side"] == "BUY":
            # add order to market
            self.orders[order_id] = {"symbol": symbol, "side": "BUY", "quantity": quantity}
            # update marking positon
            self.marking_pos[symbol] = self.marking_pos.get(symbol, 0)
             
        return self.marking_pos[symbol]
 
    def order_ack(self, data):
        order_id = data["order_id"]
        symbol = self.orders[order_id]["symbol"]
        return self.marking_pos[symbol]
     
    def order_rej(self, data):
        order_id = data["order_id"]
        order = self.orders[order_id]
        symbol = order["symbol"]
        if "reject" not in order:
            order["reject"] = True
            if order["side"] == "SELL":
                # add quantity back if order is sell
                quantity = order["quantity"]
                self.marking_pos[symbol] += quantity
            # remove order from orders no matter it is buy or sell
            # self.orders.pop(order_id)         
        return self.marking_pos[symbol]
 
    def cancel(self, data):
        order_id = data["order_id"]
        symbol = self.orders[order_id]["symbol"]
        return self.marking_pos[symbol]
         
    def cancel_ack(self, data):
        order_id = data["order_id"]
        order = self.orders[order_id]
        symbol = order["symbol"]
        # check if the order is sell
        if order["side"] == "SELL":
            # add quantity back and remove the order
            quantity = order["quantity"]
            self.marking_pos[symbol] += quantity
 
        # remove order from orders no matter it is buy or sell
        # self.orders.pop(order_id)
        return self.marking_pos[symbol]
                 
    def cancel_rej(self, data):
        order_id = data["order_id"]
        order = self.orders[order_id]
        symbol = order["symbol"]
        return self.marking_pos[symbol]
     
    def fill(self, data):
        order_id = data["order_id"]
        filled_quantity = data["filled_quantity"]
        order = self.orders[order_id]
        symbol = order["symbol"]
        if filled_quantity <= order["quantity"]:
            order["quantity"] -= filled_quantity
            if order["side"] == "BUY":
                self.marking_pos[symbol] += filled_quantity
        else:    
            if order["side"] == "BUY":
                self.marking_pos[symbol] += order["quantity"]
                order["quantity"] = 0
        return self.marking_pos[symbol]