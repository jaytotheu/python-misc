To generate tables, reports in different formats (eg. pdf, tex) a steering file is needed. The source of the data are fits files that have been generated for METIS or PHI.
Each report-parameter requires one line of definition as follows. Each column must be separated by a semicolon ";".

Column 1;       Column 2;                       Column 3;         Column 4;   Column 5; Column 6;  Column 7;   Column 8;    Column 9;   Column 10;  Column 11;    Column 12;  Column 13; Column 14; Column 15
ExpTvsMean;     Exposure_vs_Mean_@+22degC;      Exposure-Time;    Mean;       [s];      [DN];      INTTIME;    %10.3f;      han_mean;   %10.3f;     plot-mean;    noreport;   notex;     stat;      metis 

Column  1:- Internal Variable. This name must be unique. It is used further during script execution and to identify this line. No Spaces and special characters are allowed (only ANCII)
Column  2:- File name and diagram heading. This name appears in the diagram as well as file name. Spaces and special characters are allowed. File-System specific characters can cause OS specific problems (eg. "\ :"). In order to avoid dysfunctions, ASCII is recommended. 
Column  3:- Name of the X-axis and column description in the table-text file. 
Column  4:- Name of the Y-axis and legend. 
Column  5:- Unit of X-axis, used in diagram, table, etc. (Please refer to the Unit Glossary written in the header. )
Column  6:- Unit of Y-axis, used in diagram, table, etc. (Please refer to the Unit Glossary written in the header. )
Column  7:- This is the Keyword of the parameter that is analysed as X-axis. It must be the same as written in the the FITS-Header. Furthermore calculated results can be accessed by severeal keywords. See han_solo_light_saber.py --assignment for a list of keywords. (e.g.: han_mean for the mean value)
Column  8:- Number format for X-axis. This parameter (%10.3f - means Complete length= 10 Characters, 3 decimal places, float number; %10s - length 10 characters, string input)
Column  9:- This is the Keyword of the parameter that is analysed as Y-axis. It must be the same as written in the the FITS-Header. Furthermore calculated results can be accessed by severeal keywords. See han_solo_light_saber.py --assignment for a list of keywords. (e.g.: han_mean for the mean value)
Column 10:- Number format for Y-axis (compare with Col. 8). 
Column 11:- This parameter defines how the values are plotted. "plot" will plot each value in the diagram. In fits files with more images the "plot-mean" takes the average of all values of this parameter within one file and calculates and plots the average value.
Column 12:- "report" will generate a pdf-file with the gathered information, if no report is needed use "noreport"
Column 13:- "tex" will generate a LaTex-file with the gathered information, if no report is needed use "notex"
Column 14:- "stat" will generate a statistic file with frame number as well as the defined parameter (compare with Col. 7 and 9)
Column 15:- This parameter selects the camera/sensor type (metis, phi, all and default are accessable).

Example:
-----> the scripting definition for a working METIS example starts here
|||
vvv
ExpTvsMean;     Exposure_vs_Mean_@+22degC;      Exposure-Time;    Mean;       [s];      [DN];      INTTIME;    %10.3f;  han_mean;   %10.3f; plot-mean;      noreport;   notex;  stat;   metis 
ExpTvsStDev;    Exposure_vs_StDev_@+22degC;     Exposure-Time;    StDev;      [s];      [DN];      INTTIME;    %10.3f;  han_std;    %10.3f; plot-mean;      noreport;   notex;  stat;   metis 
