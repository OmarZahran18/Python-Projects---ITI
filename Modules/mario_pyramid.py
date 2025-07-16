def mario_pyramid():
    for m in range(1 , 6):
        print("*" * m)
        
        
                
def right_aligned_pyramid():
    x = 5
    for i in range(1, x + 1):
        r = [" "] * (x - i) + ["#"] * i
        print("".join(r))