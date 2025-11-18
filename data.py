import numpy as np
import pandas as pd

med_insurance = pd.read_csv('insurance.csv')

partition_by_bmi = lambda bmi: 'Underweight' if bmi < 25.0 else 'Overweight'
bmi_copy = med_insurance['bmi']
med_insurance_bmi = bmi_copy.apply(partition_by_bmi)
med_insurance_bmi = med_insurance_bmi.to_frame()

med_insurance_bmi.rename(columns={'bmi': 'weight_category'}, inplace=True)
med_insurance_bmi['bmi'] = med_insurance.bmi

partition_by_bmi_2 = lambda row: 'Normal weight' if (row.bmi >= 18.5 and row.bmi < 25.0) else row.weight_category
med_insurance_bmi['weight_category'] = med_insurance_bmi.apply(partition_by_bmi_2, axis=1)

partition_by_bmi_3 = lambda row: 'Obesity' if row.bmi > 30.0 else row.weight_category
med_insurance_bmi['weight_category'] = med_insurance_bmi.apply(partition_by_bmi_3, axis=1)

print(med_insurance_bmi.head(30))

med_insurance_2 = med_insurance[['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges']]
med_insurance_2['weight_category'] = med_insurance_bmi['weight_category']
print(med_insurance_2.head(5))

med_insurance_2 = pd.get_dummies(data=med_insurance_2, columns=['weight_category', 'region'], dtype='int')
print(med_insurance_2.head(5))

med_insurance_2.to_csv('med_insurance_processed.csv', index=False)


