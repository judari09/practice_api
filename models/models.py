class device:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def get_brand(self):
        return self.brand
    
    def get_model(self):
        return self.model
    
    def get_year(self): 
        return self.year
    
    def get_color(self):
        return self.color
    
    def set_brand(self, marca):
        self.brand = marca

    def set_model(self, modelo):
        self.model = modelo
    
    def set_year(self, year):
        self.year = year
    
    def set_color(self, color):
        self.color = color  


class laptop(device):
    def __init__(self, brand, model, year, color):
        super().__init__(brand, model, year, color)

class celular(device):
    def __init__(self, brand, model, year, color):
        super().__init__(brand, model, year, color)