# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    i_couldnt_figure_these_variables_out = [0] * elements
    merged_arr = []
    # TO-DO
    # While left and right sides have elements, compare and append
    while len( arrA ) and len( arrB ):
      if arrA[0] <= arrB[0]:
        merged_arr.append( arrA.pop( 0 ) )
      else:
        merged_arr.append( arrB.pop( 0 ) )

    # while the left side has elements, append 
    while len( arrA ):
      merged_arr.append( arrA.pop( 0 ) )

    # while the right side has elements, append
    while len( arrB ):
       merged_arr.append( arrB.pop( 0 ) )
    
    # return sorted and merged list
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # Check if List can be split
    if len( arr ) < 2:
      return arr
    
    # Divide List in Halves
    left = arr[:int( len( arr ) / 2)]
    right = arr[int( len( arr ) / 2):]

    return merge( merge_sort( left ), merge_sort( right ) )

lst = [ 5, 2, 6, 1, 1, 8, 1000, -5 ]

sortd = merge_sort( lst )
print( sortd )


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
