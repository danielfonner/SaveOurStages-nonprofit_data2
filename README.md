# SaveOurStages-nonprofit_data2
This repository contains data and analysis to support the nonprofit performing arts sector in advocating for funding through the proposed Save Our Stages program within the Heroes Small Business Lifeline Act.


### Created by Daniel F Fonner, Associate Director for Research, SMU DataArts, Southern Methodist University ###
In partnership with Theatre Communications Group and the League of American Orchestras


This analysis explores the level of earned revenue, contributed revenue, gross revenue, and expenses of nonprofit performing arts organizations in the United States. The data and calculations should provide information to inform lawmakers currently negotiating the Save Our Stages component of the Heroes Small Business Lifeline Act, which aims to provide funding to performing arts venues that have had to close due to COVID-19, and thus cutting off some revenue streams. You can read the current Senate Bill here starting on page 161: https://www.sbc.senate.gov/public/_cache/files/6/6/660e49ed-3ced-482f-9de7-938a17b48ae4/625B9431CE99F0693E2F94E3CFCAFAC9.hen20a83.pdf


To provide transparent and reproducible results, this analysis identifies financial measures related to nonprofit performing arts organizations defined by those organizations that 1) have filed a 990 or 990EZ form in the past three years, and 2) is coded as a performing arts entity idenfied with a NAICS code starting with 7111. All 990 and 990EZ data is available from the IRS (https://www.irs.gov/statistics/soi-tax-stats-annual-extract-of-tax-exempt-organization-financial-data), and NAICS classifications are available via the IRS Business Master File maintained by the Urban Institute's National Center for Charitable Statistics (https://nccs-data.urban.org/data.php?ds=bmf)


All data used is available in this repository along with the Python scirpt written to clean and analyze the data. 


The primary variables analyzed are:
 - Contributed Revenue (totcntrbs)
 - Earned Revenue/Progam Service Revenue (totprgmrevnue)
 - Gross Receipts/Revenue (grossRevCalc = totrevenue - invstmntinc - netincfndrsng + costgoodsold)
 - Total Expenses (totexpns)
 
Program Service Revenue is defined by the IRS as: 
 - "Program service revenue includes income earned by the organization for providing a government agency with a service, facility, or product that benefited that government agency directly rather than benefiting the public as a whole. Program service revenue also includes tuition received by a school, revenue from admissions to a concert or other performing arts event or to a museum; royalties received as author of an educational publication distributed by a commercial publisher; interest income on loans a credit union makes to its members; payments received by a section 501(c)(9)organization from participants or employers of participants for health and welfare benefits coverage; insurance premiums received by a fraternal beneficiary society; and registration fees received in connection with a meeting or convention."

Note that Gross Revenue/Receipts are the metric used within the current Heroes Act rather than just Total Revenue. Additionally, the Act requires removing investment and fundraising income from Gross Revenue/Receipt calculations.


## Analysis ##

Of all active nonprofit entities in the United States that have filed a 990 or 990ez in the past three years, 14,172 are classified as performing arts with aggregate expenses of over $11.6 billion. Average Earned Revenue accounts for 48% of Gross Revenue. 

The current Heroes Act Bill plans to provide maximum support to any one organization totaling no more than 45% of **Earned Revenue** with a cap of $12 million per organization. If all organizations analyzed here received the maximum allowed, that would cost $2.4 billion to fund (average:$167k, median:$19k).
 
The original Heroes Act Bill planned to provide maximum support to any one organization totaling no more than 45% of **Gross Revenue** with a cap of $12 million per organization. If all organizations analyzed here received the maximum allowed under this plan, that would cost $4.5 billion to fund (average:$315k, median:$51k).

If **all** Earned Revenue were to be eligible for support, that would cost $6 billion, and with a $12 million cap per organization the cost would be $4.5 billion (average:$317k, median:$41k).


### Priority Application Periods ###

The current Heroes Act Bill would create a 14-day priority period fo applicants recoginizing revenue declines of 90% or more and a subsequent 14-day priorty period for applicants recognizing revenue declines of 70% or more. 50% of organizations would qualify for the first period, and an additional 8% would qualify for the second period.


## Final Notes ##

This analysis is very inclusive of all nonprofit performing arts organizations (NAICS 7111). In addition to the 990 and 990EZ filers, 990N (postcard) filers may also be eligible for funding through this progrram even though this analysis does not include their financial figures as they are not required to report them to the IRS due to their small size. 19,054 990N filers are classified by NAICS 7111 codes.

If you have any questions, please contact me at dfonner@smu.edu.


## About SMU DataArts ##

SMU DataArts, the National Center for Arts Research, is a joint project of the Meadows School of the Arts and Cox School of Business at Southern Methodist University. SMU DataArts compiles and analyzes data on arts organizations and their communities nationwide and develops reports on important issues in arts management and patronage. Its findings are available free of charge to arts leaders, funders, policymakers, researchers and the general public. The vision of SMU DataArts is to build a national cultureof data-driven decision-making for those who want to see the arts and culture sector thrive. Its mission is to empower arts and cultural leaders with high-quality data and evidence-based resources and insights that help them to overcome challenges and increase impact. Publications include white papers on culturally specific arts organizations, the egalitarian nature of the arts in America, gender equity in art museum directorships, protecting organizations through downturns, and more. SMU DataArts also publishes reports on the health of the U.S. arts and cultural sector and the annual Arts Vibrancy Index, which highlights the 40 most arts-vibrant communities around the country. For more information, visit http://www.culturaldata.org/.
