class MaterialProperties:
    def __init__(self, youngsModulus : int = 0, poissonsRatio : int = 0, shearModulus : int = 0, yieldStrength : int = 0):
        self.youngsModulus = youngsModulus
        self.poissonsRatio = poissonsRatio
        if (shearModulus == 0 and youngsModulus != 0 and poissonsRatio != 0):
            self.shearModulus = youngsModulus / (2 * (1 + poissonsRatio))
        else: self.shearModulus = shearModulus
        self.yieldStrength = yieldStrength

    def __repr__(self):
        return f"youngsModulus: {self.youngsModulus}\npoissonsRatio: {self.poissonsRatio}\nshearModulus: {self.shearModulus}\nyieldStrength: {self.yieldStrength}"
