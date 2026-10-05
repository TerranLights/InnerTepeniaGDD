#!/usr/bin/env bash
# Downloads the Natural Earth layers the Tepenia maps use into data/ne_raw/ (not kept in the repo; ~25 MB), then
# prepare_base_data.py clips them to Antarctica into data/base/ (small GeoJSON, which IS kept).
set -u
HERE="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p "$HERE/data/ne_raw"; cd "$HERE/data/ne_raw"
for f in physical/ne_10m_land physical/ne_10m_antarctic_ice_shelves_polys physical/ne_10m_antarctic_ice_shelves_lines \
         physical/ne_10m_coastline physical/ne_10m_geography_regions_polys physical/ne_10m_geography_marine_polys; do
  curl -sfL -o "$(basename $f).zip" "https://naciscdn.org/naturalearth/10m/$f.zip" && unzip -oq "$(basename $f).zip" && echo "ok $f" || echo "FAILED $f"
done
