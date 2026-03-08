## Create 4 variables describing a trade you'd make:
##The asset name
##Your entry price
##Number of contracts
##Whether you're long or short (boolean) 

nq = "NQ Futures"
price = 15134.32
contracts = 100
trade = True
direction = "Long" if trade else "Short"


print(f"Asset = {nq} Price = {price} Contracts = {contracts} Type = {direction}")