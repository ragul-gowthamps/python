class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"
    
    def __add__(self, other):
        self_galleons = self.galleons + other.galleons
        self_sickles = self.sickles + other.sickles
        self_knuts = self.knuts + other.knuts
        return Vault(self_galleons, self_sickles, self_knuts)
 
potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(75, 30, 15)
print(weasley)

# galleons_total = potter.galleons + weasley.galleons
# sickles_total = potter.sickles + weasley.sickles
# knuts_total = potter.knuts + weasley.knuts

# total = Vault(galleons_total, sickles_total, knuts_total)
# print(total)

total = potter + weasley
print(total)