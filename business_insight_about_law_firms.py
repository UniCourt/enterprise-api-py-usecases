import csv
import unicourt
from unicourt import *
import sys


# Get CLIENT_ID and CLIENT_SECRET from your account
unicourt.CLIENT_ID = sys.argv[1]
unicourt.CLIENT_SECRET = sys.argv[2]
Authentication.generate_new_token()

# Find normLawFirmId for CLERKIN, SINCLAIR & MAHFOUZ, L.L.P.
normalized_law_firms, status_code = LawFirmAnalytics.search_normalized_law_firms(
    q='name:(CLERKIN, SINCLAIR & MAHFOUZ, L.L.P.)')

norm_law_firm_id = ""

for normalized_law_firm in normalized_law_firms.norm_law_firm_search_result_array:
    if normalized_law_firm.name == "CLERKIN, SINCLAIR & MAHFOUZ, L.L.P.":
        norm_law_firm_id = normalized_law_firm.norm_law_firm_id
        print("norm_law_firm_id >>>  ", norm_law_firm_id)
        break


# Extract the Top Case Type for a Law Firm, result is saved in top_case_type_for_a_law_firm.csv
case_count_analytics_by_case_type, status_code = CaseAnalytics.get_case_count_analytics_by_case_type(
    q=f'normLawFirmId:"{norm_law_firm_id}"', page_number=1)
with open('top_case_type_for_a_law_firm.csv', mode='w') as csvfile:
    csvfile_writer = csv.writer(
        csvfile, delimiter=',')
    csvfile_writer.writerow(
        ['Case Type', 'Case Type Group', 'Area Of Law', 'Case Calss', 'Case Count', 'Case Type Id'])
    for case_object in case_count_analytics_by_case_type.results[:3]:
        csvfile_writer.writerow(
            [case_object.case_type.name,
             case_object.case_type.case_type_group,
             case_object.case_type.area_of_law,
             case_object.case_type.case_class,
             case_object.case_count,
             case_object.case_type.case_type_id
             ]
        )


# Identify a Law Firm's Top Clients for a Case Type,  result is saved in top_party.csv

party_response, status = LawFirmAnalytics.get_norm_parties_associated_with_norm_law_firm(
    norm_law_firm_id='NORG5odEKsHWqrkv3i',
    page_number=1,
    q='caseTypeId:"CTYPFQK3XeZduAfEBf"'
)
with open('top_party.csv', mode='w') as party_csvfile:
    party_writer = csv.writer(
        party_csvfile, delimiter=',')
    party_writer.writerow(
        ['Party', 'NormPartyId'])
    for party_data in party_response.associated_norm_party_array[:4]:
        party_writer.writerow([party_data.name, party_data.norm_party_id])


# Identify Law Firms Representing a Particular Company in a Particular Case Type
# results can be found in law_firm_case_type.csv
case_response, status = CaseAnalytics.get_case_count_analytics_by_norm_law_firm(
    page_number=1,
    q='normPartyId:"NORGxykicNHeNjNh2D" AND caseTypeId:"CTYPFQK3XeZduAfEBf"'
)
with open('law_firm_case_type.csv', mode='w') as law_firm_case_type:
    case_writer = csv.writer(
        law_firm_case_type, delimiter=',')
    case_writer.writerow(
        ['LawFirm', 'LawFirmId', 'Cases'])
    for case_data in case_response.results[:10]:
        case_writer.writerow([case_data.norm_law_firm_name,
                              case_data.norm_law_firm_id, case_data.case_count])


# Get Client-Specific Case Counts by Jurisdiction
case_count_response, status = CaseAnalytics.get_case_count_analytics_by_court(
    q='normLawFirmId:"NORG5odEKsHWqrkv3i" AND normPartyId:"NORGxykicNHeNjNh2D" AND caseTypeId:"CTYPFQK3XeZduAfEBf"',
    page_number=1)
case_count_list = []
print(case_count_response)
for case_data in case_count_response.results:
    case_count_list.append(case_data.case_count)

total_case_count = sum(case_count_list)
total_courts = len(case_count_list)

print(
    f":: CLERKIN, SINCLAIR & MAHFOUZ, L.L.P. has filed {str(total_case_count)} Insurance lawsuits for HARTFORD CASUALTY INSURANCE COMPANY in {str(total_courts)} different courts")


# Compute Market Share


# Invalidate the generated access token
Authentication.invalidate_token()
