import streamlit as st
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
import subprocess
import os

# Configuración inicial
st.title("Docking Molecular usando RDKit y Mpro")

# Cargar el archivo PDB de la proteína
protein_file = st.file_uploader("Sube el archivo PDB de la proteína Mpro", type="pdb")

# Cargar los ligandos en formato SMILES
smiles_input = st.text_area("Ingresa los ligandos en formato SMILES (uno por línea):")

if st.button("Realizar Docking"):
    if protein_file and smiles_input:
        # Guardar la proteína localmente
        protein_path = "mpro.pdb"
        with open(protein_path, "wb") as f:
            f.write(protein_file.read())

        # Procesar los ligandos
        smiles_list = smiles_input.splitlines()
        for i, smiles in enumerate(smiles_list):
            mol = Chem.MolFromSmiles(smiles)
            if mol:
                # Generar conformaciones 3D
                mol = Chem.AddHs(mol)
                AllChem.EmbedMolecule(mol, AllChem.ETKDG())

                # Guardar como archivo MOL
                mol_file = f"ligand_{i}.mol"
                Chem.MolToMolFile(mol, mol_file)

                # Ejecutar docking usando AutoDock Vina
                vina_command = (
                    f"vina --receptor {protein_path} --ligand {mol_file} "
                    f"--out output_{i}.pdbqt --log log_{i}.txt"
                )
                subprocess.run(vina_command, shell=True)

                # Mostrar resultados
                st.write(f"Ligando {i + 1} procesado. Energías de afinidad en log_{i}.txt")
                with open(f"log_{i}.txt", "r") as log_file:
                    st.text(log_file.read())

                # Visualizar ligando
                st.image(Draw.MolToImage(mol))
    else:
        st.error("Por favor, sube un archivo PDB y proporciona ligandos en formato SMILES.")
