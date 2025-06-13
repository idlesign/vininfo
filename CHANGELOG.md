# vininfo changelog


### v1.9.1 [2025-06-13]
* ** Fix brand resolution bug introduced with Assembler support.

### v1.9.0 [2025-06-09]
* ++ Added Assembler info.
* ++ Countries database update.

### v1.8.0 [2024-01-30]

+ Add Serbia to countries.
+ Include Jeep Egypt codes.
* Add QA for Python 3.11.


### v1.7.0 [2021-12-25]

! Regions and Countries list is updated according to ISO 3780. Info for vehicles made before 2009 may be affected.
+ Model year check in Vin.verify_checksum() is now optional, on by default (see #19).


### v1.6.0 [2021-08-30]

+ WMI dict is updated.


### v1.5.1 [2021-07-14]

* Now using regex VIN validation.


### v1.5.0 [2021-02-04]

+ WMI database extended (see #8).


### v1.4.2 [2021-01-26]

* Added Kia WMI.


### v1.4.1 [2020-07-30]

* Fixed TypeError with some VINs (closes #6).


### v1.4.0 [2020-05-02]

! Dropped support for Py 2.
* Added QA for Py 3.8.
* Dropped QA for Py 3.5.


### v1.3.0

+ WMI database extended.


### v1.2.0

+ Added Vin.manufacturer_is_small property.
+ WMI database extended.


### v1.1.0

+ Allow extraction of basic information even for unsupported brands.


### v1.0.0

! Dropped QA for Python 2.
! Dropped QA for Python 3.4.
* AvtoVAZ transmission types made more specific.
* Celebrating 1.0.0.


### v0.3.0

+ Added basic info for Opel and Renault.
+ Details extractors definitions simplified.


### v0.2.0

+ Added basic info for Nissan.
* Coachwork renamed to body.


### v0.1.0

+ Basic functionality.