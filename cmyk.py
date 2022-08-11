class CMYK:
    def __init__(self, c, m, y, k):
        self.c, self.m, self.y, self.k = c, m, y, k
    
    def mix(self, other):
        
        mix_c = round((self.c + other.c) / 2, 2)
        mix_m = round((self.m + other.m) / 2, 2)
        mix_y = round((self.y + other.y) / 2, 2)
        mix_k = round((self.k + other.k) / 2,
        )
        return CMYK(mix_c, mix_m, mix_y, mix_k)
    
    def to_rgb(self):
        from rgb import RGB
        
        r = 255 * (1 - self.c) * (1 - self.k)
        g = 255 * (1 - self.m) * (1 - self.k)
        b = 255 * (1 - self.y) * (1 - self.k)

        return RGB(r, g, b)
        

    def __str__(self):
        return f"{self.c},{self.m},{self.y},{self.k}"