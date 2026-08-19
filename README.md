# Singapore Housing Signals

An observation project for understanding Singapore's housing market through policy signals rather than price prediction.

The central question is:

> **What is the Singapore Government responding to, and where is the next housing-market bottleneck likely to move?**

## What This Project Observes

Singapore Housing Signals tracks the housing market through several connected signals:

- HDB resale price momentum
- HDB resale transaction volume
- BTO housing supply
- Private residential property price momentum
- Private residential transaction volume
- Government Land Sales (GLS)
- MAS monetary policy
- Major housing policy interventions
- En bloc redevelopment and private-land recycling

The objective is not to predict the next property price movement.

Instead, the project observes how changes in price momentum, transaction activity, housing supply and government intervention interact over time.

## Current Observation Framework

The project currently uses the following framework:

**Market Signals**

Price Momentum × Persistence × Market Segment  
+ Transaction Volume

↓

**Government Response**

Demand-side measures:
ABSD / SSD / TDSR / LTV / Wait-out rules

Supply-side measures:
BTO / GLS / En Bloc land recycling

↓

**Next Bottleneck**

The project then observes where constraints move after government intervention.

Examples include:

Owner consent → Reserve price → Developer economics → Future supply → Competition for developer capital

## Current Findings

### Finding 01 — Policy Reaction Function

Singapore housing policy appears to respond not simply to absolute price levels, but to:

- price momentum,
- persistence of that momentum,
- and the market segment in which acceleration occurs.

Transaction volume appears to operate mainly as a supporting heat or confirmation signal rather than as a standalone policy trigger.

### Finding 02 — Price × Transaction Volume

Major tightening episodes often combine sustained price growth with elevated transaction activity.

However, subsequent interventions show that high transaction volume is not always required for further tightening.

This suggests that transaction volume should be interpreted together with price momentum and market segment.

### Finding 03 — Supply as a Policy Lever

Housing supply is not merely an outcome of market conditions.

It is also an active policy lever.

The current framework therefore distinguishes between:

- **Public supply:** BTO
- **New private land supply:** GLS
- **Existing private land recycling:** En bloc redevelopment

This makes it possible to observe not only demand-side cooling measures, but also how the Government changes the supply structure of the housing market.

## En Bloc Feasibility Cases

Three estates are currently used as case studies:

| Case | Estate | Primary Question |
| --- | --- | --- |
| 01 | Pine Grove | Developer economics, ABSD and mega-site redevelopment |
| 02 | Laguna Park | Owner consent, threshold reform and future supply |
| 03 | Ivory Heights | En bloc land versus Government GLS supply |

These cases are not intended to form an en bloc property database.

They are used to observe whether removing an institutional constraint actually results in land recycling, or simply moves the bottleneck elsewhere.

## Data

The project currently contains the following datasets:

| Dataset | Description |
| --- | --- |
| `HDB_Resale_Price.csv` | HDB resale price index and price momentum |
| `HDB_Transaction_Volume.csv` | HDB resale transaction activity |
| `BTO_Supply.csv` | New HDB BTO supply |
| `Private_Property_Price.csv` | Private residential property price index and price momentum |
| `Private Transaction Volume.csv` | Private residential transaction activity |
| `MAS_Policy.csv` | Monetary policy stance of the Monetary Authority of Singapore |
| `Policy_Timeline.csv` | Major housing policy and cooling-measure events |

Detailed field definitions are available in `data/DataDictionary.md`.

## Approach

Singapore Housing Signals treats the housing market as a policy-responsive system rather than a single price series.

The objective is not:

> **Where will property prices go next?**

The objective is:

> **What problem does the Government appear to be responding to now, what policy lever is being used, and where might the bottleneck move next?**

## Status

**Version 1.1**

Data coverage extends from 2001 onward where the underlying series is available.

The initial data-building stage is complete.

The project is now in the policy-observation stage, with the first three findings and three en bloc feasibility cases established.

The framework will be updated primarily on a quarterly basis as new HDB and private residential market data become available.
