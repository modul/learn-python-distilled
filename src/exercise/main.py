import requests
import json

from helper import *

def getCountryData(countryCode):
  res = requests.get(f'https://restcountries.eu/rest/v2/alpha/{countryCode}')
  res.raise_for_status()
  return res.json()

def getCovidGlobalSummary():
  res = requests.get('https://api.covid19api.com/summary')
  res.raise_for_status()
  return res.json()

def printGlobalSummary(sortBy=['TotalConfirmed', 'NewConfirmed']):
  summary = getCovidGlobalSummary()
  globalCases, countries = summary['Global'], summary['Countries']

  for sortKey in reversed(sortBy):
    countries.sort(key=lambda x: x[sortKey], reverse=True)

  print(f"Summary: global cases: {globalCases['TotalConfirmed']} (+{globalCases['NewConfirmed']}) confirmed", end=', ')
  print(f"{globalCases['TotalDeaths']} (+{globalCases['NewDeaths']}) deaths")
  print()

  printTable(['Country', 'NewConfirmed', 'TotalConfirmed', 'NewDeaths', 'TotalDeaths'], countries)


if __name__ == '__main__':
  printGlobalSummary()
