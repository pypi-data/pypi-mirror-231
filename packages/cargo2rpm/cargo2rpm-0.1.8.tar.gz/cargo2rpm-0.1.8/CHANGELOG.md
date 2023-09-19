## Release 0.1.8

This release adds another subcommand for the cargo2rpm script, which can be
used by RPM generators for bundled / vendored crate dependencies.

## Release 0.1.7

This is a fixup release for version 0.1.6. It accidentally did not include
test sources.

## Release 0.1.6

This release adds implementations of all comparison operators for the `Version`
class from the `semver` submodule, and introduces a new `PreRelease` class in
the same module for parsing and comparing version substrings that denote a
pre-release version.

This functionality was previously present in the SemVer implementation in
`rust2rpm` but was dropped because `rust2rpm` did not use it. However, other
applications relied on this functionality, so it was restored in `cargo2rpm`
to make porting from old `rust2rpm` versions to `cargo2rpm` easier.

## Release 0.1.5

This release fixes some subtle bugs in the calculation of enabled features
when resolving `BuildRequires`.

## Release 0.1.4

This release fixes a typo in the CLI argument parser which prevented the
`-n` flag ("`--no-default-features`") of some RPM macros from working.

## Release 0.1.3

This release fixes an edge case when determining whether default features
are enabled for a member of a cargo workspace.

## Release 0.1.2

This release fixes an edge cases in the "is this crate a library" heuristics:
Some crates explicitly set their crate type to "rlib", which is equivalent
to "lib", but which was not recognised as such prior to v0.1.2.

Additionally, two methods have been added: `Metadata.is_cdylib` and
`Package.cdylib`, which can be used to detect whether a crate (or any crate in a
cargo workspace) provides a `cdylib` binary target.

## Release 0.1.1

This release adds two methods on `Metadata` for processing crate description
into usable "Summary" and "description" texts for use in RPM specs based on
a few simple heuristics.

It is now also possible to override which "cargo" binary is used for generating
crate metadata by defining the `CARGO` environment variable. The now redundant
`cargo` argument was dropped from the `Metadata.from_cargo` method.

## Release 0.1.0

Initial release.
