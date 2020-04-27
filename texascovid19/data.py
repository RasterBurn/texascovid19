from .constants import *
import pandas as pd

def get_timeseries(agg_metro=False, start_date=None, metric='cases'):
  if metric == 'cases':
    csvfile = TIMESERIES_CSV
  elif metric == 'deaths':
    csvfile = DEATHS_TIMESERIES_CSV
  df = pd.read_csv(csvfile, index_col=0)
  if agg_metro:
    df = df.groupby(by=_to_metro).sum()
  if start_date:
    df = df[pd.date_range(start=start_date,
                          end=df.columns[-1])
              .strftime('%Y-%m-%d')
              .tolist()]
  return df


def get_county_timeseries(county, kind='bycity', start_date=None):
  df = pd.read_csv(f"{DATA_PATH}/{county}/{kind}/timeseries.csv", index_col=0)
  if start_date:
    df = df[pd.date_range(start=start_date,
                          end=df.columns[-1])
              .strftime('%Y-%m-%d')
              .tolist()]
  return df


def _to_metro(county):
  if county in METRO_GREATER_AUSTIN:
    return 'Greater Austin'
  if county in METRO_DFW:
    return 'DFW'
  if county in METRO_GREATER_HOUSTON:
    return 'Greater Houston'
  if county in METRO_GREATER_SAN_ANTONIO:
    return 'Greater San Antonio'
  return 'Other'
