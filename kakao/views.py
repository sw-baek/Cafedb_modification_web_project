from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
import json
import pandas as pd


# import csv
# import pandas as pd
# from kakao.models import Geocafe
#
# with open('C:/Users/BaekSeungWoo/Documents/카카오톡 받은 파일/cafe_finaldb_3.csv','r', encoding="utf-8") as f:
#     dr = csv.DictReader(f)
#     s = pd.DataFrame(dr)
# ss = []
# for i in range(len(s)):
#     st = (s['post_code'][i], s['addr'][i], s['name'][i], s['x'][i], s['y'][i], s['type'][i], s['open'][i], s['tel'][i])
#     ss.append(st)
# for i in range(len(s)):
#     Geocafe.objects.create(post_code=ss[i][0], addr=ss[i][1], name=ss[i][2], x=ss[i][3], y=ss[i][4], type=ss[i][5], open = ss[i][6], tel = ss[i][7])
#
#


