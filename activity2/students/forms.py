from django import forms

class AIMentalGrowthForm(forms.Form):
    # --- Categorical fields matching values from the dataset ---
    ERA_CHOICES = [
        ('AI Mainstream Adoption', 'AI Mainstream Adoption'),
        ('AI-Augmented Society', 'AI-Augmented Society'),
        ('Cognitive Co-Evolution', 'Cognitive Co-Evolution'),
        ('Symbiotic Intelligence Age', 'Symbiotic Intelligence Age'),
    ]
    SCENARIO_CHOICES = [
        ('Optimistic', 'Optimistic'),
        ('Mixed', 'Mixed'),
        ('Pessimistic', 'Pessimistic'),
    ]
    REGION_CHOICES = [
        ('East Asia', 'East Asia'),
        ('South Asia', 'South Asia'),
        ('Southeast Asia', 'Southeast Asia'),
        ('Europe', 'Europe'),
        ('Latin America', 'Latin America'),
        ('North America', 'North America'),
    ]
    DEMOGRAPHIC_CHOICES = [
        ('Youth (18-25)', 'Youth (18-25)'),
        ('Young Adult (26-35)', 'Young Adult (26-35)'),
        ('Middle-Aged (36-50)', 'Middle-Aged (36-50)'),
        ('Senior (51-65)', 'Senior (51-65)'),
        ('Elder (65+)', 'Elder (65+)'),
    ]
    EDUCATION_CHOICES = [
        ('Primary', 'Primary'),
        ('High School', 'High School'),
        ('Undergraduate', 'Undergraduate'),
        ('Postgraduate', 'Postgraduate'),
        ('PhD/Research', 'PhD/Research'),
    ]
    PROFESSION_CHOICES = [
        ('Technology', 'Technology'),
        ('Healthcare', 'Healthcare'),
        ('Business', 'Business'),
        ('Education', 'Education'),
        ('Skilled Trades', 'Skilled Trades'),
    ]
    TOOL_CHOICES = [
        ('None', 'None'),
        ('Basic Assistants', 'Basic Assistants'),
        ('Multi-modal AI', 'Multi-modal AI'),
        ('AGI-Adjacent Tools', 'AGI-Adjacent Tools'),
        ('Full AGI Integration', 'Full AGI Integration'),
    ]

    # --- Meta Features (Notice these are now Capitalized) ---
    Year = forms.IntegerField(
        label="Prediction Year", 
        initial=2026, 
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    Era = forms.ChoiceField(
        label="Historical Era", 
        choices=ERA_CHOICES, 
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    Scenario = forms.ChoiceField(
        label="Socioeconomic Scenario", 
        choices=SCENARIO_CHOICES, 
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    Region = forms.ChoiceField(
        label="Geographic Region", 
        choices=REGION_CHOICES, 
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    Demographic_Group = forms.ChoiceField(
        label="Demographic Cohort", 
        choices=DEMOGRAPHIC_CHOICES, 
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    Education_Level = forms.ChoiceField(
        label="Education Attainment", 
        choices=EDUCATION_CHOICES, 
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    Profession = forms.ChoiceField(
        label="Industry Profession", 
        choices=PROFESSION_CHOICES, 
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    AI_Tool_Category = forms.ChoiceField(
        label="Primary AI Tool Class", 
        choices=TOOL_CHOICES, 
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    # --- Core Numerical Metric Fields (Also Capitalized) ---
    Weekly_AI_Usage_Hours = forms.FloatField(
        label="Weekly AI Usage (Hours)", 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'e.g. 25.5'})
    )
    AI_Dependency_Score = forms.FloatField(
        label="AI Dependency Score (0-100)", 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0', 'max': '100'})
    )
    Human_Creativity_Score = forms.FloatField(
        label="Human Creativity Score (0-100)", 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0', 'max': '100'})
    )
    Critical_Thinking_Ability = forms.FloatField(
        label="Critical Thinking Ability (0-100)", 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0', 'max': '100'})
    )
    Problem_Solving_Skills = forms.FloatField(
        label="Problem Solving Skills (0-100)", 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0', 'max': '100'})
    )
    Emotional_Intelligence = forms.FloatField(
        label="Emotional Intelligence (0-100)", 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0', 'max': '100'})
    )
    Innovation_Rate = forms.FloatField(
        label="Individual Innovation Rate (0-100)", 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0', 'max': '100'})
    )
    Learning_Speed = forms.FloatField(
        label="Learning Speed Index (0-100)", 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0', 'max': '100'})
    )
    Human_Decision_Making_Involvement = forms.FloatField(
        label="Decision Autonomy (0-100)", 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0', 'max': '100'})
    )
    Social_Interaction_Quality = forms.FloatField(
        label="Social Interaction Quality (0-100)", 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0', 'max': '100'})
    )
    Cognitive_Load_Index = forms.FloatField(
        label="Cognitive Load Index (0-100)", 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0', 'max': '100'})
    )
    Mental_Wellbeing_Score = forms.FloatField(
        label="Mental Wellbeing Score (0-100)", 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0', 'max': '100'})
    )
    AI_Tool_Proficiency = forms.FloatField(
        label="AI Tool Proficiency (0-100)", 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0', 'max': '100'})
    )
    Adaptability_Score = forms.FloatField(
        label="Personal Adaptability Score (0-100)", 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0', 'max': '100'})
    )
    Attention_Span_Minutes = forms.FloatField(
        label="Attention Span Duration (Minutes)", 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0'})
    )