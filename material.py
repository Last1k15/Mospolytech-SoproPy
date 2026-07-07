class MaterialProperties:
    def __init__(self, youngModulus : int = 0, poissonsRatio : int = 0, shearModulus : int = 0, fluidityMargin : int = 0): # мод Юнга, коэф Пуассона, мод сдвига, предел текучести
        self.youngModulus = youngModulus
        self.poissonsRatio = poissonsRatio
        self.shearModulus = shearModulus
        self.fluidityMargin = fluidityMargin
    def __repr__(self):
        return f"youngModulus: {self.youngModulus}\npoissonsRatio: {self.poissonsRatio}\nfluidityMargin: {self.fluidityMargin}"
