#To create a module to calculate area of circle, triangle, rectangle

def area_circle(radius):
    ar_circ = 3.14 * radius * radius
    print (f"Area of circle is:   {ar_circ}")

def area_triangle(height, base):
    ar_tri = 0.5 * height * base
    print (f"Area of Triangle is:   {ar_tri}")

def area_rectangle(height, base):
    ar_rect = height * base
    print (f"Area of rectangle is:   {ar_rect}")