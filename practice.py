## Create 4 variables describing a trade you'd make:
##The asset name
##Your entry price
##Number of contracts
##Whether you're long or short (boolean) 

# nq = "NQ Futures"
# price = 15134.32
# contracts = 100
# trade = True
# direction = "Long" if trade else "Short"


#print(f"Asset = {nq} Price = {price} Contracts = {contracts} Type = {direction}")

# price = 15135.52
# entry = 14800
# contracts = 5
# difference = price - entry
# pnl = round(difference * 5 * 20, 2)
# percentage = round(((price - entry) / entry) * 100, 2)

# print (f"Entry = {entry} | Current Price = {price} | Points Difference = {difference} | P&L = {pnl} | Percentage = {percentage}")

# if price > entry:
#     print(f"Trade is Profitable, P&L is {pnl}")
# elif price == entry:
#     print (f"Trade is Even")
# else:
#     print(f"Trade is Unprofitable, P&L is {pnl}")

# if percentage > 2:
#     print(f"Strong Move")
# else:
#     print("Weak Move")

# prices = [14800, 14950, 15100, 15250, 15400]
# for price in prices:
#     gap = abs(price - 15000)
#     direction = "Above" if price > 15000 else "Below"
#     size = "Large" if gap > 200 else "Small"
#     print(f"The price is {price}, {direction} 15,000 | The gap is {gap}, meaning it is {size}")

# def trade_summary(price, entry):
#     if price > entry:
#         result = "profitable"
#     elif price == entry:
#         result = "flat"
#     else:
#         result = "loss"
#     PnL = price - entry

#     return f"The trade is a {result} trade, and the P&L is {PnL}"

# trade1 = trade_summary(1500, 1200)
# trade2 = trade_summary(22000, 400)
# trade3 = trade_summary(900, 1500)

# print(trade1)
# print(trade2)
# print(trade3)

# def price_analysis(closing):
#     print(f"{closing[0]} | {closing[-1]}")
#     difference = closing[-1] - closing[0]
#     for index, price in enumerate(closing):
#         print(f"The index is {index}, and the price is {price}")
#     return 

# price_analysis([15000,14800,15100,15600,14300])


trade = {"ticker" : "NQ", "entry": 14800, "current": 15143, "contracts": 10, "long": True}

def analyze_trade(trade):
    summary = "Profitable" if trade["current"] > trade["entry"] else "Non-Profitable"
    pnl = trade["current"] - trade["entry"]
    direction = "Long" if trade["long"] else "Short"
    print(f"Overall the trade is {summary} and the PnL is {pnl}. The direction of the trade was a {direction}")
    return

analyze_trade(trade)
    
