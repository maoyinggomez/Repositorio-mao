class Smartwatch:
    def __init__(self,marca,referencia):
        self.marca= marca
        self.referencia= referencia


gt2= Smartwatch("huawei","gt2")
gt2Ppro= Smartwatch("huawei","gt2Pro")
print(type(gt2))
print(type(gt2Ppro))

print(gt2.marca, gt2.referencia)
print(gt2Ppro.marca, gt2Ppro.referencia)
