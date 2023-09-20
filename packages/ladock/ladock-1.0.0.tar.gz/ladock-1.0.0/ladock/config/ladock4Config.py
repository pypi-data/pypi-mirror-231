config_content = """# Silakan melakukan editing sesuai kebutuhan dan kenyataan Anda\n
spacing = 0.75
npts = "40,40,40"
ga_num_evals = 2500
ga_pop_size = 150
mgl_directory = "/home/<arga>/MGLTools-<version>"

# Tutorial:
# Follow these steps to prepare your input files and execute the simulations:
# 1. Put your ligand files in the 'ligand_input' directory.
# 2. Put your receptor (model_*_rec.pdb) dan reference ligand (model_*_lig.pdb) files in 'model_*' directories.
# 3. Ensure your ligand input files are in formats: smi, smiles, mol, mol2, pdb, or sdf.
# 4. For ligands from online sources, add the link to 'ligand_link.txt' and put it in the 'ligand_input' directory.
# 5. Adjust the parameters in the 'config.txt' file as needed. Set the MGLTools installation directory and docking parameters in this file correctly.
"""

ligand_link_default = """# Add download links here. One link per line. Supported download link formats include: smi, smiles, mol, mol2, pdb, or sdf.
# Here's an example link without "#". (remove this link and add your own ligand file links):
# http://files.docking.org/2D/BA/BAAA.smi
# http://files.docking.org/2D/BA/BAAB.smi
"""
