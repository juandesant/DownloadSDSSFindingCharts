`sdssDR9findingChart.py` is a script that allows you to automatically download finding charts from Data Release 9 (DR9) of the Sloan Digital Sky Survey (SDSS).

It has been written without using the [`requests`](http://docs.python-requests.org/ "Requests: HTTP for Humans &mdash; Requests 1.1.0 documentation") module so that it can be run without having the users install additional dependencies.

Usage
=====

You invoke the tool with

    sdssDR9findingChart.py fileWithAstroObjects

where `fileWithAstroObjects` is a text file containing an astronomical source name per line. Non-valid names are ignored.

The result is a finding chart from SDSS DR9 as a JPEG file which is downloaded in the directory from which the `sdssDR9findingChart.py` script is called.

Installation
============

1. Download `sdssDR9findingChart.py`
2. `chmod +x sdssDR9findingChart.py`, to make it executable
3. Move it to a place in your PATH

Optionally, you can download the `object.txt` file (for instance, to `~/Downloads`), and test the script with

    sdssDR9findingChart.py ~/Downloads/objects.txt

The expected output will look like:

	Processing Sesame query for M31
	Trying to query SDSS for coords 010.6847929 +41.2690650
	Trying to write M31.jpg
	Processing Sesame query for HCG7d
	Trying to query SDSS for coords 009.8283025 +00.8919208
	Trying to write HCG7d.jpg
	Processing Sesame query for m82
	Trying to query SDSS for coords 148.9696875 +69.6793833
	Trying to write m82.jpg
	Processing Sesame query for HCG89a
	Trying to query SDSS for coords 320.0042917 -03.9221389
	Trying to write HCG89a.jpg
	Processing Sesame query for HCG1
	Trying to query SDSS for coords 006.5008343 +25.7181332
	Trying to write HCG1.jpg
	Processing Sesame query for HCG2
	Trying to query SDSS for coords 007.8751675 +08.4312495
	Trying to write HCG2.jpg
	Processing Sesame query for HCG92c
	Trying to query SDSS for coords 339.0147724 +33.9757204
	Trying to write HCG92c.jpg
	Processing Sesame query for tontoElQueLoLea
	Failed during coordinates search for tontoElQueLoLea
	list index out of range
	Processing Sesame query for CIG 96
	Trying to query SDSS for coords 033.8651667 +06.0026111
	Trying to write CIG 96.jpg
	Processing Sesame query for CIG 3
	Trying to query SDSS for coords 000.8410417 +30.7818889
	Trying to write CIG 3.jpg
	Processing Sesame query for ngc4321
	Trying to query SDSS for coords 185.7284629 +15.8218178
	Trying to write ngc4321.jpg

and the directory will contain the following files:

	$ ls -ln *.jpg
	-rw-r--r--  1 501  20  103406 21 feb 22:40 CIG 3.jpg
	-rw-r--r--  1 501  20  122245 21 feb 22:40 CIG 96.jpg
	-rw-r--r--  1 501  20  102133 21 feb 22:39 HCG1.jpg
	-rw-r--r--  1 501  20  101813 21 feb 22:40 HCG2.jpg
	-rw-r--r--  1 501  20  118322 21 feb 22:39 HCG7d.jpg
	-rw-r--r--  1 501  20  113634 21 feb 22:39 HCG89a.jpg
	-rw-r--r--  1 501  20  120794 21 feb 22:40 HCG92c.jpg
	-rw-r--r--  1 501  20   22884 21 feb 22:39 M31.jpg
	-rw-r--r--  1 501  20  106942 21 feb 22:39 m82.jpg
	-rw-r--r--  1 501  20  109373 21 feb 22:40 ngc4321.jpg

Configuration
=============

Right now, the only configuration capabilities imply editing the script and manually modifying the `sdssParamsDict` dictionary.

For more information on which options are valid, see http://skyserver.sdss3.org/dr9/en/tools/chart/chart.asp

To do
=====

* Add help to the script
* Add configuration options corresponding to the chart using 
* Create `setup.py` script so that it can be installed in a user prefix

Aknowledgements
===============

This tool has been written withing the framework of the [AMIGA project](http://amiga.iaa.es/ "AMIGA : Analysis of the interstellar Medium of Isolated GAlaxies"), and with support from Spanish grants AYA2008-06181 and AYA2011-30491-C02.

Juande Santander Vela has a contract with CSIC (National Council for Scientific Research) in the JAE-Doc modality of the "Junta de Ampliación de Estudios" program, with funding from the European Social Fund.