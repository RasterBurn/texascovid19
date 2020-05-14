import os

DATA_PATH = os.path.abspath("../data")
DSHS_URL = "https://txdshs.maps.arcgis.com/apps/opsdashboard/index.html#/ed483ecd702b4298ab01e8b9cafc8b83"
DSHS_XHR_URL = 'https://services5.arcgis.com/ACaLB9ifngzawspq/arcgis/rest/services/DSHS_COVID19_Service/FeatureServer/0/query?f=json&where=Positive%3C%3E0&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=Positive%20desc&resultOffset=0&resultRecordCount=254&resultType=standard&cacheHint=true'
TIMESERIES_CSV = f"{DATA_PATH}/timeseries.csv"
DEATHS_TIMESERIES_CSV = f"{DATA_PATH}/deaths_timeseries.csv"
WILCO_URL = "http://www.wcchd.org/COVID-19/covid-19_case_breakdown.php"
WILCO_AGE_DISTRO_XHR_URL = "https://gis.wilco.org/ags/rest/services/wcchd/Williamson_County_Age_Group/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&outStatistics=%5B%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22Q_0_to_17%22%2C%22outStatisticFieldName%22%3A%22Q_0_to_17%22%7D%2C%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22Q_18_to_40%22%2C%22outStatisticFieldName%22%3A%22Q_18_to_40%22%7D%2C%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22Q_41_to_60%22%2C%22outStatisticFieldName%22%3A%22Q_41_to_60%22%7D%2C%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22Q_61_to_80%22%2C%22outStatisticFieldName%22%3A%22Q_61_to_80%22%7D%2C%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22Over_80%22%2C%22outStatisticFieldName%22%3A%22Over_80%22%7D%5D&resultType=standard"
WILCO_CITY_XHR_URL = "https://gis.wilco.org/ags/rest/services/wcchd/Williamson_County_Cases/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=City_of_Residence%20asc&resultOffset=0&resultRecordCount=4000&resultType=standard"
WILCO_GENDER_XHR_URL = "https://gis.wilco.org/arcgis/rest/services/wcchd/Williamson_County_Gender/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&outStatistics=%5B%7B%22statisticType%22%3A%22avg%22%2C%22onStatisticField%22%3A%22MalePercentage%22%2C%22outStatisticFieldName%22%3A%22MalePercentage%22%7D%2C%7B%22statisticType%22%3A%22avg%22%2C%22onStatisticField%22%3A%22FemalePercentage%22%2C%22outStatisticFieldName%22%3A%22FemalePercentage%22%7D%5D&outSR=102100"
WILCO_STATUS_XHR_URL = "https://gis.wilco.org/arcgis/rest/services/wcchd/Williamson_County_Status_v3/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&outSR=102100&resultOffset=0&resultRecordCount=50"

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
