
"""
เขียนโปรแกรมหาจำนวนเลข 0 ที่อยู่ติดกันหลังสุดของค่า factorial ด้วย Python โดยห้ามใช้ math.factorial เช่น 7! = 5040 มีเลข 0 ต่อท้าย 1 ตัว, 10! = 3628800 มีเลข 0 ต่อท้าย 2 ตัว

"""
def get_count_zero_in_fact(number):
    count = 0
    fact_value = 1
    for i in range(1,number+1):
        fact_value = fact_value * i
    
    for i in range(len(str(fact_value))-1,-1,-1):
        if(str(fact_value)[i]=="0"):
            count+=1
        else:
            break
    return count

input_number = int(input("input : ")) 
print(get_count_zero_in_fact(input_number))  