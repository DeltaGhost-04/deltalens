# DeltaLens Data Sources

## Research Area

Mississippi Delta, Mississippi, USA.

## Initial Research Targets

| Dataset                          | Potential use                                              | Verification needed                              |
| -------------------------------- | ---------------------------------------------------------- | ------------------------------------------------ |
| MARIS geographic datasets        | Boundaries and geographic context                          | Dataset license, coverage, and update date       |
| Mississippi parcel mapping       | Parcel boundaries and property attributes                  | County coverage, permitted use, and currency     |
| Tax-forfeited property inventory | Identify properties in the state's tax-forfeited inventory | Current status and eligibility for redevelopment |

## Data Quality Rules

* Record the source and retrieval date for every dataset.
* Preserve the original source identifiers where appropriate.
* Do not treat tax delinquency or tax forfeiture as proof of vacancy.
* Do not treat a parcel's appearance in imagery as conclusive evidence of abandonment.
* Clearly identify synthetic or demonstration data.

## Active Geographic Services

### Mississippi Western Parcel Boundaries

- **Provider:** Mississippi GIS service; parcel data credited to MDEQ, MGI, and county tax assessor offices, among other contributors.
- **Service:** MS_MDEQPARCELS_West_2024
- **Service URL:** https://gis.mississippi.edu/server/rest/services/Cadastral/MS_MDEQPARCELS_West_2024/MapServer
- **Layer ID:** 0
- **Use in DeltaLens:** Optional geographic parcel-boundary overlay.
- **Dataset label:** 2024, as identified by the service name.
- **Accessed:** 2026-10-10
- **Limitations:** Parcel coverage, attribute completeness, and update dates may vary. Parcel boundaries do not establish vacancy, abandonment, blight, ownership eligibility, or redevelopment potential.
- **Verification status:** Public service identified; local coverage and rendering still need to be tested.