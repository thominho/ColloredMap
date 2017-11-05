from utils import *
from csp import *
import math, random, sys, time, bisect, string
from search import *
import itertools, re

australia = MapColoringCSP(list('RGB'),
                           'SA: WA NT Q NSW V; NT: WA Q; NSW: Q V; T: ')

print "Please Press a Number from 1-9"
print "Press 1 for MRV+FC with USA"
print "Press 2 for Mac with USA"
print "Press 3 for Minimum Conflicts with USA"
print "Press 4 for MRV+FC with France"
print "Press 5 for Mac with France"
print "Press 6 for Minimum Conflicts with France"
print "Press 7 for MRV+FC with Australia(causion for this one may not work)"
print "Press 8 for Mac with Australia(causion for this one may not work)"
print "Press 9 for Minimum Conflicts with Australia(causion for this one may not work)"
choice=input()
start_time = time.time()
if(choice==1):
    k = backtracking_search(usa,mrv,unordered_domain_values,forward_checking)
elif(choice==2):
    k = backtracking_search(usa,first_unassigned_variable,unordered_domain_values,mac)
elif(choice==3):
    k = min_conflicts(usa)
elif(choice==4):
    k = backtracking_search(france, mrv,unordered_domain_values,forward_checking)
elif(choice==5):
    k = backtracking_search(france,first_unassigned_variable,unordered_domain_values,mac)
elif(choice==6):
    k = min_conflicts(france)
elif(choice==7):
    k = backtracking_search(australia, mrv,unordered_domain_values,forward_checking)
elif(choice==8):
    k = backtracking_search(australia,first_unassigned_variable,unordered_domain_values,mac)
elif(choice==9):
    k = min_conflicts(australia)
elapsed_time = time.time() - start_time
print "elapsed_time = ",elapsed_time,"secs"
print k
print"done"
