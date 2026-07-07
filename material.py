class MaterialProperties:
    def __init__(self, youngModulus : int, poissonsRatio : int, fluidityMargin : int = 0): # мод Юнга, коэф Пуассона, предел текучести
        self.youngModulus = youngModulus
        self.poissonsRatio = poissonsRatio
        self.fluidityMargin = fluidityMargin
    def __repr__(self):
        return f"youngModulus: {self.youngModulus}\npoissonsRatio: {self.poissonsRatio}\nfluidityMargin: {self.fluidityMargin}"
