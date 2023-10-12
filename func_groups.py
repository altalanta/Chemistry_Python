import re

def suggest_functional_groups(molecular_formula):
    # Initialize counts
    count_oxygen = 0
    count_sulfur = 0
    count_nitrogen = 0
    count_hydrogen = 0

    # Use regular expressions to parse the molecular formula 
  
    
    elements = re.findall(r'([A-Z][a-z]*)(\d*)', molecular_formula)
    

    for element, count_str in elements:
        count = int(count_str) if count_str else 1  # If no count is provided, assume 1
        if element == 'O':
            count_oxygen += count
        elif element == 'S':
            count_sulfur += count
        elif element == 'N':
            count_nitrogen += count
        elif element == 'H':
            count_hydrogen += count

    functional_groups = []

    # Suggestions based on counts
    if count_oxygen >= 1 and count_hydrogen >=1:
        functional_groups.append("Alcohol")
    if count_oxygen >= 2:
        functional_groups.append("Ketone")
    if count_oxygen >= 2 and count_hydrogen >= 1:
        functional_groups.append("Carboxylic Acid")
    if count_sulfur >= 1:
        functional_groups.append("Thiol")
    if count_nitrogen >= 1:
        functional_groups.append("Amine")
    if count_nitrogen >= 1 and count_hydrogen >= 2:
        functional_groups.append("Amide")

    return functional_groups

# Input for the molecular formula
compound_formula = input('Enter a molecular formula (e.g., H2O): ').upper()

if compound_formula:
    functional_groups = suggest_functional_groups(compound_formula)

    if functional_groups:
        print(f"Possible functional groups in {compound_formula}:")
        for group in functional_groups:
            print(f"- {group}")
    else:
        print(f"No functional groups detected in {compound_formula}")
