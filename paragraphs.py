# Exercise 3.1
# Given the following vowels 'a', 'e', 'i', 'o', 'u'
# Count each vowel inside the text file
# **Output:
# Vowel name    Count
#     a         170
# **Sum of all the vowels in paragraph 1
# **Sum of all the vowels in paragraph 2
# **Sum of vowels in paragraph 1 and 2
# **Print the results of the union between both paragraphs
# **Print the results of the intersection between both paragraphs
# **Print the results of the diference between both paragraphs
# **Print the most used word on each paragraph
# **Print the least used word on each paragraph
# If only one word is found, just add it to an 
# array and print the lenngth of the array.

vowels = [{'a':0,'e':0,'i':0,'o':0,'u':0}]

paragraph1= "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec placerat lacus sed lacinia suscipit. Pellentesque pulvinar tempus dui, non facilisis dolor vestibulum et. Suspendisse potenti. Duis in molestie orci, feugiat eleifend nisi. Aliquam consequat tortor id nisl interdum mattis. In hac habitasse platea dictumst. Suspendisse aliquam tincidunt velit. Phasellus pretium fermentum leo id rutrum. Fusce suscipit augue sit amet pulvinar vulputate. Proin pretium mauris vitae purus efficitur auctor. Vestibulum est lorem, varius a tempus non, consequat vel risus. Nam laoreet velit sit amet ipsum tincidunt luctus. Nunc gravida tortor a leo efficitur, et maximus enim pharetra."
paragraph2="Mauris tincidunt commodo lorem a pellentesque. Nam rutrum luctus neque. Maecenas porttitor dolor in sollicitudin ultrices. Aliquam eget blandit massa. Sed bibendum suscipit finibus. Suspendisse potenti. Nullam nec luctus diam, at bibendum dui. Ut vestibulum venenatis finibus. Mauris sed turpis at ante facilisis rhoncus. Phasellus molestie pharetra sagittis. Ut tincidunt, turpis sodales dapibus commodo, quam nisi mollis quam, at maximus quam tortor vitae nibh. Phasellus posuere aliquam erat sed elementum. Pellentesque faucibus, nulla eget hendrerit venenatis, tellus enim posuere dui, eu iaculis nibh ipsum a ligula. Quisque scelerisque odio sit amet libero iaculis rutrum. In hac habitasse platea dictumst."

count = {}.fromkeys(vowels,0)
for char in paragraph1:
    if char in count:
        count[char] += 1
print(count)
