import csv
import string

f = open('foods.csv')
data = f.read()

foods = data.split('\n')

length = len(foods)
#print(cities[0])
#print(cities)

def bubbleSort(foods):
    for passnum in range(len(foods)-1,0,-1):
        for i in range(passnum):
            if foods[i]>foods[i+1]:
                temp = foods[i]
                foods[i] = foods[i+1]
                foods[i+1] = temp

bubbleSort(foods)
print(foods)

def sortfoods():
    global foods
    foods.sort()

def binarySearch():
    global foods, found, foodssearch, lower_bound, middle_pos, upper_bound

    foodssearch = input("Which food are you looking for?")
    lower_bound = 0
    upper_bound = len(foods)-1
    found = False
    while lower_bound <= upper_bound and not found:
        middle_pos = (lower_bound+upper_bound) // 2
        if foods[middle_pos] < foodssearch:
            lower_bound = middle_pos + 1
        elif foods[middle_pos] > foodssearch:
            upper_bound = middle_pos - 1
        else:
            found = True
    if found:

        print("This food is at position number", middle_pos)
    else:
        print("That food is not included in this list.")
        binarySearch()

def main():
        sortfoods()
        binarySearch()


if __name__ == "__main__":
    main()
