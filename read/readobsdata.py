#!/usr/bin/env python3

################################################################
# readoddata.py
#
# observational data reading class
#
# this file is part of the aerocom_pt package
#
#################################################################
# Created 20171024 by Jan Griesfeller for Met Norway
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
from aerocom_pt.read.read_aeronet_sdav2 import *
from aerocom_pt.read.read_aeronet_sunv2 import *
import aerocom_pt.config as const


class ReadObsData(ReadAeronetSDAV2,ReadAeronetSunV2):
	"""aerocom_pt observation data reading class
	"""

	SUPPORTED_DATASETS = [const.AERONETSDA20NAME, const.AERONETSUN20NAME]
	SDA_TEST_FILE='/lustre/storeA/project/aerocom/aerocom1/AEROCOM_OBSDATA/AeronetSun2.0.SDA.daily/renamed/920801_160312_Zvenigorod.ONEILL_20'
	SUN_TEST_FILE='/lustre/storeA/project/aerocom/aerocom1/AEROCOM_OBSDATA/AeronetRaw2.0/renamed/920801_170401_Zambezi.lev20'
	#
	DATASET_IDX_AERONETSDA2_0 = 0
	DATASET_IDX_AERONETSUN2_0 = 1

	def __init__(self, DataSetsToRead, VerboseFlag=False):
		if isinstance( DataSetsToRead, list):
			self.DataSetsToRead =  DataSetsToRead
		else:
			self.DataSetsToRead = [DataSetsToRead]

		self.VerboseFlag = VerboseFlag
		self.data = {}
		self.index = len(self.data)
		self.FILEMASKS = []
		self.__version__ = 0.01
		self.DATASETNAMES = []
		self.SuperClasses = {}
		self.infiles = []
		#now init the needed superclasses
		#pdb.set_trace()

		for DataSetToRead in self.DataSetsToRead:
			#skip unknown data sets
			#pdb.set_trace()
			if DataSetToRead == ReadObsData.SUPPORTED_DATASETS[ReadObsData.DATASET_IDX_AERONETSDA2_0]:
				#AeronetSDAV2
				Dummy = ReadAeronetSDAV2(VerboseFlag = VerboseFlag)	

			elif DataSetToRead == ReadObsData.SUPPORTED_DATASETS[ReadObsData.DATASET_IDX_AERONETSUN2_0]:
				#Aeronet direct sun V2
				Dummy = ReadAeronetSunV2(VerboseFlag = VerboseFlag)

			else:
				continue

			self.DATASETNAMES.append(Dummy.DATASET_NAME)
			self.FILEMASKS.append(Dummy.FILEMASK)
			self.SuperClasses[DataSetToRead] = Dummy


	def __iter__(self):
		return self

	def __next__(self):
		if self.index == 0:
			raise StopIteration
		self.index = self.index - 1
		return self.data[self.index]

	def __repr__(self):
		Out=[]
		for dataset in self.data:
			Out.append(dataset+':')
			for stationid in self.data[dataset]:
				Out.append(stationid)

		return '\n'.join(Out)



	###################################################################################


	def ReadDaily(self):
		"""Read observations"""

		for DataSetToRead in self.DataSetsToRead:
			self.SuperClasses[DataSetToRead].ReadDaily()
			self.data[DataSetToRead] = self.SuperClasses[DataSetToRead].data




###################################################################################



