import os
import joblib  # <-- CHANGED: Using joblib instead of standard pickle
import numpy as np
from django.shortcuts import render
from django.conf import settings
from .forms import AIMentalGrowthForm

# ---------------------------------------------------------
# 1. AUTO-DETECT ML FILES
# ---------------------------------------------------------
SEARCH_FOLDERS = [
    os.path.join(settings.BASE_DIR, 'ml'),                  
    os.path.join(settings.BASE_DIR, 'students'),            
    os.path.dirname(os.path.abspath(__file__))              
]

model, scaler, target_encoder = None, None, None
debug_msg = f"Could not find .pkl files. Looked in: {SEARCH_FOLDERS}"

for folder in SEARCH_FOLDERS:
    m_path = os.path.join(folder, 'best_ml_model.pkl')
    s_path = os.path.join(folder, 'scaler.pkl')
    e_path = os.path.join(folder, 'target_label_encoder.pkl')
    
    if os.path.exists(m_path) and os.path.exists(s_path) and os.path.exists(e_path):
        try:
            # CHANGED: Now using joblib.load() which handles scikit-learn models natively
            model = joblib.load(m_path)
            scaler = joblib.load(s_path)
            target_encoder = joblib.load(e_path)
            
            debug_msg = f"Successfully loaded models from: {folder}"
            print(f">>> {debug_msg}")
            break 
        except Exception as e:
            debug_msg = f"Found files in {folder} but got an error loading them: {e}"
            print(f">>> {debug_msg}")

# ---------------------------------------------------------
# 2. CALIBRATED MAPPINGS
# ---------------------------------------------------------
ERA_MAPPING = {
    'AI Mainstream Adoption': 0, 'AI-Augmented Society': 1,
    'Cognitive Co-Evolution': 2, 'Symbiotic Intelligence Age': 3
}
SCENARIO_MAPPING = {'Mixed': 0, 'Optimistic': 1, 'Pessimistic': 2}
REGION_MAPPING = {
    'East Asia': 0, 'Europe': 1, 'Latin America': 2,
    'North America': 3, 'South Asia': 4, 'Southeast Asia': 5
}
DEMOGRAPHIC_MAPPING = {
    'Elder (65+)': 0, 'Middle-Aged (36-50)': 1, 'Senior (51-65)': 2,
    'Young Adult (26-35)': 3, 'Youth (18-25)': 4
}
EDUCATION_MAPPING = {
    'High School': 0, 'PhD/Research': 1, 'Postgraduate': 2,
    'Primary': 3, 'Undergraduate': 4
}
PROFESSION_MAPPING = {
    'Business': 0, 'Education': 1, 'Healthcare': 2,
    'Skilled Trades': 3, 'Technology': 4
}
TOOL_MAPPING = {
    'AGI-Adjacent Tools': 0, 'Basic Assistants': 1, 'Full AGI Integration': 2,
    'Multi-modal AI': 3, 'None': 4
}

# ---------------------------------------------------------
# 3. VIEWS
# ---------------------------------------------------------
def predict_view(request):
    result = None
    
    if request.method == 'POST':
        form = AIMentalGrowthForm(request.POST)
        if form.is_valid():
            
            if not model or not scaler or not target_encoder:
                result = f"SYSTEM ERROR: {debug_msg}"
                
            else:
                try:
                    data = form.cleaned_data
                    
                    era_encoded = ERA_MAPPING.get(data['Era'], 0)
                    scenario_encoded = SCENARIO_MAPPING.get(data['Scenario'], 0)
                    region_encoded = REGION_MAPPING.get(data['Region'], 0)
                    demo_encoded = DEMOGRAPHIC_MAPPING.get(data['Demographic_Group'], 0)
                    edu_encoded = EDUCATION_MAPPING.get(data['Education_Level'], 0)
                    prof_encoded = PROFESSION_MAPPING.get(data['Profession'], 0)
                    tool_encoded = TOOL_MAPPING.get(data['AI_Tool_Category'], 4)
                    
                    cognitive_composite = (data['Critical_Thinking_Ability'] + data['Problem_Solving_Skills']) / 2
                    
                    feature_vector = [
                        data['Year'], era_encoded, scenario_encoded, region_encoded,
                        demo_encoded, edu_encoded, prof_encoded, tool_encoded,
                        data['Weekly_AI_Usage_Hours'], data['AI_Dependency_Score'],
                        data['Human_Creativity_Score'], data['Critical_Thinking_Ability'],
                        data['Problem_Solving_Skills'], data['Emotional_Intelligence'],
                        data['Innovation_Rate'], data['Learning_Speed'],
                        data['Human_Decision_Making_Involvement'], data['Social_Interaction_Quality'],
                        data['Cognitive_Load_Index'], data['Mental_Wellbeing_Score'],
                        data['AI_Tool_Proficiency'], data['Adaptability_Score'],
                        data['Attention_Span_Minutes'], cognitive_composite
                    ]
                    
                    input_matrix = np.array(feature_vector).reshape(1, -1)
                    scaled_input = scaler.transform(input_matrix)
                    raw_prediction = model.predict(scaled_input)
                    
                    # ... [previous prediction code remains exactly the same] ...
                    result = target_encoder.inverse_transform(raw_prediction)[0]
                    
                    # 1. FIX: Use PredictionHistory to save the data
                    try:
                        from .models import PredictionHistory
                        PredictionHistory.objects.create(
                            demographic=data['Demographic_Group'],
                            profession=data['Profession'],
                            weekly_hours=data['Weekly_AI_Usage_Hours'],
                            prediction_result=result
                        )
                    except Exception as e:
                        print(f"Database Save Error: {e}") # This will print to terminal if it fails
                        
                except Exception as e:
                    result = f"Error during data processing: {str(e)}"
    else:
        form = AIMentalGrowthForm()
        
    return render(request, 'predict.html', {'form': form, 'result': result})

# 2. FIX: Use PredictionHistory to load the data
def history_view(request):
    try:
        from .models import PredictionHistory
        records = PredictionHistory.objects.all().order_by('-created_at')
    except Exception as e:
        print(f"Database Load Error: {e}")
        records = []
        
    return render(request, 'history.html', {'records': records})