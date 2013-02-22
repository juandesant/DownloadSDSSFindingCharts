`sdssDR9findingChart.py` is a script that allows you to automatically download finding charts from Data Release 9 (DR9) of the Sloan Digital Sky Survey (SDSS).

It has been written without using the [`requests`](http://docs.python-requests.org/ "Requests: HTTP for Humans &mdash; Requests 1.1.0 documentation") module so that it can be run without having the users install additional dependencies.

Usage
=====

You invoke the tool with

    sdssDR9findingChart.py fileWithAstroObjects

where `fileWithAstroObjects` is a text file containing an astronomical source name per line. Non-valid names are ignored.

The result is a finding chart from SDSS DR9 as a JPEG file which is downloaded in the directory from which the `sdssDR9findingChart.py` script is called.

Configuration
=============

Right now, the only configuration capabilities imply editing the script and manually modifying the `sdssParamsDict` dictionary.

For more information on which options are valid, see http://skyserver.sdss3.org/dr9/en/tools/chart/chart.asp

To do
=====

* Add help to the script
* Add configuration options corresponding to the chart using 

Aknowledgements
===============

This tool has been written withing the framework of the [AMIGA project](http://amiga.iaa.es/ "AMIGA : Analysis of the interstellar Medium of Isolated GAlaxies"), and with support from Spanish grants AYA2008-06181 and AYA2011-30491-C02.

Juande Santander Vela has a contract with CSIC (National Council for Scientific Research) in the JAE-Doc modality of the "Junta de Ampliación de Estudios" program, with funding from the European Social Fund.