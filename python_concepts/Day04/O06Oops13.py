
class Shopping:

    def __init__(self, prod, prc, qty):
        self.prod = prod
        self.prc = prc
        self.qty = qty

    def get_details(self):
        print(f"Name of the product :{self.prod}\nPrice of the product :{self.prc}\nQuantity ordered :{self.qty}")

    def __amtAfter_GST(self):           # private Method
        # GST = 18%
        tp = self.prc * self.qty
        GST = tp + (tp * 0.18)
        return GST

    def InvAmount(self):
        return self.__amtAfter_GST()

shp1 = Shopping("pepsi", 45, 150)
print(shp1.InvAmount())

# shp1.__amtAfter_GST()

print("-" * 60)
print(Shopping.__dict__)
