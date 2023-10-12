import streamlit as st

# Define a dictionary with atomic weights
atomic_weights = {
    'H': 1.00794,
    'C': 12.011,
    'O': 15.999,
    'N': 14.00674,
    'S': 32.065,
    'Cl': 35.435,
    'Br': 79.904,
    'F': 18.998,
    'I': 126.90,
    'Fe': 55.845,
    'Cu': 63.546,
    'K': 39.0983,
    'Na': 22.9897,
    'Zn': 65.38,
    'Ca': 40.078,
    # Add more elements as needed
}

def calculate_molecular_weight(molecular_formula):
    # Initialize the total molecular weight
    total_weight = 0.0

    # Use regular expressions to parse the molecular formula
    import re
    elements = re.findall(r'([A-Z][a-z]*)(\d*)', molecular_formula)

    for element, count_str in elements:
        count = int(count_str) if count_str else 1  # If no count is provided, assume 1
        atomic_weight = atomic_weights[element]
        total_weight += count * atomic_weight

    return total_weight

# Streamlit app
st.title("Molecular Weight Calculator")

# Input for the molecular formula
compound_formula = st.text_input('Enter a molecular formula (e.g., H2O):')

if compound_formula:
    # Calculate the molecular weight
    molecular_weight = calculate_molecular_weight(compound_formula)

    # Display the result
    st.write(f"The molecular weight of {compound_formula} is {molecular_weight} g/mol")
