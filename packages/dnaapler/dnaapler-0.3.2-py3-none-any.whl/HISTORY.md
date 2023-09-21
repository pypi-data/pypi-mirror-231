# History

# 0.3.2 (2023-09-20)

* Changes `Orffinder` to `Genefinder`  to support `pyrodigal` v3.
* Updates dependency to `pyrodigal >=v3`.

# 0.3.1 (2023-09-01)

* Minor release to fix an error with dnaapler all #38 thanks @samnooij

# 0.3.0 (2023-08-18)

* `dnaapler all` subcommand added thanks @alexweisberg
* `dnaapler all` implements `--ignore` to ignore some contigs


# 0.2.0 (2023-08-08)

* `dnaapler nearest` subcommand added
* `dnaapler bulk` subcommand added
* dnaA database filtered to keep only bona-file dnaA genes (i.e. GN=dnaA)
* Adds `-e` parameter to vary BLAST evalue if desired
* Adds `-a` autocomplete parameter if user wants to reorient sequences with mystery or nearest methods in case the BLAST based method fails

# 0.1.0 (June 2023)

* Completely overhauled
* First stable released with pypi and conda 
* `dnaapler chromosome` added
* `dnaapler custom` added
* `dnaapler mystery` added 
* `dnaapler phage` added
* `dnaapler plasmid` added


# 0.0.1 (2022-10-12)

* First release (conda only `conda install -c gbouras dnaapler`)
