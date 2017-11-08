from mol_scraper import scraper
import imolecule
import argparse

# Global:
molecule = "Caffeine"

# Construct the argument parser:
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--molecule", default=molecule, help="Input molecule.")
args = vars(ap.parse_args())


def visualize(smiles):
    imolecule.draw(smiles)


def search(molecule):
    img, smiles = scraper(molecule)
    if smiles is None:
        error = "Molecule not found. Maybe the name is misswritten... (?)"
    else:
        visualize(smiles)


if __name__ == '__main__':
    mol = args["molecule"]
    search(mol)
