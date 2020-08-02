This repository demonstrates that GitHub Packages does not work with NuGet packages which have build metadata in their version. ([Discussion here](https://github.community/t/bug-nuget-support-build-metadata-properly/117606/3))

It does so using GitHub Actions. Manually initiate the "Test GitHub Packages" workflow and it will automatically pack and publish two packages: One with build metadata and one without.

Then for each of the following, we spawn a job to create a new console project and add the specified package:

Package | Version | Notes
--------|---------|------
`PackageWithoutBuildMetadata` | 0.0.x | Typical package restore
`PackageWithoutBuildMetadata` | 0.0.x+BuildMetadata | Demonstrates that build metadata is ignored. (The package will be added successfully.)
`PackageWithBuildMetadata` | 0.0.x | Typical package restore for package with build metadata, does not work on GitHub Packages
`PackageWithBuildMetadata`  | 0.0.x+BuildMetadata | Demonstrates that GitHub Packages doesn't even work with explicitly specified build metadata.

All jobs should succeed. However as of 2020-08-02 the `PackageWithBuildMetadata` ones will fail with GitHub Packages.

# NuGet.org test

In addition to the GitHub Packages workflow, there is an additional workflow demonstrating the NuGet.org works as expect (using the [NuGet.org ingegration environment](https://int.nugettest.org/).)

To run this workflow, you mustconfigure a repository secret called `NUGETTEST_API_KEY` with your API key. (Although since I've already uploaded these packages you wouldn't be able to anyway.)

Note that since NuGet.org requires automated validation to complete before listing packages, the workflow will need to be re-ran once validation completes in order for the restore jobs to succeed.
