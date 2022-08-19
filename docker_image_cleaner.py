#!/usr/bin/python3

# ------------------------------------------------
# Program by hvv19890828
#
#
# Version      Date           Info
# 1.0          19-08-2022     First born unicorn
#
# ----------------------------------------------

import docker
import re
from datetime import datetime
from dateutil.parser import isoparse

# Termination filters prompt
tag_pattern = input('Enter image tag pattern: ')
termination_age = int(input('Enter termination age (in minutes): '))
imgs_to_save = int(input('Enter a number of images to preserve: '))

client = docker.from_env()
images_i = client.images.list()

time_fmt = '%Y-%m-%d %H:%M:%S'
for i in client.images.list():
   # Image match markers collection
   repo_name_i = str(i.tags)
   repo_name_match_i = re.findall(tag_pattern, repo_name_i)
   # Image age calculation
   creation_date_i = str(isoparse(i.attrs["Created"]))
   creation_date_fmtd_i = re.sub(r"\..*", "", creation_date_i)
   current_date_i = str(datetime.now())
   current_date_fmtd_i = re.sub(r"\..*", "", current_date_i)
   tstamp1_i = datetime.strptime(current_date_fmtd_i, time_fmt)
   tstamp2_i = datetime.strptime(creation_date_fmtd_i, time_fmt)
   tdiff_i = tstamp1_i - tstamp2_i
   tdiff_mins_i = int(round(tdiff_i.total_seconds() / 60))

   # Image deletion approval
   deletion_approval = False
   img_amount = 0
   images_j = client.images.list()
   for j in client.images.list():
      # Image match markers collection
      repo_name_j = str(j.tags)
      repo_name_match_j = re.findall(tag_pattern, repo_name_j)
      # Image age calculation
      creation_date_j = str(isoparse(j.attrs["Created"]))
      creation_date_fmtd_j = re.sub(r"\..*", "", creation_date_j)
      current_date_j = str(datetime.now())
      current_date_fmtd_j = re.sub(r"\..*", "", current_date_j)
      tstamp1_j = datetime.strptime(current_date_fmtd_j, time_fmt)
      tstamp2_j = datetime.strptime(creation_date_fmtd_j, time_fmt)
      tdiff_j = tstamp1_j - tstamp2_j
      tdiff_mins_j = int(round(tdiff_j.total_seconds() / 60))
      # Comparison
      if len(repo_name_match_j) > 0 and tdiff_mins_i >= tdiff_mins_j:
         img_amount += 1
         if img_amount > imgs_to_save :
            deletion_approval = True
         else:
            deletion_approval = False

   # Image deletion
   image_id = (str(i.id).replace("sha256:", ""))
   if tdiff_mins_i >= termination_age and deletion_approval and len(repo_name_match_i) > 0 :
      client.images.remove(image=image_id, force=True)
      print("Deleted: " + repo_name_i + " " + str(i.id))

