To generate tables, reports in different formats (eg. pdf, tex) a steering file is needed. The source of the data are fits files that have been generated for METIS or PHI.
Each report-parameter requires one line of definition as follows. Each column must be separated by a semicolon ";".

Column 1;       Column 2;           Column 3;   Column 4;   Column 5;   Column 6;   Column 7;                                           Column 8
variable;       00_output_name;     plot;       report;     tex;        stat;       This is the first line of the statistics header.    (; This may be additional comments by the author.)
FitsVsDefMean; FitsVsDefStd; FitsVsDefIntTime; FitsVsDefSoftwareVersion; FitsVsDefDX_Size; FitsVsDefDY_Size; FitsVsDefHot_Pixel; FitsVsDefHot_Pixel_Th; FitsVsDefCold_Pixel; FitsVsDefCold_Pixel_Th
ExpTvsMean; 
ExpTvsStDev;

Column  1:- Internal Variable. This name must be unique. It is used further during script execution and to identify this line. No Spaces and special characters are allowed (only ANCII, no underscore at the beginning).
Column  2:- File name and diagram heading. This name appears in the diagram as well as file name. Spaces and special characters are allowed. File-System specific characters can cause OS specific problems (eg. "\ :"). In order to avoid dysfunctions, ASCII is recommended. 
Column  3:- Describes whether a plot of the given information is generated. This only works, if the X-axis is equally defined. 
Column  4:- "report" will generate a pdf-file with the gathered information, if no report is needed use "noreport".
Column  5:- "tex" will generate a LaTex-file with the gathered information, if no report is needed use "notex".
Column  6:- "stat" will generate a statistic file with a header and a table of all data inside. Using the X-axis of the first data package and the Y-axis of every data package.
Column  7:- This is the first line of the header. It has to be defined and should include the main information of the data. 
Column  8:- This is an additional line of the header, follwing the unit glossary. It is optional and can be left blank. Even the full column can be removed. It given the author the possible to comment its data statistics. 

Example:
-----> the scripting definition for a working example starts here
|||
vvv
example1;   00_example;     noplot;     noreport;   notex;      stat;       This is the line occuring in the header file of the statistics. ;  This appears behind the Unit glossary of the header file. 
ExpTvsMean; ExpTvsStDev
