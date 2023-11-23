# Django_project_Graduation_Project

## Project Overview

Welcome to our graduation project in the field of Bioinformatics! The main goal of this project is to contribute to the preservation of health by leveraging advanced technologies for the detection of genetically passed or mutation-induced cancers.

### Understanding BRCA1 Mutations

Mutations in the BRCA1 gene can significantly impact an individual's susceptibility to specific types of cancer. For instance, a mutation in the BRCA1 gene is linked to an increased risk of breast cancer, including the aggressive triple-negative breast cancer, which can pose challenges in treatment.

## Machine Learning Model

Our project incorporates a machine learning model designed to predict breast cancer based on DNA data analysis. Here's an overview of the model:

### Pre-processing Module

The images in our dataset vary in sizes. To ensure uniformity, we employ a pre-processing module that resizes all images in the dataset to a standardized size. This step is crucial for consistent input to the machine learning model.

### Feature Extraction Module

In the feature extraction phase, we utilize the VGG16 pre-trained model to extract 4096 deep features from the dataset. Addressing potential issues of model overfitting, we mitigate improper bias and variance by reducing the dimensionality of the data.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/Django_project_Graduation_Project.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Django_project_Graduation_Project
    ```

3. Set up the Django environment:

    ```bash
    # Create and activate a virtual environment
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

    # Install dependencies
    pip install -r requirements.txt

    # Run migrations
    python manage.py migrate
    ```

4. Run the Django development server:

    ```bash
    python manage.py runserver
    ```

## Contributing

Feel free to contribute to this project by submitting issues or pull requests.

## Acknowledgments

We extend our gratitude to all contributors and acknowledge the utilization of pre-trained models like VGG16 in our feature extraction module.


