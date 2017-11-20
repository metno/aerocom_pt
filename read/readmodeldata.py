#!/usr/bin/env python3

################################################################
# readmodeldata.py
#
# model data reading class
#
# this file is part of the aerocom_pt package
#
#################################################################
# Created 20171030 by Jan Griesfeller for Met Norway
#
# Last changed: See git log
#################################################################

#Copyright (C) 2017 met.no
#Contact information:
#Norwegian Meteorological Institute
#Box 43 Blindern
#0313 OSLO
#NORWAY
#E-mail: jan.griesfeller@met.no
#This program is free software; you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation; either version 3 of the License, or
#(at your option) any later version.
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#GNU General Public License for more details.
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#MA 02110-1301, USA


import pdb
import os
import glob
from collections import OrderedDict
import sys
import numpy as np
from datetime import datetime
import pandas as pd
import re
import aerocom_pt.config as const
import iris


class ReadModelData():
    """aerocom_pt model data reading class
    """
    MODELDIRS = const.MODELDIRS

    __version__ = 0.01
    _TESTFILE = "/lustre/storeA/project/aerocom/aerocom-users-database/CCI-Aerosol/CCI_AEROSOL_Phase2/AATSR_SU_v4.3/renamed/aerocom.AATSR_SU_v4.3.daily.od550aer.2008.nc"

    def __init__(self, ModelNamesToRead, StartTime, EndTime, VerboseFlag = False):

        self.data = {}
        if isinstance(ModelNamesToRead, dict):
            #dictionary
            for ModelName in ModelNamesToRead:
                self.data[ModelName] = {}
        elif isinstance(ModelNamesToRead, list):
            #list
            for ModelName in ModelNamesToRead:
                self.data[ModelName] = {}
        else:
            self.data[ ModelNamesToRead] = {}

        self.ModelNamesToread = ModelNamesToRead
        self.VerboseFlag = VerboseFlag
        self.StartTime = StartTime  #start time as datetime
        self.EndTime = EndTime      #end time as datetime
        self.FILEMASKS = []
        self.__version__ = 0.01
        self.MODELDIRS = const.MODELDIRS    #directories to search for a model directory
        self.ModelDir = {}  #save the location in there

        #Fill self.ModelDir
        ReadModelData.GetModelDir(self)

    ###################################################################################


    def FindModelFiles(self):
        """
        method to find model files

        :param self:
        :return:
        """
    ###################################################################################


    def __repr__(self):
        Out=[]
        for dataset in self.data:
            Out.append(dataset+':')
            for stationid in self.data[dataset]:
                Out.append(stationid)

        return '\n'.join(Out)



    ###################################################################################
    def GetModelDir(self):
        """method to get the directory the model data for a given model resides in"""

        # Return the model directory
        # and put that in self.ModelDir


        for ModelName in self.data:
            # loop through the list of models
            for FolderToSearchIn in self.MODELDIRS:
                if self.VerboseFlag:
                    print('Searching in: ', FolderToSearchIn)
                # get the directories
                if os.path.isdir(FolderToSearchIn):
                    dir = glob.glob(FolderToSearchIn + ModelName)
                    if len(dir) > 0:
                        self.ModelDir[ModelName] = dir[0]
                        if self.VerboseFlag:
                            print('Found: ', dir[0])
                            break
                    else:
                        continue
                else:
                    if self.VerboseFlag:
                        print('directory: ', FolderToSearchIn, ' does not exist')

    ###################################################################################
    def GetModelFiles(self):
        """method to find the model files"""

    ###################################################################################



    def ReadDaily(self):
        """Read daily model"""

        for model in self.ModelNamesToread:
            ModelDir = self.ModelDir[model]


###################################################################################



