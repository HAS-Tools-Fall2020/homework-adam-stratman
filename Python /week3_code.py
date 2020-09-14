
# %%
boulder_precip_in = [0.70, 0.75, 1.85]
boulder_precip_in

boulder_precip_in[1]
months = ["January", "Febuary", "March"]
months
jan = 0.70
boulder_avg_precip = [1, jan, "january"]
boulder_avg_precip

len(boulder_avg_precip)

precip_by_location =[46.23,"inches", "New york City"]
precip_by_location[2]



# %%
del months[2]

# %%
months
# %%
months.append("March")
# %%
months
# %%
boulder_avg_precip.append(666)
# %%
boulder_avg_precip
# %%
b=9 
a=10
a+b
# %%
b/a
# %%
b*a
# %%
march_precip_in = (1.85)
# %%
march_precip_in
# %%
in_to_mm=(25.4)

march_precip_in*in_to_mm
# %%
march_precip_mm= (march_precip_in*in_to_mm)
# %%
march_precip_mm
# %%
type(march_precip_mm)
# %%
annual_ave_precip_nyc=(42.65)
dec_avg_precip_nyc=(3.58)
annual_ave_precip_nyc+=dec_avg_precip_nyc
annual_ave_precip_nyc
# %%
print("january precipitation", annual_ave_precip_nyc)
# %%
Is three greater than 4?

# %%
3<4

# %%
4<3
# %%
id(a)

id(3)
# %%
boulder_precip_months = ('jan, feb, mar, apr, may, june, july, aug, sept, oct, nov, dec')
boulder_precip_inches = (0.70, 0.75, 1.85 , 2.93, 3.05 , 2.02, 1.93, 1.62, 1.84, 1.31, 1.39, 0.84)
# %%
boulder_precip_inches= (boulder_precip_inches.copy*25.4)
# %%
new_list=old_list.copy()

# %%
x=0
if x == 10:
    print("x is equal to 10.")
else:
    print("x has a value of", x, "which is not equal to 10.")
# %%
x=0
# %%
x=0
y=100
if x>y:
    print("x has a value of", x, "which is greater than",y)
else:
    print("x has a value of", x, "which is less than", y)
# %%
avg_monthly_precip = [0.70,  0.75, 1.85, 2.93, 3.05, 2.02, 
                      1.93, 1.62, 1.84, 1.31, 1.39, 0.84]
if 0.70 in avg_monthly_precip:
    print("Value is in list.")
else:     
    print("Value is not in list.")
# %%
if 0.71 in avg_monthly_precip:
    print("Value is in list.")
else:     
    print("Value is not in list.")
# %%
hastools.path.exists()
# %%
os.path.exists()
# %%
