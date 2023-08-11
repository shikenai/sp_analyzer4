from django.shortcuts import render

import os
import pandas as pd
from django.http import JsonResponse
import json


def test(request):
    return JsonResponse({"key": "balue"})
