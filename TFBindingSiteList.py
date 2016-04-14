# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 16:25:42 2016
Written for IBS 574 Bioinformatics and Computational Biology final project

@author: Lukas Hoffmann
"""

# Import data from a ConSite output table of putative transcription factor binding sites.
# ConSite: http://consite.genereg.net
# ConSite uses the JASPAR database.

class TFBindingSiteList(object):
    # Filename: Consite output table of putative transcription factor binding sites.
    #
    # Since Consite is web-only I had to copy each table into a textfile and
    # make sure it had the same format as described below
    #
    # File format: each line has info for one matched transcription factor binding site
    # Fields are separated by whitespace (possibly multiple tabs and spaces)
    # Field 1: Transcription factor name (from JASPAR database)
    # Field 2: Sequence that matched to transcription factor
    # Field 3: From (start location)
    # Field 4: To (stop location)
    # Field 5: Score (computed using Position Weight Matrix - unfortunately not the relative score)
    # Field 6: Strand (most TFs can be effective binding to either strand so accept all matches)
    
    def __init__(self, filename):
        self.filename = filename
        with open(self.filename) as f:
            dat = f.readlines()            
        dat = [line.rstrip('\r\n') for line in dat] # strip trailing newlines
        dat = [line.split() for line in dat] # parse each entry into columns
        
        # Check for 6 entries
        datlen = [len(line) for line in dat if len(line) != 6]
        if len(datlen) > 0:
            raise IndexError('At least one line in ' + filename + ' does not have 6 entries')     

        # Not necessary to convert to upper case because ConSite always uses the same JASPAR lists
        # But if comparing to transcription factors from other data sources, that may be necessary
        self.tf =       [line[0] for line in dat]
        self.sequence = [line[1] for line in dat]
        self.from_ =    [line[2] for line in dat]
        self.to =       [line[3] for line in dat]
        self.score =    [line[4] for line in dat]
        self.strand =   [line[5] for line in dat]
        
        self.tfset = set(self.tf) # unique TF names