# Data Dictionary

This document defines the datasets used in the Singapore Housing Signals project.

The purpose of this project is to observe Singapore's housing market through policy signals rather than to predict property prices.

---

# HDB_Resale_Price.csv

## Purpose

Track the momentum of Singapore's HDB resale market.

### Columns

| Column | Description |
|---------|-------------|
| Quarter | Reporting quarter (e.g. 2026-Q2) |
| PriceIndex | Official HDB Resale Price Index |
| QoQ | Quarter-on-quarter growth (%) |
| YoY | Year-on-year growth (%) |
| Source | Data source |
| Updated | Last updated date |

---

# Private_Property_Price.csv

## Purpose

Track the momentum of Singapore's private residential market.

### Columns

| Column | Description |
|---------|-------------|
| Quarter | Reporting quarter |
| PriceIndex | Official Private Residential Property Price Index |
| QoQ | Quarter-on-quarter growth (%) |
| YoY | Year-on-year growth (%) |
| Source | Data source |
| Updated | Last updated date |

---

# Transaction_Volume.csv

## Purpose

Track housing market liquidity.

### Columns

| Column | Description |
|---------|-------------|
| Quarter | Reporting quarter |
| HDBResale | Number of HDB resale transactions |
| PrivateNewSale | Number of private new sales |
| PrivateResale | Number of private resale transactions |
| Source | Data source |
| Updated | Last updated date |

---

# BTO_Supply.csv

## Purpose

Track future housing supply.

### Columns

| Column | Description |
|---------|-------------|
| Quarter | Reporting quarter |
| Units | Number of BTO units launched |
| Source | Data source |
| Updated | Last updated date |

---

# MAS_Policy.csv

## Purpose

Track Singapore's monetary policy stance.

### Columns

| Column | Description |
|---------|-------------|
| Date | Policy announcement date |
| PolicyStance | Tightening / Neutral / Easing |
| Remarks | Summary of policy decision |
| Source | Data source |
| Updated | Last updated date |

---

# Policy_Timeline.csv

## Purpose

Record major government policy events affecting the housing market.

### Columns

| Column | Description |
|---------|-------------|
| Date | Policy announcement date |
| Policy | Policy name |
| Category | Cooling Measure / Supply / Financing / Tax / Other |
| Description | Short description |
| Source | Data source |
| Updated | Last updated date |

---

# BTO_Supply.csv

## Purpose

Track the supply of new HDB BTO flats as a housing supply signal.

### Columns

| Column | Description |
|--------|-------------|
| Quarter | Reporting quarter (e.g. 2026-Q2) |
| BTO_Supply | Number of BTO flats launched |
| YoY | Year-on-year change (%) |
| Source | Data source |
| Updated | Last updated date |
