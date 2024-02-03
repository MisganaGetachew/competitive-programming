def swap_case(s):
    n =  []
    for i in s:
        if i == i.upper():
            i = i.lower()
        elif i == i.lower():
            i =  i.upper()  
        n.append(i)
            
             
            
    return "".join(n)
    
