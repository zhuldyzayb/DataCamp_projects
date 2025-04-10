import pandas as pd
from pandas.api.types import CategoricalDtype
# 1. Columns containing categories with only two factors must be stored as Booleans (bool).
# 2. Columns containing integers only must be stored as 32-bit integers (int32).
# 3. Columns containing floats must be stored as 16-bit floats (float16).
# 4. Columns containing nominal categorical data must be stored as the category data type.
# 5. Columns containing ordinal categorical data must be stored as ordered categories,
#    and not mapped to numerical values, with an order that reflects the natural order of the column.
# 6. The DataFrame should be filtered to only contain students with 10
#    or more years of experience at companies with at least 1000 employees, as their
#    recruiter base is suited to more experienced professionals at enterprise companies.

ds_jobs = pd.read_csv("customer_train.csv")
#print(ds_jobs.info())
# 0   student_id              19158 non-null  int64
# 1   city                    19158 non-null  object
# 2   city_development_index  19158 non-null  float64
# 3   gender                  14650 non-null  object
# 4   relevant_experience     19158 non-null  object
# 5   enrolled_university     18772 non-null  object
# 6   education_level         18698 non-null  object
# 7   major_discipline        16345 non-null  object
# 8   experience              19093 non-null  object
# 9   company_size            13220 non-null  object
# 10  company_type            13018 non-null  object
# 11  last_new_job            18735 non-null  object
# 12  training_hours          19158 non-null  int64
# 13  job_change              19158 non-null  float64
# dtypes: float64(2), int64(2), object(10)
# memory usage: 2.0+ MB

ds_jobs_transformed = ds_jobs.copy()
# int32
ds_jobs_transformed['student_id'] = ds_jobs_transformed['student_id'].astype('int32')
ds_jobs_transformed['training_hours'] = ds_jobs_transformed['training_hours'].astype('int32')
# bool
ds_jobs_transformed['job_change'] = ds_jobs_transformed['job_change'].map({1:True, 0:False})
ds_jobs_transformed['gender'] = ds_jobs_transformed['gender'].map({'Male':True, 'Female':False})
ds_jobs_transformed['relevant_experience'] = ds_jobs_transformed['relevant_experience'].map(
    {'Has relevant experience':True, 'No relevant experience':False})
# float16
ds_jobs_transformed['city_development_index'] = ds_jobs_transformed['city_development_index'].astype('float16')
# category
ds_jobs_transformed['city'] = ds_jobs_transformed['city'].astype('category')
ds_jobs_transformed['major_discipline'] = ds_jobs_transformed['major_discipline'].astype('category')
ds_jobs_transformed['company_type'] = ds_jobs_transformed['company_type'].astype('category')

# ordered category
# education_level:
ed_levels = CategoricalDtype(categories=['Primary School', 'High School', 'Graduate', 'Masters', 'Phd'], ordered=True)
ds_jobs_transformed['education_level'] = ds_jobs_transformed['education_level'].astype(ed_levels)
# enrolled_university:
en_levels = CategoricalDtype(categories=['no_enrollment', 'Part time course', 'Full time course'], ordered=True)
ds_jobs_transformed['enrolled_university'] = ds_jobs_transformed['enrolled_university'].astype(en_levels)
# experience:
exp_levels = ['<1', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
              '13', '14', '15', '16', '17', '18', '19', '20', '>20']
experience = CategoricalDtype(categories = exp_levels, ordered = True)
ds_jobs_transformed['experience'] = ds_jobs_transformed['experience'].astype(experience)
# company_size:
comp_levels = ['<10', '10-49', '50-99', '100-499', '500-999', '1000-4999', '5000-9999', '10000+']
company_size = CategoricalDtype(categories = comp_levels, ordered=True)
ds_jobs_transformed['company_size'] = ds_jobs_transformed['company_size'].astype(company_size)
# last_new_job:
job_cats = ['never', '1', '2', '3', '4', '>4']
job_levels = CategoricalDtype(categories=job_cats, ordered=True)
ds_jobs_transformed['last_new_job'] = ds_jobs_transformed['last_new_job'].astype(job_levels)


# students with 10 or more years of experience
ds_jobs_transformed = ds_jobs_transformed[ds_jobs_transformed['experience'].isin(['10', '11', '12',
                                        '13', '14', '15', '16', '17', '18', '19', '20', '>20'])]
# companies with at least 1000 employees
ds_jobs_transformed = ds_jobs_transformed[ds_jobs_transformed['company_size'].isin(['1000-4999', '5000-9999', '10000+'])]
print(ds_jobs_transformed.info())
