
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
import os 
import numpy as np
import earthpy as et 
# %%
avg_month_precip_url = 'https://ndownloader.figshare.com/files/12565616'
et.data.get_data(url=avg_month_precip_url)
os.chdir(os.path.join(et.io.HOME, 'earth-analytics'))
avg_month_precip_path = os.path.join("data", "earthpy-downloads", 
                                     "avg-monthly-precip.txt")
# %%
if os.path.exists(avg_month_precip_path):
    print("This is a valid path.")
else:
    print("This path does not exist.")
# %%
if os.path.exists(avg_month_precip_path):
    avg_month_precip = np.loadtxt(avg_month_precip_path)
    print(avg_month_precip)
else:
    print("This path does not exist.")
# %%
x=5
y=10
if x < y:
    print("x started with value of", x)
    x += 5
    print("It now has a value of", x, "which is equal to y.")
elif x > y:
    print("x started with value of", x)
    x -= 5
    print("It now has a value of", x, "which is equal to y.")

else:
    print("x started with a value of", x, "which is already equal to y.")

# %%
x=10
if x < y:
    print("x started with value of", x)
    x += 5
    print("It now has a value of", x, "which is equal to y.")

elif x > y:
    print("x started with value of", x)
    x -= 5
    print("It now has a value of", x, "which is equal to y.")

else:
    print("x started with a value of", x, "which is already equal to y.")
# %%
list_of_values =[1,2,3,4,5,6,7,8]
print(list_of_values)
# %%
for avalue in list_of_values:
    print(avalue)
for avalue in list_of_values:
    print("the current value is:", avalue+1)

# %%
os.path.join("data")
# %%
my_path = os.path.join("Python")
# %%
import os
import earthpy as et 

getcwd[]
# %%
os.path.join("earth-analytics", "data")
my_path = os.path.join("earth-analytics", "data")
# %%
os.path.exists(my_path)
# %%
chdir("path-to-dir")
# %%

print(get.cwd)
# %%
os.getcwd()
# %%
os.chdir(path_to_dir)
# %%
os.chdir()

# %%
et.io.HOME
# %%
os.path.exists(et.io.Home)
# %%
my_ea_path = os.path.join(et.io.HOME, "earth-analytics")

# %%
os.path.exists(my_ea_path)

# %%
my_ea_path = os.path.join(et.io.HOME, "earth-analytics")

# %%
os.mkdir("path/to/dir/here")
# %%
os.mkdir(my_ea_path)
# %%
import matplotlib
# %%
import numpy as np 

# %%
print(avg_month_precip)
# %%
avg_monthly_precip = np.array([0.70, 0.75, 1.85])
# %%
print(avg_monthly_precip)
# %%
precip_2002_2013 = np.array([
    [1.07, 0.44, 1.50],
    [0.27, 1.13, 1.72]
])
# %%
print(precip_2002_2013)
# %%
