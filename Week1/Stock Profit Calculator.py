def claculate_profit_loss():
    print('Stock Profit/Loss Calculator')
    try: 
        buy_price = float(input('Enter buying price per share: '))
        sell_price = float(input('Enter selling price per share: '))
        quantity = int(input('Enter number of shares: '))
        investment = buy_price * quantity
        returns = sell_price * quantity
        profit_loss = returns - investment
        print('Total Investment:' , investment)
        print('Total Returns:', returns)
        if profit_loss >0:
            print('Profit: ', profit_loss)
        elif profit_loss <0:
            print('Loss: ', profit_loss)
        else:
            print('No profit, No Loss')
    except ValueError:
        print('Invalid input.')
claculate_profit_loss()
