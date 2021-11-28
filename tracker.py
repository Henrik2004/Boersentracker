import yfinance as yf

share = input("Which share?: ")

share1 = yf.Ticker(share)

print("Dividends:\n"+str(share1.dividends)+"\n")
print("Actions:\n"+str(share1.actions)+"\n")
print("Cashflow:\n"+str(share1.cashflow)+"\n")
print("Financials:\n"+str(share1.financials)+"\n")
print("Earnings:\n"+str(share1.earnings)+"\n")
print("Balancesheet:\n"+str(share1.balancesheet)+"\n")
print("Splits:\n"+str(share1.splits)+"\n")