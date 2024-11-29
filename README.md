### DeepFashion Project

This repository contains a project for working with the **DeepFashion** dataset. The aim is to explore, pre-process, and build models for fashion-related tasks such as category classification, attribute prediction, and landmark detection.

#### Project Structure
- `data/`: Stores the raw and processed dataset files.
- `notebooks/`: Contains Jupyter Notebooks for exploratory data analysis and prototyping.
- `models/`: Stores trained model checkpoints.
- `src/`: Contains source code for data pre-processing, training, and utility functions.
- `outputs/`: Stores logs, visualisations, and other results.

#### Repository Structure
```bash
DeepFashion-Project/
├── data/
│   ├── raw/                   # Raw dataset files
│   ├── processed/             # Pre-processed files
├── notebooks/                 # Jupyter Notebooks for experiments
├── models/                    # Saved model checkpoints
├── src/                       # Source code for project modules
│   ├── data_preprocessing.py
│   ├── model_training.py
│   ├── utils.py
├── outputs/                   # Results like plots, logs, and metrics
│   ├── logs/
│   ├── visualizations/
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── .gitignore                 # Files and folders to ignore in Git
├── LICENSE                    # License for the project
└── setup.py                   # Package setup (optional)
```
#### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/DeepFashion-Project.git
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Dataset
Download the DeepFashion dataset from CUHK Project Page and place the raw files in the `data/raw/` folder.

4. Usage
 - Pre-process the Data:

```bash
python src/data_preprocessing.py
```
 - Train a Model:
```bash
python src/model_training.py
```
 - View Results: Outputs will be saved in the `outputs/` folder.

### License
MIT License
