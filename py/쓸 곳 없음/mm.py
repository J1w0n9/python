planet = [
    ["수성", 2440, 0.055]
    ["금성", 6052, 0.815]
    ["지구", 6378, 1.0]
    ["화성", 3390, 0.107]
    ["목성", 69911, 317.832] 
]
maxScale= planet[0]
for i in range(1, 8):
    if maxScale < planet[i]:
        maxScale = planet[i]
print(maxScale)