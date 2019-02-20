#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 

# get gtfs files and osm file
import gtfs_osm_download.py

# copy static files to processed dir
import load_static_files.py

# process gtfs files to create files in processed dir for use by js in website tools
import gtfs_preprocessing 
import transitscore_israel # check that long processing steps (2 hours)are not commented out in imported file
import muni_scores
import high_freq_lines_israel
import lines_on_street
import tpd_at_stops_israel
import stops_in_muni_pre_edit
import stops_in_muni_pre2post_edit # you can also manually edit the pre file to create the post file and rerun the script with this commented out
import tpd_in_muni_per_line
import stops_near_trainstops_pre_edit
import trainstopautoeditpre2post_v1 # you can also manually edit the pre file to create the post file and rerun the script with this commented out
import tpd_near_trainstops_per_line

# convert the py file to js to use in index.html js code
import config_py2js 
# need todo - change service period for display in about in docs/tool_descriptions_e.js and docs/tool_descriptions_h.js

# copy files from processed dir with date in name to local website dir for testing. rename files to remove date from filenames
import copyprocessed2website

# gzip big data files for upload to cloud
import gzip_big_files

# upload files to cloud website dir from local website dir
import upload2aws_s3

#process TTM files
import navitia_update.py