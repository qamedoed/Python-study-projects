euro = float(input("Стоимость покупки в евро: "))

euro_to_usd = 1.25
usd_to_rub = 60.87

rubles = euro * euro_to_usd * usd_to_rub

print("Стоимость в рублях:", rubles)