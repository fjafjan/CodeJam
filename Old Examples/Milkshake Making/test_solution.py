f_in = open('B-small-practice.in')
f_out = open('B-small-practice.out', 'w')

#f_in = open('B-large-practice.in')
#f_out = open('B-large-practice.out', 'w')

## The number of test cases
N = int(f_in.readline())

for i in range(5):
    ## The number of milkshake flavours
    M = int(f_in.readline())
    ## The number of costumers
    C = int(f_in.readline())
    
    print "in this test case we have ", M, " milkshake flavors and ", C, " customers"
    for j in range(C):
        preferences = f_in.readline()
        print "preferences are ", preferences
