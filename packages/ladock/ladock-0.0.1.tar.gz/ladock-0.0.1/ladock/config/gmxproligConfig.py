config_content = """# Silakan melakukan editing sesuai kebutuhan dan kenyataan Anda
# Nilai untuk -bt (box type):
box_type = "triclinic"

# Nilai untuk -d (distance)
distance = "1.2"  

# Nilai untuk -cs (coordinate file for solvent):
coordinate_file = "spc216.gro"


# This directory structure has been created using LADOCK. Follow these steps to prepare your input files and execute the simulations:

# 1. Place each receptor and two ligands (three separate .pdb format files) in the "complex" folder.
# 2. Make necessary edits to the mdp files as needed.
# 3. Ensure that receptor files contain the characters "rec*.pdb" in their names.
# 4. Ensure that ligand files contain the characters "lig*.pdb" in their names.
# 5. Verify that the required dependencies, such as acpype, openbabel, and gromacs, are installed and functioning properly.
# 6. Execute the following command in the LADOCK_lagmx directory: `ladock --run lagmx`.
"""

