from django.shortcuts import render

import os
import pandas as pd
from django.http import JsonResponse
from django.shortcuts import redirect
import json
from myapp.models import GeneralSettings


def test(request):
    return JsonResponse({'key1': {'value1A': 1,
                                  'value1B': 2},
                         'key2': {'value2A': 1,
                                  'value2B': 2}})


def home(request):
    return redirect("http://localhost:5173/")


def general_settings(request):
    return JsonResponse({"hello": "world"})
