#!/usr/bin/env bash
set -euo pipefail

ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)
SPEC="$ROOT/packaging/rpm/bc250-fancurve.spec"
NAME=$(awk '$1 == "Name:" { print $2; exit }' "$SPEC")
VERSION=$(awk '$1 == "Version:" { print $2; exit }' "$SPEC")
TOPDIR=${RPMTOPDIR:-"$HOME/rpmbuild"}
SOURCES="$TOPDIR/SOURCES"

mkdir -p "$SOURCES"

# Build from the committed tree, matching the source archive expected by the
# spec. Commit changes before running this script if they should be packaged.
git -C "$ROOT" archive \
    --format=tar.gz \
    --prefix="$NAME-$VERSION/" \
    HEAD > "$SOURCES/$NAME-$VERSION.tar.gz"

rpmbuild -ba \
    --define "_topdir $TOPDIR" \
    "$SPEC"
