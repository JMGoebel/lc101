def get_country_codes(prices):
    price_list = prices.split(",")
    temp_list = [item[:item.find("$")] for item in price_list]
    return ",".join(temp_list)

print(get_country_codes("NZ$300, KR$1200, DK$5"))
print(get_country_codes("US$40, AU$89, JP$200"))
print(get_country_codes("AU$23, NG$900, MX$200, BG$790, ES$2"))
print(get_country_codes("CA$40"))


