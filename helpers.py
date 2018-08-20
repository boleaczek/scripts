def getMarkedParams(params, expected):
    paramsDictionary = dict()
    
    consumed = 0
    while(consumed < len(params)):
        if params[consumed].startswith('-') == False or\
        params[consumed] in expected == False :
            consumed += 1
            continue
        
        paramsDictionary[params[consumed][1:]] = params[consumed + 1]
        consumed += 1
    
    return paramsDictionary
        
def getParams(params, expected):
    found = set()

    for param in params:
        if param in expected:
            found.add(param)
    
    return found