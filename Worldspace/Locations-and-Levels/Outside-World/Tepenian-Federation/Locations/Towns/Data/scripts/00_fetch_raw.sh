#!/usr/bin/env bash
# Download the raw inputs used by the inventory pipeline into $RAW (default: ./raw). Access date of the original run: 2026-10-03/04.
RAW="${RAW:-./raw}"; mkdir -p "$RAW"; cd "$RAW"
UA="Mozilla/5.0 (research script; contact kuros.kalacs@terranlights.com)"
# 1. COMNAP Antarctic Facilities Information page (links to the two files below) and the files themselves
curl -sL -A "$UA" https://www.comnap.aq/antarctic-facilities-information -o comnap_afi.html
curl -sL -A "$UA" https://www.comnap.aq/s/Facilities_Nov2024.csv -o comnap_facilities.csv            # 114 rows, ISO-8859-1
curl -sL -A "$UA" https://www.comnap.aq/s/COMNAP_Antarctic_Station_Catalogue.pdf -o comnap_catalogue.pdf  # Aug 2017 catalog, 86 pp
# 2. Wikipedia wikitext via the MediaWiki API (pages parsed by 04_wikipedia_pull_and_parse.py, which also re-fetches them)
for t in Research_stations_in_Antarctica Antarctic_field_camps Historic_Sites_and_Monuments_in_Antarctica List_of_airports_in_Antarctica; do
  curl -s -A "$UA" "https://en.wikipedia.org/w/api.php?format=json&action=parse&prop=wikitext&redirects=1&page=$t" -o "wp_$t.json"
done
# 3. SCAR Composite Gazetteer: old URL https://data.aad.gov.au/aadc/gaz/scar/ answers 301 -> https://placenames.aq (single-page app);
#    its data API (PostgREST) is https://placenames.aq/api  (feature_types, place_names_consolidated, ...)
curl -sL -A "$UA" https://placenames.aq/api/ -o pn_api.json
curl -sL -A "$UA" "https://placenames.aq/api/feature_types?select=feature_type_code,feature_type_name,definition&limit=500" -o pn_ft.json
echo "now run: 01 (needs comnap_catalogue.pdf), 02, 02b, 03, 03b, 04a, 04, 05, 06, 07, 08 in that order"
