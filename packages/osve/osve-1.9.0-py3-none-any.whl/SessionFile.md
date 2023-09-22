# OSVE Session File

## Introduction
The OSVE Session File is a text file in JSON format intended to specify to OSVE
the settings or paramaters to use during initialisation, simulation and
reporting steps.

## The Session File template explained

The following JSON object keywords are mandatory unless specified as [OPTIONAL].
Some keyword are marked as [NOT_USED], this just remarks that this keyword is not use by OSVE itself but is used for traceability purpouses.

```json
{
  "sessionConfiguration": {
      -- Main session object containing the specified OSVE settings.
    "sessionID": "pt-if-test-0002-minor-moons",
       -- [NOT_USED] String with the identifier for this OSVE execution.
    "version": "1.0.1",
       -- [NOT_USED] String with the Session object version, just to have control if any keyword is updated/removed.
    "source": {
       -- [OPTIONAL][NOT_USED] Object intended to define the source or the origin of the data used for this OSVE execution.
       "segmentation_info": {
         -- [OPTIONAL][NOT_USED] Object intended to define the source segmentation details.
        "plan_id": "",
          -- [OPTIONAL][NOT_USED] String with the identifier of the source segmentation plan being used.
        "mnemonic": "",
          -- [OPTIONAL][NOT_USED] String with the mnemonic of the source segmentation being used.
        "name": "",
          -- [OPTIONAL][NOT_USED] String with the name of the source segmentation being used.
        "description": "",
          -- [OPTIONAL][NOT_USED] String with the description of the source segmentation being used.
       },
       "trajectory_info": {
         -- [OPTIONAL][NOT_USED] Object intended to define the source trajectory details.
         "trajectory": "",
          -- [OPTIONAL][NOT_USED] String with the source trajectory being used.
       }
    },
    "simulationConfiguration": {
       -- [OPTIONAL] Object intended to define the simulation settings for being used during the OSVE execution.
      "timeStep": 1,
       -- [OPTIONAL] Integer or double specifiying the time step or time resolution in seconds being used during the OSVE simulation. Default value is 1 second.
      "outputTimeStep": 60,
       -- [OPTIONAL] Integer or double specifiying the time step or time resolution in seconds being used by OSVE while generating the output data. In case of not specified the "timeStep" value will be used.
      "filterStartTime": "yyyy-mm-ddThh:mm:ss.mmmZ",
       -- [OPTIONAL] String with the format "yyyy-mm-ddThh:mm:ss.mmmZ" specifiying the OSVE simulation start time. In case of
       not specified OSVE will take the latest start date from each of the timeline files (ITL, PTR, JSON).
      "filterEndTime": "yyyy-mm-ddThh:mm:ss.mmmZ",
       -- [OPTIONAL] String with the format "yyyy-mm-ddThh:mm:ss.mmmZ" specifiying the OSVE simulation end time. In case of
       not specified OSVE will take the earliest end date from each of the timeline files (ITL, PTR, JSON).
      "resizePtrBlocks": false,
       -- [OPTIONAL] Boolean specifiying if the PTR blocks shall be resized in case of possible during the PTR resolving step. Default value is false.
      "simulateTimeline": true,
       -- [OPTIONAL] Boolean specifiying if the timelines shall be executed after the PTR resolving step. Default value is true.
    },
    "attitudeSimulationConfiguration": {
       -- [OPTIONAL] Object intended to define the attitude simulation settings for being used by AGE(AGM) during the OSVE execution. In case of not specified, OSVE will run the simulation without using AGE(AGM).
      "kernelsList": {
         -- [OPTIONAL] Object intended to define SPICE kernel settings for being used by AGE(AGM) during the OSVE execution.
        "id": "CREMA 3.0",
          -- [OPTIONAL][NOT_USED] String with the identifier of the kernel list to be used by AGE(AGM).
        "version": "1.0.0",
          -- [OPTIONAL][NOT_USED] String with the kernelsList object version, just to have control if any keyword is updated/removed.
        "baselineRelPath": "KERNEL",
          -- [OPTIONAL] String with the relative path to reference all the kernels in the "fileList" array. Default empty string.
        "fileList": [
          -- [OPTIONAL] Array of objects with the SPICE kernels to load.
          {
            "fileRelPath": "meta.tm",
               -- String with the relative path of the SPICE kernel to load.
            "description": "meta.tm"
               -- [OPTIONAL] String with the description of the SPICE kernel to load.
          }
        ]
      },
      "baselineRelPath": "CONFIG/AGE",
       -- [OPTIONAL] String with the relative path to reference all the AGM configuration files. Default empty string.
      "ageConfigFileName": "AGMConfig_PT.xml",
       -- String with the relative path to the AGM configuration file in XML format.
      "fixedDefinitionsFile": "CFG_AGM_JUI_MULTIBODY_FIXED_DEFINITIONS.xml",
       -- [OPTIONAL] String with the relative path of the AGM fixed definitions file in XML format.
      "predefinedBlockFile": "CFG_AGM_JUI_MULTIBODY_PREDEFINED_BLOCK.xml",
       -- [OPTIONAL] String with the relative path of the AGM predefined blocks file in XML format.
      "eventDefinitionsFile": "CFG_AGM_JUI_MULTIBODY_EVENT_DEFINITIONS.xml"
       -- [OPTIONAL] String with the relative path of the AGM event definitions file in XML format.
    },
    "instrumentSimulationConfiguration": {
      -- [OPTIONAL] Object intended to define the instrument simulation settings for being used by ISE(EPSng) during the OSVE execution. In case of not specified, OSVE will run the simulation without using ISE(EPSng).
      "baselineRelPath": "./CONFIG/ISE",
       -- [OPTIONAL] String with the relative path to reference all the EPSng configuration files. Default empty string.
      "unitFileName": "units.def",
       -- String with the relative path of the EPS Units definition file.
      "configFileName": "eps.cfg",
       -- String with the relative path of the EPS configuration file.
      "eventDefFileName": "events.juice.def"
       -- String with the relative path of the EPS event definitions file.
    },
    "inputFiles": {
      -- [OPTIONAL] Object intended to define the input files to use during the OSVE execution.
      "baselineRelPath": "PTR",
       -- [OPTIONAL] String with the relative path to reference all the input files. Default empty string.
      "jsonSegmentFilePath": ""
       -- [OPTIONAL] String with the relative path of the JSON timeline file for AGE(AGM), could not be provided if "xmlPtrPath" is present. Default empty string.
      "xmlPtrPath": "PTR_PT_V3.ptx",
       -- [OPTIONAL] String with the relative path of the Pointing Requests file (PTR) for AGE(AGM), could not be provided if "jsonSegmentFilePath" is present. Default empty string.
      "segmentTimelineFilePath": "ITL/TOP_timelines.itl",
       -- [OPTIONAL] String with the relative path of the Instrument Timeline (ITL) to simulate with ISE(EPSng). Default empty string.
      "eventTimelineFilePath": "TOP_events.evf",
       -- [OPTIONAL] String with the relative path of the Events file (EVF) for being used by ISE(EPSng). Default empty string.
      "modellingConfiguration": {
       -- [OPTIONAL] Object intended to define the Experiment modelling files for being used by ISE(EPSng).
        "baselineRelPath": "EDF",
         -- [OPTIONAL] String with the relative path to reference all the modelling files. Default empty string.
        "edfFileName": "TOP_experiments.edf",
         -- [OPTIONAL] String with the relative path of the Experiment Definitions file (EDF) for being used by ISE(EPSng). Default empty string.
        "observationDefFileName": ""
         -- [OPTIONAL] String with the relative path of the Observations Definitions file for being used by ISE(EPSng). Default empty string.
      }
    },
    "outputFiles": {
     -- [OPTIONAL] Object intended to define the output files that OSVE will generate after the execution.
      "baselineRelPath": "OUTPUT",
       -- [OPTIONAL] String with the relative path to reference all the output files. Default empty string.
      "simOutputFilesPath": "eps_output",
       -- [OPTIONAL] String with the relative path of the folder where ISE(EPSng) will place all the simulation outputs, if not present or empty no simulation output will be generated. Default empty string.
      "ckAttitudeFilePath": "test.ck",
       -- [OPTIONAL] String with the SPICE CameraKernel (CK) that AGE(AGM) will generate after the OSVE execution, if not present or empty, no CK will be generated. Default empty string.
      "ckConfig": {
       -- [OPTIONAL] Object intended to define the CK generation parameters.
        "ckFrameId": -28000,
         -- Integer specifiying the SPICE spacecraft reference frame identifier to use for the CK generation. This CK will map the attitude to pass from the specified reference frame to J2000 
         reference frame. Default frame id is -28001 that refers to JUICE_SPACECRAFT_PLAN found at the
         juice_v??.tf frames kernel found at the JUICE SPICE Kernel Dataset.
        "ckTimeStep": 300
         -- Integer specifiying the time resolution in seconds to use during the CK generation. Default is 300 seconds.

         -- NOTE: In case any of these keywords are missing or wrong, the default values will be used for
         both keywords.
      },
      "txtAttitudeFilePath": "quaternions.csv",
       -- [OPTIONAL] String with the relative path where AGE(AGM) will place the CSV containing the spacecraft quaternions per timestep to pass from the spacecraft frame to J2000. Default empty string, the CSV will not be generated.
      "attitudeXmlPtr": "PTR_RESOLVED.ptx",
       -- [OPTIONAL] String with the relative path where AGE(AGM) will place the resolved PTR. Default empty string, the PTR will not be generated.
      "simDataFilePath": "agmData.csv",
       -- [OPTIONAL] String with the relative path where AGE(AGM) will place the CSV with some parameters extracted during the AGE(AGM) simulation (Solar arrays values, power and spacecraft quaternions). Default empty string, the CSV will not be generated.
      "powerFilePath": "power.csv",
       -- [OPTIONAL] String with the relative path where AGE(AGM) will place the CSV with the Solar Arrays available power extracted during the AGE(AGM) simulation. Default empty string, the CSV will not be generated.
      "powerConfig": {
       -- [OPTIONAL] Object intended to define the Solar Arrays avaliable power CSV generation parameters. Only supported if "powerFilePath" is present.
        "powerTimeStep": 30
         -- Integer specifiying the time resolution in seconds to use during the power CSV generation. If not specifed, the "timeStep" value will be used.
      }
    },
    "logging": {
      -- [OPTIONAL] Object intended to define the logging parameters of OSVE.
      "stdOutLogLevel": "INFO",
       -- [OPTIONAL] String with the log level defined for OSVE when writing on the standard output. Supported values: OK, DEBUG, INFO, WARNING, ERROR, FATAL, NONE. Default value is INFO.
      "jsonLogFile": "log.json"
       -- [OPTIONAL] String with the relative path where OSVE will write all the logs in JSON format. The log level for this JSON file is DEBUG. Default empty string, no JSON log file will be generated.
    }
  }
}
```