class Order:
    def __init__(self, is_buy, qty, price):
        self.is_buy = is_buy
        self.qty = qty
        self.price = price

    def __repr__(self):
        return '{} {}@${:.1f}'.format(
            'buy' if self.is_buy else 'sell',
            self.qty,
            self.price)
    
    def __gt__(self, other):
        return self.price > other.price

class OrderBook:
    def __init__(self):
        self._orders = []

    def __enter__(self):
        return self

    def __exit__(self, *args):
        '''
        formats and prints the order book as the test cases expect
        '''
        buys, sells = self._split_into_buy_and_sell_orders()
        buys = sorted(buys)
        sells = sorted(sells)
        
        for o in [*buys, *sells]:
            print(o)

    def _split_into_buy_and_sell_orders(self):
        '''
        splits orders into buy and sell orders.
        returns a pair of iterables:
        first iterable points to the first buy order.
        second points to the first sell order.
        '''
        from itertools import tee, filterfalse
        is_buy = lambda o: o.is_buy
        buys, sells = tee(self._orders)
        return filter(is_buy, buys), filterfalse(is_buy, sells)


    def add(self, order):
        '''
        checks the opposing side's available orders.
        for a buy order, look at existing sell orders, and vice versa.
        if a trade is possible, update the order book accordingly.
        otherwise, insert the order into the book.
        '''
        other = self._find_trade(order)
        while(other!=None):
            print('here')
            if(other.qty>order.qty):
                other.qty-=order.qty
                order.qty=0
                break
            else:
                order.qty-=other.qty
                self._orders.remove(other)
          
                other = self._find_trade(order)
                
        if(order.qty>0):
            print('added')
            
            self._orders.append(order)  
            

    def _find_trade(self, order):
        '''
        returns an order for the best "match" for a give order.
        for buy orders, this would be the lowest sell price.
        for sell orders,the highest buy price.
        if no orders meet the criteria, return None.
        '''
        ret = None
        i = 0
        max=0
        min=1000000
        print(self._orders)
        while i < len(self._orders):
            if order.is_buy != self._orders[i].is_buy and order.is_buy==False:
                print('sell')
                if order.price <= self._orders[i].price and self._orders[i].price>max :
                    ret = self._orders[i]
                    max=self._orders[i].price
                    
            elif order.is_buy != self._orders[i].is_buy and order.is_buy==True:
                if order.price>=self._orders[i].price and self._orders[i].price<min:
                    print('buy')
                    ret = self._orders[i]
                    min=self._orders[i].price
                    string="("
            i+=1    
        print(ret)
                    
        return ret
            
def parse(order_book):
    while True:
        line = input().strip().split()
        if line[0] == 'end':
            
            
            break

        is_buy = line[0] == 'buy'
        qty, price = line[1:]
        qty=int(qty)
        price=float(price)
        order_book.add(Order(is_buy, qty, price))

with OrderBook() as order_book:
    parse(order_book)
    order_book.add(Order(True, 10, 11.0))

    

