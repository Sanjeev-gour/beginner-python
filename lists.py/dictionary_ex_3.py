import math



def circ_cal(r):
    
    area = math.pi*r*r
    circumference = 2*math.pi*r*r
    diameter = 2*r
    return area,circumference,diameter


def main():
    radius = int(input("Enter the radius of circle"))
    area, c, d = circ_cal(radius)
    print(f"area: {area}, circumference: {c}, diameter: {d}")
    

        
if __name__ == '__main__':
    main()
                     