from __future__ import print_function
import sys 
if __name__ == '__main__':
    n = int(raw_input())
    ls=[x for x in range(1,n+1)]
    print(*ls,sep='',end='\n')
