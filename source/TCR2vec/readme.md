# TCR Embedding Using TCR2vec  

This project utilizes the TCR2vec method to generate embeddings for TCR CDR3 sequences or full-length TCRβ chains.

## Dependencies   

Run `pip install tcr2vec` to install the required dependencies.  

## Data   

A sample CSV file containing TCR sequences is provided in the `data` directory. The `CDR3.beta` column contains CDR3 amino acid sequences, while the `full_seq` column contains full-length TCRβ chain sequences. To generate embeddings for full-length sequences, refer to the "Reconstruction of full TCR" section in the original TCR2vec repository.   

## Pre-trained Models

To use pre-trained TCR2vec models, download:  

- The [full-length TCR model](https://drive.google.com/file/d/1Nj0VHpJFTUDx4X7IPQ0OGXKlGVCrwRZl/view?usp=sharing) 
- The [CDR3-only model](https://drive.google.com/file/d/1crwG2kLj8O3qQ1zfu8YbEk6cNb5aUD4e/view?usp=sharing)  

## Usage  

For more details, refer to the original TCR2vec repository:
https://github.com/jiangdada1221/TCR2vec/tree/main
