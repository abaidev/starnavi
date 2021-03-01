import os
import clearbit
from pyhunter import PyHunter

my_hunter_api_key = os.environ.get("MY_HUNTER_API_KEY")

hunter = PyHunter(my_hunter_api_key)

# clearbit.key = os.environ.get('CLEARBIT_SECRET_KEY')
# user = clearbit.Enrichment.find(
#   email='some@gmail.com',
#   stream=True
# )