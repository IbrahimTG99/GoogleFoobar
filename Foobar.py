#challenge 2
#task 2

#nice code
#i like it
#Python is best


def solution(total_lambs):
    
    if total_lambs==0:
        return 0
    i=1
    j=0
    k=0
    ind=1
    lambs_left=total_lambs
    while lambs_left>0:
       k=i
       i+=j
       if i>=lambs_left:
        break
       j=k
       lambs_left-=i
       ind+=1
       
    i=1
    ind2=1
    lambs_left=total_lambs
    while lambs_left>0:        
      lambs_left-=i
      i*=2
      if i>lambs_left:
        break
      ind2+=1
    return (ind-ind2)