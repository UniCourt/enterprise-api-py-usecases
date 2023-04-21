import csv
import unicourt
from unicourt import *
import sys


# Get CLIENT_ID and CLIENT_SECRET from your account
unicourt.CLIENT_ID = sys.argv[1]
unicourt.CLIENT_SECRET = sys.argv[2]
Authentication.generate_new_token()

# Locate Cases Involving Law Firm
response, status = CaseSearch.search_cases(
    q='(Attorney:(PossibleNormLawFirm:(normLawFirmId:"NORGHsUK4FHHEdEtkh")))', order='desc', sort='filedDate', page_number=1)
for case_data_dict in response.case_search_result_array:
    print(case_data_dict, "\n")
# Invalidate the generated access token
Authentication.invalidate_token()
