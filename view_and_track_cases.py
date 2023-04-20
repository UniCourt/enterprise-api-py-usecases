import unicourt
from unicourt import *
import sys

from unicourt.model.case_update_request import CaseUpdateRequest
from unicourt.model.case_track_request import CaseTrackRequest
from unicourt.model.case_track_schedule import CaseTrackSchedule

# Get CLIENT_ID and CLIENT_SECRET from your account
unicourt.CLIENT_ID = sys.argv[1]
unicourt.CLIENT_SECRET = sys.argv[2]

# API login
Authentication.generate_new_token()


# Get courtId for Los Angeles County Superior Court
court_response, status = CourtStandards.get_courts(
    q='name:(Los Angeles County Superior Court)')
for court_data in court_response.court_array:
    la_court_id = court_data.court_id


# UniCourt Court Data API to View and Track a Case
case, status = CaseSearch.search_cases(q='caseNumber:"14K07777"',
                                       sort='filedDate', order='desc', page_number=1)
case_id = None
for case_data in case.case_search_result_array:
    case_id = case_data.case_id


# View case details
response, status = CaseDocket.get_case(case_id=case_id)
print(response)


# Tracking a Case
track_response, status = CaseTracking.track_case(
    case_track_request=CaseTrackRequest(
        case_track_params=CaseUpdateRequest(
            case_id=case_id
        ),
        schedule=CaseTrackSchedule(
            type="weekly",
            days=[1, 3, 5],
        ),
    )
)

print(track_response)
# Invalidate the generated access token
Authentication.invalidate_token()
