import unicourt
from unicourt import *
import sys


# Get CLIENT_ID and CLIENT_SECRET from your account
unicourt.CLIENT_ID = sys.argv[1]
unicourt.CLIENT_SECRET = sys.argv[2]
Authentication.generate_new_token()

lawfirm_analytics = LawFirmAnalytics.search_normalized_law_firms(
    q='name:(PATENAUDE & FELIX A PROFESSIONAL CORPORATION)')


print(lawfirm_analytics)
# Invalidate the generated access token
Authentication.invalidate_token()
