oil_prices=[
    {
        "oil_type": "petrol",
        "prices":[
            {"year":"2018","price":100},
            {"year":"2019","price":120},
               {"year":"2019","price":130},
        ]

    }     
]




print("-"*70)
for oil in oil_prices :
    print(f"Oil_type: {oil.get('oil_type').capitalize()}")
    prices = oil.get('prices')

    
    total = 0
    for price in prices:
        p=price.get('price')
        total=total+p
        print(f"Price({price.get('year')}):{p}")
        

    print(f"Price : {total}")
    avg_price= 









