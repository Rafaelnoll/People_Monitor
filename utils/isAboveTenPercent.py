def isAboveTenPercent(number, total):
    tenPercent = total * 0.1

    if(number <= (total + tenPercent)):
        return True
    
    return False
