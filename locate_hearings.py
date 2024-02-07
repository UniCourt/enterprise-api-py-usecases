import csv
import unicourt
from unicourt import *
import sys


# Get CLIENT_ID and CLIENT_SECRET from your account
unicourt.CLIENT_ID = sys.argv[1]
unicourt.CLIENT_SECRET = sys.argv[2]
Authentication.generate_new_token()

# Locate Hearings
response, status = CaseSearch.search_cases(
    q='(CourtLocation:(name:(Stanley Mosk Courthouse))) AND filedDate:[2022-11-06T00:00:00 TO 2022-12-06T00:00:00] AND (Hearing:(hearingDate:[now TO now+30d]))', order='desc', sort='filedDate', page_number=1)
for case_data_dict in response.case_search_result_array:
    print(case_data_dict, "\n")


# Get Hearing Details
response, status = CaseDocket.get_case_hearings(
    case_id='CASEarf7613462fa75', page_number=1)

print(response)

# Get attorney in a case
response, status = CaseDocket.get_case_attorneys(
    case_id='CASEarf7613462fa75', page_number=1)

print(response)

# Find Normalized Attorneys
response, status = AttorneyAnalytics.get_norm_attorney_by_id(
    norm_attorney_id='NATYpPnmW8AyT8QvjT')

print(response)

# Invalidate the generated access token
Authentication.invalidate_token()
