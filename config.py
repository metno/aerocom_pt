# general config module
# All configuration constants are here
#
# The file is divided in the sub sections 
# - general		(general)
# - reading		(read)
# - plotting	(plot)
# - statistics	(stat)
# - writing		(write)
###############################################################
#Parameter for monthly means
#the key is used for the file naming, the value denotes the months used to calculate
import numpy as np



###############################################################
# Plot config start
StatParam={}
StatParam['monthly']={}
StatParam['monthly']['mALLYEARmonthly']=np.arange(1,13)
StatParam['monthly']['m01monthly']=1
StatParam['monthly']['m02monthly']=2
StatParam['monthly']['m03monthly']=3
StatParam['monthly']['m04monthly']=4
StatParam['monthly']['m05monthly']=5
StatParam['monthly']['m06monthly']=6
StatParam['monthly']['m07monthly']=7
StatParam['monthly']['m08monthly']=8
StatParam['monthly']['m09monthly']=9
StatParam['monthly']['m10monthly']=10
StatParam['monthly']['m11monthly']=11
StatParam['monthly']['m12monthly']=12
StatParam['monthly']['mDJFmonthly']=[12,1,2]
StatParam['monthly']['mMAMmonthly']=[3,4,5]
StatParam['monthly']['mJJAmonthly']=[6,7,8]
StatParam['monthly']['mSONmonthly']=[9,10,11]

StatParam['daily']={}
StatParam['daily']['mALLYEARdaily']=np.arange(1,13)
StatParam['daily']['m01daily']=1
StatParam['daily']['m02daily']=2
StatParam['daily']['m03daily']=3
StatParam['daily']['m04daily']=4
StatParam['daily']['m05daily']=5
StatParam['daily']['m06daily']=6
StatParam['daily']['m07daily']=7
StatParam['daily']['m08daily']=8
StatParam['daily']['m09daily']=9
StatParam['daily']['m10daily']=10
StatParam['daily']['m11daily']=11
StatParam['daily']['m12daily']=12
StatParam['daily']['mDJFdaily']=[12,1,2]
StatParam['daily']['mMAMdaily']=[3,4,5]
StatParam['daily']['mJJAdaily']=[6,7,8]
StatParam['daily']['mSONdaily']=[9,10,11]

# plot config end
###############################################################


###############################################################
# stat config start
#GCOS requirements
fC_GCOSPercentCrit=np.float(0.1)
fC_GCOSAbsCrit=np.float(0.04)
# stat config end
###############################################################

###############################################################
# read config start

#obs reading information

#cC_ObsNetworkDataDir[iC_ObsNet_AeronetSunOrig]=OBSNETWORK_DATADIR_PREFIX+'aerocom1/AEROCOM_OBSDATA/AeronetSunNRT/data/'
#cC_ObsNetworkDataDir[iC_ObsNet_AeronetSunRaw20]=OBSNETWORK_DATADIR_PREFIX+'aerocom1/AEROCOM_OBSDATA/AeronetRaw2.0/renamed/'
#cC_ObsNetworkDataDir[iC_ObsNet_AeronetSunRaw15]=OBSNETWORK_DATADIR_PREFIX+'aerocom1/AEROCOM_OBSDATA/AeronetRaw1.5/renamed/'
#cC_ObsNetworkDataDir[iC_ObsNet_Aethalometer]=OBSNETWORK_DATADIR_PREFIX+'aerocom1/AEROCOM_OBSDATA/aethalometer/'
#cC_ObsNetworkDataDir[iC_ObsNet_EBASNRT]=OBSNETWORK_DATADIR_PREFIX+'aerocom1/AEROCOM_OBSDATA/EBAS_NRT/'
#cC_ObsNetworkDataDir[iC_ObsNet_AeronetSun20AllPoints]=OBSNETWORK_DATADIR_PREFIX+'aerocom1/AEROCOM_OBSDATA/AeronetSun2.0AllPoints/renamed/'
#cC_ObsNetworkDataDir[iC_ObsNet_EBASMultiColumn]=OBSNETWORK_DATADIR_PREFIX+'aerocom1/AEROCOM_OBSDATA/EBASMultiColumn/'
#;cC_ObsNetworkDataDir[iC_ObsNet_WOUDCOzoneSonds]='/fou/emep/People/semeena/Measurements/Sondes/NOAA/'
#cC_ObsNetworkDataDir[iC_ObsNet_WOUDCOzoneSonds]=OBSNETWORK_DATADIR_PREFIX+'aerocom1/AEROCOM_OBSDATA/NDACC.Ozone.Sondes/'
#cC_ObsNetworkDataDir[iC_ObsNet_AeronetSunSDADaily]=$
   #OBSNETWORK_DATADIR_PREFIX+'aerocom1/AEROCOM_OBSDATA/AeronetSun2.0.SDA.daily/renamed/'

#names of the different obs networks
OBSNET_NONE='NONE'
NOMODELNAME='OBSERVATIONS-ONLY'

#names of the different obs networks
AERONETSUN20NAME='AERONETSun2.0'
AERONETSDA20NAME='AERONETSDA2.0'
AERONETSUNAPNAME='AeronetSun_2.0_AP'
EBASMULTICOLUMNNAME='EBASMC'
AERONNETSUN20NRTNAME='AeronetSun_2.0_NRT'
EEANAME='EEAAQeRep'


#obs data paths
OBSNETWORK_DATADIR_PREFIX='/lustre/storeA/project/aerocom/'
CONFIG_OBSDATAPATHS={}
CONFIG_OBSDATAPATHS[AERONETSUN20NAME]=OBSNETWORK_DATADIR_PREFIX+'aerocom1/AEROCOM_OBSDATA/AeronetRaw2.0/renamed/'
CONFIG_OBSDATAPATHS[AERONETSDA20NAME]=OBSNETWORK_DATADIR_PREFIX+'aerocom1/AEROCOM_OBSDATA/AeronetSun2.0.SDA.daily/renamed/'
CONFIG_OBSDATAPATHS[EBASMULTICOLUMNNAME]=OBSNETWORK_DATADIR_PREFIX+''
CONFIG_OBSDATAPATHS[AERONNETSUN20NRTNAME]=OBSNETWORK_DATADIR_PREFIX+''
CONFIG_OBSDATAPATHS[EEANAME]=OBSNETWORK_DATADIR_PREFIX+'aerocom1/AEROCOM_OBSDATA/EEA_AQeRep.testing/renamed/'

#model data paths
CONFIG_MODELDATAPTHS={}
OBSNETWORK_DATADIR_PREFIX='/lustre/storeA/project/aerocom/'



dict_ObsNetworkParam={}
dict_ObsNetworkParam[AERONETSDA20NAME]={}
dict_ObsNetworkParam[AERONETSDA20NAME]['DataDir']=(
	''.join([OBSNETWORK_DATADIR_PREFIX, 'aerocom1/AEROCOM_OBSDATA/AeronetSun2.0.SDA.daily/renamed/']))
dict_ObsNetworkParam[AERONETSDA20NAME]['cC_ObsNetworkName']=('Obs: AeronetSDA 2.0 daily')
dict_ObsNetworkParam[AERONETSDA20NAME]['Revision']='20160312'

dict_ObsNetworkParam[AERONETSUN20NAME]={}
dict_ObsNetworkParam[AERONETSUN20NAME]['DataDir']=(
	''.join([OBSNETWORK_DATADIR_PREFIX, 'aerocom1/AEROCOM_OBSDATA/AeronetRaw2.0/renamed/']))
dict_ObsNetworkParam[AERONETSUN20NAME]['cC_ObsNetworkName']=('Obs: AeronetSun 2.0')
dict_ObsNetworkParam[AERONETSUN20NAME]['Revision']='20151121'

dict_ObsNetworkParam[AERONETSUNAPNAME]={}
dict_ObsNetworkParam[EBASMULTICOLUMNNAME]={}
dict_ObsNetworkParam[AERONNETSUN20NRTNAME]={}
dict_ObsNetworkParam[EEANAME]={}
#dict_ObsNetworkParam[EEANAME]['DataDir']=(
	#''.join([OBSNETWORK_DATADIR_PREFIX, 'aerocom1/AEROCOM_OBSDATA/EEA_AQeRep/renamed/']))
dict_ObsNetworkParam[EEANAME]['DataDir']=(
	''.join([OBSNETWORK_DATADIR_PREFIX, 'aerocom1/AEROCOM_OBSDATA/EEA_AQeRep.testing/renamed/']))
dict_ObsNetworkParam[EEANAME]['cC_ObsNetworkName']=('Obs: Airbase')
dict_ObsNetworkParam[EEANAME]['Revision']='201601'
#dict_ObsNetworkParam['']={}

cC_ModelDirs=[]
#for testing of MFDataset since the original data is netcdf4
#cC_ModelDirs.append('/lustre/storeB/project/aerocom/user_data/jang/')
cC_ModelDirs.append(''.join([OBSNETWORK_DATADIR_PREFIX,'htap/ECMWF/']))
cC_ModelDirs.append(''.join([OBSNETWORK_DATADIR_PREFIX,'aerocom1/']))
cC_ModelDirs.append(''.join([OBSNETWORK_DATADIR_PREFIX,'aerocom2/']))
cC_ModelDirs.append(''.join([OBSNETWORK_DATADIR_PREFIX,'aerocom1/ECLIPSE/']))
cC_ModelDirs.append(''.join([OBSNETWORK_DATADIR_PREFIX,'htap/CCI_AEROSOL_Phase1/']))
cC_ModelDirs.append(''.join([OBSNETWORK_DATADIR_PREFIX,'htap/CCI_AEROSOL_Phase2/']))
cC_ModelDirs.append(''.join([OBSNETWORK_DATADIR_PREFIX,'aerocom2/ACCMIP/']))
cC_ModelDirs.append(''.join([OBSNETWORK_DATADIR_PREFIX,'aerocom1/NorESM/']))
cC_ModelDirs.append(''.join([OBSNETWORK_DATADIR_PREFIX,'aerocom2/EMEP_COPERNICUS/']))
cC_ModelDirs.append(''.join([OBSNETWORK_DATADIR_PREFIX,'aerocom2/EMEP/']))
cC_ModelDirs.append(''.join([OBSNETWORK_DATADIR_PREFIX,'aerocom2/EMEP_GLOBAL/']))
cC_ModelDirs.append(''.join([OBSNETWORK_DATADIR_PREFIX,'aerocom2/EMEP_SVN_TEST/']))
cC_ModelDirs.append(''.join([OBSNETWORK_DATADIR_PREFIX,'aerocom2/NorESM_SVN_TEST/']))
cC_ModelDirs.append(''.join([OBSNETWORK_DATADIR_PREFIX,'aerocom2/INCA/']))
cC_ModelDirs.append(''.join([OBSNETWORK_DATADIR_PREFIX,'htap/HTAP-PHASE-I/']))
cC_ModelDirs.append(''.join([OBSNETWORK_DATADIR_PREFIX,'htap/HTAP-PHASE-II/']))
cC_ModelDirs.append(''.join([OBSNETWORK_DATADIR_PREFIX,'aerocom1/AEROCOM-PHASE-I/']))
cC_ModelDirs.append(''.join([OBSNETWORK_DATADIR_PREFIX,'aerocom1/AEROCOM-PHASE-II/']))
cC_ModelDirs.append(''.join([OBSNETWORK_DATADIR_PREFIX,'aerocom1/AEROCOM-PHASE-III/']))


# read config end
###############################################################

cC_StdDevExt='SIGMA'
#cC_ObsDataCacheDir='./cache/'
cC_ObsDataCacheDir='/lustre/storeA/users/jang/cache/'
cC_StdNameIniFile='./StdNames.ini'



