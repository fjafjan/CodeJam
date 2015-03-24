f_in = open('A-small-practice.in')
f_out = open('A-small-practice.out', 'w')

f_in = open('A-large-practice.in')
f_out = open('A-large-practice.out', 'w')


## The number of test cases
N = int(f_in.readline())


def find_minimum(v1, v2):
    v1.sort()
    v2.sort(reverse = True)
    
#    print "sorted v1 and v2 are", v1, v2
    scalar_prod = 0
    for i, j in zip(v1, v2):
        scalar_prod += i*j
    print "the scalar prod is ", scalar_prod
    return scalar_prod

for i in range(N):
    ## The number of "dimensions", aka numbers in each vector
    dimension = int(f_in.readline())
    v1 = ((f_in.readline()).strip()).split()
    v1 = [int(j) for j in v1]
    v2 = ((f_in.readline()).strip()).split()
    v2 = [int(j) for j in v2]
#    print "our two vectors are", v1, v2
    ## Okay so what we want is the MAXIMUM negative scalar product. Something that seems like it would work would be to just pair the 
    ## largest in one with the smaller in the other. 
    scalar_prod = find_minimum(v1, v2)
    f_out.write("Case #"+str(i+1)+":  "+ str(scalar_prod) + '\n')
