def unique_in_order(sequence):
    
    elements = len(sequence)
    elements = elements - 1
    
    if elements == 0:
        
        return print("Sequence is empty")
    
    else:
        
        for i in (0, range(elements)):
            
            if sequence[i] == sequence[i+1]:
                sequence.remove[i+1]
                
                
            
    return print(sequence)