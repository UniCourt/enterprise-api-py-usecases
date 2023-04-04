import unicourt
from unicourt import *
import sys

# Get CLIENT_ID and CLIENT_SECRET from your account
unicourt.CLIENT_ID = sys.argv[1]
unicourt.CLIENT_SECRET = sys.argv[2]
Authentication.generate_new_token()

# Retrieve the normLawFirmId value for Kirkland & Ellis
normalized_law_firms, status_code = LawFirmAnalytics.search_normalized_law_firms(
    q="name:(Kirkland & Ellis)")


normalized_law_firm_id = ""
# Lets pic normLawFirmId value NORGHsUK4FHHEdEtkh, which is associated
# with the name "Kirkland & Ellis L.L.P." from the above response

for normalized_law_firm in normalized_law_firms.norm_law_firm_search_result_array:
    if normalized_law_firm.name == "KIRKLAND & ELLIS L.L.P.":
        normalized_law_firm_id = normalized_law_firm.norm_law_firm_id
        print(normalized_law_firm_id)
        break

# Pass normalized_law_firm_id value to CaseAnalytics.get_case_count_analytics_by_case_type
case_count_analytics_by_case_types, status_code = CaseAnalytics.get_case_count_analytics_by_case_type(
    q='normLawFirmId:"NORGHsUK4FHHEdEtkh"', page_number=1)

# From the above response lets print top 20 case count and case type for Kirkland and Ellis
for case_object in case_count_analytics_by_case_types.results[:10]:
    print(
        f"CaseType: {case_object.case_type.area_of_law}", " - ", f"CaseCount:  {case_object.case_count}")


# Invalidate the generated access token
Authentication.invalidate_token()
