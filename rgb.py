class RGB:
    def __init__(self, r, g, b):
        self.r, self.g, self.b = r, g, b
    
    def to_cmyk(self):
        from cmyk import CMYK
        r_dash = round(self.r / 255, 2)
        g_dash = round(self.g / 255, 2)
        b_dash = round(self.b / 255, 2)

        k = round(1 - max(r_dash, g_dash, b_dash), 2)
        
        c = round((1 - r_dash - k) / (1 - k), 2)
        m = round((1 - g_dash - k) / (1 - k), 2)
        y = round((1 - b_dash - k) / (1 - k), 2)

        return CMYK(c, m, y, k)
    
    def __str__(self):
        return f"({self.r}, {self.g}, {self.b})"

