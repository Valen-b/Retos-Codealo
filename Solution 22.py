def sum_two_smallest_numbers(lista):
  
    min0 = 0
    min1 = 0
    l = len(lista)
    if l == 0:
        return 0

    elif l == 1:
        return lista[0]*2

    else:

        min0 = lista[0]
        min1 = lista[l-1]
        i = 1
        while i < l - i - 1:
            if lista[i] < min0:
                    min0 = lista[i]
            if lista[l-i-1] < min1:
                    min1 = lista[l-i-1]
            i += 1

        return min0 + min1
      
sum_two_smallest_numbers([])

print(sum_two_smallest_numbers([19, 5, 11, 2, 6, 7]))  
print(sum_two_smallest_numbers([3, 87, 45, 12, 7]))  
print(sum_two_smallest_numbers([10]))  