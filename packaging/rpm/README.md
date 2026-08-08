# RPM packaging

The cooling component is packaged individually as `bc250-fancurve`. Future
BC-250 utilities can have their own RPMs and specs.

## Build

The helper creates a source archive from `HEAD` and runs `rpmbuild`:

```sh
./packaging/rpm/build.sh
```

The resulting RPMs are written below `~/rpmbuild/RPMS/` by default. Set
`RPMTOPDIR` to use another rpmbuild tree:

```sh
RPMTOPDIR="$PWD/.rpmbuild" ./packaging/rpm/build.sh
```

The source archive is intentionally made from the committed tree. Commit the
changes to be packaged before running the helper. The spec currently uses
version `0.1.0`; update its `Version` and changelog for a release.

After installing the RPM, enable and start the controller with:

```sh
sudo systemctl enable --now bc250-fancurve.service
```

The package does not enable services automatically. The configuration is
installed as `%config(noreplace)` at `/etc/bc250-fancurve.conf`, so local
changes are preserved across upgrades.

Before publishing the package, replace the placeholder license metadata in
the spec and add the repository's actual license file.
