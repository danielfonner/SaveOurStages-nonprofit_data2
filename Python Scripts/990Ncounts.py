#SaveOurStagesAnalysis.py

# Created by Daniel F Fonner, Associate Director for Research, SMU DataArts - 10/29/2020
# In partnership with Theatre Communications Group and the League of American Orchestras

# This analysis explores the level of earned revenue, contributed revenue, gross revenue, and expenses of nonprofit performing arts organizations.
# The data and calculations should provide information to inform lawmakers currently negotiating the Save Our Stages bill to provide funding to
# performing arts venues that have had to close due to COVID-19, and thus cutting off some revenue streams.
# You can read the current Senate Bill here startng on page 161: https://www.sbc.senate.gov/public/_cache/files/6/6/660e49ed-3ced-482f-9de7-938a17b48ae4/625B9431CE99F0693E2F94E3CFCAFAC9.hen20a83.pdf


# Import libraries
import csv
import numpy as np
import pandas as pd
import statistics
import math


dfBMF = pd.read_csv("bmf_4-2020_nccs.csv")

df990Ndata = pd.read_csv('data-download-epostcard.txt', sep='|', index_col=False, 
                 names=['EIN','Tax Year','Name','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23'])

df = pd.merge(df990Ndata[['EIN','Tax Year','Name']], dfBMF[['EIN','NAME','STATE','NAICS','NTEEFINAL','OUTNCCS']], how='inner', on='EIN')
df.drop_duplicates(subset = "EIN", keep = "last", inplace = True)

# Keep rows that start with NAICS 7111 (https://www.naics.com/naics-code-description/?code=7111)
# Keep rows for NCCS's BMF inclusion/exclusion reasoning (https://nccs-data.urban.org/dd2.php?close=1&form=BMF+08/2016)

df['NAICS'] = df['NAICS'].astype(str)
df = df[(df['NAICS'].str.startswith('7111'))|(df['NAICS'].str.startswith('7113') & (df['NTEEFINAL'].str.startswith('A')))]
df = df[df['OUTNCCS']=='IN']
df.drop('OUTNCCS', axis=1, inplace=True)  

print(len(df))
# Convert dataframe to CSV and save
saveName = "990N_CleanedPerformingArtsData_SaveOurStages.csv"
convertToCSV = df.to_csv(saveName)


# End
print("Complete")