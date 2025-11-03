import os
from pathlib import Path
home = Path.home()

sDir = os.path.join(home, '.cache/fict_repo/data/supporting_data/materials/')  # directory where the skin layer models will be stored
sDir_lesion_ver0 = os.path.join(home, '.cache/fict_repo/data/supporting_data/materials/lesions_release/ver0/')
sDir_lesion_ver1 = os.path.join(home, '.cache/fict_repo/data/supporting_data/materials/lesions_release/ver1/')
sDir_hdri = os.path.join(home, '.cache/fict_repo/data/supporting_data/hdri/') # directory where lighting HDRI files are stored
param_dir = os.path.join(home, '.cache/fict_repo/data/supporting_data/')  # directory where the .csv files are stored
