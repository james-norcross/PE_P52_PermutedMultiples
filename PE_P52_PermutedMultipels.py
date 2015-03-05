## Author: James Norcross
## Date: 3/5/15
## Description: Finds smallest integer x for which 2x, 3x, 4x, 5x and 6x
## are perumtations of x

## n1, n2 integer
## returns True if n2 is permutation of n1, False otherwise
def isPermutation(n1, n2):
    list1 = list(str(n1))
    list2 = list(str(n2))
    if(len(list1) != len(list2)):
        return False
    for i in list1:
        if(list1.count(i) != list2.count(i)):
            return False
    return True

done = False
x = 0
order = 1


while(not done):
    
    for x in range(1*order, int((10*order - 1)/6) + 1): ## can limit range so x and 6x have same number of digits
        
        if (isPermutation(x, 2*x) and \
            isPermutation(x, 3*x) and \
            isPermutation(x, 4*x) and \
            isPermutation(x, 5*x) and \
            isPermutation(x, 6*x)):
            
            done = True
            print "The smallest integer for which x, 2x, 3x, 4x, 5x and 6x are perumutations"
            print "of one another is " + str(x)
            break
        
    order *= 10

