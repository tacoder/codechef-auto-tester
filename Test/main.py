from core.Parser import getContest,getJsonDataFromUrl
from core import Constants
getContest( 'DEC15', getJsonDataFromUrl( Constants.CODECHEF_API_URL + 'DEC15' ) )