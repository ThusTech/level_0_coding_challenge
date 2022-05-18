def area_of_triangle(first_side,second_side,third_side):
    
    semi_perimeter = 0.5*(first_side+second_side+third_side)
    area = sqrt(semi_perimeter*(semi_perimeter-first_side)*(semi_perimeter-second_side)*(semi_perimeter-third_side))

    return area


area = area_of_triangle(3,6,7)
print(area)