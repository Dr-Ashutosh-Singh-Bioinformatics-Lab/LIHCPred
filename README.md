# LIHCPred: A Tool for Identification of LIHC using Machine Learning.
Liver hepatocellular carcinoma (LIHC) is the most common type of primary liver cancer, typically arising from chronic liver disease or cirrhosis. Identifying biomarkers for LIHC is crucial for early detection, diagnosis, and prognosis. Biomarkers guide personalized treatment, monitor disease progression, and improve patient outcomes by enabling timely interventions. Biomarkers are pivotal in this regard, providing noninvasive means for early detection, facilitating prompt treatment initiation, and potentially boosting survival rates. Hence, the recognition and validation of biomarkers are of primary importance in effectively addressing liver cancer.


## Introduction

LIHCPred is an innovative solution for identifying liver hepatocellular carcinoma (HCC) through transcriptomic profiling. By leveraging advanced machine learning algorithms, this cutting-edge technology analyzes tissue biomarkers to provide highly accurate prognoses for liver cancer.

Furthermore, the integration of machine learning allows continuous refinement of the predictive model's accuracy as more data is gathered, enhancing its reliability and effectiveness over time. LIHCPred represents a significant breakthrough in the early detection of HCC, potentially leading to earlier interventions and improved patient outcomes.

To further strengthen our approach, we selected 55 features using a range of Feature Selection Methods. These include the Fast Correlation-Based Filter Method (FCBF), Spike and Slab ("spikeslab"), Univariate statistical tests (F-test), and wrapper methods like Boruta and Recursive Feature Elimination (RFE). Additionally, we employed embedded methods such as XGBoost, SVC linear with the SelectFromModel class from scikit-learn, Random Forest, Extra Trees with Feature Importance, and LASSO (a regularization-based embedded method). By combining Filter, Wrapper, and Embedded feature selection techniques, we used an ensemble approach to identify features present in at least five methods. These 55 features show potential as biomarkers for classifying and predicting normal versus cancerous patients.




Installation and Usage:

You can install the package using the following command:


    git clone https://github.com/GITractCancer/LIHCPred.git
    cd LIHCPred



### Predict using LIHCPred

    import pandas as pd
    from LIHCPred import predict

    df = pd.read_csv("path/to/your/data.csv")

    predict(df, model_type='svc')

    
Specify the model type you want to use Models


## Models

The following classifiers are supported:

    svc
    rf
    ab
    xgb
    dt
    et
    lr
    gnb
    knn
    mlp
