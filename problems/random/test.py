def calulate_conversion(conversion_rates, start_currency, end_currency):
    currencies = {}
    for conversion in conversion_rates:
        to_currency = conversion[0]
        from_currency = conversion[1]
        rate = conversion[2]
        currencies[to_currency] = currencies.get(to_currency, []) + [
            (from_currency, rate)
        ]
        currencies[from_currency] = currencies.get(from_currency, []) + [
            (to_currency, 1 / rate)
        ]

    print(currencies)


"""
    
    AUD--1.45---USD----110----JPY----0.0070---GBP
    
    
"""

test_case_1 = {
    "conversion_rates": [
        ["USD", "JPY", 110],  # 1 USD -> 110 JPY || 1 JPY -> 1 / 110 USD
        ["USD", "AUD", 1.45],  # 1 USD -> 1.45 AUD || 1 AUD -> 1 / 1.45 USD
        ["JPY", "GBP", 0.0070],  # 1 JPY -> 0.0070 GBP || 1 GBP -> 1 / 0.0070 JPY
    ],
    "start_currency": "GBP",
    "end_currency": "AUD",  # 1 GBP -> ? AUD
    "result": 1.89,
}


res = calulate_conversion(
    test_case_1["conversion_rates"],
    test_case_1["start_currency"],
    test_case_1["end_currency"],
)
# assert res == test_case_1["result"]
