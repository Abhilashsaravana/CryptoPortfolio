import requests
import json
from tkinter import *

crypto =Tk()
crypto.title("Portfolio")



mycoins=[
    {
        "symbol" : "BTC",
        "amountowned" : 1,
        "price" : 29000     
    },
    {
        "symbol" : "ETH",
        "amountowned" : 5,
        "price" : 1900
    },
    {
        "symbol" : "BNB",
        "amountowned" : 12,
        "price" : 240
    },
    {
        "symbol" : "DOGE",
        "amountowned" : 50,
        "price" : 0.065
    },
    {
        "symbol" : "LTC",
        "amountowned" : 50,
        "price" : 90
    }
]
def color(val):
    if val<0:
        return "red"
    else:
        return "green"
def portfolio():
    apis = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=10&CMC_PRO_API_KEY=324a21d8-0319-46e2-b6dd-2335d7b9d098")
    api = json.loads(apis.text)
    portfolioprof,currvalue = 0,0
    j = 1
    for i in range(len(api["data"])):
        for coin in mycoins:
            if(coin["symbol"] == api["data"][i]["symbol"]):
                print(api["data"][i]["name"],"(",api["data"][i]["symbol"],")")
                print("Price : %.2f"%(api["data"][i]["quote"]["USD"]["price"]))
                print("Cryptos : ",coin["amountowned"])
                print("Amount paid : ", coin["amountowned"]*coin["price"])
                print("Current Value : ",coin["amountowned"]*api["data"][i]["quote"]["USD"]["price"])
                print("Profit/coin : ",api["data"][i]["quote"]["USD"]["price"] - coin["price"] )
                print("Total Profit : ",coin["amountowned"]*api["data"][i]["quote"]["USD"]["price"] - coin["amountowned"]*coin["price"] ,"\n")
                portfolioprof += coin["amountowned"]*api["data"][i]["quote"]["USD"]["price"] - coin["amountowned"]*coin["price"]
                currvalue += coin["amountowned"]*api["data"][i]["quote"]["USD"]["price"]
                label = Label(crypto,text=api["data"][i]["name"],bg="white",fg="black",padx="2",pady="2",borderwidth=2,relief="groove")
                label.grid(row=j,column=0,sticky=N+S+E+W)
                label = Label(crypto,text=api["data"][i]["symbol"],bg="white",fg="black",padx="2",pady="2",borderwidth=2,relief="groove")
                label.grid(row=j,column=1,sticky=N+S+E+W)
                label = Label(crypto,text="$%.3f"%api["data"][i]["quote"]["USD"]["price"],bg="white",fg="black",padx="2",pady="2",borderwidth=2,relief="groove")
                label.grid(row=j,column=2,sticky=N+S+E+W)
                label = Label(crypto,text=coin["amountowned"],bg="white",fg="black",padx="2",pady="2",borderwidth=2,relief="groove")
                label.grid(row=j,column=3,sticky=N+S+E+W)
                label = Label(crypto,text="$%.3f"%(coin["amountowned"]*coin["price"]),bg="white",fg="black",padx="2",pady="2",borderwidth=2,relief="groove")
                label.grid(row=j,column=4,sticky=N+S+E+W)
                label = Label(crypto,text="$%.3f"%(coin["amountowned"]*api["data"][i]["quote"]["USD"]["price"]),bg="white",fg="black",padx="2",pady="2",borderwidth=2,relief="groove")
                label.grid(row=j,column=5,sticky=N+S+E+W)
                label = Label(crypto,text="$%.3f"%(api["data"][i]["quote"]["USD"]["price"] - coin["price"]) ,bg="white",fg=color(api["data"][i]["quote"]["USD"]["price"] - coin["price"]),padx="2",pady="2",borderwidth=2,relief="groove")
                label.grid(row=j,column=6,sticky=N+S+E+W)
                label = Label(crypto,text="$%.3f"%(coin["amountowned"]*api["data"][i]["quote"]["USD"]["price"] - coin["amountowned"]*coin["price"]) ,bg="white",fg=color(coin["amountowned"]*api["data"][i]["quote"]["USD"]["price"] - coin["amountowned"]*coin["price"]),padx="2",pady="2",borderwidth=2,relief="groove")
                label.grid(row=j,column=7,sticky=N+S+E+W)
                j+=j


    label = Label(crypto,text="$%.3f"%portfolioprof,bg="white",fg=color(portfolioprof),padx="2",pady="2",borderwidth=2,relief="groove")
    label.grid(row=j,column=7,sticky=N+S+E+W)
    label = Label(crypto,text="$%.3f"%currvalue,bg="white",fg="black",padx="2",pady="2",borderwidth=2,relief="groove")
    label.grid(row=j,column=5,sticky=N+S+E+W)
    api =""
    label = Button(crypto,text="Refresh",bg="burlywood4",command=portfolio,fg="white",font="arial 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
    label.grid(row=j+1,column=0,sticky=N+S+E+W)



label = Label(crypto,text="Name",bg="burlywood4",fg="white",font="arial 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
label.grid(row=0,column=0,sticky=N+S+E+W)
label = Label(crypto,text="Symbol",bg="burlywood4",fg="white",font="arial 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
label.grid(row=0,column=1,sticky=N+S+E+W)
label = Label(crypto,text="Price",bg="burlywood4",fg="white",font="arial 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
label.grid(row=0,column=2,sticky=N+S+E+W)
label = Label(crypto,text="Cryptos owned",bg="burlywood4",fg="white",font="arial 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
label.grid(row=0,column=3,sticky=N+S+E+W)
label = Label(crypto,text="Amount Paid",bg="burlywood4",fg="white",font="arial 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
label.grid(row=0,column=4,sticky=N+S+E+W)
label = Label(crypto,text="Current Value",bg="burlywood4",fg="white",font="arial 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
label.grid(row=0,column=5,sticky=N+S+E+W)
label = Label(crypto,text="Profit/coin",bg="burlywood4",fg="white",font="arial 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
label.grid(row=0,column=6,sticky=N+S+E+W)
label = Label(crypto,text="Total Profit",bg="burlywood4",fg="white",font="arial 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
label.grid(row=0,column=7,sticky=N+S+E+W)

portfolio()


crypto.mainloop()