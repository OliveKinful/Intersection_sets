#definig the find intersection
def find_intersection(set1, set2):
    return set1 & set2

#sample for set1 and set2
set1 = {1, 2, 3, 4, 5, 6}
set2 = {3, 4, 7, 8, 9, 10}

intersection_set = find_intersection(set1,set2)
print("Intersection:", intersection_set)