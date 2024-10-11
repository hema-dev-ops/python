# Function to calculate the area of a triangle using base and height
def triangle_area(base, height):
    return 0.5 * base * height

# Input from the user
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculate and print the area
area = triangle_area(base, height)
print(f"The area of the triangle is {area:.2f}")
