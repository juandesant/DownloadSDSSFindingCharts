Introduction
============

`sdssDR9findingChart` is a script that allows you to automatically download finding charts from Data Release 9 (DR9) of the Sloan Digital Sky Survey (SDSS).

It has been written without using the [`requests`](http://docs.python-requests.org/ "Requests: HTTP for Humans &mdash; Requests 1.1.0 documentation") module so that it can be run without having the users install additional dependencies.

Usage
=====

You invoke the tool with

    sdssDR9findingChart [-options] fileWithAstroObjects

where `fileWithAstroObjects` is a text file containing an astronomical source name per line. Non-valid names are ignored.

The result is a finding chart from SDSS DR9 as a JPEG file which is downloaded in the directory from which the `sdssDR9findingChart` script is called.

See available options in the [Configuration](Configuration) section.

Installation
============

1. `wget https://github.com/juandesant/DownloadSDSSFindingCharts/archive/master.zip`
2. `unzip master.zip`
3. `cd DownloadSDSSFindingCharts-master/`
4. `python setup.py install`

The source code includes the `object.txt` file, with which you can test the script by typing

    sdssDR9findingChart objects.txt

The expected output will look like:

    Processing Sesame query for M31
    Processing Sesame query for HCG7d
    Processing Sesame query for m82
    Processing Sesame query for HCG89a
    Querying SDSS for coordinates 10.68470833 +41.26875000 (M31)
    Querying SDSS for coordinates 9.82830417 +0.89190833 (HCG7d)
    Querying SDSS for coordinates 320.00427083 -3.92211667 (HCG89a)
    Querying SDSS for coordinates 148.96745833 +69.68022222 (m82)
    Download of M31.jpg completed
    Processing Sesame query for HCG1
    Download of HCG89a.jpg completed
    Processing Sesame query for HCG2
    Querying SDSS for coordinates 6.50000000 +25.71666667 (HCG1)
    Download of m82.jpg completed
    Processing Sesame query for HCG92c
    Querying SDSS for coordinates 7.85000000 +8.44666667 (HCG2)
    Querying SDSS for coordinates 339.01483333 +33.97575000 (HCG92c)
    Download of HCG1.jpg completed
    Processing Sesame query for tontoElQueLoLea
    Error. Coordinates for tontoElQueLoLea not found in Sesame
    list index out of range
    Processing Sesame query for CIG 96
    Error. Coordinates for CIG 96 not found in Sesame
    list index out of range
    Processing Sesame query for CIG 3
    Error. Coordinates for CIG 3 not found in Sesame
    list index out of range
    Processing Sesame query for ngc4321
    Download of HCG2.jpg completed
    Querying SDSS for coordinates 185.72874583 +15.82238056 (ngc4321)
    Download of HCG92c.jpg completed
    Download of ngc4321.jpg completed
    Download of HCG7d.jpg completed

and the directory will contain the following files:

	$ ls -ln \*.jpg
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

The tool allows the same configuration available in the web tool:

* Setting horizontal and vertical sizes (`-x`, `-y`)
* Setting image resolution by pixel scale (`-s`), or zoom-ratio (`-z`)
* Automatically adjusting size based on recession velocity (`-r`)
* Grid and cross-hairs (`-G`)
* Overlay label of image properties (`-L`)
* Colormap inversion (`-I`)
* Marking of photometric and spectroscopic objects (`-P`, `-S`)
* Outlines of objects, bounding boxes, fields, masks, and plates (`-O`, `-B`, `-F`, `-M`, `-Q`)

The tool also sports two modes (selectable with the `--mode` option): `OBJECT_LIST`, where the file provided does not contain coordinates, but names that can be resolved with Sesame; and `SDSS_COORDINATES`, in which the file provides coordinates for the objects (a column named `name`, `source`, `target` or `objid` is looked up to use —if available— for naming the resulting images, but is not used to query Sesame), and optionally a column named `size` can be used to automatically size the image so that it fills the field (`-c/--size-column`).

You can get the whole list of options using the `-h` or `--help` options:

    Usage: sdssDR9findingChart [options] file
    
    Options:
      -h, --help            show this help message and exit
      -x PIXEL, --x-size=PIXEL
                            The finding chart will be PIXEL pixels wide. Default
                            value, 512.
      -y PIXEL, --y-size=PIXEL
                            The finding chart will be PIXEL pixels high. Default
                            value, 512.
      -s SCALE, --scale=SCALE
                            The finding chart pixel resolution will be SCALE arc-
                            seconds per pixel. Defaults to 0.396127 arc-seconds
                            per pixel (native SDSS pixel resolution).
      -z ZOOM-RATIO, --zoom=ZOOM-RATIO
                            The finding chart pixel resolution will be zoomed by
                            ZOOM-RATIO from specified scale ratio (native scale
                            ratio if -s is not used). Values above 1 imply zooming
                            in, values below 1 zooming out. Used alone, is
                            equivalent to the -s option with a SCALE value of
                            0.396127/ZOOM-RATIO.
      -r VELOCITY, --rescale=VELOCITY
                            When this option is set, the size of the image is
                            chosen so that most of the object can fit the image.
                            Works more reliably for objects with recessional
                            velocities >1500 km/s. If you want to know the actual
                            scale, use it with the -L option. The autosizing
                            mechanism will try to assume a scaling proportional to
                            the ration of the given VELOCITY and the object
                            velocity as reported by Sesame. It cannot work with
                            the SDSS_COORDINATES option. Use the --size-column
                            option instead.
      -c, --size-column     This option can only be used with the SDSS_COORDINATES
                            option. If present, the file must contain a column
                            named size, which shows the size of the object in
                            arcseconds. The script will use the size column to
                            compute the scale that will keep the galaxy centered
                            and zoomed in.
      -G, --grid            Corresponds with the G option in the SDSS web chart
                            tool; when used, the image sports a grid with  and
                            crosshairs.
      -L, --label           Corresponds with the L option in the SDSS web chart
                            tool; when used, the image has a label overlay
                            indicating the chart parameters.
      -I, --invert          Corresponds with the I option in the SDSS web chart
                            tool; when set, the image color map is inverted.
      -P, --photometric-objects
                            Corresponds with the P option in the SDSS web chart
                            tool; shows light-blue circles around SDSS photometric
                            objects.
      -S, --spectroscopic-objects
                            Corresponds with the S option in the SDSS web chart
                            tool; shows red squares around SDSS spectroscopic
                            objects.
      -O, --outlines        Corresponds with the O option in the SDSS web chart
                            tool; shows green outlines around SDSS photometric
                            objects, showing where the area for which the
                            photometry is calculated.
      -B, --bounding-boxes  Corresponds with the B option in the SDSS web chart
                            tool; shows pink squares that bound SDSS photometric
                            objects.
      -F, --fields          Corresponds with the F option in the SDSS web chart
                            tool; shows gray outlines demarcating the SDSS fields.
      -M, --masks           Corresponds with the M option in the SDSS web chart
                            tool; shows pink footprints around masked objects,
                            such as bright objects and data artifacts.
      -Q, --plates          Corresponds with the Q option in the SDSS web chart
                            tool; shows circular plates (in lavender) used for
                            spectra collection.
      -m MODE, --mode=MODE  MODE can be either OBJECT_LIST or SDSS_COORDINATES. If
                            set to OBJECT_LIST, each line is expected to have an
                            object name, and Sesame will be used to obtain RA and
                            DEC. This is the default. If set to SDSS_COORDINATES,
                            the file is supposed to be either comma-, blank-, or
                            tab-separated, with at least columns for RA y Dec. If
                            a column with name size is present, the tool will try
                            to fit the size into the frame.
    


For more information on which options are valid, see http://skyserver.sdss3.org/dr9/en/tools/chart/chart.asp

Aknowledgements
===============

This tool has been written withing the framework of the [AMIGA project](http://amiga.iaa.es/ "AMIGA : Analysis of the interstellar Medium of Isolated GAlaxies"), and with support from Spanish grants AYA2008-06181 and AYA2011-30491-C02.

Juande Santander Vela has a contract with CSIC (National Council for Scientific Research) in the JAE-Doc modality of the "Junta de Ampliación de Estudios" program, with funding from the European Social Fund.