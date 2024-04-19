# classify and compute BMI
def BMIcalculator(Height, Mass):
    
    # compute BMI
    BMI = (Mass)/(Height*Height)
    
    # classify
    for t1, t2 in [(16, 'severely underweight'), 
                (18.5, 'underweight'), 
                (25, 'normal'), (30, 'overweight'), 
                (35, 'moderately obese'), 
                (float('inf'), 'severely obese')]:
    
        if BMI <= t1:
            print('Your BMI is', BMI, 'and the person is :', t2)
            break


height = float(input("enter your height: "))
mass = float(input("enter your mass: "))    
BMIcalculator(height, mass)