# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 14:36:22 2016
Written for IBS 574 Bioinformatics and Computational Biology final project
@author: Lukas Hoffmann
"""

# For this analysis, in all 3 papers we want only those genes differentially
# expressed / associated with Area X specifically and not any other song nucleus

class GeneLists(object):
    def __init__(self):     
        # From Pfenning et al. 2014 Figure S7 and Table S3C.
        # They found 78 genes specialized in Area X versus surrounding striatum and 
        # also specialized in human basal ganglia versus externtal.
        # 3 of those were found to be false positives with IHC so there's only 75 in this
        # list. Some of these 75 may be false positives because
        # they didn't check every gene with IHC.
        self.pfenning = list(set([
            'NPTX2',
            'GDA',
            'NOV',
            'PGM2L1',
            'NRSN1',
            'ANKFN1',
            'CACNG3',
            'C1orf187',
            'DOK6',
            'KIAA2022',
            'NOL4',
            'HPCAL4',
            'PCDH8',
            'CDH4',
            'RPRML',
            'ODZ3',
            'TIAM1',
            'CHSY3',
            'ZNF831',
            'SYNPR',
            'NTS',
            'IVNS1ABP',
            'ANLN',
            'TMCC3',
            'MGLL',
            'CA2',
            'PLCL1',
            'CDKN2C',
            'PLP1',
            'GLTP',
            'NKX6-2',
            'REEP3',
            'PAQR8',
            'HOMER3',
            'CDH7',
            'HMOX1',
            'TMBIM1',
            'ST18',
            'INIP',
            'SLC6A1',
            'AGFG1',
            'GLDN',
            'APOD',
            'MBP',
            'CEBPD',
            'INPP5A',
            'PVALB',
            'PDE10A',
            'EFHD1',
            'SEMA7A',
            'CPLX1',
            'ATP2A2',
            'C1orf95',
            'EMP2',
            'ABHD5',
            'GSTZ1',
            'USP31',
            'SLC16A6',
            'BCHE',
            'C14orf37',
            'WDR85',
            'DRD2',
            'PPP2R2B',
            'PI16',
            'CAMTA1',
            'RCAN2',
            'SLC6A9',
            'SLC6A6',
            'VAMP1',
            'SV2B',
            'GREM1',
            'RGS12',
            'ABTB2',
            'RBMS1',
            'GALNT1']))
    
        
        # From Whitney et al. 2014, Table S8
        # 1162 genes in Area X that were regulated by singing in Fig. 4B
        # Of those, select only the 861 that were selectively regulated in Area X and cut ones without a gene symbol
        # TO GET THIS TO WORK I HAD TO SAVE IT AS A TAB-DELIMINTED TEXT FILE OTHERWISE I GOT ERRORS
        filename = 'Papers\Supplementary Table S8 - Singing Regulated Transcripts v53.txt'
        with open(filename) as f:
            dat = f.readlines()            
        dat = dat[3:-1] # strip headings and last line
        dat = [line.rstrip('\r\n') for line in dat] # strip trailing newlines
        dat = [line.split('\t') for line in dat] # parse each entry into columns
        
        # Extract gene symbols in the Area X cluster but not the HVC, LMAN or RA clusters
        # Note this extracts the 861 genes from Figure 4B, not the 433
        # "strict region enhanced cluster" genes from Figure S12
        dat = [col[1] for col in dat if col[9] != 'NA' and col[10] == 'NA' and col[11] == 'NA' and col[12] == 'NA']
        dat = [g for g in dat if g] # some transcripts didn't have gene symbols, cut those    
        self.whitney = list(set(dat))
 
        # From Zhang et al. 2014, Table S28
        # 227 genes that had convergent accelerated evolution (high dN/dS ratio) 
        #   in vocal learning songbird species
        # Of those, select only the 165 that were expressed in songbird brain.
        # Of those, select only the 151 that were expressed in the song nuclei.
        # Of those, select only those that were either (a) differentially expressed 
        #   in Area X relative to other song nuclei, or (b) specialized in Area X compared
        #   to surrounding areas
        filename = 'Papers\Zhang-Table_S28.txt'
        with open(filename) as f:
            dat = f.readlines()     

        dat = dat[2:] # strip headings
        dat = [line.rstrip('\r\n') for line in dat] # strip trailing newlines
        dat = [line.split('\t') for line in dat] # parse each entry into columns

        # Extract gene symbols that had Area X listed AS THE ONLY NUCLEUS
        # in "Differential expression among song nuclei" (only want X-specific
        # genes) or AS ONE OF THE NUCLEI in "Specialized in song nuclei compared 
        # to surrounding areas" (matches Pfenning et al.'s genes that are differentially
        # expressed in Area X versus surrounding striatum)
        dat = [col[0] for col in dat if (col[9]=='Area X down' or col[9]=='Area X up')
            or ('Area X' in col[10])]
        self.zhangS28 = list(set(dat))
        
        # From Zhang et al. 2014, Table S31
        # "38 [genes] had one to two amino acid substitutions present only in vocal learners"
        # Of those, select only those that were differentially expressed in Area X relative to other
        #   song nuclei
        self.zhangS31 = [
            'C12ORF35',
            'CHGB',
            'KIAA1919',
            'PIK3R4',
            'SACS',
            'TSEN2']
            
        # From Zhang et al. 2014, Table S34
        # "accelerated evolution [among vocal learning songbird species] in noncoding 
        # sequences" --> 332 elements were associated with 278 genes
        # Of those, select only the 198 of which were expressed in song nuclei
        # Of those, select only "Area X specialized genes"
        filename = 'Papers\Zhang-Table_S34.txt'
        with open(filename) as f:
            dat = f.readlines()     
        dat = dat[4:-1] # strip headings
        dat = [line.rstrip('\r\n') for line in dat] # strip trailing newlines
        dat = [line.split('\t') for line in dat] # parse each entry into columns
        
        # Extract gene symbols that only had "Area X specialized", not
        # "RA specialized" or "HVC specialized" or "RA specialized birds and 
        # human LMC". Table S34 did not have LMAN data.
        dat = [col[10] for col in dat if col[14]=='' and col[15]=='+' and col[16]=='']
        self.zhangS34 = list(set(dat))

        # Some genes were written in lowercase
        self.pfenning = [g.upper() for g in self.pfenning]
        self.whitney =  [g.upper() for g in self.whitney]
        self.zhangS28 = [g.upper() for g in self.zhangS28]
        self.zhangS31 = [g.upper() for g in self.zhangS31]
        self.zhangS34 = [g.upper() for g in self.zhangS34]
        self.zhang = list(set(self.zhangS28 + self.zhangS31 + self.zhangS34))
