import csv
import unicourt
from unicourt import *
import sys


# Get CLIENT_ID and CLIENT_SECRET from your account
unicourt.CLIENT_ID = sys.argv[1]
unicourt.CLIENT_SECRET = sys.argv[2]
Authentication.generate_new_token()

# Find Top Defense Attorneys, results will be saved in top_defense_attorney.csv

case_response, status = CaseAnalytics.get_case_count_analytics_by_norm_attorney(
    q='courtId:"CORTV4vCEaKrhystBz" AND partyRoleGroupId:"PTYG73uQdgJdpA3ebc" AND normJudgeId:"NJUDGmsXhpTkmt7m3d" AND areaOfLawId:"AOFLAQAm5WsAdhXKdH"',
    page_number=1
)
with open('top_defense_attorney.csv', mode='w') as csvfile:
    csv_writer = csv.writer(
        csvfile, delimiter=',')
    csv_writer.writerow(
        ['NormAttorney',	'NormAttorneyId',	'Case Counts'])
    for case_data in case_response.results[:10]:
        csv_writer.writerow([case_data.norm_attorney_name,
                            case_data.norm_attorney_id, case_data.case_count])
# Find Top Opposing Attorneys for a Plaintiff's Attorney
# Top ten attorneys who most frequently appear in opposition to BRADFORD JOHN DEJARDIN can be found in top_opposing_attorney.csv
opp_attr_response, status = CaseAnalytics.get_case_count_analytics_by_opposing_norm_attorney_for_a_norm_attorney(
    q='areaOfLawId:"AOFLAQAm5WsAdhXKdH" AND courtId:"CORTV4vCEaKrhystBz" AND normJudgeId:"NJUDGmsXhpTkmt7m3d"',
    norm_attorney_id="NATYst9Ko4FSNjbJtH",
    page_number=1)
with open('top_opposing_attorney.csv', mode='w') as csv_opp_file:
    opp_csv_writer = csv.writer(
        csv_opp_file, delimiter=',')
    opp_csv_writer.writerow(
        ['NormAttorney',	'NormAttorneyId',	'Case Counts'])
    for oppose_attorney in opp_attr_response.results[:10]:
        opp_csv_writer.writerow([oppose_attorney.norm_attorney_name,
                                 oppose_attorney.norm_attorney_id, oppose_attorney.case_count])


# Invalidate the generated access token
Authentication.invalidate_token()
