#Problem: The grades at Koala University are awarded based on the number of marks awarded
#for the course out of 100. Marks of 90 or above receive the grade of “gum leaf cluster”. Marks
#less than that but of 60 or above receive the grade of “leafy twig”. Marks less than that but
#of 45 or above receive the grade of “gum leaf”. Anything less gets the grade of “dead twig”.
#Write a program that asks the user for a number of marks, and prints the grade awarded.

print("Koala Unversity Marks")
n = int(input("Enter your marks: "))
if n >= 90:
    print("Gum leaf Cluster")
elif n >= 60:
    print("Leafy Twig")
elif n >= 45:
    print("Gum leaf")
elif n < 45:
    print("Dead Twig")