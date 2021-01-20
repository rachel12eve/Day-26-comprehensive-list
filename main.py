numbers=[1,2,3]
new_list=[n+1 for n in numbers]
print(new_list)

name="Angela"
new_list=[n for n in name]
print(new_list)

names=["Alex", "Beth", "Caroline","Dave", "Eleanor","Faddie"]
# new list=[new item for old item in old list if test
long_names=[name.upper() for name in names if len(name)>4]
print(long_names)
