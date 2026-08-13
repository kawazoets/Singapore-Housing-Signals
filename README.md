# Singapore Housing Signals

An observation project for understanding Singapore's housing market through policy signals rather than price prediction.


## What This Project Observes

Singapore Housing Signals tracks the housing market through several connected signals:

- HDB resale price movements
- HDB resale transaction volume
- BTO housing supply
- Private residential property price movements
- Private residential transaction volume
- MAS monetary policy
- Major housing policy interventions

The objective is not to predict the next property price movement.

Instead, the project observes how prices, transaction activity, housing supply, monetary policy and government interventions interact over time.

## Data

The project currently contains the following datasets:

| Dataset | Description |
|---|---|
| `HDB_Resale_Price.csv` | HDB resale price index and price momentum |
| `HDB_Transaction_Volume.csv` | HDB resale transaction activity |
| `BTO_Supply.csv` | New HDB BTO supply |
| `Private_Property_Price.csv` | Private residential property price index and price momentum |
| `Private Transaction Volume.csv` | Private residential transaction activity |
| `MAS_Policy.csv` | Monetary policy stance of the Monetary Authority of Singapore |
| `Policy_Timeline.csv` | Major housing policy and cooling-measure events |

Detailed field definitions are available in `data/DataDictionary.md`.

## Approach

This project treats Singapore's housing market as a system rather than a single price series.

The basic observation framework is:

**Price → Transactions → Supply → Policy → Response**

By placing these signals on a common timeline, the project aims to identify changes in market conditions and the interaction between government policy and housing-market behaviour.

## Status

Data coverage is being built from 2001 onward where the underlying series is available.

The project is currently in the data-building and observation stage.
