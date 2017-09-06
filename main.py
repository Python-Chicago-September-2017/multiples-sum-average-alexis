count = 1
mult_five = 5

#odd numbers from 1 to 1000
while(count < 1000):
    if (count % 2 != 0):
        print "the odd numbers up to 1000",count
    count += 1
# multiples of 5 form 5 to 1,000,000
for num in range(5,1000001):
    if (num%5 == 0):
        print num

# THis is the sum List

a = [1, 2, 5, 10, 255, 3]

suma = 0
for num in a:
    suma += num
print "The sum of the values in the array is:", suma

#The average in the list
average = suma/len(a)
print "The average is {}".format(average)


