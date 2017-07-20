import random

word1 = ["boujee", "pillow", "milly rock"]
word2 = ["on the block", "in my sock", "boys in the house"]
word3 = ["and my gravy", "hats off", "apples to oranges"]
word4 = ["in the stomach", "on your face", "crazy woman"]
word5 = ["knocking on my door", "chicken nuggets", "french fries on my thighs"]
word6 = ["my blue moon", "leaving the country", "fleeing from the feelings"]
word7 = ["dabbing on the street", "chicken is not dairy", "chicken is a form of dairy"]
word8 = ["girls who crave food", "fill up the candy", "this rap is fire"]
word9 = ["I got electrocuted from the wire", "found you in a dump", "five veggies to a flat belly"]
word10 = ["copyright chloe and lydia 2017", "find us on the rap game",
"sean, chad, and shane you got no game"]

random_num = random.randint(0,2)
print(word1[random_num] + " " + word2[random_num] + " " + word3[random_num]
+ " " + word4[random_num] + " " + word5[random_num] + " " + word6[random_num]
+ " " + word7[random_num] + " " + word8[random_num] + " "
+ word9[random_num] + " " + word10[random_num])
