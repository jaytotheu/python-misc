'''
Program:        Heuristic Analysis of Solar Orbiter Data
Institut:       Max-Planck-Institut fuer Sonnensystemforschung
Adress:         Justus-von-Liebig-Weg 3, 37077 Goettingen, Germany
Author:         Julian Utehs
Maintainer:     Julian Utehs
E-mail:         utehs@mps.mpg.de

Description:    This program provides the analysis of Solar Orbiter Camera Data. It analyses the given .fits-files from the PHI, METIS and STAR1000 integrated cameras. A back-up mode for a not specified camera is also given. It writes back at least a summary file in the working directory. If special analysis is required additionally plots and statistics are also created.

Copyricht:      Copyright (c) <2014> <Max-Planck-Institute for solar system research>

Licence:        All right reserved. Copying, modifying or using this software requires the permission by the institute director. For further information please contact the Max-Planck-Institute for solar system research administration.
                The above copyright notice and the eventually given permission notice shall be included in all copies or substantial portions of the Software.

Warranty:       THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Foresight:      Due to its massiv data processing and therefore the automatic data handling, the control given by a gui is not yet recommended nor required. Further functionalities may be included or being handled as seperated scripts. Precompilation of the source code unfortunately failed (see bug report under Version 0.08). Hence there won't be a precompilation in the near future. As the script seems to be fast enough, a precompilation may not be necessary. RAW support is implemented in the seperated program RAWtoFITS.py. This porgram complies the given requirements. 

Version:        0.01 - Kick off
Date:           2014, 18. August

Version:        0.02 - Added and improved plot information for user, improved phi image analysing
Date:           2014, 18. August

Version:        0.03 - Added statistics function in XvsY class, add a lot of comments, add header functionality to CombZ class
Date:           2014, 22. August

Version:        0.04 - Simplified writeHeader, so that all external write header function where useless and removed, unify meanPlot and plot in XvsY-class, tidy up
Date:           2014, 25. August

Version:        0.05 - Reviced listimage function --> became getFileList function, added hot and cold pixel function, cleaned up a little
Date:           2014, 26. August

Version:        0.06 - Unified meanPlot() and plot() function in class CombZ, added new ToDos, Added a legend in all plot functions, added LaTeX Output for XvsY class
Date:           2014, 27. August

Version:        0.07 - Added comments and added a rudimentary report function to the XvsY class, first try of building an executable, Added argument vector for -o output folder, -r recursive, -f grafik format, --help
Date:           2014, 28. August

Version:        0.08 - bash script written to start the han_solo program, precompilation failed due to software bug in the cx_freeze package (see https://bugs.launchpad.net/ubuntu/+source/cx-freeze/+bug/898119 for further details), precompilation defered
Date:           2014, 29. August

Version:        0.09 - Improved the report function (XvsY class)
Date:           2014, 01. September

Version:        0.10 - Added np.float64 precision due to an incorrect mean calculation
Date:           2014, 03. September

Version:        0.11 - Added depth analysis for pixelwise operation, improved help function
Date:           2014, 15. September

Version:        0.12 - Added depth analysis for metis images, correct bug: write metis and phi summaries, if both are present in the folder; updated printHelp function
Date:           2014, 18. September

Version:        0.13 - Added depth mean and standard deviation for phi outputs
Date:           2014, 15. Oktober

Version:        0.14 - Added depth standard mean and standard standard deviation for phi outputs
Date:           2014, 22. Oktober

Version:        0.15 - Added depth standard mean and standard standard deviation for metis images
Date:           2014, 22. Oktober

Version:        1.00 - Outsourced the class definitions, added look-up table support, han solo light saber edition alpha version released
Date:           2014, 20. November

Version:        1.01 - Several fixes, full functionality rebuild
Date:           2014, 21. November

Version:        1.02 - Fixed problems with the image type difinition (try, except added), fixed problems with image dimension readout
Date:           2015, 06. January

Version:        1.03 - Source path interrogationen in main added, fixed typo in decidedAppendant which had resulted in exception routine without an error
Date:           2015, 07. January

Version:        1.04 - Fixed problem of combz class access in definition routine
Date:           2015, 12. January

Version:        1.05 - Updated the help function, updated the assignment function due to get a better communication with the user, removed debug print invocation resulting into error with different headers, fixed false function involking in evaluation of the xvsy variables (simplePlot has been invoked, mean-plot was intended)
Date:           2015, 06. February

Version:        1.06 - Fixed bug in main loop, looking for len(image.shape) not for len(image), to get the dimension and therefore the presence of multiple frame images
Date:           2015, 11. February

Version:        1.07 - Changed Frame unit from [Number] to [N] in xvsy.stat and combz.stat function, added units to plot function labeling, added min and max function, fixed bug that named the output files of stat and tex by the variable name and not by the given name, data for stat and tex files will overwrite the files and not be appended to them
Date:           2015, 05. March

Version:        1.08 - Fixed issue with not written header, integrated han_dark, han_bright, han_phi_i_mean, han_phi_i_std, han_dyn_low_std, han_dyn_high_std, reduced the source code lines especially in the decidedAppendant function, removed getExposureTime and checkFitsCard due to unutilized reasons, making han_solo_light_saber.py ready for python3
Date:           2015, 13. March

Version:        1.09 - Optimized performance
Date:           2015, 16. March

Version:        1.10 - added addHeader function to avoid porblems with not avaible header keys
Date:           2015, 17. March

Version:        1.11 - added print header to xvsy.py, added the han_depth_fits variable as bug fix for the depth analysis
Date:           2015, 19. March

Version:        1.12 - bug fix for the han_depth_fits variable
Date:           2015, 13. April

Version:        1.13 - Added raise::image function
Date:           2015, 13. April

Version:        1.14 - Added lookup_path in the statistics output header, making the input parameter order independent
Date:           2015, 13. April

Version:        1.15 - Added comments
Date:           2015, 10. August

Version:        1.16 - Changed default colours for a better contrast
Date:           2016, 15. Januar

Version:        1.17 - Making control functions in xvsy.csv and combz.csv look-up table case insensitive, removing metis image correction function
Date:           2016, 15. Januar

Version:        1.18 - Bug fix at the point len(image.shape) for 'all' (# Doesn't it has to be image.shape at this point?) causing trouble with several frames
Date:           2016, 15. Januar

Version:        2.00 - Changed to python 3.5 as standard python version, switching to astropy instead of pyfits (not supported anymore), changed subclass interaction (not )
Date:           2016, 

# ToDos:
# Add CombZ report
# Add CombZ exportLatex
# Add variance to han_solo han_var
# getFiles instead of os.walk maybe use os.scandir (if not recursive)?
'''

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ----------------------------------------------------------------
# Required Python packages are imported
# ----------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

import numpy as np
import os as os
import csv as csv
import xvsy as xvsy  # importing the xvsy.XvsY class
import combz as combz  # importing the CombZ class
import sys as sys
if (sys.version.startswith('3')):
    pyversion = 3
    from astropy.io import fits as pyfits
else:
    pyversion = 2
    import pyfits as pyfits


### Shows warnings as error, for debug only.
# import warnings
# warnings.simplefilter("error")




# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ------------------------------------------------------------------------------
# Function Definition
# ------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



# ----------------------------------------------------------------
# Printing Logo
# ----------------------------------------------------------------

def printHanSolo():
    print (('Heuristic Analysis of Solar Orbiter Data --- Light Saber Edition \n\rCalculating as fast as LIGHT to get Stable, Adaptive and Bearing Engineering Results.\n\r' +
'777777777777777777777777777777777777777777777777I++=:~+IIII777777777777777777777 \n\r777777777777777777777777777777777777777777777I:,:,:,:,.,:,:~+?I77777777777777777 \n\r77777777777777777777777777777777777777777777,,,,,::,,,.,,,,,,:~+7777777777777777 \n\r777777777777777777777777777777777777777777+~,,,.,,,,,,,..,,:,,:==777777777777777 \n\r777777777777777777777777777777777777777777:,,,,,=,,,,,:...,,~:,:~+77777777777777 \n\r77777777777777777777777777777777777777777:.,,...,,,,:::,,,,,,,::~~77777777777777 \n\r777777:?:77777777777777777777777777777777,,,,,..,,,,:?I?=:,,,,,:~:=7777777777777 \n\r77777,,,,7777777777777777777777777777777=,,..,,.,,:=?77777?:,.,,~,:7777777777777 \n\r77777I,,:=777777777777777777777777777777,,,..,,,,+?+?I7777I?~,.,,,::777777777777 \n\r777777:,,,77777777777777777777777777777,,,,,,,,:~+??III77IIII+,,,:,,I77777777777 \n\r7777777,,+~777777777777777777777777777I,,,,,,,,~~~=++????II???=,,,,,+77777777777 \n\r7777777,,,:+77777777777777777777777777I~,..,.,,,,,,,:+=~::~~==+,,,,:=I7777777777 \n\r77777777,,,:7777777777777777777777777777.,,.,,.,,,,.:I?=~=+?=++,.~::~I7777777777 \n\r77777777,,,~=777777777777777777777777777,,,,,,~++?+,=IIII777I??+:,,:I77777777777 \n\r77777777,,,,7777777777777777777777777777,,.,,,:=++~,?I??7777??++,,,=777777777777 \n\r77777777=,,,~777777777777777777777777777,,,.,,,:=+,,?I?I=III??+::?~7777777777777 \n\r777777777,,,,777777777777777777777777777,,,,,.,,=..,,~:+I+???++,:+77777777777777 \n\r777777777,,,?777777777777777777777777777~,..,,.,,,.,?=IIII??+++,,777777777777777 \n\r777777777?,,,:7777777777777777777777777777,.,,,..,,,::~?++?++?+~+777777777777777 \n\r777777=,,,,,,,+777777777777777777777777777777,..,.,,=+??++=++=,I7777777777777777 \n\r77777,::,.,,:,,+77777777777777777777777777777=..,..,=?I+=====?777777777777777777 \n\r77777+,+,,.,,,,,+7777777777777777777777777777,,..,,:+?I?+===??I77777777777777777 \n\r777777,,,,,,,,,,,77777777777777777777777777+,.......,,:~:~+??+,=7777777777777777 \n\r777777=.,,,,,,,,,7777777777777777777777777,,...........,=????+=:~7I7777777777777 \n\r7777777?,,~+,.,,,:777777777777777777777I,,...........,++?I?????,~I,,,,,:?7777777 \n\r77777777,,,,~,,~,,,7777777777777777?:,,,,..........,,,~++?????+,=7,,,,,,,.,,,:?I \n\r77777777,,.::.,,,:,77777777777?~,....,.??:......,,,,,:~=+?+??I=:=~,..,.....,,,,, \n\r7777777?:+?+:II+I~?777777777?,,.......=?I?=:.....,,=====+???I+?:?,..,,.....,..,, \n\r77777::~IIIII::+?I777777777I,........,I7777I?=,:::,++?++?IIII7,:,,..........,,,, \n\r777~~?II?IIII+,:??77777777I:...........,~=:.~II++?++II?+IIII7I~.,,...........,,, \n\r77,,,,~=I?I?++I?I?7777777~7:................,,7I?II?II???I~,.,.....,.......,,,., \n\r77,,..:,~?++++III~777777::I,..................,7?????II?I:I....,,...........,.., \n\r77==..,~=,,~III??777777=~=I,..................,7+??II???I,7,..............,,..,, \n\r77I,,,,,,,~I???+7777777:+?I:.................,.:I+?III???~7:...............,,.,, \n\r777:,,.,+I??++~I777777,:+I7:....................7I????????77,,...............,,, \n\r7777:,=????+?=I777777?:,,77:...................,??I??+??+I77,.................., \n\r77777=,:~~+++?7777777,,I??7:....................,7???+??~777I,..............,.., \n\r77777?,,=+=??II77777,~~~I7+~..................,.,II?++++,7777................,., \n\r77777:,,+???I7777777===?I?,,..................:+,:7??++~:7777.................,. \n\r77777:,,=?I?7777777=??I7777,..................7I:,~7?==,I7777+.,................ \n\r777777,:~??7777777=+?I7777?,.................,?I7==~I+~,777777,...............,I \n\r777777,::+=777777?~?II77I~...................,77II7==I:~777777?...............:I \n\r777777I:~,7I77777~+III7I?...................,?7I???77I?777I7777...............~7 \n\r7777777++?II77777??IIIII+...................,777777777III777777:..............~7 \n\r77777=~:+II?7I777?IIIII?:....................IIII??III777777777?..............:I \n\r77777I:~?I??I?I777IIIII+,...................,IIIIII?7I777777777?..............:+ \n\r777777,:?7I?+II7777~~=++,...................~++?+??IIII77777777I..............,= \n\r777777,,+II+=III77II7I~~....,,..............??IIIIII7I777777777I..............,~ \n\r777777=,:II==??I7777?I?~,..,7,..............7777777777777777777?...............,'))
    return True



# ----------------------------------------------------------------
# Getting Metis image error - deprecated 
# ----------------------------------------------------------------

def getMETISImageError(image_size):
    '''The METIS analysis software has a driver problem. Thus the first 2048 pixel contain invalid data. Hence they have to be removed. Due to the fact, that picture data is normally stored in rows and columns, full rows has to be removed. This function given back this number of rows.'''
    return ((2047//image_size[2]) + 1)  # Floor Devision + 1




# ----------------------------------------------------------------
# Scanning for files
# ----------------------------------------------------------------

def getFileList(src_path, recursive, file_ext):
    '''Returns file list based on the source directory. The file extension and a recursive search can be choosen. '''
    file_list = []                              # Creates an empty list
    try:
        local_file_list = os.walk(src_path)     # Get all elements of the path and his child directories
    except IOError: # as (errno, strerror):     # Error handling, if src_path does not exists
        print (('Error can\'t find Directory: ' + src_path))    # Informing the user
        return file_list                                        # Breaking out of function
    for (path, dirs, files) in local_file_list:     # For all elements, if it is a file with the ending file_ext, append it to the file_list
        if len(files) > 0:                          # Checking whether local_file_list is empty
            for f in files:                             # loop of all files
                g = f.lower()                           # making it case unsensitive
                if (g.endswith('.' + file_ext) == True):
                    file_list.append(os.path.normpath(path + os.sep +f)) # Added path due to problems with the recursive function, file_list.append(os.path.join(os.path.abspath(path) + os.sep, f)) # os.path.dirname(path) ? Which version is better?
        if (recursive != True):                     # If recursive is not true, break out of the for-loop --> only the first iteration is pass through
            break
    file_list.sort()
    return file_list  # absolut path




# ----------------------------------------------------------------
# Removing files
# ----------------------------------------------------------------

def removeFilesFromList(file_list, file_ending, file_ext):
    '''Removes the files with a special ending from the file list. This function was necessary because the result is written in the same file as the input, but should not be analyzed again.'''
    clean_file_list = [] # Creates an empty list
    for l in range(len(file_list)): # Crawling the files
        if (file_list[l].endswith(file_ending + '.' + file_ext) == False): # If file ends with the extension and ending, it is added to the clean_file_list
            clean_file_list.append(file_list[l])
    return clean_file_list




# ----------------------------------------------------------------
# Calculating number of hot pixels 
# ----------------------------------------------------------------

def calcHotPixel(image, mean, sigma):
    '''This function gives back the number of hot pixels, that can be found in the image. A hot pixel is defined by a value greater than (image_mean + 6*sigma).'''
    return len(image[image > (mean + (6*sigma))]) # gives back the length of the image array where the value exceeds mean + 6*sigma




# ----------------------------------------------------------------
# Calculating number of cold pixels 
# ----------------------------------------------------------------

def calcColdPixel(image, mean, sigma):
    '''This function gives back the number of cold pixels, that can be found in the image. A cold pixel is defined by a value smaller than (image_mean - 3*sigma).'''
    return len(image[image < (mean - (3*sigma))]) # gives back the length of the image array where the value remains under mean - 3*sigma



# ----------------------------------------------------------------
# Reading image parameter including error handling
# ----------------------------------------------------------------

def readImageParameter(hdr, key_word, out_format):
    '''Tries to read the image parameter. If no parameter is found, the value is set to [N/A], making it obvious that an error occurred. '''
    try:
        tmp = out_format % hdr[key_word] # Tries to write the header key word to the output
    except: # KeyError as (keyerror): # Exception handling
        tmp = "%10s" % 'N/A'
        print (('Warning: ' + str(key_word) + ' not found. Please check the fits headers.')) # Please test this function again. 
    finally:
        return tmp 



# ----------------------------------------------------------------
# Printing help text
# ----------------------------------------------------------------

def printHelp(version):
    '''Prints the help function, invoked by < --help > '''
    print ('Han-Solo - Heuristic Analysis of Solar Orbiter Data \n\r')
    print ('Light Saber Edition')
    print ('Usage: han_solo_light_saber.py [OPTIONS] ... SOURCE')
    print ('OR:    han_solo_light_saber.py [OPTIONS] ... SOURCE ... [-o OUTPUT]')
    print ('OR:    han_solo_light_saber.py SOURCE ... [OPTIONS] ... [-o OUTPUT]')
    print ('Please do NOT define the output before the source is defined.\n\r')
    print ('Spaces in the path name are not supported.\n\r')
    print ('--------------------------------------------------------------------------------')
    print ('Avaible arguments are: ')
    print ('     -r, --recursive     analyses the folder recursively')
    print ('         --details       prints more details on the ongoing process')
    print ('     -f, --format        [format] saves the plot in the given format,\n\r                         avaible formats are png, jpg and eps')
    print ('     -o, --output        defines the output folder,\n\r                         default is the source path')
    print ('     -D, --depth         makes a depth analysis of fits images and \n\r                         saves them to the folder mean_std_fits')
    print ('     -F, --frame         makes a frame analysis of fits images and \n\r                         saves a dataset for every image')
    print ('     -G, --gain          makes a gain analysis of fits images and \n\r                          saves them to the folder gain_fits')
    print ('     -l, --lookup        defines the look-up folder,\n\r                         default is the source path\n\r                         searching for xvsy.csv and combz.csv')
    print ('         --assignment    prints all assigned variables')
    print ('         --help          prints this help page\n\r')
    print ('--------------------------------------------------------------------------------')
    print ('Example: python han_solo_light_saber.py /path/to/directory -r -f jpg')
    print ('Performs an analysis to all fits images in directory /path/to/directory\n\r and its recursive directories. Gives back the images in jpg format.\n\r')
    print ('Example: python han_solo_light_saber.py /path/to/directory --details -o /path/to/output')
    print ('Performs an analysis to all fits files in directory /path/to/directory.\n\r Writes the output into the directory /path/to/output. Gives back a\n\r bunch of information during the process.\n\r')
    print ('--------------------------------------------------------------------------------')
    print ('Report bugs to utehs@mps.mpg.de')
    print ('Homepage: www.mps.mpg.de')
    print (('Version: ' + version))
    return True





# ----------------------------------------------------------------
# Printing the possible allingment for the image parameter
# ----------------------------------------------------------------

def printAllingment():
    '''Prints all predifinied variables that are readoutable.'''
    print ('This list shows the possible value that can be accessed by the user. ')
    print ('i can be replaced with [1..4] for the intended quadrant output of isphi images.')
    print ('han_fits             - gives back the number of the fits frame - often used for statistics')
    print ('han_mean             - gives back the mean value of all pixels in a frame')
    print ('han_std              - gives back the standard deviation of all pixels in a frame')
    print ('han_size_x           - gives back the x size of the frame')
    print ('han_size_y           - gives back the x size of the frame')
    print ('han_hot              - gives back the number of hot pixels')
    print ('han_hot_th           - gives back the threshold for the hot pixel decision')
    print ('han_cold             - gives back the number of cold pixels')
    print ('han_cold_th          - gives back the threshold for the cold pixel decision')
    print ('han_low              - gives back the mean value of the lowermost half of pixels')
    print ('han_high             - gives back the mean value of the upper half of pixels')
    print ('han_dyn_low          - gives back the mean value of the lowermost half of pixels ignoring one sigma from the mean value')
    print ('han_dyn_high         - gives back the mean value of the upper half of pixels ignoring one sigma from the mean value')
    print ('han_dyn_low_std      - gives back the std value of the lowermost half of pixels ignoring one sigma from the mean value')
    print ('han_dyn_high_std     - gives back the std value of the upper half of pixels ignoring one sigma from the mean value')
    print ('han_contrast         - gives back the contrast value')
    print ('han_min              - gives back the minimum value')
    print ('han_max              - gives back the maximum value')
    print ('han_dark             - gives back the number of pixels in han_dyn_low')
    print ('han_bright           - gives back the number of pixels in han_dyn_high')
    print ('han_phi_i_mean       - gives back the mean value of the choosen quadrant')
    print ('han_phi_i_std        - gives back the std value of the choosen quadrant')
    print ('The following values can only be choosen, if depth analysis is performed.')
    print ('han_depth_fits       - gives back a 0 required for the statistics')
    print ('han_depth_name       - gives back the name of the processed image')
    print ('han_depth_n_frames   - gives back the number of frames')
    print ('han_depth_mean_mean_value    - gives back the mean value for the mean image')
    print ('han_depth_mean_std_value     - gives back the standard deviation value for the mean image')
    print ('han_depth_std_mean_value     - gives back the mean value for the standard deviation image')
    print ('han_depth_std_std_value      - gives back the standard deviation value for the standard deviation image')
    print ('han_depth_phi_i_mean_mean  - gives back the mean value for the output quadrant i of the mean image')
    print ('han_depth_phi_i_mean_std   - gives back the standard deviation value for the output quadrant i of the mean image')
    print ('han_depth_phi_i_std_mean   - gives back the mean value for the output quadrant i of the standard deviation image')
    print ('han_depth_phi_i_std_std    - gives back the standard deviation value for the output quadrant i of the standard deviation image')
    return 0




# ----------------------------------------------------------------
# Internal variable assignment
# ----------------------------------------------------------------
    
def getInternalVariable(unknown_var, unknown_format, image_var):
    '''Gives back the internal variable value. Takes the name and format for the wanted variable and the calculated variable array. Gives back a string of the formated value.''' 
    image_var_all = ['han_fits', 'han_mean', 'han_std', 'han_size_x', 'han_size_y', 'han_hot', 'han_hot_th', 'han_cold', 'han_cold_th', 'han_low', 'han_high', 'han_dyn_low', 'han_dyn_high', 'han_contrast', 'han_min', 'han_max', 'han_dark', 'han_bright', 'han_phi_1_mean', 'han_phi_2_mean', 'han_phi_3_mean', 'han_phi_4_mean', 'han_phi_1_std', 'han_phi_2_std', 'han_phi_3_std', 'han_phi_4_std', 'han_dyn_low_std', 'han_dyn_high_std']
    image_var_depth = ['han_depth_mean_mean', 'han_depth_mean_std', 'han_depth_std_mean', 'han_depth_std_std', 'han_depth_phi_1_mean_mean', 'han_depth_phi_1_mean_std', 'han_depth_phi_1_std_mean', 'han_depth_phi_1_std_std', 'han_depth_phi_2_mean_mean', 'han_depth_phi_2_mean_std', 'han_depth_phi_2_std_mean', 'han_depth_phi_2_std_std', 'han_depth_phi_3_mean_mean', 'han_depth_phi_3_mean_std', 'han_depth_phi_3_std_mean', 'han_depth_phi_3_std_std', 'han_depth_phi_4_mean_mean', 'han_depth_phi_4_mean_std', 'han_depth_phi_4_std_mean', 'han_depth_phi_4_std_std', 'han_depth_fits', 'han_depth_name', 'han_depth_n_frames']
    
    tmp = "%10s" % 'N/A'
    if unknown_var.lower().startswith('han_depth_'): 
        for i in range(len(image_var_depth)):
            if (unknown_var.lower() == image_var_depth[i]):
                tmp = unknown_format % image_var[i]
                break
    else:
        for i in range(len(image_var_all)):
            if (unknown_var.lower() == image_var_all[i]):
                tmp = unknown_format % image_var[i]
                break
    if (tmp == '       N/A'): # PLEASE VERIFY THIS
        print (('Warning: ' + unknown_var + '  -  Internal Variable not defined.'))
    return tmp




# ----------------------------------------------------------------
# Get header information into the right format
# ----------------------------------------------------------------

def addHeader(hdr, key_name, key_format):
    try:
        tmp = key_format % hdr[key_name] # 
    except:
        tmp = '       N/A' # 
    return tmp



# ----------------------------------------------------------------
# Append the data to the analysis classes (see xvsy.py)
# ----------------------------------------------------------------

def decidedAppendant(xvsypointer, image_var_all, x_name, y_name, x_format, y_format, current_frame, fits_list, hdr):
    if x_name.lower().startswith('han_') and not x_name.lower().startswith('han_depth_') and y_name.lower().startswith("han_depth_") :
        print (('Isochronical access to normal variables and depth variables is not possible since they belong to different stages of calculation at input stream: ' + xvsypointer.attributes[0]))
        return False
    if y_name.lower().startswith('han_') and not y_name.lower().startswith('han_depth_') and x_name.lower().startswith("han_depth_") :
        print (('Isochronical access to normal variables and depth variables is not possible since they belong to different stages of calculation at input stream: ' + xvsypointer.attributes[0]))
        return False
    try:
        if x_name.lower().startswith("han_") and y_name.lower().startswith("han_"):
            xvsypointer.appendDuple(getInternalVariable(x_name, x_format, image_var_all), getInternalVariable(y_name, y_format, image_var_all), current_frame, fits_list)
        elif x_name.lower().startswith("han_"):
            xvsypointer.appendDuple(getInternalVariable(x_name, x_format, image_var_all), addHeader(hdr, y_name, y_format), current_frame, fits_list)
        elif y_name.lower().startswith("han_"):
            xvsypointer.appendDuple(addHeader(hdr, x_name, x_format), getInternalVariable(y_name, y_format, image_var_all), current_frame, fits_list)
        else:
            xvsypointer.appendDuple(addHeader(hdr, x_name, x_format), addHeader(hdr, y_name, y_format), current_frame, fits_list)
    except:
        print (('Problems with look-up input stream on position: ' + xvsypointer.attributes[0]))
    return True





# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ------------------------------------------------------------------------------
# Start Analysis
# ------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def startAnalysis(src_path, work_path, lookup_path, version, fits_list, grafic_format, depth_analysis, frame_analysis, gain_analysis, colours, details):
    if (sys.version.startswith('3')):
        readfile = "r"
        writefile = "w"
        appendfile = "a"
    else:
        readfile = "rb"
        writefile = "wb"
        appendfile = "ab"

    local_dict = {}
    var_names = []
    combz_names = []
    var_request = []
    load_image = False
    with open(lookup_path + 'xvsy.csv', readfile) as f:
        reader = csv.reader(f, delimiter = ';')
        for row in reader:
            try:
                fitstest = xvsy.XvsY(row[1].strip(), row[2].strip(), row[3].strip(), row[4].strip(), row[5].strip(), row[6].strip(), row[7].strip(), row[8].strip(), row[9].strip(), row[10].strip().lower(), row[11].strip().lower(), row[12].strip().lower(), row[13].strip().lower(), row[14].strip().lower()) # Removing unneeded spaces in front and behind the string, initializing the class with the values
                local_dict[ row[0] ] = fitstest #'somevar_%s' % row[0]] = fitstest # Already forgotten of which use it is
                var_names.append(row[0].strip())
                var_request.append(row[6].strip())
                var_request.append(row[8].strip())
            except:
                print (('Error in look-up input stream at position: ' + row[0] + '\r\nPlease check whether an input information is missing and if the delimiter is of the right kind.'))
    print ('List of all images found in the directory:')
    print (fits_list)
    if (details == True):
        print ('List of all variables found in the look-up table:')
        print (var_names)
    
    clean_request_list = [] # Creates an empty list
    for l in range(len(var_request)): # Crawling the files
        if (var_request[l].startswith('han_') == True) and (var_request[l] not in clean_request_list): # If file starts han_ it is added to the clean_request_list
            clean_request_list.append(var_request[l])
    var_request = clean_request_list
    
    for l in range(len(var_request)):
        if (var_request[l].startswith('han_') == True):
            load_image = True
            break
    
    if (details == True):
        print ('List of all requested variables:')
        print (var_request)
    
    if 'han_phi_1_mean' or 'han_phi_2_mean' or 'han_phi_3_mean' or 'han_phi_4_mean' or 'han_phi_1_std' or 'han_phi_2_std' or 'han_phi_3_std' or 'han_phi_4_std' in var_request:
        calc_phi = True
    else:
        calc_phi = False
    if 'han_cold' or 'han_cold_th' or 'han_hot' or 'han_hot_th' in var_request:
        calc_hot_cold = True
    else:
        calc_hot_cold = False
    if 'han_low' or 'han_high' or 'han_dyn_low' or 'han_dyn_high' or 'han_contrast' or 'han_min' or 'han_max' or 'han_dark' or 'han_bright' in var_request:
        calc_dyn_contrast = True
    else:
        calc_dyn_contrast = False
    if 'han_min' or 'han_max' in var_request:
        calc_min_max = True
    else:
        calc_min_max = False
    
    image_var_all = []
    image_var_depth = []

    for l in range(len(fits_list)):
        print (('\r\n' + 'The following image is analysed: ' + fits_list[l]))
        hdulist  = pyfits.open(fits_list[l])
        image    = hdulist[0].data  ### Do not need to open the image, if only Header Information is searched for... then the regular dimension has to be read out of the header. 
        hdr      = hdulist[0].header
#        num_of_frames = len(image)
        ### Change due to image dimension reasons...
        if (len(image.shape) == 3):
            num_of_frames = len(image)
        else:
            num_of_frames = 1
        if (details == True):
            print ('Number of frames:')
            print (num_of_frames)
        image_dimension = image.shape
        if (details == True):
            print ('Image Dimension:')
            print (image_dimension)
        ### ... !

#        # StW 30.7.2014  checking for table
#        if (len(hdulist) == 2):
#            tbl = hdulist[1].header
#            tbl_data = hdulist[1].data
        
        try:  # checking the image type
            if (hdr['SWCLASS'] == 'isphi::Image'):
                print ('The image type is: Phi Image')
                image_type = 'Phi Image'
            elif (hdr['SWCLASS'] == 'metis::Image'):
                print ('The image type is: metis::Image')
                image_type = 'metis::Image'
            elif (hdr['SWCLASS'] == 'raise::Image'):
                print ('The image type is: raise::Image')
                image_type = 'raise::Image'
            elif (hdr['SWCLASS'] == 'star1000::Image'):
                print ('The image type is: star1000::Image')
                image_type = 'star1000::Image'
            else:
                print ('The image type is: No known image type detected.')
                image_type = 'default::Image'
        except:
            print ('Software class in header not defined. Falling back to image type default.')
            image_type = 'default::Image'

        if depth_analysis:
            depth_image_size = image.shape
            # print depth_image_size
            if (len(depth_image_size) == 3): # Not secure here, a depth analysis is senseless if the image just have one frame
                image_x = depth_image_size[2]
                image_y = depth_image_size[1]
            else:
                image_x = depth_image_size[1]
                image_y = depth_image_size[0]
            depth_image = np.zeros((image_y, image_x))
            depth_std   = np.zeros((image_y, image_x))
            depth_tmp   = np.zeros((image_y, image_x))
            depth_mean  = np.zeros((image_y, image_x))

        for current_frame in range(num_of_frames):
            print (('The following frame is analysed: ' + str(current_frame+1)))
            if (image_type == 'metis::Image') :
                #tmp_image = image[current_frame, getMETISImageError(image_dimension):1024] # Cut of the lines of erroneous pixels due to a driver software problem/ hardware problem
                tmp_image = image[current_frame]
                tmp_depth_image = image[current_frame]
                [image_phi_1_mean, image_phi_2_mean, image_phi_3_mean, image_phi_4_mean, image_phi_1_std, image_phi_2_std, image_phi_3_std, image_phi_4_std] = [0,0,0,0,0,0,0,0]
            elif (image_type == 'raise::Image') :
                tmp_image = image[current_frame]
                tmp_depth_image = image[current_frame]
                [image_phi_1_mean, image_phi_2_mean, image_phi_3_mean, image_phi_4_mean, image_phi_1_std, image_phi_2_std, image_phi_3_std, image_phi_4_std] = [0,0,0,0,0,0,0,0]
            elif (image_type == 'Phi Image') :
                tmp_phi_1 = image[current_frame, 0:2047, 0:511] # PLEASE VERIFY THE ROWS AND COLOUMS, IS THIS FUNCTION RIGHT OR WRONG??? Verified. Check for complications.
                if calc_phi:
                    image_phi_1_mean = np.mean(tmp_phi_1, dtype=np.float64)
                    image_phi_1_std = np.std(tmp_phi_1, dtype=np.float64)
                    tmp_phi_2 = image[current_frame, 0:2047, 512:1023]
                    image_phi_2_mean = np.mean(tmp_phi_2, dtype=np.float64)
                    image_phi_2_std = np.std(tmp_phi_2, dtype=np.float64)
                    tmp_phi_3 = image[current_frame, 0:2047, 1024:1535]
                    image_phi_3_mean = np.mean(tmp_phi_3, dtype=np.float64)
                    image_phi_3_std = np.std(tmp_phi_3, dtype=np.float64)
                    tmp_phi_4 = image[current_frame, 0:2047, 1536:2047]
                    image_phi_4_mean = np.mean(tmp_phi_4, dtype=np.float64)
                    image_phi_4_std = np.std(tmp_phi_4, dtype=np.float64)
                else:
                    [image_phi_1_mean, image_phi_2_mean, image_phi_3_mean, image_phi_4_mean, image_phi_1_std, image_phi_2_std, image_phi_3_std, image_phi_4_std] = [0,0,0,0,0,0,0,0]
                # tmp_phi_1 = image[current_frame, 0:2, 0:3] <-- x 0-2,  y 0-3 im aktuellen Bild (dreidimensionales Array)
                tmp_image = image[current_frame]
                tmp_depth_image = image[current_frame]
            elif (image_type == 'star1000::Image'):
                tmp_image = image[current_frame]
                tmp_depth_image = image[current_frame]
                [image_phi_1_mean, image_phi_2_mean, image_phi_3_mean, image_phi_4_mean, image_phi_1_std, image_phi_2_std, image_phi_3_std, image_phi_4_std] = [0,0,0,0,0,0,0,0]
            else:
                [image_phi_1_mean, image_phi_2_mean, image_phi_3_mean, image_phi_4_mean, image_phi_1_std, image_phi_2_std, image_phi_3_std, image_phi_4_std] = [0,0,0,0,0,0,0,0]
                if (len(image.shape) == 3):
                    tmp_image = image[current_frame]
                    tmp_depth_image = image[current_frame]
                else:
                    tmp_image = image
                    tmp_depth_image = image

            tmp_image = np.array(tmp_image)
            image_size = tmp_image.shape
            print (image_size)
            
            image_mean = np.mean(tmp_image, dtype=np.float64)
            image_std = np.std(tmp_image, dtype=np.float64)
            if calc_hot_cold:
                image_hot = calcHotPixel(tmp_image, image_mean, image_std)
                image_hot_th = image_mean + 6*image_std
                image_cold = calcColdPixel(tmp_image, image_mean, image_std)
                image_cold_th = image_mean - 3*image_std
            else: 
                [image_hot, image_hot_th, image_cold, image_cold_th] = [0, 0, 0, 0]
            
            if calc_dyn_contrast:
                tmp_low = tmp_image[np.where(tmp_image < image_mean)]
                tmp_high = tmp_image[np.where(tmp_image > image_mean)]
                
                tmp_low_mean = np.mean(tmp_low, dtype=np.float64)
                tmp_high_mean = np.mean(tmp_high, dtype=np.float64)
                
                dyn_low = tmp_low[np.where(tmp_low < (np.mean(tmp_low, dtype=np.float64) + np.std(tmp_low, dtype=np.float64)))]
                dyn_high = tmp_high[np.where(tmp_high > (np.mean(tmp_high, dtype=np.float64) - np.std(tmp_high, dtype=np.float64)))]
                
                image_dark   = len(dyn_low)
                image_bright = len(dyn_high)
                
                dyn_low_mean = np.mean(dyn_low, dtype=np.float64)
                dyn_high_mean = np.mean(dyn_high, dtype=np.float64)
                
                dyn_low_std = np.std(dyn_low, dtype=np.float64)
                dyn_high_std = np.std(dyn_high, dtype=np.float64)
                
                tmp_contrast = ((np.mean(dyn_high, dtype=np.float64)-np.mean(dyn_low, dtype=np.float64))/(np.mean(dyn_high, dtype=np.float64)+np.mean(dyn_low, dtype=np.float64)))
            else:
                [tmp_low, tmp_high, tmp_low_mean, tmp_high_mean, dyn_low, dyn_high, image_dark, image_bright, dyn_low_mean, dyn_high_mean, dyn_low_std, dyn_high_std, tmp_contrast] = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                
            if calc_min_max:
                image_min = np.amin(tmp_image)
                image_max = np.amax(tmp_image)
            else:
                [image_min, image_max] = [0, 0]
            
            if (len(image_size) == 3): # TODO: Test this sequence with normal data.
                image_x = image_size[2]
                image_y = image_size[1]
            else:
                image_x = image_size[1]
                image_y = image_size[0]

            image_var_all = [l, image_mean, image_std, image_x, image_y, image_hot, image_hot_th, image_cold, image_cold_th, tmp_low_mean, tmp_high_mean, dyn_low_mean, dyn_high_mean, tmp_contrast, image_min, image_max, image_dark, image_bright, image_phi_1_mean, image_phi_2_mean, image_phi_3_mean, image_phi_4_mean, image_phi_1_std, image_phi_2_std, image_phi_3_std, image_phi_4_std, dyn_low_std, dyn_high_std] # Check whether there is a problem with x and y

            if depth_analysis:
                depth_image = depth_image + tmp_depth_image

            for i in range(len(var_names)):
                place = var_names[i]
                local_class_pointer = local_dict[place]
                local_x_name = local_dict[place].controls[0]
                local_y_name = local_dict[place].controls[2]
                local_x_format = local_dict[place].controls[1]
                local_y_format = local_dict[place].controls[3]
                if (not local_x_name.lower().startswith('han_depth_')) and (not local_y_name.lower().startswith('han_depth_')): # Add the option of generic image type by simply compare the look up input with the hdr key
                    if (local_dict[place].attributes[5] == 'all'):
                        decidedAppendant(local_class_pointer, image_var_all, local_x_name, local_y_name, local_x_format, local_y_format, current_frame, fits_list[l], hdr)
                    if (local_dict[place].attributes[5] == 'metis' and image_type == 'metis::Image'):
                        decidedAppendant(local_class_pointer, image_var_all, local_x_name, local_y_name, local_x_format, local_y_format, current_frame, fits_list[l], hdr)
                    if (local_dict[place].attributes[5] == 'raise' and image_type == 'raise::Image'):
                        decidedAppendant(local_class_pointer, image_var_all, local_x_name, local_y_name, local_x_format, local_y_format, current_frame, fits_list[l], hdr)
                    if (local_dict[place].attributes[5] == 'phi' and image_type == 'Phi Image'):
                        decidedAppendant(local_class_pointer, image_var_all, local_x_name, local_y_name, local_x_format, local_y_format, current_frame, fits_list[l], hdr)
                    if (local_dict[place].attributes[5] == 'star1000' and image_type == 'star1000::Image'):
                        decidedAppendant(local_class_pointer, image_var_all, local_x_name, local_y_name, local_x_format, local_y_format, current_frame, fits_list[l], hdr)
                    if (local_dict[place].attributes[5] == 'default' and image_type == 'default::Image'):
                        decidedAppendant(local_class_pointer, image_var_all, local_x_name, local_y_name, local_x_format, local_y_format, current_frame, fits_list[l], hdr)
            hdulist.close()
            
# depth analysis
        if depth_analysis:
            depth_mean = depth_image/(len(list(range(num_of_frames))))

            for current_frame in range(num_of_frames):
                tmp_depth_image = image[current_frame]
                depth_tmp = tmp_depth_image - depth_mean
                depth_tmp = np.square(depth_tmp)
                depth_std = depth_std + depth_tmp

            depth_std = depth_std/(len(list(range(num_of_frames))) -1)
            depth_std = np.sqrt(depth_std)
            depth_mean_mean_value = np.mean(depth_mean, dtype=np.float64)
            depth_mean_std_value = np.std(depth_mean, dtype=np.float64)
            depth_std_mean_value = np.mean(depth_std, dtype=np.float64)
            depth_std_std_value = np.std(depth_std, dtype=np.float64)

            print ('Depth standard deviation value:')
            print (depth_std_std_value)
            out_hdu_std = pyfits.PrimaryHDU(data=[depth_mean, depth_std], header=hdr)
            tmp_base = os.path.basename(fits_list[l])
            tmp_ext = ''
            (tmp_name, tmp_ext) = os.path.splitext(tmp_base)
            try:
                out_hdu_std.writeto(os.path.join(os.path.abspath(work_path) + os.sep, 'mean-std-fits' + os.sep, tmp_name + '_mean_std.fits'))
            except IOError as ioex:
#                print 'errno: ', ioex.errno
                if (ioex.errno == 2):
                    try:
                        os.mkdir('mean-std-fits')
                        out_hdu_std.writeto(os.path.join(os.path.abspath(work_path) + os.sep, 'mean-std-fits' + os.sep + tmp_name + '_mean_std.fits'))
                    except:
                        print ('No directory could be created.')
                else:
                    print ('Files already exist.')
            if (image_type == 'Phi Image'):
                tmp_phi_depth = depth_mean[0:2047, 0:511]
                image_phi_depth_1_mean_mean = np.mean(tmp_phi_depth, dtype=np.float64)
                image_phi_depth_1_mean_std = np.std(tmp_phi_depth, dtype=np.float64)
                tmp_phi_depth = depth_std[0:2047, 0:511]
                image_phi_depth_1_std_mean = np.mean(tmp_phi_depth, dtype=np.float64)
                image_phi_depth_1_std_std = np.std(tmp_phi_depth, dtype=np.float64)
                tmp_phi_depth = depth_mean[0:2047, 512:1023]
                image_phi_depth_2_mean_mean = np.mean(tmp_phi_depth, dtype=np.float64)
                image_phi_depth_2_mean_std = np.std(tmp_phi_depth, dtype=np.float64)
                tmp_phi_depth = depth_std[0:2047, 512:1023]
                image_phi_depth_2_std_mean = np.mean(tmp_phi_depth, dtype=np.float64)
                image_phi_depth_2_std_std = np.std(tmp_phi_depth, dtype=np.float64)
                tmp_phi_depth = depth_mean[0:2047, 1024:1535]
                image_phi_depth_3_mean_mean = np.mean(tmp_phi_depth, dtype=np.float64)
                image_phi_depth_3_mean_std = np.std(tmp_phi_depth, dtype=np.float64)
                tmp_phi_depth = depth_std[0:2047, 1024:1535]
                image_phi_depth_3_std_mean = np.mean(tmp_phi_depth, dtype=np.float64)
                image_phi_depth_3_std_std = np.std(tmp_phi_depth, dtype=np.float64)
                tmp_phi_depth = depth_mean[0:2047, 1536:2047]
                image_phi_depth_4_mean_mean = np.mean(tmp_phi_depth, dtype=np.float64)
                image_phi_depth_4_mean_std = np.std(tmp_phi_depth, dtype=np.float64)
                tmp_phi_depth = depth_std[0:2047, 1536:2047]
                image_phi_depth_4_std_mean = np.mean(tmp_phi_depth, dtype=np.float64)
                image_phi_depth_4_std_std = np.std(tmp_phi_depth, dtype=np.float64)
            else:
                [image_phi_depth_1_mean_mean, image_phi_depth_1_mean_std, image_phi_depth_1_std_mean, image_phi_depth_1_std_std, image_phi_depth_2_mean_mean, image_phi_depth_2_mean_std, image_phi_depth_2_std_mean, image_phi_depth_2_std_std, image_phi_depth_3_mean_mean, image_phi_depth_3_mean_std, image_phi_depth_3_std_mean, image_phi_depth_3_std_std, image_phi_depth_4_mean_mean, image_phi_depth_4_mean_std, image_phi_depth_4_std_mean, image_phi_depth_4_std_std] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

            image_var_depth = [depth_mean_mean_value, depth_mean_std_value, depth_std_mean_value, depth_std_std_value, image_phi_depth_1_mean_mean, image_phi_depth_1_mean_std, image_phi_depth_1_std_mean, image_phi_depth_1_std_std, image_phi_depth_2_mean_mean, image_phi_depth_2_mean_std, image_phi_depth_2_std_mean, image_phi_depth_2_std_std, image_phi_depth_3_mean_mean, image_phi_depth_3_mean_std, image_phi_depth_3_std_mean, image_phi_depth_3_std_std, image_phi_depth_4_mean_mean, image_phi_depth_4_mean_std, image_phi_depth_4_std_mean, image_phi_depth_4_std_std, 0, tmp_name, num_of_frames]
            
            for i in range(len(var_names)):
                place = var_names[i]
                local_class_pointer = local_dict[place]
                local_x_name = local_dict[place].controls[0]
                local_y_name = local_dict[place].controls[2]
                local_x_format = local_dict[place].controls[1]
                local_y_format = local_dict[place].controls[3]
                if (local_x_name.lower().startswith('han_depth_') or local_y_name.lower().startswith('han_depth_')):
                    if (local_dict[place].attributes[5] == 'all'):
                        decidedAppendant(local_class_pointer, image_var_depth, local_x_name, local_y_name, local_x_format, local_y_format, current_frame, fits_list[l], hdr)
                    if (local_dict[place].attributes[5] == 'metis' and image_type == 'metis::Image'):
                        decidedAppendant(local_class_pointer, image_var_depth, local_x_name, local_y_name, local_x_format, local_y_format, current_frame, fits_list[l], hdr)
                    if (local_dict[place].attributes[5] == 'raise' and image_type == 'raise::Image'):
                        decidedAppendant(local_class_pointer, image_var_depth, local_x_name, local_y_name, local_x_format, local_y_format, current_frame, fits_list[l], hdr)
                    if (local_dict[place].attributes[5] == 'phi' and image_type == 'Phi Image'):
                        decidedAppendant(local_class_pointer, image_var_depth, local_x_name, local_y_name, local_x_format, local_y_format, current_frame, fits_list[l], hdr)
                    if (local_dict[place].attributes[5] == 'star1000' and image_type == 'star1000::Image'):
                        decidedAppendant(local_class_pointer, image_var_depth, local_x_name, local_y_name, local_x_format, local_y_format, current_frame, fits_list[l], hdr)
                    if (local_dict[place].attributes[5] == 'default' and image_type == 'default::Image'):
                        decidedAppendant(local_class_pointer, image_var_depth, local_x_name, local_y_name, local_x_format, local_y_format, current_frame, fits_list[l], hdr)
                        
# frame analysis
        if frame_analysis:
            depth_mean = depth_image/(len(list(range(num_of_frames))))

            for current_frame in range(num_of_frames):
                tmp_depth_image = image[current_frame]
                depth_tmp = tmp_depth_image - depth_mean
                depth_tmp = np.square(depth_tmp)
                depth_std = depth_std + depth_tmp

            depth_std = depth_std/(len(list(range(num_of_frames))) -1)
            depth_std = np.sqrt(depth_std)
            depth_mean_mean_value = np.mean(depth_mean, dtype=np.float64)
            depth_mean_std_value = np.std(depth_mean, dtype=np.float64)
            depth_std_mean_value = np.mean(depth_std, dtype=np.float64)
            depth_std_std_value = np.std(depth_std, dtype=np.float64)

            print ('Depth standard deviation value:')
            print (depth_std_std_value)
            out_hdu_std = pyfits.PrimaryHDU(data=[depth_mean, depth_std], header=hdr)
            tmp_base = os.path.basename(fits_list[l])
            tmp_ext = ''
            (tmp_name, tmp_ext) = os.path.splitext(tmp_base)
            try:
                out_hdu_std.writeto(os.path.join(os.path.abspath(work_path) + os.sep, 'mean-std-fits' + os.sep, tmp_name + '_mean_std.fits'))
            except IOError as ioex:
#                print 'errno: ', ioex.errno
                if (ioex.errno == 2):
                    try:
                        os.mkdir('mean-std-fits')
                        out_hdu_std.writeto(os.path.join(os.path.abspath(work_path) + os.sep, 'mean-std-fits' + os.sep + tmp_name + '_mean_std.fits'))
                    except:
                        print ('No directory could be created.')
                else:
                    print ('Files already exist.')
            if (image_type == 'Phi Image'):
                tmp_phi_depth = depth_mean[0:2047, 0:511]
                image_phi_depth_1_mean_mean = np.mean(tmp_phi_depth, dtype=np.float64)
                image_phi_depth_1_mean_std = np.std(tmp_phi_depth, dtype=np.float64)
                tmp_phi_depth = depth_std[0:2047, 0:511]
                image_phi_depth_1_std_mean = np.mean(tmp_phi_depth, dtype=np.float64)
                image_phi_depth_1_std_std = np.std(tmp_phi_depth, dtype=np.float64)
                tmp_phi_depth = depth_mean[0:2047, 512:1023]
                image_phi_depth_2_mean_mean = np.mean(tmp_phi_depth, dtype=np.float64)
                image_phi_depth_2_mean_std = np.std(tmp_phi_depth, dtype=np.float64)
                tmp_phi_depth = depth_std[0:2047, 512:1023]
                image_phi_depth_2_std_mean = np.mean(tmp_phi_depth, dtype=np.float64)
                image_phi_depth_2_std_std = np.std(tmp_phi_depth, dtype=np.float64)
                tmp_phi_depth = depth_mean[0:2047, 1024:1535]
                image_phi_depth_3_mean_mean = np.mean(tmp_phi_depth, dtype=np.float64)
                image_phi_depth_3_mean_std = np.std(tmp_phi_depth, dtype=np.float64)
                tmp_phi_depth = depth_std[0:2047, 1024:1535]
                image_phi_depth_3_std_mean = np.mean(tmp_phi_depth, dtype=np.float64)
                image_phi_depth_3_std_std = np.std(tmp_phi_depth, dtype=np.float64)
                tmp_phi_depth = depth_mean[0:2047, 1536:2047]
                image_phi_depth_4_mean_mean = np.mean(tmp_phi_depth, dtype=np.float64)
                image_phi_depth_4_mean_std = np.std(tmp_phi_depth, dtype=np.float64)
                tmp_phi_depth = depth_std[0:2047, 1536:2047]
                image_phi_depth_4_std_mean = np.mean(tmp_phi_depth, dtype=np.float64)
                image_phi_depth_4_std_std = np.std(tmp_phi_depth, dtype=np.float64)
            else:
                [image_phi_depth_1_mean_mean, image_phi_depth_1_mean_std, image_phi_depth_1_std_mean, image_phi_depth_1_std_std, image_phi_depth_2_mean_mean, image_phi_depth_2_mean_std, image_phi_depth_2_std_mean, image_phi_depth_2_std_std, image_phi_depth_3_mean_mean, image_phi_depth_3_mean_std, image_phi_depth_3_std_mean, image_phi_depth_3_std_std, image_phi_depth_4_mean_mean, image_phi_depth_4_mean_std, image_phi_depth_4_std_mean, image_phi_depth_4_std_std] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

            image_var_depth = [depth_mean_mean_value, depth_mean_std_value, depth_std_mean_value, depth_std_std_value, image_phi_depth_1_mean_mean, image_phi_depth_1_mean_std, image_phi_depth_1_std_mean, image_phi_depth_1_std_std, image_phi_depth_2_mean_mean, image_phi_depth_2_mean_std, image_phi_depth_2_std_mean, image_phi_depth_2_std_std, image_phi_depth_3_mean_mean, image_phi_depth_3_mean_std, image_phi_depth_3_std_mean, image_phi_depth_3_std_std, image_phi_depth_4_mean_mean, image_phi_depth_4_mean_std, image_phi_depth_4_std_mean, image_phi_depth_4_std_std, 0, tmp_name, num_of_frames]
            
            for i in range(len(var_names)):
                place = var_names[i]
                local_class_pointer = local_dict[place]
                local_x_name = local_dict[place].controls[0]
                local_y_name = local_dict[place].controls[2]
                local_x_format = local_dict[place].controls[1]
                local_y_format = local_dict[place].controls[3]
                if (local_x_name.lower().startswith('han_depth_') or local_y_name.lower().startswith('han_depth_')):
                    if (local_dict[place].attributes[5] == 'all'):
                        decidedAppendant(local_class_pointer, image_var_depth, local_x_name, local_y_name, local_x_format, local_y_format, current_frame, fits_list[l], hdr)
                    if (local_dict[place].attributes[5] == 'metis' and image_type == 'metis::Image'):
                        decidedAppendant(local_class_pointer, image_var_depth, local_x_name, local_y_name, local_x_format, local_y_format, current_frame, fits_list[l], hdr)
                    if (local_dict[place].attributes[5] == 'raise' and image_type == 'raise::Image'):
                        decidedAppendant(local_class_pointer, image_var_depth, local_x_name, local_y_name, local_x_format, local_y_format, current_frame, fits_list[l], hdr)
                    if (local_dict[place].attributes[5] == 'phi' and image_type == 'Phi Image'):
                        decidedAppendant(local_class_pointer, image_var_depth, local_x_name, local_y_name, local_x_format, local_y_format, current_frame, fits_list[l], hdr)
                    if (local_dict[place].attributes[5] == 'star1000' and image_type == 'star1000::Image'):
                        decidedAppendant(local_class_pointer, image_var_depth, local_x_name, local_y_name, local_x_format, local_y_format, current_frame, fits_list[l], hdr)
                    if (local_dict[place].attributes[5] == 'default' and image_type == 'default::Image'):
                        decidedAppendant(local_class_pointer, image_var_depth, local_x_name, local_y_name, local_x_format, local_y_format, current_frame, fits_list[l], hdr)

# gain analysis
        if gain_analysis:
            depth_mean = depth_image/(len(list(range(num_of_frames))))

            for current_frame in range(num_of_frames):
                tmp_depth_image = image[current_frame]
                depth_tmp = tmp_depth_image - depth_mean
                depth_tmp = np.square(depth_tmp)
                depth_std = depth_std + depth_tmp

            depth_std = depth_std/(len(list(range(num_of_frames))) -1)
            depth_std = np.sqrt(depth_std)
            depth_mean_mean_value = np.mean(depth_mean, dtype=np.float64)
            depth_mean_std_value = np.std(depth_mean, dtype=np.float64)
            depth_std_mean_value = np.mean(depth_std, dtype=np.float64)
            depth_std_std_value = np.std(depth_std, dtype=np.float64)

            print ('Depth standard deviation value:')
            print (depth_std_std_value)
            out_hdu_std = pyfits.PrimaryHDU(data=[depth_mean, depth_std], header=hdr)
            tmp_base = os.path.basename(fits_list[l])
            tmp_ext = ''
            (tmp_name, tmp_ext) = os.path.splitext(tmp_base)
            try:
                out_hdu_std.writeto(os.path.join(os.path.abspath(work_path) + os.sep, 'mean-std-fits' + os.sep, tmp_name + '_mean_std.fits'))
            except IOError as ioex:
#                print 'errno: ', ioex.errno
                if (ioex.errno == 2):
                    try:
                        os.mkdir('mean-std-fits')
                        out_hdu_std.writeto(os.path.join(os.path.abspath(work_path) + os.sep, 'mean-std-fits' + os.sep + tmp_name + '_mean_std.fits'))
                    except:
                        print ('No directory could be created.')
                else:
                    print ('Files already exist.')
            if (image_type == 'Phi Image'):
                tmp_phi_depth = depth_mean[0:2047, 0:511]
                image_phi_depth_1_mean_mean = np.mean(tmp_phi_depth, dtype=np.float64)
                image_phi_depth_1_mean_std = np.std(tmp_phi_depth, dtype=np.float64)
                tmp_phi_depth = depth_std[0:2047, 0:511]
                image_phi_depth_1_std_mean = np.mean(tmp_phi_depth, dtype=np.float64)
                image_phi_depth_1_std_std = np.std(tmp_phi_depth, dtype=np.float64)
                tmp_phi_depth = depth_mean[0:2047, 512:1023]
                image_phi_depth_2_mean_mean = np.mean(tmp_phi_depth, dtype=np.float64)
                image_phi_depth_2_mean_std = np.std(tmp_phi_depth, dtype=np.float64)
                tmp_phi_depth = depth_std[0:2047, 512:1023]
                image_phi_depth_2_std_mean = np.mean(tmp_phi_depth, dtype=np.float64)
                image_phi_depth_2_std_std = np.std(tmp_phi_depth, dtype=np.float64)
                tmp_phi_depth = depth_mean[0:2047, 1024:1535]
                image_phi_depth_3_mean_mean = np.mean(tmp_phi_depth, dtype=np.float64)
                image_phi_depth_3_mean_std = np.std(tmp_phi_depth, dtype=np.float64)
                tmp_phi_depth = depth_std[0:2047, 1024:1535]
                image_phi_depth_3_std_mean = np.mean(tmp_phi_depth, dtype=np.float64)
                image_phi_depth_3_std_std = np.std(tmp_phi_depth, dtype=np.float64)
                tmp_phi_depth = depth_mean[0:2047, 1536:2047]
                image_phi_depth_4_mean_mean = np.mean(tmp_phi_depth, dtype=np.float64)
                image_phi_depth_4_mean_std = np.std(tmp_phi_depth, dtype=np.float64)
                tmp_phi_depth = depth_std[0:2047, 1536:2047]
                image_phi_depth_4_std_mean = np.mean(tmp_phi_depth, dtype=np.float64)
                image_phi_depth_4_std_std = np.std(tmp_phi_depth, dtype=np.float64)
            else:
                [image_phi_depth_1_mean_mean, image_phi_depth_1_mean_std, image_phi_depth_1_std_mean, image_phi_depth_1_std_std, image_phi_depth_2_mean_mean, image_phi_depth_2_mean_std, image_phi_depth_2_std_mean, image_phi_depth_2_std_std, image_phi_depth_3_mean_mean, image_phi_depth_3_mean_std, image_phi_depth_3_std_mean, image_phi_depth_3_std_std, image_phi_depth_4_mean_mean, image_phi_depth_4_mean_std, image_phi_depth_4_std_mean, image_phi_depth_4_std_std] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

            image_var_depth = [depth_mean_mean_value, depth_mean_std_value, depth_std_mean_value, depth_std_std_value, image_phi_depth_1_mean_mean, image_phi_depth_1_mean_std, image_phi_depth_1_std_mean, image_phi_depth_1_std_std, image_phi_depth_2_mean_mean, image_phi_depth_2_mean_std, image_phi_depth_2_std_mean, image_phi_depth_2_std_std, image_phi_depth_3_mean_mean, image_phi_depth_3_mean_std, image_phi_depth_3_std_mean, image_phi_depth_3_std_std, image_phi_depth_4_mean_mean, image_phi_depth_4_mean_std, image_phi_depth_4_std_mean, image_phi_depth_4_std_std, 0, tmp_name, num_of_frames]
            
            for i in range(len(var_names)):
                place = var_names[i]
                local_class_pointer = local_dict[place]
                local_x_name = local_dict[place].controls[0]
                local_y_name = local_dict[place].controls[2]
                local_x_format = local_dict[place].controls[1]
                local_y_format = local_dict[place].controls[3]
                if (local_x_name.lower().startswith('han_depth_') or local_y_name.lower().startswith('han_depth_')):
                    if (local_dict[place].attributes[5] == 'all'):
                        decidedAppendant(local_class_pointer, image_var_depth, local_x_name, local_y_name, local_x_format, local_y_format, current_frame, fits_list[l], hdr)
                    if (local_dict[place].attributes[5] == 'metis' and image_type == 'metis::Image'):
                        decidedAppendant(local_class_pointer, image_var_depth, local_x_name, local_y_name, local_x_format, local_y_format, current_frame, fits_list[l], hdr)
                    if (local_dict[place].attributes[5] == 'raise' and image_type == 'raise::Image'):
                        decidedAppendant(local_class_pointer, image_var_depth, local_x_name, local_y_name, local_x_format, local_y_format, current_frame, fits_list[l], hdr)
                    if (local_dict[place].attributes[5] == 'phi' and image_type == 'Phi Image'):
                        decidedAppendant(local_class_pointer, image_var_depth, local_x_name, local_y_name, local_x_format, local_y_format, current_frame, fits_list[l], hdr)
                    if (local_dict[place].attributes[5] == 'star1000' and image_type == 'star1000::Image'):
                        decidedAppendant(local_class_pointer, image_var_depth, local_x_name, local_y_name, local_x_format, local_y_format, current_frame, fits_list[l], hdr)
                    if (local_dict[place].attributes[5] == 'default' and image_type == 'default::Image'):
                        decidedAppendant(local_class_pointer, image_var_depth, local_x_name, local_y_name, local_x_format, local_y_format, current_frame, fits_list[l], hdr)

# Evaluation
    with open(lookup_path + 'combz.csv', readfile) as g:
        reder = csv.reader(g, delimiter = ';')
        t = 0
        for row in reder:
            if (t == 0):
                try:
                    print (('Initialising: ' + row[0]))
                    fitstest = combz.CombZ(row[1].strip(), row[6].strip(), row[2].strip().lower() , row[3].strip().lower() ,  row[4].strip().lower() ,  row[5].strip().lower() )
                    local_dict[ row[0] ] = fitstest
                    combz_names.append(row[0].strip())
                    if ( len(row) == 8 ):
                        local_dict[row[0]].header.append(row[7])
                except:
                    print (('Error in look-up input stream at position ' + row[0] + '\r\nPlease check whether an input information is missing and if the delimiter is of the right kind.'))
            if (t == 1):
                for j in range(len(row)):
                    number_of_combz = len(combz_names)-1
                    place = combz_names[number_of_combz]
                    tmp_place = row[j].split()
                    tmp_test = ''
                    tmp_test = tmp_place[0]
                    if (details == True):
                        print (('Adding: ' + tmp_test))
                    local_dict[place].appendArraysOfValues(local_dict[tmp_test])
                t = t-2
            t = t+1
    for i in range(len(var_names)):
        place = var_names[i]
        if (details == True):
            print (('Next variable:' + var_names[i]))
        if local_dict[place].controls[4] == 'plot':
            try:
                local_dict[place].plot(work_path, 'nomean', grafic_format, colours, local_dict[place].attributes[0], 2, 2, 15)
            except:
                print (('Problems with plotting ' + var_names[i]))
        if local_dict[place].controls[4] == 'plot-mean':
            try:
                local_dict[place].plot(work_path, 'mean', grafic_format, colours, local_dict[place].attributes[0], 2, 2, 15)
            except:
                print (('Problems with plotting ' + var_names[i]))
        if local_dict[place].controls[4] == 'simple-plot':
            try:
                local_dict[place].simplePlot()
            except:
                print (('Problems with plotting ' + var_names[i]))
        if local_dict[place].controls[5] == 'report':
            if local_dict[place].controls[4] == 'plot-mean':
                try:
                    local_dict[place].report(work_path, 'mean', grafic_format)
                except:
                    print (('Problems with report at ' + var_names[i]))
            else:
                try:
                    local_dict[place].report(work_path, 'nomean', grafic_format)
                except:
                    print (('Problems with report at ' + var_names[i]))
        if local_dict[place].controls[6] == 'tex':
            try:
                destination = open((work_path + local_dict[place].attributes[0] + '.tex'), writefile)
                local_dict[place].exportLatex(destination)
            except:
                print (('Problems with LaTex tabular at ' + var_names[i]))
        if local_dict[place].controls[7] == 'stat':
            try:
                destination = open((work_path + local_dict[place].attributes[0] + '.txt'), writefile)
                local_dict[place].writeHeader(destination, src_path, work_path, lookup_path, local_dict[place].attributes[0] + '.txt', version)
            except:
                print (('Problems with writing header at ' + var_names[i]))
        if local_dict[place].controls[7] == 'stat':
            try:
                destination = open((work_path + local_dict[place].attributes[0] + '.txt'), appendfile)
                local_dict[place].statistics(destination)
            except:
                print (('Problems with writing the statistics at ' + var_names[i]))
    for i in range(len(combz_names)):
        place = combz_names[i]
        if local_dict[place].controls[0] == 'plot':
            try:
                local_dict[place].plot(work_path, 'nomean', grafic_format, colours, local_dict[place].attributes[0], 2, 2, 15)
            except:
                print (('Problems with plotting ' + combz_names[i]))
        if local_dict[place].controls[0] == 'plot-mean':
            try:
                local_dict[place].plot(work_path, 'mean', grafic_format, colours, local_dict[place].attributes[0], 2, 2, 15)
            except:
                print (('Problems with plotting ' + combz_names[i]))
        if local_dict[place].controls[1] == 'report':
            if local_dict[place].controls[0] == 'plot-mean':
                #try:
                    local_dict[place].report(work_path, 'mean', grafic_format)
                #except:
                #    print (('Problems with report at ' + combz_names[i]))
            else:
                #try:
                    local_dict[place].report(work_path, 'nomean', grafic_format)
                #except:
                #    print (('Problems with report at ' + combz_names[i]))
        if local_dict[place].controls[2] == 'tex':
            try:
                destination = open((work_path +  local_dict[place].attributes[0] + '.tex'), writefile)
                local_dict[place].exportLatex(destination)
            except:
                print (('Problems with LaTex tabular at ' + combz_names[i]))
        if local_dict[place].controls[3] == 'stat':
            try:
                destination = open((work_path + local_dict[place].attributes[0] + '.txt'), writefile)
                local_dict[place].writeHeader(destination, src_path, work_path, lookup_path, local_dict[place].attributes[0] + '.txt', version)
            except:
                print (('Problems with writing header at ' + combz_names[i]))
        if local_dict[place].controls[3] == 'stat':
            try:
                destination = open((work_path + local_dict[place].attributes[0] + '.txt'), appendfile)
                local_dict[place].statistics(destination)
            except:
                print (('Problems with writing the statistics at ' + combz_names[i]))
    return 0



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ------------------------------------------------------------------------------
# Main Function
# ------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def main(argv):
    '''Define all variables that are needed for the rest of the analysis. These might be handled in the future in a gui. Please do not apply of different image types. This won't lead to an error, but the data may not be valid. '''
    version = '1.15'
    src_path = ''
    work_path = ''
    lookup_path = ''
    grafic_format = 'png'
    details = False
    recursive = False
    search_source = True
    wait_search = False
    depth_analysis = False
    frame_analysis = False
    gain_analysis = False
    colours=['r*-','g<-','m+-','k>-','bo-','y*-','c*-','b<-','r>-','k<-','g<-','m<-','y<-','c>-','bo-','ro-']
    try:
        for i in range(len(argv)):
            if (search_source == True):
                if (os.path.isdir(argv[i]) == True):
                    if (wait_search == True): 
                        wait_search = False
                    else:
                        src_path = argv[i]
                        search_source = False
            if (argv[i] == '-r') or (argv[i] == '--recursive'):
                recursive = True
            if (argv[i] == '--depth') or (argv[i] == '-D'):
                depth_analysis = True
            if (argv[i] == '--frame') or (argv[i] == '-F'):
                frame_analysis = True
            if (argv[i] == '--gain') or (argv[i] == '-G'):
                gain_analysis = True
            if (argv[i] == '-f') or (argv[i] == '--format'):
                try:
                    grafic_format = argv[i+1]
                    if (grafic_format == 'jpg'):
                        print ('jpg format has been choosen.')
                    elif (grafic_format == 'jpeg'):
                        print ('jpg format has been choosen.')
                    elif (grafic_format == 'eps'):
                        print ('eps format has been choosen.')
                    elif (grafic_format == 'png'):
                        print ('png format has been choosen.')
                    else:
                        print ('A not known grafic format has been choosen. Thus is has been reset to the default format png.')
                        grafic_format = 'png'
                except:
                    print ('Error: Grafic format is not correct or not given. Thus the default format png is choosen.')
                    grafic_format = 'png'
            if (argv[i] == '--details'):
                details = True
            if (argv[i] == '-o') or (argv[i] == '--output'):
                try:
                    work_path = argv[i+1]
                    if (os.path.isdir(work_path) == True):
                        #print (('Working directory is: ' + work_path))
                        wait_search = True
                    else:
                        print ('Error: Working path does not exist.')
                        return False
                except:
                    print ('Error: No Working directory.')
                    # return False OR work_path = src_path
            if (argv[i] == '-l') or (argv[i] == '--lookup'):
                try:
                    lookup_path = argv[i+1]
                    if (os.path.isdir(lookup_path) == True):
                        #print (('Look-up directory is: ' + lookup_path))
                        wait_search = True
                    else:
                        print ('Error: Look-up path does not exist.')
                        return False
                except:
                    print ('Error: Look-up directory was not assigned correctly.')
            if (argv[i] == '--help'):
                printHelp(version)
                return False
            if (argv[i] == '--assignment'):
                printAllingment()
                return False
    except:
        print ('han_solo: Missing operands.')
        print ('Try: \'han_solo --help \' for more information.')
        return False

    if (bool(src_path) == False):
        print ('Source path not found.')
        return False
    if (bool(work_path) == False): # An empty string is False, if len(work_path) == 0
        work_path = src_path
    src_path = os.path.normpath(os.path.abspath(src_path)) + os.sep
    if (bool(lookup_path) == False): # An empty string is False, if len(lookup_path) == 0
        lookup_path = src_path + 'lookup/'
    work_path = os.path.normpath(os.path.abspath(work_path)) + os.sep
    lookup_path = os.path.normpath(os.path.abspath(lookup_path)) + os.sep
    os.chdir(work_path)
    print ('Recursive:')
    print (recursive)
    print ('Grafic format:')
    print (grafic_format)
    print ('Details ?:')
    print (details)
    printHanSolo()
    print (('The source directory is:  ' + src_path))
    print (('The working directory is: ' + work_path))
    print (('The look-up directory is: ' + lookup_path))
    fits_list = getFileList(src_path, recursive, 'fits')
    fits_list = removeFilesFromList(fits_list, '_mean_std', 'fits')
    startAnalysis(src_path, work_path, lookup_path, version, fits_list, grafic_format, depth_analysis, frame_analysis, gain_analysis, colours, details)
    return 0

if __name__ == '__main__':
    main(sys.argv)
