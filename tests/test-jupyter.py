#!/usr/bin/python2.7
import sys
from operator import itemgetter
from datetime import datetime
from datetime import timedelta

sys.path.append('/mnt/e/root/pip/applicationinsights_jupyter')
from applicationinsights_jupyter import Jupyter

jupyterObj = Jupyter('DEMO_APP', 'DEMO_KEY')
result = jupyterObj.getAIData("requests | where timestamp > ago(1d) | summarize count() by bin(timestamp, 1h)")
#axes = jupyterObj.sortAxes(result["Rows"], itemgetter(0), 0, 1)
result = jupyterObj.getAIMetricData(metric="requests/count", \
        startTime=(datetime.now() - timedelta(minutes=15)).isoformat(), \
        endTime=datetime.now().isoformat(), \
        interval="PT5M",\
        aggregation="sum")

metrics = jupyterObj.extractTimeSeriesMetrics(result, metric="requests/count", aggregation="sum")
axes = jupyterObj.sortAxes(metrics, itemgetter(0), 0, 1)

jupyterObj = Jupyter('DEMO_APP', 'DEMO_KEY', "https://api.aimon.applicationinsights.io/")
result = jupyterObj.getAIData("availabilityResults| summarize count(success==1), count(success==0) by bin(timestamp, 5m)", verify=False)
#print(axes)
#print(result)
