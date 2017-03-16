# ----------------------------------------------------------------------------------------------------
# Class Definition
# ----------------------------------------------------------------------------------------------------
# Version:      2.00.01
# Last change:  28. November 2016

import numpy as np
import os as os
import matplotlib.pyplot as mplpyplot
import csv as csv
import time as time
import sys as sys
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT, TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, inch
from reportlab.lib import colors
#import xvsy as xvsy
#import combz as combz
import pandas as pd

class XvsY: 
    '''Class of two-dimensional data array. '''
    def __init__(self, glob_name, x_axis, y_axis, x_unit, y_unit, x_key_word, x_format, y_key_word, y_format, bool_plot, bool_report, bool_tex, bool_stat, im_type): 
        '''Initializes the class. Some attributes of the class have to be defined, since they are needed is several functions.'''
        self.x = []
        self.y = []
        self.frame_num = []
        self.src_name = []
        self.attributes = [glob_name, x_axis, y_axis, x_unit, y_unit, im_type]
        self.controls = [x_key_word, x_format, y_key_word, y_format, bool_plot, bool_report, bool_tex, bool_stat]
        
    def appendDuple(self, m, n, cls_frame_num, cls_src_name): 
        '''Appends an information duple to the class. The frame and the image number have to be added due to assignment.'''
        self.x.append(m)
        self.y.append(n)
        self.frame_num.append(cls_frame_num)
        self.src_name.append(cls_src_name) 
        
    def simplePlot(self):
        '''Simple plot opens a plot in order to have a look on the calculated data during runtime.'''
        fig = mplpyplot.figure()
        try: # Tries whether the given data is of integer or float type. Strings can not be plotted. 
            mplpyplot.plot(self.x, self.y)
        except ValueError:
            return False
        fig.suptitle(self.attributes[0])
        mplpyplot.xlabel(self.attributes[1])
        mplpyplot.ylabel(self.attributes[2])
        mplpyplot.show()
        mplpyplot.close()
        return True
        
    def plot(self, cls_work_path, cls_mean, cls_ending, cls_colour, cls_label, cls_linewidth, cls_markersize, cls_fontsize):
        ''' The meanPlot function writes .png-pictures into the work directory. At the same x-positions the mean of the y-values is taken. The class attributes are used to appoint the plot. '''
        sequence = []
        x_local = []
        y_local = []
        for l in range(len(self.x)): # Builds a list to use the sort() function
            sequence.append((self.x[l], self.y[l]))
        sequence.sort()
        sequence_mean = []
        ymean = []
        if (cls_mean == 'mean'):
            for i in range(len(sequence)-1): #-1 # Calculates the mean values of the entries
                (xf,yf) = sequence[i]
                (xs,ys) = sequence[i+1]
                if (xf != xs):
                    ymean.append(float(yf))
                    sequence_mean.append((xf, np.mean(ymean)))
                    ymean = []
                    if (i == (len(sequence)-2)): # Handling last case (recently -2)
                        ymean.append(float(ys))
                        sequence_mean.append((xs, np.mean(ymean)))
                else: 
                    ymean.append(float(yf))
                    if (i == (len(sequence)-2)): # Handling last case (recently -2)
                        ymean.append(float(ys))
                        sequence_mean.append((xs, np.mean(ymean)))
            for l in range(len(sequence_mean)): # Writes back the sorted mean values. 
                (xm,ym)= sequence_mean[l]
                x_local.append(xm)
                y_local.append(ym)
        else:
            for l in range(len(sequence)): # Writes back the sorted values. 
                (xm,ym)= sequence[l]
                x_local.append(xm)
                y_local.append(ym)
        fig = mplpyplot.figure()
        try: # Tries whether the given data is of integer or float type. Strings can not be plotted. 
            mplpyplot.plot(x_local, y_local, cls_colour[0], label = cls_label, linewidth = cls_linewidth, markersize=cls_markersize )
            mplpyplot.legend((self.attributes[2],), loc='best') #fig.legend(p, (self.attributes[2],), loc='upper right') # Added trailing comma due to the fact that legend needs a sequence of string 'string' - ['SequenceOfString'], ('SequenceOfString',). Its input should be a list, not a string on its own. loc='upper left' or 'lower center' are possible positions. 
        except ValueError: 
            return False
        fig.suptitle(self.attributes[0], fontsize=cls_fontsize) # self.attributes[] will cause problems if not defined. 
        mplpyplot.xlabel(self.attributes[1] + ' in ' + self.attributes[3], fontsize=cls_fontsize)
        mplpyplot.ylabel(self.attributes[2] + ' in ' + self.attributes[4], fontsize=cls_fontsize)
        if (cls_mean == 'mean'):
            print  (('Printing: ' + cls_work_path + self.attributes[0] + '_mean.' + cls_ending))
            fig.savefig( cls_work_path + self.attributes[0]+ '_mean' + '.' + cls_ending, dpi = 300)
        else: 
            print  (('Printing: ' + cls_work_path + self.attributes[0] + '.' + cls_ending))
            fig.savefig( cls_work_path + self.attributes[0]+ '.' + cls_ending, dpi = 300)
        mplpyplot.close()
        return True
        
    def report(self, cls_work_path, cls_mean, cls_ending):
        '''The report function writes a pdf-document into the working directory that contains all data and if already created the plot of the XvsY class.'''
        report_path = cls_work_path + self.attributes[0] + '_report.pdf'
        doc = SimpleDocTemplate(report_path, pagesize=A4, rightMargin=1*cm,leftMargin=1*cm, topMargin=2.5*cm,bottomMargin=2.5*cm)
        report = []
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='normal', alignment=TA_LEFT, fontname='Arial', leading=14))
        styles.add(ParagraphStyle(name='center', alignment=TA_CENTER, fontname='Arial', leading=14))
        spacer_large = 20
        spacer_small = 12
        title = 'Summary report for ' + self.attributes[0]
        ptext = '<font size=16>%s</font>' % title
        report.append(Paragraph(ptext, styles["center"]))
        report.append(Spacer(1, spacer_large))
        title = 'Table Data'
        ptext = '<font size=14>%s</font>' % title
        report.append(Paragraph(ptext, styles["normal"]))
        report.append(Spacer(1, spacer_large))
        table_data = []
        table_data.append(['Source File', 'Frame', self.attributes[1], self.attributes[2]])
        table_data.append(['', '', self.attributes[3], self.attributes[4]])
        for i in range(len(self.src_name)):
            table_data.append([os.path.basename(self.src_name[i]), self.frame_num[i], self.x[i], self.y[i]])
        t = Table(table_data);
        t.setStyle(TableStyle([('BACKGROUND',(0,0),(0,-1),colors.gray),
                       ('BACKGROUND',(0,0),(-1,0),colors.gray),
                       ('TEXTCOLOR',(0,0),(0,-1),colors.white),
                       ('ALIGN',(0,0),(-1,-1),'CENTER'),
                       ('ALIGN',(0,0),(0,-1),'LEFT'),
                       ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                       ('TEXTCOLOR',(1,0),(-1,0),colors.black),
                       ('TEXTCOLOR',(0,0),(-1,0),colors.white),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ]));
        report.append(t);
        report.append(PageBreak());
        try:
            if (cls_mean == 'mean'):
                graph = os.path.join(cls_work_path + self.attributes[0] + '_mean.' + cls_ending)
            else: 
                graph = os.path.join(cls_work_path + self.attributes[0] + '.' + cls_ending)
        except: 
            print ('No plot is used for the report.')
        cls_image = im = Image(graph, width=16*cm, height=12*cm);
        report.append(cls_image)
        doc.build(report)
        return True
    
    def exportLatex(self, dest_file): # Please revice this function to concentrate the code
        '''This function exports the data, which is stored in the XvsY class, into a LaTex table. This table is written into the given file.'''
        diverting = [self.x, self.y]
        diverting = np.transpose(diverting)
        output = pd.DataFrame(diverting)
        table = output.to_latex()
        dest_file.write(table)
        return True
        
    def statistics(self, dest_file): 
        '''This function appends a statistic to the given file f. The image file name is limited to 40 characters. '''
        csv_file = csv.writer(dest_file, delimiter=";",  lineterminator='\r\n')#, newline='') Does not function on a linux machine with newline!!! Big big trouble here...
        stat_list = []
        stat_list.append("%40s" % 'Name: ') # Writes Name, Frame and x-y-names
        stat_list.append("%10s" % 'Frame: ')
        stat_list.append("%10s" % self.attributes[1])
        stat_list.append("%10s" % self.attributes[2])
        csv_file.writerow(stat_list)
        stat_list = []
        stat_list.append("%40s" % '[String]') # Writes the units of Name, Frame and x-y-names
        stat_list.append("%10s" % '[N]')
        stat_list.append("%10s" % self.attributes[3])
        stat_list.append("%10s" % self.attributes[4])
        csv_file.writerow(stat_list)
        for l in range(len(self.x)): # Writes the data into the file
            stat_list = []
            stat_list.append("%40s" % os.path.basename(self.src_name[l]))
            stat_list.append("%10d" % self.frame_num[l])
            if isinstance(self.x[l], str): #basestring):
                stat_list.append(self.x[l])
            else:
                try:
                    stat_list.append("%10d" % self.x[l])
                except:
                    print ('Unknown data type in function xvsy.py --> statistics.')
            if isinstance(self.y[l], str): #basestring):
                stat_list.append(self.y[l])
            else:
                try:
                    stat_list.append("%10d" % self.y[l])
                except:
                    print ('Unknown data type in function xvsy.py --> statistics.')
            csv_file.writerow(stat_list)
        return True

    def writeHeader(f_obj, src_path, work_path, lookup_path, dest_file, cls_version):
        w_separator = '-------------------------------------------------'
        try: 
            f_obj.write('\r\n' + 
                    w_separator + '\r\n' * 2 + 
                    'This file was generated automatically providing calculated & gathered results by ' + '\r\n' + 
                    'Han SolO (han_solo_light_saber.py) with version: ' + cls_version + '\r\n' + 
                    'Date: ' +  time.strftime("%a %b %d  %H:%M:%S  %Y", time.gmtime()) + '\r\n' * 2 + 
                    'Source Directory: ' + src_path + '\r\n' + 
                    'Working Directory: ' + work_path + '\r\n' + 
                    'Lookup Directory: ' + lookup_path + '\r\n' * 3 + 
                    'Unit Glossary: ' + '\r\n' + 
                    w_separator + '\r\n' + 
                    '[String]     ==> arbitary Text String' + '\r\n' + 
                    '[yyyy-mm-dd] ==> Used date format: Year-Month-Day' + '\r\n' + 
                    '[hh:mm:ss]   ==> Used time format: Hour:Minute:Second' + '\r\n' + 
                    '[N]          ==> enumerate value' + '\r\n' + 
                    '[s]          ==> Time duration in Seconds' + '\r\n' + 
                    '[Boolean]    ==> Funktion set (1) or NOT set (0)' + '\r\n' + 
                    '[degC]       ==> Temperature in Degree Centigrade (degC)' + '\r\n' + 
                    '[DN]         ==> Digital Number read or calculated from adc' + '\r\n' + 
                    '[nm]         ==> used filter wavelength [10e-9m]' + '\r\n' * 2 + w_separator + '\r\n' * 2)
        except: 
            print (('Error: Printing header file ' + dest_file + ' was not possible.'))
        finally:
            print (('Writing header for ' + dest_file + ' succesfully finished.'))
            f_obj.close()
        return True

