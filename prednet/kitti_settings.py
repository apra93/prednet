from pathlib import Path
REPO_DIR = Path(__file__).resolve().parent.parent
PN_DIR = REPO_DIR / 'prednet'

# Where KITTI data will be saved if you run process_kitti.py
# If you directly download the processed data, change to the path of the data.
DATA_DIR = PN_DIR / 'kitti_data/'

# Where model weights and config will be saved if you run kitti_train.py
# If you directly download the trained weights, change to appropriate path.
WEIGHTS_DIR = PN_DIR / 'model_data_keras2/'

# Where results (prediction plots and evaluation file) will be saved.
RESULTS_SAVE_DIR = PN_DIR / 'kitti_results/'
