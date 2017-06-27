# Excercise 2.2
#a=1, e=2, i=3, o=4, u=5
#x = "Tesla" => [2,3]
#y = "Buick"
#z = "Ferrari"
#w = "Ford"
#t = "Lamborghini"
#p = "Masertati"
# Iterate over all the cars
# **Create an array for each car => print(car_vowels_array)
# Each array will hold the vowel value => x = "Tesla" => [2,3]
# **At the end construct an array containing all the cars vowels 
# print(car_vowels_from_all_the_cars)         
# **With the previous array filter the vowel value like this:
# vowel_value %2 == 0: 'Buy it'
# vowel_value %3 == 0: 'Sell it'







a=1
e=2
i=3
o=4
u=5

x = "Tesla"
y = "Buick"
z = "Ferrari"
w = "Ford"
t = "Lamborghini"
p = "Masertati"

vowels=[a,e,i,o,u]
vowelname=['a','e','i','o','u']
consonants=[x,y,z,w,t,p]


for i in consonants:
    letters=[]
    for j,b in range(len(vowelname)):
        if b in i:
            letters.append(vowels[j])
    print(i, letters)
