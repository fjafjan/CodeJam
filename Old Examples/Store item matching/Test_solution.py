f_in = open('A-small-practice.in')
f_out = open('A-small-practice.out', 'w')

f_in = open('A-large-practice.in')
f_out = open('A-large-practice.out', 'w')

N = int(f_in.readline())
print "the number of test cases is ", N

## This can/should be sped up by only looking at items with a larger subindex.
def solve(credit, items):
    for i in range(len(items)):
        item = items[i]
        if (credit - item) in items[i+1:]:
            return [items.index(item)+1, items[i+1:].index(credit-item)+i+2]

for i in range(0,N):
    ## Read three lines containing what we need to know
    credit = int(f_in.readline())
    n_items = int(f_in.readline())
    items = ((f_in.readline()).strip()).split()
    items = [int(j) for j in items]
    # Just to make sure that reading is correct
#    print "we have ", credit, " credit  and ", n_items, " items that are each ", items 
    # Then we solve this case and print it in the output file.
    solution = solve(credit, items)
    print "the solution is ", solution
#    output_string = gen_output(i, solution)
    
    f_out.write("Case #"+str(i+1)+":  "+str(solution[0]) + " " + str(solution[1]) + '\n')
    
# Make sure tha the output file looks rihgt
f_out.close()
f_in.close()
