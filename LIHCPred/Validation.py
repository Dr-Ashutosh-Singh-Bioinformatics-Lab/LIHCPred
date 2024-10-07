# LIHC/Validation.py

import os
import pandas as pd
import joblib

def predict(df, model_type='svc'):
    # List of selected genes
    selected_genes = [
    'SEMA3F', 'MARCO', 'NOX4', 'PHACTR3', 'SLC5A1', 'RASD2', 'PVALB', 'CDKN3', 'CLEC4M', 'THBS4', 
    'SCAMP3', 'MSTO1', 'TCF15', 'PLVAP', 'ANGPTL6', 'HIGD1B', 'B4GALNT1', 'STAB2', 'ARHGEF39', 
    'CAPN11', 'TRPC6', 'CEP131', 'PPOX', 'PRCC', 'TTC13', 'CXCL14', 'DIPK2B', 'FBXO43', 'TOMM40L', 
    'FCN2', 'FLAD1', 'LRRC14', 'BMP10', 'PYGO2', 'EBF1', 'BMPER', 'TEPSIN', 'ZNF526', 'APLN', 'CD34', 
    'SH3BP5L', 'TEX26', 'GBA', 'TIGD5', 'CHRM2', 'GJC1', 'COLEC10', 'C14orf180', 'GABRD', 'COL15A1', 
    'MXD3', 'EBF2', 'SLC26A6', 'SPTY2D1OS', 'TERT'
    ]

     # Select features from dataframe
    df_selected = df[selected_genes]
    
    # Construct model path
    model_path = os.path.join(os.path.dirname(__file__), 'models', f'{model_type.lower()}.pkl')
    
    # Check if model file exists
    if not os.path.exists(model_path):
        raise ValueError(f"Model '{model_type}' not found. Ensure the model file exists at {model_path}.")
    
    # Load the model
    model = joblib.load(model_path)
    
    # Make predictions
    y_pred = model.predict(df_selected)
    
    # Add predictions to dataframe
    df['Prediction'] = ['Cancer' if pred == 1 else 'Normal' for pred in y_pred]
    
    # Save predictions to CSV file
    df.to_csv('predictions.csv', index=False)
    
    # Print diagnosis
    count_cancer = y_pred.sum()
    count_normal = len(y_pred) - count_cancer
    percentage_cancer = count_cancer / len(y_pred)
    percentage_normal = count_normal / len(y_pred)
    
    if percentage_cancer > 0.6:
        print(f"LIHC patient detected, {percentage_cancer*100:.2f}%")
    else:
        print(f"Normal patient detected, {percentage_normal*100:.2f}%")

