def cm_to_inch(cm):
    return cm / 2.54

def inch_to_cm(inch):
    return inch * 2.54

def kg_to_lbs(kg):
    return kg * 2.20462

def lbs_to_kg(lbs):
    return lbs / 2.20462

def celsius_to_kelvin(c):
    return c + 273.15

if __name__ == "__main__":
    # Test the conversion functions
    print("=== TEST MODE Checking Formulas ===")
    print(f"2.54 cm to inches: {cm_to_inch(2.54)}")
    print(f"1 inches to cm: {inch_to_cm(1):.2f}")
    print(f"10 kg to lbs: {kg_to_lbs(10):.2f}")
    print(f"0 Celsius to Kelvin: {celsius_to_kelvin(0):.2f}")
    print("=== End of Tests ===")