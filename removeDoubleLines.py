'''
Program:        removeDoubleLines.py - Remove double empty lines in the given document, saves it as nameOfFile_R in the same folder.
Institut:       Max-Planck-Institut fuer Sonnensystemforschung
Adress:         Justus-von-Liebig-Weg 3, 37077 Goettingen, Germany
Author:         Julian Utehs
Maintainer:     Julian Utehs
E-mail:         utehs@mps.mpg.de

Description:    This program takes a document and removes the double empty lines. 

Copyricht:      Copyright (c) <2014> <Max-Planck-Institute for solar system research> 

Licence:        This software is licenced under the General Puplic Licence version 3 or later. For the original text see https://www.gnu.org/licenses/gpl.html or contact the program author. 
                The above copyright notice and the eventually given permission notice shall be included in all copies or substantial portions of the Software. 

Warranty:       THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 

Version:        0.01 - Kick off
Date:           2015, 08. April
'''

import os
import sys as sys
import string as string


def removingDoubleLines(src_file):
    src = open(src_file, "r")
    (path, ext) = os.path.splitext(src_file)
    dst = open(path + "_R" + ext, "w")
    for line in src:
        if not line.strip(): continue
        dst.write(line)
    return 0


def main(argv): 
    version = '0.01'
    try:
        for i in range(len(argv)):
            if (os.path.isfile(argv[i])) and (i >= 1):
                src_file   = argv[i]
    except: 
        print 'removeDoubleLines: Missing operands.'
    removingDoubleLines(src_file)
    return True
    
if (__name__ == '__main__'):
    bool_return = main(sys.argv)
    if not (bool_return):
        print 'Script did not finished correctly.'
