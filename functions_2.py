def volume_cylinder(radius, height):
    v = 22/7 * radius**2 * height
    return v

print((volume_cylinder(7, 10), ))
print((volume_cylinder(10.65, 32.33), ))


#key - value pairs arguement
v1 = volume_cylinder(height=17, radius=10)

#optional parameter
def volume_cone(radius, height, decimals=2):
    v = 1/3 * 22/7 * radius**2 * height
    v = round(v, decimals)
    return v

print(volume_cone(20, 15, decimals=3))
print(volume_cone(20, 15))


