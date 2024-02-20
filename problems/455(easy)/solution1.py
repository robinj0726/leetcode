def findContentChildren(g, s):
    # Sort the lists in ascending order
    g.sort()
    s.sort()
    
    # Initialize counters for satisfied children and available cookies
    satisfied = 0
    cookie = 0
    
    # Iterate through the lists
    while satisfied < len(g) and cookie < len(s):
        # If the current cookie can satisfy the current child, increment counters
        if s[cookie] >= g[satisfied]:
            satisfied += 1
        # regardless of whether the current cookie can satisfy the current child
        # the cookie counter is incremented 
        cookie += 1
    
    # Return the number of satisfied children
    return satisfied