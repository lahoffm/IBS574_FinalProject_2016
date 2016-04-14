# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 12:10:56 2016
Written for IBS 574 Bioinformatics and Computational Biology final project - 
promoter regions in songbird Area X specialized genes versus promoter regions
in the same genes in mammalian vocal learning and nonlearning species

@author: Lukas Hoffmann
"""

from genelists import GeneLists # should be in same folder
from TFBindingSiteList import TFBindingSiteList

printOutput = True

# Which Area-X specialized genes are in each paper and combination of papers
gl = GeneLists(); # list of Area X specialized genes in three papers: see comments in genelists.py
pfenningWhitney = list(set(gl.pfenning) & set(gl.whitney))
pfenningZhang = list(set(gl.pfenning) & set(gl.zhang))
whitneyZhang = list(set(gl.whitney) & set (gl.zhang))
all3 = list(set(gl.pfenning) & set(gl.whitney) & set(gl.zhang))

if printOutput:
    print(gl.pfenning) # specialized in Area X and human basal ganglia
    print(gl.whitney) # specialized in Area X and singing-related
    print(gl.zhang) # specialized in Area X and accelerated evolution in vocal learning songbirds
    print(len(gl.pfenning))
    print(len(gl.whitney))
    print(len(gl.zhang))
    print(pfenningWhitney)
    print(pfenningZhang)
    print(whitneyZhang)
    print(all3)

# Get list of transcription factors that could bind to upstream promoter sequences
# of the genes CDH4 and MGLL identified in the analysis printed out above
# (from Consite: see comments in TFBindingSiteList.py)
tmp = TFBindingSiteList('cdh4_TFbindsites_human.txt')
cdh4_human = tmp.tfset
tmp = TFBindingSiteList('cdh4_TFbindsites_chimpanzee.txt')
cdh4_chimpanzee = tmp.tfset
tmp = TFBindingSiteList('cdh4_TFbindsites_zebrafinch.txt')
cdh4_zebrafinch = tmp.tfset
tmp = TFBindingSiteList('cdh4_TFbindsites_manakin.txt')
cdh4_manakin = tmp.tfset
tmp = TFBindingSiteList('mgll_TFbindsites_human.txt')
mgll_human = tmp.tfset
tmp = TFBindingSiteList('mgll_TFbindsites_chimpanzee.txt')
mgll_chimpanzee = tmp.tfset
tmp = TFBindingSiteList('mgll_TFbindsites_zebrafinch.txt')
mgll_zebrafinch = tmp.tfset
tmp = TFBindingSiteList('mgll_TFbindsites_manakin.txt')
mgll_manakin = tmp.tfset


if printOutput:
    print('-'*100 + '\n' + '-'*100 + '\n' + '-'*100)
    print(cdh4_human)
    print(cdh4_chimpanzee)
    print(cdh4_zebrafinch)
    print(cdh4_manakin)
    print(mgll_human)
    print(mgll_chimpanzee)
    print(mgll_zebrafinch)
    print(mgll_manakin)
    print('-'*100 + '\n' + '-'*100 + '\n' + '-'*100)

    print('CDH4, shared by vocal learners:')
    cdh4_sharedVL = cdh4_zebrafinch & cdh4_human
    print(sorted(cdh4_sharedVL, key=str.lower))
    print('CDH4, shared by vocal learners but not shared with chimpanzees:')
    # The resulting set has elements of the left-hand set with all elements from the right-hand set removed.
    # An element will be in the result if it is in the left-hand set and not in the right-hand set.
    print(sorted(cdh4_sharedVL - cdh4_chimpanzee, key=str.lower))
    print('CDH4, shared by vocal learners but not shared with non-learners:')    
    print(sorted((cdh4_sharedVL - cdh4_chimpanzee) - cdh4_manakin, key=str.lower))

    print('MGLL, shared by vocal learners:')
    mgll_sharedVL = mgll_zebrafinch & mgll_human
    print(sorted(mgll_sharedVL, key=str.lower)) 
    print('MGLL, shared by vocal learners but not shared with chimpanzees:')
    print(sorted(mgll_sharedVL - mgll_chimpanzee, key=str.lower))
    print('MGLL, shared by vocal learners but not shared with non-learners:')    
    print(sorted((mgll_sharedVL - mgll_chimpanzee) - mgll_manakin, key=str.lower))