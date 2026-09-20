class India:
    def capital(self):
        print("capital- New Delhi")
    def currency(self):
        print("The currency of India indian rupees")

class USA:
    def capital(self):
        print("capital- Washington DC")
    def currency(self):
        print("The currency of USA is US dollars")

obj_ind = India()
obj_USA = USA()

for country in (obj_ind, obj_USA):
    country.capital()
    country.currency()