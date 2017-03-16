# ----------------------------------------------------------------------------------------------------
# Class Definition
# ----------------------------------------------------------------------------------------------------
# Version:      2.00.00
# Last Change:  28. November 2016

import numpy as np
import os as os
import matplotlib.pyplot as mplpyplot
import time as time
import csv as csv
import sys as sys
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT, TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, inch
from reportlab.lib import colors
import xvsy as xvsy
#import combz as combz
import pandas as pd
        
class CombZ(): 
    '''Class of the list z, which is the third dimension for the class XvsY. Definition of the plot and report function.'''
    def __init__(self, glob_name, infoheader, bool_plot, bool_report, bool_tex, bool_stat): 
        '''Initializes the CombZ class. Ist contains an array of XvsY class elements. No other elements should be inserted (high crash possibility for internal functions). There is also a header array [not used yet].'''
        self.z = [] 
        self.header = [infoheader]
        self.attributes = [glob_name]
        self.controls = [bool_plot, bool_report, bool_tex, bool_stat]
        
    def appendArraysOfValues(self, DataPairOfXvsYClass):
        '''Please do only insert data in the format of XvsY class. '''
        self.z.append(DataPairOfXvsYClass)
        
    def simplePlot(self, cls_fontsize):
        '''Simple plot opens a plot in order to have a look on the calculated data during runtime.'''
        fig = mplpyplot.figure()
        for l in range(len(self.z)):
            try: # Tries whether the given data is of integer or float type. Strings can not be plotted. 
                mplpyplot.plot(self.z[l].x, self.z[l].y)
            except ValueError:
                return False
        fig.suptitle(self.z[0].attributes[0])
        mplpyplot.xlabel(self.z[0].attributes[1])
        mplpyplot.ylabel(self.z[0].attributes[2])
        mplpyplot.show()
        mplpyplot.close()
        return True
        
    def plot(self, cls_work_path, cls_mean, cls_ending, cls_colour, cls_label, cls_linewidth, cls_markersize, cls_fontsize):
        ''' The meanPlot function writes .png-pictures into the work directory. At the same x-positions the mean of the y-values is taken. The class attributes are used to appoint the plot. '''
        fig = mplpyplot.figure()
        sequence = []
        x_local = []
        y_local = []
        names = []
        p = []
        for l in range(len(self.z)): # Do everything for all entries of the self.z[] array.
            for i in range(len(self.z[l].x)): # Builds a list to use the sort() function
                sequence.append((self.z[l].x[i], self.z[l].y[i]))
            sequence.sort()
            if (cls_mean == 'mean'):
                sequence_mean = []
                ymean = []
                for i in range(len(sequence)-1): # Calculates the mean values of the entries
                    (xf,yf) = sequence[i]
                    (xs,ys) = sequence[i+1]
                    if (xf != xs):
                        ymean.append(float(yf))
                        sequence_mean.append((xf, np.mean(ymean)))
                        ymean = []
                    else: 
                        ymean.append(float(yf))
                        if (i == (len(sequence)-2)): 
                            ymean.append(float(ys))
                            sequence_mean.append((xs, np.mean(ymean)))
                for i in range(len(sequence_mean)): # Writes back the sorted mean values. 
                    (xm,ym)= sequence_mean[i]
                    x_local.append(xm)
                    y_local.append(ym)
            else: 
                for i in range(len(sequence)): # Writes back the sorted values. 
                    (xm,ym)= sequence[i]
                    x_local.append(xm)
                    y_local.append(ym)
            try: # Tries whether the given data is of integer or float type. Strings can not be plotted. 
                p.append(mplpyplot.plot(x_local, y_local, cls_colour[l], label = cls_label, linewidth = cls_linewidth, markersize=cls_markersize))
                names.append(self.z[l].attributes[2])
            except ValueError:
                print ('Error in CombZ.plot() - function. Probably the class does not contain valid data (int or float). Please check this.')
                return False
            sequence = []
            x_local = []
            y_local = []
        mplpyplot.legend(names, loc='best')
        fig.suptitle(self.z[0].attributes[0], fontsize=cls_fontsize) # self.attributes[] will cause problems if not defined. 
        mplpyplot.xlabel(self.z[0].attributes[1] + ' in ' + self.z[0].attributes[3], fontsize=cls_fontsize)
        mplpyplot.ylabel(self.z[0].attributes[2] + ' in ' + self.z[0].attributes[4], fontsize=cls_fontsize)
        if (cls_mean == 'mean'):
            print  (('Printing: ' + cls_work_path + self.z[0].attributes[0] + '_mean_array.' + cls_ending))
            fig.savefig(cls_work_path + self.z[0].attributes[0]+ '_mean' + '_array.' + cls_ending, dpi = 300)
        else:
            print  (('Printing: ' + cls_work_path + self.z[0].attributes[0] + '_array.' + cls_ending))
            fig.savefig(cls_work_path + self.z[0].attributes[0]+ '_array.' + cls_ending, dpi = 300)
        mplpyplot.close()
        return True
        
    def report(self, cls_work_path, cls_mean, cls_ending): # ToDo
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
#        table_data = []
        stat_list = []
        try:
            stat_list.append("%40s" % 'Name: ')
            stat_list.append("%10s" % 'Frame: ')
            for l in range(len(self.z)): 
                stat_list.append("%10s" % self.z[l].attributes[2])
            stat_list = []
            stat_list.append("%40s" % '[String]')
            stat_list.append("%10s" % '[N]')
            for l in range(len(self.z)): 
                stat_list.append("%10s" % self.z[l].attributes[4])
            for l in range(len(self.z[0].y)):
                stat_list = []
                stat_list.append("%40s" % os.path.basename(self.z[0].src_name[l]))
                stat_list.append("%10d" % self.z[0].frame_num[l])
                for m in range(len(self.z)):
                    stat_list.append(self.z[m].y[l])

#            table_data.append(['Source File', 'Frame', self.z[0].attributes[1], self.attributes[2]]) # there a for loop is needed 
#            table_data.append(['', '', self.attributes[3], self.attributes[4]]) # Here as well
#        table_data = stat_list
        except:
            print ('Hier laueft was falsch...')
#        for i in range(len(self.src_name)):
#            table_data.append([os.path.basename(self.src_name[i]), self.frame_num[i], self.x[i], self.y[i]]) # can i write rows?
        try:
            t = Table(stat_list);
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
        except:
            print ('Problem I am searching for you.')
        try:
            if (self.controls[0] == 'plot-mean'):
                graph = os.path.join(cls_work_path + self.attributes[0] + '_mean.' + cls_ending) # Is this name used for the plot, please verify
                cls_image = im = Image(graph, width=16*cm, height=12*cm);
                report.append(cls_image)
            elif (self.controls[0] == 'plot'): 
                graph = os.path.join(cls_work_path + self.attributes[0] + '.' + cls_ending)
                cls_image = im = Image(graph, width=16*cm, height=12*cm);
                report.append(cls_image)
            else:
                pass
        except: 
            print ('No plot is used for the report.')
        doc.build(report)
        return True
        
    def exportLatex(self, dest_file):
        pass
        
    def statistics(self, f):
        csv_file = csv.writer(f, delimiter=";",  lineterminator='\r\n')#, newline='') Does not work on a linux machine with newline. Big big trouble here...
        stat_list = []
        stat_list.append("%40s" % 'Name: ')
        stat_list.append("%10s" % 'Frame: ')
        for l in range(len(self.z)): 
            stat_list.append("%10s" % self.z[l].attributes[2])
        csv_file.writerow(stat_list)
        stat_list = []
        stat_list.append("%40s" % '[String]')
        stat_list.append("%10s" % '[N]')
        for l in range(len(self.z)): 
            stat_list.append("%10s" % self.z[l].attributes[4])
        csv_file.writerow(stat_list)
        for l in range(len(self.z[0].y)):
            stat_list = []
            stat_list.append("%40s" % os.path.basename(self.z[0].src_name[l]))
            stat_list.append("%10d" % self.z[0].frame_num[l])
            for m in range(len(self.z)):
                stat_list.append(self.z[m].y[l])
            csv_file.writerow(stat_list)
        return True
        
    def writeHeader(self, f_obj, src_path, work_path, lookup_path, dest_file, cls_version):
        w_separator = '-------------------------------------------------'
        try: 
            f_obj.write(self.header[0])
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
            try: 
                f_obj.write('\r\n' + self.header[1] + '\r\n' * 2)
            except: 
                print (('No additional header information is given for ' + dest_file + '.'))
        except: 
            print (('Error: Printing header file ' + dest_file + ' was not possible.'))
        finally:
            print (('Writing header for ' + dest_file + ' succesfully finished.'))
            f_obj.close()
        return True
