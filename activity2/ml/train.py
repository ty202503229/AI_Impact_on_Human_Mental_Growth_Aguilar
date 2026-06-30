import pandas as pd
import numpy as np
import joblib
import warnings

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report

warnings.filterwarnings('ignore')

def main():
    print("Loading dataset...")
    # 1. Load Data
    try:
        df = pd.read_csv('dataset/AI_Impact_on_Human_Mental_Growth.csv')
    except FileNotFoundError:
        print("Error: 'AI_Impact_on_Human_Mental_Growth.csv' not found in the current directory.")
        return

    # 2. Data Cleaning
    print("Cleaning data...")
    df = df.drop_duplicates()

    # Drop irrelevant and heavy text columns
    cols_to_drop = ['Row_ID', 'Positive_Effects_of_AI', 'Negative_Effects_of_AI']
    df = df.drop(columns=[c for c in cols_to_drop if c in df.columns], errors='ignore')

    # Separate categorical and numeric columns
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

    if 'Outcome_Label' in categorical_cols:
        categorical_cols.remove('Outcome_Label')

    # Drop rows without a target variable
    df = df.dropna(subset=['Outcome_Label'])

    # Impute missing values
    num_imputer = SimpleImputer(strategy='median')
    df[numeric_cols] = num_imputer.fit_transform(df[numeric_cols])

    cat_imputer = SimpleImputer(strategy='most_frequent')
    if len(categorical_cols) > 0:
        df[categorical_cols] = cat_imputer.fit_transform(df[categorical_cols])

    # Outlier treatment using IQR
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df[col] = np.clip(df[col], lower_bound, upper_bound)

    # 3. Feature Engineering
    print("Engineering features...")
    if 'Critical_Thinking_Ability' in df.columns and 'Problem_Solving_Skills' in df.columns:
        df['Cognitive_Composite_Score'] = df['Critical_Thinking_Ability'] + df['Problem_Solving_Skills']
        numeric_cols.append('Cognitive_Composite_Score')

    # Encode categorical features
    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])

    # Encode Target Variable
    target_le = LabelEncoder()
    df['Outcome_Label'] = target_le.fit_transform(df['Outcome_Label'])

    X = df.drop(columns=['Outcome_Label'])
    y = df['Outcome_Label']

    # 4. Data Scaling (Standardization based on your scaler.pkl)
    print("Scaling features...")
    scaler = StandardScaler()
    X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

    # 5. Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # 6. Model Training (Gradient Boosting based on your best_ml_model.pkl)
    print("Training Gradient Boosting Classifier...")
    model = GradientBoostingClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # 7. Evaluation
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"\nModel Accuracy on Test Set: {acc * 100:.2f}%\n")
    print("Classification Report:")
    # Use target_le to get the original class names for the report
    target_names = [str(cls) for cls in target_le.classes_]
    print(classification_report(y_test, y_pred, target_names=target_names))

    # 8. Exporting the Model and Preprocessors
    print("Exporting model and preprocessors...")
    joblib.dump(model, 'best_ml_model.pkl')
    joblib.dump(scaler, 'scaler.pkl')
    joblib.dump(target_le, 'target_label_encoder.pkl')
    
    # Optional: Save a clean version of the dataset for reference
    df_clean_final = pd.concat([X_scaled, y], axis=1)
    df_clean_final.to_csv('best_clean_dataset.csv', index=False)

    print("\nTraining complete! Successfully saved:")
    print(" - best_ml_model.pkl")
    print(" - scaler.pkl")
    print(" - target_label_encoder.pkl")
    print(" - best_clean_dataset.csv")

if __name__ == "__main__":
    main()