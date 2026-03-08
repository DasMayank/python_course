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

price = 15135.52
entry = 14800
contracts = 5
difference = price - entry
pnl = difference * 5 * 20
percentage = round(((price - entry) / entry) * 100, 2)x 

print (f"Entry = {entry} | Current Price = {price} | Points Difference = {difference} | P&L = {pnl} | Percentage = {percentage}")