# A brevet time calculator for CIS 322 #

Eliot Martin | eliotm@uoregon.edu

## Overview

This is a reimplementation of the RUSA ACP controle time calculator (https://rusa.org/octime_acp.html). This API is 
implemented with Flask and AJAX and tested fully using nose tests (located in the tests folder). 

## Algorithm

Controle open and close times are calculated by dividing the controle distance by the maximum and minimum speeds, respectively (maximum and minimum speeds are outlined here https://rusa.org/pages/acp-brevet-control-times-calculator). This time is rounded to the nearest minute.

Furthermore, there is a small bias for closing times with controles under 60 km that is calculated by subtracting the controle distance from 60 and dividing by 60. This value is then added to the usual closing time.

Finally, each brevet distance has predetermined closing times. Thus, controles greater than the brevet distance get no additional time as the closing time is now based on the brevet.

## USAGE
Build image and run in docker from brevets folder (where the dockerfile is located). To specify port, copy 
credentials-skel.ini as credentials.ini and fill in file with appropriate information. 


## Credits

Michal Young, Ram Durairajan, Steven Walton, Joe Istas.
