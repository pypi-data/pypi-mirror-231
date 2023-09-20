# FPromptify

## Installation

You can install FPromptify using pip. First, clone the repository and navigate to the project directory:

```bash
pip install git+https://github.com/hiendang7613/FPromptify.git
cd FPromptify
pip install -r requirements.txt
```

## Usage

To use FPromptify, run the following command in your terminal:

```bash
main.py --directory_path <path_to_dir> --mode <'CV' or 'JD'>
```

- `mode`: This parameter allows you to choose between two modes: Named Entity Recognition on 'CV' for CV or 'JD' for Job Description labeling.
- `path_to_dir`: Specify the path to the directory containing your PDF data for NER or text data for JD labeling. ## default: 'data_dir/CV' or 'data_dir/JD'
