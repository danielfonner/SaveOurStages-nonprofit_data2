# SaveOurStages-nonprofit_data2

![SMU DataArts Logo](https://da.culturaldata.org/images/logos/DataArts.RB.webonly.rgb.png)

This repository contains data and analysis to support the nonprofit performing arts sector in advocating for funding through the proposed Save Our Stages program within the Heroes Small Business Lifeline Act.

### NOTE THAT SAVE OUR STAGES WAS RENAMED TO THE SHUTTERED VENUE OPERATORS GRANT (SVOG) PROGRAM ###

You can find more detailed information about the program here: https://www.sba.gov/funding-programs/loans/coronavirus-relief-options/shuttered-venue-operators-grant

From the SBA: "Eligible (shuttered venues) applicants may qualify for SVO Grants equal to 45% of their gross earned revenue, with the maximum amount available for a single grant award of $10 million." In addition to performing arts venues, "Relevant museum operators, zoos and aquariums who meet specific criteria" may also be elegible. An analysis of nonprofit museums can be found below after the performing arts information.




### Created by Daniel F Fonner, Associate Director for Research, SMU DataArts, Southern Methodist University ###
In collaboration with Theatre Communications Group and the League of American Orchestras


This analysis explores the level of earned revenue, gross revenue, and expenses of nonprofit performing arts organizations in the United States. The data and calculations should provide information to inform lawmakers currently negotiating the Save Our Stages component of the Heroes Small Business Lifeline Act, which aims to provide funding to performing arts venues that have had to close due to COVID-19, and thus cutting off some revenue streams. You can read the current Senate Bill here starting on page 161: https://www.sbc.senate.gov/public/_cache/files/6/6/660e49ed-3ced-482f-9de7-938a17b48ae4/625B9431CE99F0693E2F94E3CFCAFAC9.hen20a83.pdf


To provide transparent and reproducible results, this analysis identifies financial measures related to nonprofit performing arts organizations defined by those organizations that 1) have filed a 990 or 990EZ form in the past three years, and 2) is coded as a performing arts entity idenfied by one of the following criteria:
 - A NAICS code beginning with 7111 (https://www.naics.com/naics-code-description/?code=7111)
 - A NAICS code beginning with 7113 (https://www.naics.com/naics-code-description/?code=7113) AND an NTEE code beginning with the letter 'A' (https://nccs.urban.org/publication/irs-activity-codes)


All 990 and 990EZ data is available from the IRS (https://www.irs.gov/statistics/soi-tax-stats-annual-extract-of-tax-exempt-organization-financial-data), and NAICS classifications are available via the IRS Business Master File maintained by the Urban Institute's National Center for Charitable Statistics (https://nccs-data.urban.org/data.php?ds=bmf). This analysis combines all 990 and 990EZ data processed in 2017, 2018, and 2019 keeping the most recent 990 data for each organization based on EIN. This ensures that all current/active nonprofit performing arts organizations are accounted for since organizations have a 3 year filing window before their tax exempt status is revoked.


This repository contains cleaned 990/990EZ/990N data along with the Python scirpts written to clean and analyze the data. 


The primary variables analyzed are:
 - Earned Revenue/Progam Service Revenue (earned_program_service_rev)
 - Gross Receipts/Revenue (gross_rev, which is Total Revenue plus expense values removed from gross figures in "other revenue" on 990s and 990EZs. This value aligns with Box G on the first page of 990s)
 - Total Expenses (total_exp)
 
Program Service Revenue is defined by the IRS as: 
 - "Program service revenue includes income earned by the organization for providing a government agency with a service, facility, or product that benefited that government agency directly rather than benefiting the public as a whole. Program service revenue also includes tuition received by a school, revenue from admissions to a concert or other performing arts event or to a museum; royalties received as author of an educational publication distributed by a commercial publisher; interest income on loans a credit union makes to its members; payments received by a section 501(c)(9)organization from participants or employers of participants for health and welfare benefits coverage; insurance premiums received by a fraternal beneficiary society; and registration fees received in connection with a meeting or convention." Additionally, "Rental income received from an exempt function is another example of program-related investment income", which is to be included in Program Service Revenue on a 990.



## Analysis ##

Of all active nonprofit entities in the United States that have filed a 990 or 990ez in the past three years, 14,597 are classified as performing arts with aggregate expenses of over $11.6 billion. Average Earned Revenue accounts for 39% of Gross Revenue (47% of Total Revenue). 

The current Heroes Act Bill plans to provide maximum support to any one organization totaling no more than 45% of **Earned Revenue** with a cap of $12 million per organization. If all organizations analyzed here received the maximum allowed, that would cost $2.4 billion to fund (oranizations would recieve on average: $162k, median:$17k).
 
The original Heroes Act Bill planned to provide maximum support to any one organization totaling no more than 45% of **Gross Revenue** with a cap of $12 million per organization. If all organizations analyzed here received the maximum allowed under this plan, that would cost $5.0 billion to fund (oranizations would recieve on average: $342k, median:$53k).

Beyond the two stated plans, an additional proposal would provide support to organizations covering 100% of **Earned Revenue** totaling no more than 45% of **Gross Revenue** with a cap of $12 million per organization. If all organizations analyzed here received the maximum allowed under this plan, that would cost $3.7 billion to fund (oranizations would recieve on average: $254k, median:$30k).

A final proposal would provide maximum support to any one organization totaling no more than 45% of **Earned Revenue** with a cap of $10 million per organization. If all organizations analyzed here received the maximum allowed, that would cost $2.3 billion to fund (organizations would receive on average: $158k, median:$17k).

## Museum Analysis - added February 5, 2021 ##

Defining museums, zoos, aquariums, and historical societies utiized NAICS codes 712110 "museums", 712120 "historical sites", and 712130 "zoos and botanical gardens; NAICS definitions can be found here: https://www.naics.com/naics-code-description/?code=7121.  Corresponding NTEE codes include A50, A51, A52, A54, A56, A57, A80, A82, and D50. You can find the NTEE code definitions here: https://nccs.urban.org/publication/irs-activity-codes.  For this group, there were 11,865 990/990EZ filers (22,418 990N filers without financial information due to their small size).

When analyzing the museum, zoo, and historical organizations under the Shuttered Venue Operators Grant Program, if all organizations analyzed received maximum support of the SVOG program that could not exceed 45% of Earned revenue with a $10M cap per organization, that would cost $1.65B to fund (organizations receiving on average $140k, median $1.2k)

Note that the average/median analysis of performing arts organizations ($158k/$17k) compared to museums ($140k/$1.2k) showed that the business models of the sectors are very different with performing arts organizations having earned revenue account for 47% of total revenue as compared to 26% for museums. This shows potential difficulties for different types of organizations seeking funds from the SVOG program when earned revenue is the criteria used by the SBA.

## Final Notes ##

This analysis is **very inclusive** of all nonprofit performing arts organizations (NAICS 7111 and (NAICS 7113 & NTEE'A')). In addition to the 990 and 990EZ filers, 990N (postcard) filers may also be eligible for funding through this program even though this analysis does not include their financial figures as they are not required to report them to the IRS due to their small size. Using the above NAICS/NTEE criteria, 19,054 990N filers are classified as performing arts organizations.

It is possible that some of the organizations included here would not qualify for funding under the Save Our Stages plan as they do not operate a specific venue. However, we are not able to assess venue ownership/operation via publicly available data. As such, we have erred on the side of inclusivity.

Lastly, if one wanted to explore information related to the count of for-profit entities as well as non-profit entities in the US classified by the NAICS codes listed above, one could use data from the Census' Business Pattern Data program. You can download a table showing the number of establishments in the US by filtering on the column "2017 NAICS Code": https://www2.census.gov/programs-surveys/nonemployer-statistics/tables/2018/combine18us.xlsx. When viewing those counts of establishments, it is important to keep the Census definitions (2nd tab in the spreadsheet) in mind if one is tryinig to compare to the IRS 990 data; for example the 990N organizations noted above most likely would not be counted in the Business Pattern Data due to their small size and potential lack of a physical location.

If you have any questions, please contact me at dfonner@smu.edu.


## About SMU DataArts ##

SMU DataArts, the National Center for Arts Research, is a joint project of the Meadows School of the Arts and Cox School of Business at Southern Methodist University. SMU DataArts compiles and analyzes data on arts organizations and their communities nationwide and develops reports on important issues in arts management and patronage. Its findings are available free of charge to arts leaders, funders, policymakers, researchers and the general public. The vision of SMU DataArts is to build a national cultureof data-driven decision-making for those who want to see the arts and culture sector thrive. Its mission is to empower arts and cultural leaders with high-quality data and evidence-based resources and insights that help them to overcome challenges and increase impact. Publications include white papers on culturally specific arts organizations, the egalitarian nature of the arts in America, gender equity in art museum directorships, protecting organizations through downturns, and more. SMU DataArts also publishes reports on the health of the U.S. arts and cultural sector and the annual Arts Vibrancy Index, which highlights the 40 most arts-vibrant communities around the country. For more information, visit http://www.culturaldata.org/.
