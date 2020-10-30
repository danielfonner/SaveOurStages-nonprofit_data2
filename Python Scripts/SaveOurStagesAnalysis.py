#SaveOurStagesAnalysis.py

# Created by Daniel F Fonner, Associate Director for Research, SMU DataArts
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


# Import BMF and 990 and 990ez CSVs
# BMF from  National Center for Charitable Statistics at the Urban Institute as it includes NAICS codes: https://nccs-data.urban.org/data.php?ds=bmf
# 990 Data from the IRS (https://www.irs.gov/statistics/soi-tax-stats-annual-extract-of-tax-exempt-organization-financial-data)

# This analysis combines all 990 and 990ez data processed in 2017, 2018, and 2019 keeping the most recent 990 data for each organization based on EIN.
# This ensures that all current/active nonprofit performing arts organizations are accounted for since organizations have a 3 year filing window before their tax exempt status is revoked.

dfBMF = pd.read_csv("bmf_4-2020_nccs.csv")

dfData990_2017 = pd.read_csv("2017_990.csv", usecols=['EIN','tax_pd','totcntrbgfts','totprgmrevnue','rntlexpnsreal','rntlexpnsprsnl','cstbasisecur','cstbasisothr','lessdirfndrsng','lessdirgaming','lesscstofgoods','totrevenue','totfuncexpns'])
dfData990ez_2017 = pd.read_csv("2017_990ez.csv", usecols=['EIN','tax_pd','totcntrbs','prgmservrev','basisalesexpnsothr','direxpns','costgoodsold','totrevnue','totexpns'])
dfData990_2018 = pd.read_csv("2018_990.csv", usecols=['EIN','tax_pd','totcntrbgfts','totprgmrevnue','rntlexpnsreal','rntlexpnsprsnl','cstbasisecur','cstbasisothr','lessdirfndrsng','lessdirgaming','lesscstofgoods','totrevenue','totfuncexpns'])
dfData990ez_2018 = pd.read_csv("2018_990ez.csv", usecols=['EIN','tax_pd','totcntrbs','prgmservrev','basisalesexpnsothr','direxpns','costgoodsold','totrevnue','totexpns'])
dfData990_2019 = pd.read_csv("2019_990.csv", usecols=['EIN','tax_pd','totcntrbgfts','totprgmrevnue','rntlexpnsreal','rntlexpnsprsnl','cstbasisecur','cstbasisothr','lessdirfndrsng','lessdirgaming','lesscstofgoods','totrevenue','totfuncexpns'])
dfData990ez_2019 = pd.read_csv("2019_990ez.csv", usecols=['EIN','tax_pd','totcntrbs','prgmservrev','basisalesexpnsothr','direxpns','costgoodsold','totrevnue','totexpns'])



##### Clean the various 990 and 990ez to align with variable names that are the same.
# 2017 990

dfData990_2017['Source'] = '2017-990'
dfData990_2017['GrossRev'] = dfData990_2017['totrevenue'] + dfData990_2017['rntlexpnsreal'] + dfData990_2017['rntlexpnsprsnl'] + dfData990_2017['cstbasisecur'] + dfData990_2017['cstbasisothr'] + dfData990_2017['lessdirfndrsng'] + dfData990_2017['lessdirgaming'] + dfData990_2017['lesscstofgoods']
dfData990_2017 = dfData990_2017[['EIN','tax_pd','totcntrbgfts','totprgmrevnue','totrevenue','totfuncexpns','GrossRev','Source']]
dfData990_2017.columns = ['EIN','tax_pd','contributed_rev','earned_program_service_rev','total_rev','total_exp','gross_rev','Source']

conditions = [((.45*dfData990_2017['gross_rev'])<=12000000),((.45*dfData990_2017['gross_rev'])>12000000)]
choices = [(.45*dfData990_2017['gross_rev']),(12000000)]
dfData990_2017['45_of_Gross_max_12m'] = np.select(conditions,choices) 

conditions = [((.45*dfData990_2017['earned_program_service_rev'])<=12000000),((.45*dfData990_2017['earned_program_service_rev'])>12000000)]
choices = [(.45*dfData990_2017['earned_program_service_rev']),(12000000)]
dfData990_2017['45_of_Earned_max_12m'] = np.select(conditions,choices)

conditions = [((dfData990_2017['earned_program_service_rev'])<=(dfData990_2017['45_of_Gross_max_12m'])),((dfData990_2017['earned_program_service_rev'])>(dfData990_2017['45_of_Gross_max_12m']))]
choices = [(dfData990_2017['earned_program_service_rev']),(dfData990_2017['45_of_Gross_max_12m'])]
dfData990_2017['100_of_Earned_upto_45_Gross_max_12m'] = np.select(conditions,choices)


# 2017 990EZ

dfData990ez_2017['Source'] = '2017-990ez'
dfData990ez_2017['GrossRev'] = dfData990ez_2017['totrevnue'] + dfData990ez_2017['basisalesexpnsothr'] + dfData990ez_2017['direxpns'] + dfData990ez_2017['costgoodsold']
dfData990ez_2017 = dfData990ez_2017[['EIN','tax_pd','totcntrbs','prgmservrev','totrevnue','totexpns','GrossRev','Source']]
dfData990ez_2017.columns = ['EIN','tax_pd','contributed_rev','earned_program_service_rev','total_rev','total_exp','gross_rev','Source']

conditions = [((.45*dfData990ez_2017['gross_rev'])<=12000000),((.45*dfData990ez_2017['gross_rev'])>12000000)]
choices = [(.45*dfData990ez_2017['gross_rev']),(12000000)]
dfData990ez_2017['45_of_Gross_max_12m'] = np.select(conditions,choices) 

conditions = [((.45*dfData990ez_2017['earned_program_service_rev'])<=12000000),((.45*dfData990ez_2017['earned_program_service_rev'])>12000000)]
choices = [(.45*dfData990ez_2017['earned_program_service_rev']),(12000000)]
dfData990ez_2017['45_of_Earned_max_12m'] = np.select(conditions,choices)

conditions = [((dfData990ez_2017['earned_program_service_rev'])<=(dfData990ez_2017['45_of_Gross_max_12m'])),((dfData990ez_2017['earned_program_service_rev'])>(dfData990ez_2017['45_of_Gross_max_12m']))]
choices = [(dfData990ez_2017['earned_program_service_rev']),(dfData990ez_2017['45_of_Gross_max_12m'])]
dfData990ez_2017['100_of_Earned_upto_45_Gross_max_12m'] = np.select(conditions,choices)


# 2018 990

dfData990_2018['Source'] = '2018-990'
dfData990_2018['GrossRev'] = dfData990_2018['totrevenue'] + dfData990_2018['rntlexpnsreal'] + dfData990_2018['rntlexpnsprsnl'] + dfData990_2018['cstbasisecur'] + dfData990_2018['cstbasisothr'] + dfData990_2018['lessdirfndrsng'] + dfData990_2018['lessdirgaming'] + dfData990_2018['lesscstofgoods']
dfData990_2018 = dfData990_2018[['EIN','tax_pd','totcntrbgfts','totprgmrevnue','totrevenue','totfuncexpns','GrossRev','Source']]
dfData990_2018.columns = ['EIN','tax_pd','contributed_rev','earned_program_service_rev','total_rev','total_exp','gross_rev','Source']

conditions = [((.45*dfData990_2018['gross_rev'])<=12000000),((.45*dfData990_2018['gross_rev'])>12000000)]
choices = [(.45*dfData990_2018['gross_rev']),(12000000)]
dfData990_2018['45_of_Gross_max_12m'] = np.select(conditions,choices) 

conditions = [((.45*dfData990_2018['earned_program_service_rev'])<=12000000),((.45*dfData990_2018['earned_program_service_rev'])>12000000)]
choices = [(.45*dfData990_2018['earned_program_service_rev']),(12000000)]
dfData990_2018['45_of_Earned_max_12m'] = np.select(conditions,choices)

conditions = [((dfData990_2018['earned_program_service_rev'])<=(dfData990_2018['45_of_Gross_max_12m'])),((dfData990_2018['earned_program_service_rev'])>(dfData990_2018['45_of_Gross_max_12m']))]
choices = [(dfData990_2018['earned_program_service_rev']),(dfData990_2018['45_of_Gross_max_12m'])]
dfData990_2018['100_of_Earned_upto_45_Gross_max_12m'] = np.select(conditions,choices)


# 2018 990EZ

dfData990ez_2018['Source'] = '2018-990ez'
dfData990ez_2018['GrossRev'] = dfData990ez_2018['totrevnue'] + dfData990ez_2018['basisalesexpnsothr'] + dfData990ez_2018['direxpns'] + dfData990ez_2018['costgoodsold']
dfData990ez_2018 = dfData990ez_2018[['EIN','tax_pd','totcntrbs','prgmservrev','totrevnue','totexpns','GrossRev','Source']]
dfData990ez_2018.columns = ['EIN','tax_pd','contributed_rev','earned_program_service_rev','total_rev','total_exp','gross_rev','Source']

conditions = [((.45*dfData990ez_2018['gross_rev'])<=12000000),((.45*dfData990ez_2018['gross_rev'])>12000000)]
choices = [(.45*dfData990ez_2018['gross_rev']),(12000000)]
dfData990ez_2018['45_of_Gross_max_12m'] = np.select(conditions,choices) 

conditions = [((.45*dfData990ez_2018['earned_program_service_rev'])<=12000000),((.45*dfData990ez_2018['earned_program_service_rev'])>12000000)]
choices = [(.45*dfData990ez_2018['earned_program_service_rev']),(12000000)]
dfData990ez_2018['45_of_Earned_max_12m'] = np.select(conditions,choices)

conditions = [((dfData990ez_2018['earned_program_service_rev'])<=(dfData990ez_2018['45_of_Gross_max_12m'])),((dfData990ez_2018['earned_program_service_rev'])>(dfData990ez_2018['45_of_Gross_max_12m']))]
choices = [(dfData990ez_2018['earned_program_service_rev']),(dfData990ez_2018['45_of_Gross_max_12m'])]
dfData990ez_2018['100_of_Earned_upto_45_Gross_max_12m'] = np.select(conditions,choices)


# 2019 990

dfData990_2019['Source'] = '2019-990'
dfData990_2019['GrossRev'] = dfData990_2019['totrevenue'] + dfData990_2019['rntlexpnsreal'] + dfData990_2019['rntlexpnsprsnl'] + dfData990_2019['cstbasisecur'] + dfData990_2019['cstbasisothr'] + dfData990_2019['lessdirfndrsng'] + dfData990_2019['lessdirgaming'] + dfData990_2019['lesscstofgoods']
dfData990_2019 = dfData990_2019[['EIN','tax_pd','totcntrbgfts','totprgmrevnue','totrevenue','totfuncexpns','GrossRev','Source']]
dfData990_2019.columns = ['EIN','tax_pd','contributed_rev','earned_program_service_rev','total_rev','total_exp','gross_rev','Source']

conditions = [((.45*dfData990_2019['gross_rev'])<=12000000),((.45*dfData990_2019['gross_rev'])>12000000)]
choices = [(.45*dfData990_2019['gross_rev']),(12000000)]
dfData990_2019['45_of_Gross_max_12m'] = np.select(conditions,choices) 

conditions = [((.45*dfData990_2019['earned_program_service_rev'])<=12000000),((.45*dfData990_2019['earned_program_service_rev'])>12000000)]
choices = [(.45*dfData990_2019['earned_program_service_rev']),(12000000)]
dfData990_2019['45_of_Earned_max_12m'] = np.select(conditions,choices)

conditions = [((dfData990_2019['earned_program_service_rev'])<=(dfData990_2019['45_of_Gross_max_12m'])),((dfData990_2019['earned_program_service_rev'])>(dfData990_2019['45_of_Gross_max_12m']))]
choices = [(dfData990_2019['earned_program_service_rev']),(dfData990_2019['45_of_Gross_max_12m'])]
dfData990_2019['100_of_Earned_upto_45_Gross_max_12m'] = np.select(conditions,choices)


# 2019 990EZ

dfData990ez_2019['Source'] = '2019-990ez'
dfData990ez_2019['GrossRev'] = dfData990ez_2019['totrevnue'] + dfData990ez_2019['basisalesexpnsothr'] + dfData990ez_2019['direxpns'] + dfData990ez_2019['costgoodsold']
dfData990ez_2019 = dfData990ez_2019[['EIN','tax_pd','totcntrbs','prgmservrev','totrevnue','totexpns','GrossRev','Source']]
dfData990ez_2019.columns = ['EIN','tax_pd','contributed_rev','earned_program_service_rev','total_rev','total_exp','gross_rev','Source']

conditions = [((.45*dfData990ez_2019['gross_rev'])<=12000000),((.45*dfData990ez_2019['gross_rev'])>12000000)]
choices = [(.45*dfData990ez_2019['gross_rev']),(12000000)]
dfData990ez_2019['45_of_Gross_max_12m'] = np.select(conditions,choices) 

conditions = [((.45*dfData990ez_2019['earned_program_service_rev'])<=12000000),((.45*dfData990ez_2019['earned_program_service_rev'])>12000000)]
choices = [(.45*dfData990ez_2019['earned_program_service_rev']),(12000000)]
dfData990ez_2019['45_of_Earned_max_12m'] = np.select(conditions,choices)

conditions = [((dfData990ez_2019['earned_program_service_rev'])<=(dfData990ez_2019['45_of_Gross_max_12m'])),((dfData990ez_2019['earned_program_service_rev'])>(dfData990ez_2019['45_of_Gross_max_12m']))]
choices = [(dfData990ez_2019['earned_program_service_rev']),(dfData990ez_2019['45_of_Gross_max_12m'])]
dfData990ez_2019['100_of_Earned_upto_45_Gross_max_12m'] = np.select(conditions,choices)





### Combine the 990 files and join with BMF, keeping the most recent 990 for each organization
dataframes990sList = [dfData990_2017,dfData990ez_2017,dfData990_2018,dfData990ez_2018,dfData990_2019,dfData990ez_2019]
df990Combined = pd.concat(dataframes990sList)

df990Combined.sort_values(by=['tax_pd'])
df990Combined.drop_duplicates(subset = "EIN", keep = "last", inplace = True)

df = pd.merge(df990Combined, dfBMF[['EIN','NAME','STATE','NAICS','NTEEFINAL','OUTNCCS']], how='inner', on='EIN')


# Keep rows that start with NAICS 7111 (https://www.naics.com/naics-code-description/?code=7111)
# Additionally, to align with the bill, keep rows that have NAICS codes starting with 7113 AND an NTEE code starting with 'A' (https://www.naics.com/naics-code-description/?code=7113) (https://nccs.urban.org/publication/irs-activity-codes)
# Keep rows for NCCS's BMF inclusion/exclusion reasoning (https://nccs-data.urban.org/dd2.php?close=1&form=BMF+08/2016)

df['NAICS'] = df['NAICS'].astype(str)
df = df[(df['NAICS'].str.startswith('7111'))|(df['NAICS'].str.startswith('7113') & (df['NTEEFINAL'].str.startswith('A')))]
df = df[df['OUTNCCS']=='IN']
df.drop('OUTNCCS', axis=1, inplace=True)  

print(len(df))


# Convert dataframe to CSV and save
saveName = "CleanedPerformingArtsData_SaveOurStages.csv"
convertToCSV = df.to_csv(saveName)


# Calculations
newCols = ['Variable', 'Count', 'Sum', 'Mean', 'Median', 'Minimum', 'Maximum']
dfCalculations = pd.DataFrame(columns = newCols)

columnsToCalculate = ['contributed_rev','earned_program_service_rev','total_rev','total_exp','gross_rev','45_of_Gross_max_12m','45_of_Earned_max_12m','100_of_Earned_upto_45_Gross_max_12m']
for cols in columnsToCalculate:
    columnToList = df[cols].tolist()

    Count = len(columnToList)
    Sum = sum(columnToList)
    Mean = int(statistics.mean(columnToList))
    Median = int(statistics.median(columnToList))
    Minimum = min(columnToList)
    Maximum = max(columnToList)

    currentRowCount = dfCalculations.shape[0]
    currentRowCountPlusOne = currentRowCount + 1
    dfCalculations.loc[currentRowCountPlusOne] = [cols,Count,Sum,Mean,Median,Minimum,Maximum]

# Convert dataframe to CSV and save
saveName = "SummaryStats_SaveOurStages.csv"
convertToCSV = dfCalculations.to_csv(saveName)


# End
print("Complete")
