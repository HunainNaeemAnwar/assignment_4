C = 299792458  
loop_break=True

def calculate_mass(mass:float) -> float:
    """calculate energy using Eintein's mass-energy equivalence formula"""
    energy:float = mass * C ** 2
    return energy
def main():
    global loop_break2
    while loop_break:
        try:
            mass=float(input("Enter the mass of the object in kilograms: "))
            print("e = m * c^2..")
            print(f"mass: {mass}")  
            print(f"c: {C}")
            energy=calculate_mass(mass)
            print(f"The energy of the object is {energy} joules.")
            loop_break=False
        except ValueError:
            print("Invalid input. Please enter a valid mass.")

if __name__ == "__main__":
        main()
