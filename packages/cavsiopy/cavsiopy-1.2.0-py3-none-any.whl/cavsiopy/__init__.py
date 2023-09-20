from colorama import Fore, Back, Style 

def citing_warning():
    """
    prints a citation warning for cavsiopy users to remind them to cite
    cavsiopy in publications.
    """
    print() # create a newline
    print(Style.BRIGHT + Fore.WHITE + Back.RED + "IMPORTANT: Please make sure to cite cavsiopy in publications that"
          " use cavsiopy functions/modules/plots using DOI: https://doi.org/10.5281/zenodo.8361256")
          
citing_warning()
