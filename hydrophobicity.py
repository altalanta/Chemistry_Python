from rdkit import Chem
from rdkit.Chem import Crippen

def estimate_hydrophobicity(molecular_smiles):
    try:
        mol = Chem.MolFromSmiles(molecular_smiles)
        if mol:
            logp = Crippen.MolLogP(mol)
            return logp
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Input for the molecular SMILES notation
molecular_smiles = input('Enter the molecular SMILES notation: ')

if molecular_smiles:
    logp = estimate_hydrophobicity(molecular_smiles)
    if logp is not None:
        if logp < 0:
            print(f"The molecule is hydrophilic (LogP = {logp})")
        else:
            print(f"The molecule is hydrophobic (LogP = {logp})")
    else:
        print("Invalid molecular structure.")
