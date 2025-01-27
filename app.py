import streamlit as st
from rdkit import Chem
from rdkit.Chem import AllChem

# Título de la app
st.title("Docking Molecular de SARS-CoV-2 Mpro")

# Input de SMILES
ligando = st.text_input("Ingresa la estructura SMILES del ligando:")

if ligando:
    # Conversión SMILES a Mol
    mol = Chem.MolFromSmiles(ligando)
    if mol:
        # Generar la estructura 3D
        AllChem.EmbedMolecule(mol)
        # Mostrar la estructura 3D
        mol_file = 'ligando.pdb'
        Chem.MolToPDBFile(mol, mol_file)

        # Descargar el archivo PDB del ligando
        st.success("Ligando convertido a 3D y guardado.")
        st.download_button(label="Descargar PDB del Ligando", data=open(mol_file, 'rb'), file_name="ligando.pdb")
    else:
        st.error("SMILES no válido.")

