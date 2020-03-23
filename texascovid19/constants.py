import os

DATA_PATH = os.path.abspath("../data")
DSHS_URL = "https://www.dshs.state.tx.us/news/updates.shtm"
TIMESERIES_CSV = f"{DATA_PATH}/timeseries.csv"

#### METRO AREAS

# https://en.wikipedia.org/wiki/Greater_Houston
METRO_GREATER_HOUSTON =  [
  'Harris',
  'Fort Bend',
  'Montgomery',
  'Brazoria',
  'Galveston',
  'Liberty',
  'Waller',
  'Chambers',
  'Austin'
]
POPULATION_GREATER_HOUSTON_2010 = 5_920_416
POPULATION_GREATER_HOUSTON_2018_EST = 6_997_384

# https://en.wikipedia.org/wiki/Dallas–Fort_Worth_metroplex
METRO_DFW = [
  'Collin',
  'Dallas',
  'Denton',
  'Ellis',
  'Hunt',
  'Kaufman',
  'Rockwall',
  'Hood',
  'Johnson',
  'Parker',
  'Somervell',
  'Tarrant',
  'Wise'
]
POPULATION_DFW_2010 = 6_426_214
POPULATION_DFW_2018_EST = 7_690_420

# https://en.wikipedia.org/wiki/Greater_Austin
METRO_GREATER_AUSTIN = [
  'Bastrop',
  'Caldwell',
  'Hays',
  'Travis',
  'Williamson'
]
POPULATION_GREATER_AUSTIN_2010 = 1_716_309
POPULATION_GREATER_AUSTIN_2018_EST = 2_168_316


# https://en.wikipedia.org/wiki/Greater_San_Antonio
METRO_GREATER_SAN_ANTONIO = [
  'Atascosa',
  'Bandera',
  'Bexar',
  'Comal',
  'Guadalupe',
  'Kendall',
  'Medina',
  'Wilson'
]
POPULATION_GREATER_SAN_ANTONIO_2010 = 2_142_508
POPULATION_GREATER_SAN_ANTONIO_2018_EST = 2_518_036

