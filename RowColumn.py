'''
Program:        RowColumn.py - Giving back a graph of the Row and Column values. Calculating the minimum, maximum, average and median. 
Institut:       Max-Planck-Institut fuer Sonnensystemforschung
Adress:         Justus-von-Liebig-Weg 3, 37077 Goettingen, Germany
Author:         Julian Utehs
Maintainer:     Julian Utehs
E-mail:         utehs@mps.mpg.de

Description:    This program provides graphes for analysing the rows and columns. 

Copyricht:      Copyright (c) <2014> <Max-Planck-Institute for solar system research> 

Licence:        All right reserved. Copying, modifying or using this software requires the permission by the institute director. For further information please contact the Max-Planck-Institute for solar system research administration. 
                The above copyright notice and the eventually given permission notice shall be included in all copies or substantial portions of the Software. 

Warranty:       THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 

Version:        0.01 - Kick off
Date:           2015, 23. March

Version:        0.02 - Corrected issues with the image_x and image_y, if not more then two arguments are given. Has to be checked again. 
Date:           2015, 23. March
'''

import pyfits
import numpy as np
import pylab as py
import os
import sys as sys
import matplotlib.pyplot as mplpyplot


def plotRowColumn(src_file, frame_number, dst_path, row_or_column, title, y_min, y_max, y_ave, y_med, x_label, y_label, ending, colour, linewidth, markersize, fontsize):
        '''  '''
        tmp_base = os.path.basename(src_file)
        tmp_ext = ''
        (tmp_name, tmp_ext) = os.path.splitext(tmp_base)
        
        fig = mplpyplot.figure()
        p = []
        names = []
        
        p.append(mplpyplot.plot(range(len(y_min)), y_min, colour[0], label = 'Minimum', linewidth = linewidth, markersize=markersize))
        names.append('Minimum')
        
        p.append(mplpyplot.plot(range(len(y_max)), y_max, colour[1], label = 'Maximum', linewidth = linewidth, markersize=markersize))
        names.append('Maximum')
        
        p.append(mplpyplot.plot(range(len(y_ave)), y_ave, colour[2], label = 'Average', linewidth = linewidth, markersize=markersize))
        names.append('Average')
        
        p.append(mplpyplot.plot(range(len(y_med)), y_med, colour[3], label = 'Median', linewidth = linewidth, markersize=markersize))
        names.append('Median')
        
        mplpyplot.legend(names, loc='best')

        fig.suptitle(title, fontsize=fontsize)
        mplpyplot.xlabel(x_label + ' in [DN]', fontsize=fontsize)
        mplpyplot.ylabel(y_label + ' in [DN]', fontsize=fontsize)
        try:
            fig.savefig(os.path.join(os.path.abspath(dst_path) + os.sep, 'row-column' + os.sep, tmp_name + '_' + row_or_column + '_frame_' + str(frame_number) + '.' + ending), dpi = 400)
        except IOError as ioex:
            if (ioex.errno == 2):
                try:
                    os.mkdir('row-column')
                    fig.savefig(os.path.join(os.path.abspath(dst_path) + os.sep, 'row-column' + os.sep, tmp_name + '_' + row_or_column + '_frame_' + str(frame_number) + '.' + ending), dpi = 400)
                except:
                    print ('No directory could be created.')
            else:
                print ('Files already exist.')
        mplpyplot.close()
        return True


def getFileList(src_path, recursive, file_ext):
    '''Returns file list based on the source directory. The file extension and a recursive search can be choosen. Gives back the absolut path of the files.'''
    file_list = []    
    try:
        local_file_list = os.walk(src_path) # Get all elements of the path and his child directories
    except IOError as (errno, strerror):
        print 'Error can\'t find Directory: ' , src_path # Error handling
    for (path, dirs, files) in local_file_list: # For all elements, if it is a file with the ending file_ext, append it to the file_list
        if len(files) > 0:
            for f in files:
                g = f.lower()
                if (g.endswith('.' + file_ext) == True):
                    file_list.append(os.path.normpath(path + os.sep +f)) # Added path due to problems with the recursive function, file_list.append(os.path.join(os.path.abspath(path) + os.sep, f)) # os.path.dirname(path) ? Which version is better?
        if (recursive != True): # If recursive is not true, break out of the for-loop --> only the first iteration is pass through
            break
    file_list.sort()
    return file_list # absolut path


def printHelp(version):
    print ('Help for RowColumn.py. ')
    return 0


def startAnalysis(fits_list, dst_path):
    
    print (fits_list)
    print (dst_path)
    
    colours=['b*-','r<-','m+-','g>-','ko-','y*-','c*-','b<-','r>-','k<-','g<-','m<-','y<-','c>-','bo-','ro-']

    
    for l in range(len(fits_list)):
        print (('\r\n' + 'The following image is analysed: ' + fits_list[l]))
        hdulist  = pyfits.open(fits_list[l])
        image    = hdulist[0].data
        hdr      = hdulist[0].header
        
        if (len(image.shape) == 3):
            num_of_frames = len(image)
        else:
            num_of_frames = 1
        
        image_dimension = image.shape
        print ('Image Dimension:')
        print (image_dimension)
        
        
        for current_frame in range(num_of_frames):
            if (num_of_frames > 1):
                tmp_image = image[current_frame]
            else:
                tmp_image = image
#            print (tmp_image)
            
            image_size = tmp_image.shape
            print image_size
            if (len(image_size) == 3):
                image_x = image_size[2]
                image_y = image_size[1]
            else:
                image_x = image_size[0]
                image_y = image_size[1]
            print ('Number of Rows:')
            print (image_x)
            print ('Number of Columns:')
            print (image_y)
### Rows
            tmp_row_min = np.zeros((image_x))
            tmp_row_max = np.zeros((image_x))
            tmp_row_ave = np.zeros((image_x))
            tmp_row_med = np.zeros((image_x))
#            print tmp_row_min
            for i in range(image_x):
                print (image_y)
                print (image_x)
                print i
                tmp_row = tmp_image[0, i, 0:image_y]
                tmp_row_min[i] = np.min(tmp_row)
#                print ('Minimum:')
#                print tmp_row_min[i]
                tmp_row_max[i] = np.max(tmp_row)
#                print ('Maximum:')
#                print tmp_row_max[i]
                tmp_row_ave[i] = np.mean(tmp_row)
#                print ('Average:')
#                print tmp_row_ave[i]
                tmp_row_med[i] = np.median(tmp_row)
#            print (tmp_row)
            #print (tmp_row_min)
            #print (tmp_row_max)
            #print (tmp_row_ave)
            #print (tmp_row_med)
            plotRowColumn(fits_list[l], current_frame, dst_path, 'row', 'Rows', tmp_row_min, tmp_row_max, tmp_row_ave, tmp_row_med, 'Row Number', 'Value', 'png', colours,  1, 1, 15)
            
### Column
            tmp_column_min = np.zeros((image_y))
            tmp_column_max = np.zeros((image_y))
            tmp_column_ave = np.zeros((image_y))
            tmp_column_med = np.zeros((image_y))
            for i in range(image_y):
                tmp_column = tmp_image[0:image_x, i]
                tmp_column_min[i] = np.min(tmp_column)
#                print ('Minimum:')
#                print tmp_column_min[i]
                tmp_column_max[i] = np.max(tmp_column)
#                print ('Maximum:')
#                print tmp_column_max[i]
                tmp_column_ave[i] = np.mean(tmp_column)
#                print ('Average:')
#                print tmp_column_ave[i]
                tmp_column_med[i] = np.median(tmp_column)
#            print (tmp_column)
            #print (tmp_column_min)
            #print (tmp_column_max)
            #print (tmp_column_ave)
            #print (tmp_column_med)
            plotRowColumn(fits_list[l], current_frame, dst_path, 'column', 'Columns', tmp_column_min, tmp_column_max, tmp_column_ave, tmp_column_med, 'Column Number', 'Value', 'png', colours,  1, 1, 15)
    return 0



def main(argv): 
    src_path = ''#'/home/utehs/Documents/programming/rowcolumn/Spielwiese/'
    dst_path = ''
    search_source = True
    recursive = False
    version = '0.02'
    try:
        for i in range(len(argv)):
            if (search_source == True):
                if (os.path.isdir(argv[i]) == True) and (i>0):
                    src_path = argv[i]
                    search_source = False
            if (argv[i] == '-r') or (argv[i] == '--recursive'): # Add recursive support in future releases
                recursive = True
            if (argv[i] == '-o') or (argv[i] == '--output'):
                search_source = False
                try:
                    dst_path = argv[i+1]
                    if (os.path.isdir(dst_path) == True):
                        print 'All FFT files will be written to directory: ' + dst_path
                    else: 
                        print 'Error: Destination path is not a directory.'
                        return False
                except: 
                    print 'Error: Something went wront with the destination path.'
            if (argv[i] == '--help'):
                printHelp(version)
                return False
    except: 
        print 'RowColumn: Missing operands.'
        print 'Try: \'python RowColumn.py --help \' for more information.'
        return False
#    print src_file
    if (src_path):
        file_list = getFileList(src_path, recursive, 'fits')
    print file_list
    if not (dst_path):
        dst_path = src_path
    os.chdir(dst_path)
    startAnalysis(file_list, dst_path)
    return True
    
if (__name__ == '__main__'):
    bool_return = main(sys.argv)
    if (bool_return):
        print 'Script finished correctly.'
