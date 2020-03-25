import os

DATA_PATH = os.path.abspath("../data")
DSHS_URL = "https://txdshs.maps.arcgis.com/apps/opsdashboard/index.html#/ed483ecd702b4298ab01e8b9cafc8b83"
DSHS_XHR_URL = "https://services5.arcgis.com/ACaLB9ifngzawspq/arcgis/rest/services/COVID19County_ViewLayer/FeatureServer/0/query?f=json&where=Count_%3C%3E0&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=Count_%20desc&resultOffset=0&resultRecordCount=254&cacheHint=true"
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


#### OTHER STATE INFO ######

NY_URL = "https://coronavirus.health.ny.gov/county-county-breakdown-positive-cases"
