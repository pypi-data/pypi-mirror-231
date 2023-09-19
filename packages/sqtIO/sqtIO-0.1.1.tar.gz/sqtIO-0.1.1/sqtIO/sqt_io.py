#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 11:50:53 2023

@author: prashanthciryam
"""

import pandas as pd
import re
from copy import deepcopy

class SQTObject(list):
    def as_df(self):
        prots = [protein.as_df() for protein in self]
        sqt_df = pd.concat(prots,ignore_index=True)
        return sqt_df
    def as_unique_df(self):
        uniques = [proteinGroup.unique().as_df() for proteinGroup in self]
        sqt_df = pd.concat(uniques,ignore_index = True)
        return sqt_df    

class SQTProteinGroupObject(object):
    def __init__(self,accessions,metadata,peptides):
        self.accessions=accessions
        self.metadata=metadata
        self.peptides=peptides
    def unique(self):
        uniqPeps = deepcopy(self.peptides)
        newProt = deepcopy(self)
        uniqPeps = uniqPeps[uniqPeps['Unique']=='*']
        newProt.peptides = uniqPeps
        return newProt
    def as_df(self):
        name = '; '.join(self.accessions)
        df = deepcopy(self.peptides)
        df['Name'] = name
        return df
    def extractNSAF(proteinList):
        tupList = []
        for protein in proteinList:
            acc = protein.accessions
            nsaf = protein.metadata['NSAF'].astype(float).tolist()
            tempList = list(zip(acc,nsaf))
            tupList+=tempList
        return dict(tupList)
    
class HeaderSizeMismatchError(Exception):
    "Raise error when header sizes don't match properly"
    pass

def read_sqt(fN):
    with open(fN) as f:
        f = f.read()
    f = f.split('\n\n')[1].split('Proteins')[0].splitlines()
    data = [d.split('\t') for d in f][:-1]
    h1,h2 = data[0],data[1]
    data = data[2:]
    indList = []
    for d in data:
        if len(d)==len(h1):
            indList.append('x')
        elif len(d)==len(h2):
            indList.append('y')
        else:
            raise HeaderSizeMismatchError
    inds = ''.join(indList)
    headers = [m.span() for m in re.finditer('x+',inds)]
    entries = [m.span() for m in re.finditer('y+',inds)]
    extractDict = dict(zip(headers,entries))
    proteinList = SQTObject()
    for key,val in extractDict.items():
        hstart,hend = key
        heads = data[hstart:hend]
        accs = [h[0] for h in heads]
        metadata = pd.DataFrame(heads,columns=h1)
        dstart,dend = val
        ds = data[dstart:dend]
        df = pd.DataFrame(ds,columns=h2)
        protein = SQTProteinGroupObject(accs, metadata, df)
        proteinList.append(protein)
    return proteinList
def getNSAF(proteinList):
    tupList = []
    for protein in proteinList:
        acc = protein.accessions
        nsaf = protein.metadata['NSAF'].astype(float).tolist()
        tempList = list(zip(acc,nsaf))
        tupList+=tempList
    return dict(tupList)
def SQTtoDF(proteinList):
    prots = [protein.as_df() for protein in proteinList]
    sqt_df = pd.concat(prots,ignore_index=True)
    return sqt_df
def custom_match(x):
    pattern = r'^(?!.*Reverse)(?!.*sp\|)(?!.*tr\|)(?:(?=.*fshiftMinus)(?!.*fshiftPlus)|(?=.*fshiftPlus)(?!.*fshiftMinus))'

    return bool(re.search(pattern, x))
def onlyShifts(df):
    mask = df['Name'].apply(custom_match)
    filtered = df[mask]
    cols = ['Name','Sequence','XCorr','DeltCN','Conf%','PPM','Unique']
    filtered = filtered[cols]
    return filtered