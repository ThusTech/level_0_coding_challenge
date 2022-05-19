def area_of_triangle(first_side,second_side,third_side):
    
    semi_perimeter = (first_side+second_side+third_side)/2
    area = (semi_perimeter*(semi_perimeter-first_side)*(semi_perimeter-second_side)*(semi_perimeter-third_side))**0.5

    return area
