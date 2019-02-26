#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# config file for transitanalystisrael tools  
#

# product templates - not done yet....!!!!
#Monthly auto update on AWS EC2 and S3
#get_service_date = auto
#python_processing = aws_ec2

#Monthly auto update on local pc
#get_service_date = auto
#python_processing = local_pc

#On demand date on AWS EC2 and S3
#get_service_date = on_demand
#python_processing = aws_ec2

#On demand date on S3 only (no TTM)
#get_service_date = on_demand
#python_processing = local_pc

#On demand date on local pc
#get_service_date = on_demand
#python_processing = local_pc

#On demand date on local pc no TTM
#get_service_date = on_demand
#python_processing = local_pc


# common config
gtfsdate = '20190202'
serviceweekstartdate = '20190202'
gtfsdirbase = 'israel'
gtfspath = '..\\gtfs\\'
osmpath = '..\\osm\\'
staticpath = '..\\static_data\\' 
processedpath = '..\\processed\\'
#processedpath = 'C:\\transitanalyst\\temp\\'
temppath = '..\\temp\\'
websitelocalcurrentpath = '..\\website_current\\'
websitelocalpastpath = '..\\website_past\\'
websitelocalnodatapath = '..\\website_no_data\\'
pythonpath = '..\\root\\'
sstarttimeall = '00:00:00'
sstoptimeall = '24:00:00'
bigjs2gzip = 500000
language = 'hebrew'

# line_freq config
freqtpdmin = 60

# lines_on_street config
areatpdmin = 10

# muni_fairsharescore config

# muni_score_charts config

# muni_tpd_per_line config

# muni_transitscore config

# tpd_at_stops_per_line config

# tpd_near_trainstops_per_line config 
neartrainstop = 500.0 # meters for stop to be considered near trainstop before editing
autoeditrefdate = '20181021'

# transitscore config

# transit_time_map config
# curent_or_past is changed to past in the js config file by copyprocessed2website.py when moving website_current to website_past
current_or_past = 'current'

# transit_time_map url config - local or AWS API Getway for Transit Analyst production
# local address should be: "http://localhost:9191"
time_map_server_url = "https://ll7ijshrc0.execute-api.eu-central-1.amazonaws.com/NavitiaTimeMap/"

#
