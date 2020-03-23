from .constants import *
import pandas as pd

def get_timeseries(agg_metro=False):
  df = pd.read_csv(TIMESERIES_CSV, index_col=0)
  if agg_metro:
    df = df.groupby(by=_to_metro).sum()
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
