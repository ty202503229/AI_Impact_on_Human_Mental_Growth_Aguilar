AI Impact on Human Mental Growth Predictor

A Django-based machine learning web application that predicts how an individual's engagement with Artificial Intelligence affects their cognitive and mental growth outcomes. This repository features a complete predictive pipeline, integrating a serialized Scikit-Learn model suite into a dynamic web form with automated logging to a MySQL database.

Goal & Objective

The primary objective of this project is to build an empirical tracking and predictive framework capable of evaluating an individual's behavioral patterns, demographic status, and cognitive metrics against their projected mental development in the AI era. 

By analyzing user-submitted feature inputs, the app classifies the human mental trajectory into three distinct actionable outcomes:
1. **Positive Growth** — High human cognitive performance outshining or co-evolving constructively with AI usage.
2. **Stagnant / Moderate** — Balanced or neutral impact, indicating neither significant advancement nor cognitive decay.
3. **Cognitive Decline Risk** — Over-reliance patterns where heavy AI offloading signals risk factors for cognitive atrophy.


Dataset Description

The predictive models are trained on data tracking demographic variables alongside detailed psychological, operational, and cognitive attributes.

**Dataset Source URL:** [AI Impact on Human Mental Growth Dataset](https://www.kaggle.com/datasets) *(Replace with your specific dataset download link if hosted on Kaggle or custom source)*

Features & Columns Breakdown

The dataset comprises 24 core input features split across categorical metrics, user behaviors, and internal cognitive measurements:

| Feature Name | Data Type | Description |
| :--- | :--- | :--- |
| **Row_ID** | Integer | Unique identifier for each data row. |
| **Year** | Integer | The simulated chronological year of the data capture. |
| **Era** | Categorical | Broad socio-technological phase (e.g., *AI Mainstream Adoption*, *Symbiotic Intelligence Age*). |
| **Scenario** | Categorical | Socio-economic outlook context (*Optimistic*, *Mixed*, *Pessimistic*). |
| **Region** | Categorical | Geographic distribution of the sample population. |
| **Demographic_Group** | Categorical | Target generation/age tier (e.g., *Youth (18-25)*, *Young Adult (26-35)*, *Senior*). |
| **Education_Level** | Categorical | Highest educational achievement status. |
| **Profession** | Categorical | Industry vertical or technical background area. |
| **AI_Tool_Category** | Categorical | Core type of AI tools used frequently (e.g., *Basic Assistants*, *AGI-Adjacent Tools*). |
| **Weekly_AI_Usage_Hours** | Numerical | Quantitative workload volume interaction with AI platforms per week. |
| **AI_Dependency_Score** | Numerical | Scaled metric measuring psychological or workflow reliance on AI outputs. |
| **Human_Creativity_Score** | Numerical | Standard test metric rating human independent abstract ideation. |
| **Critical_Thinking_Ability**| Numerical | Performance score evaluating deductive logic and underlying evaluation. |
| **Problem_Solving_Skills** | Numerical | Competency indicators regarding standalone structural problem resolution. |
| **Emotional_Intelligence** | Numerical | Assessment index of empathy, self-regulation, and interpersonal soft skills. |
| **Innovation_Rate** | Numerical | Metric quantifying active deployment of unique, productive ideas. |
| **Learning_Speed** | Numerical | Adaptive pace index evaluating absorption rates of new data sets. |
| **Human_Decision_Making_Involvement** | Numerical | Proportional percentage of final choices made entirely without system guidance. |
| **Social_Interaction_Quality**| Numerical | Empirical rating of real-world community communication health. |
| **Cognitive_Load_Index** | Numerical | Measure of active working-memory strain experienced by the user. |
| **Mental_Wellbeing_Score** | Numerical | Quantified measure of emotional stability and low burn-out frequency. |
| **AI_Tool_Proficiency** | Numerical | Technical execution score evaluating accuracy of prompting and system utilization. |
| **Adaptability_Score** | Numerical | Metric tracking dynamic response capacity to evolving environmental shifts. |
| **Attention_Span_Minutes** | Numerical | Maximum uninterrupted focal period observed for complex tasks. |
| **Outcome_Label** *(Target)*| Categorical | **Target variable classification:** `Positive Growth`, `Stagnant / Moderate`, or `Cognitive Decline Risk`. |


Data Cleaning & Preparation Techniques

To construct an un-biased, clean dataset suitable for production-level machine learning inference, the following pipeline steps were implemented:

1. **Handling Missing & Invalid Values:** Null variables, extreme out-of-range bounds, and duplicate entries were scrubbed and rectified to ensure input feature integrity.
2. **Feature Engineering:** Creation of an operational `Cognitive_Composite_Score` mapping interactions between analytical skills and working strain markers to assist the underlying tree splitting criteria.
3. **Categorical Encoding:** String-based inputs (e.g., Demographic Groups, Profession tiers) were encoded uniformly using label maps or one-hot vectors to convert text into numeric tensors readable by Scikit-Learn.
4. **Feature Standardization & Scaling:** Numerical measurements across varying magnitudes (such as raw minutes vs out-of-100 indexes) were normalized using a **Standard Scaler** (`scaler.pkl`), centering values to zero-mean and unit variance:
   $$z = \frac{x - \mu}{\sigma}$$
5. **Target Normalization:** The target class was parsed using a `TargetEncoder` (`target_label_encoder.pkl`) mapping numerical arrays safely back into intuitive human-readable strings inside the user interface.


Modeling, Algorithms, & Evaluation Metrics

Multiple experimental iterations were conducted to determine optimal separation surfaces between the cognitive outcome classes.

Selected Algorithmic Paradigm
The production model utilizes an optimized **Gradient Boosting Classifier** (`best_ml_model.pkl`). This ensemble method sequentially constructs weak decision trees, with each new model calculating corrections based on residual classification error optimization via a specialized log-loss objective function.

Performance Evaluation Metrics
To validate model performance, the classification experiments were assessed using the following metrics:

**Accuracy Score:** Measures the overall fraction of correctly predicted cognitive outcomes across all three classes.
**Log-Loss (Cross-Entropy Loss):** The fundamental objective minimized during training, measuring how close the predicted class probabilities align with the true categorical target vector.
**Precision & Recall:** * *Precision* tracks the app's capability to avoid false alarms (e.g., mislabeling a stable student as high-risk).
  * *Recall (Sensitivity)* ensures the model detects true cases of `Cognitive Decline Risk` without skipping actual vulnerable profiles.
**F1-Score:** Harmonic mean combining Precision and Recall parameters to guarantee strong performance even on potentially imbalanced class distributions.
