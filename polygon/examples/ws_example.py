from wscore import WebSocketClient, STOCKS_CLUSTER
import json

def connection_message(message):
    print("Connecting to Polygon WebSocket Client", message)
    print(message[39:-2])
    
def main():
    key = "_t__ozhe3p5ACaYlHpPk2y4oEj7KkElP"
    my_client = WebSocketClient(STOCKS_CLUSTER, key, connection_message)
    my_client.run_async()
    f = open("StockList.dat", 'r')
    for line in f:
        jmsg = my_client.subscribe("A."+line)
        print(jmsg)
        
 def on_message(self, msg):
    print(json.dumps(msg, indent=4, sort_keys=True))
    self.message_count += 1
 



''' Move this part of code outside the client before deployment'''
if __name__ == "__main__":
    main()
