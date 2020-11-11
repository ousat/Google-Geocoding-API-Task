
import json

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from geoUpdater.settings import OUTPUT_FILEPATH

from geo.process_file import update_column

VALID_TYPES = ["csv", "xls", "xlsx"]
# Create your views here.

def home(request):
    '''
        returns home screen
    '''
    return render(request, "home.html")

@csrf_exempt
def upload_excel(request):
    '''
        reads file , processes and saves the output file
    '''
    try:
        file_input = request.FILES["file"]

        # print(vars(file_input))
        result = update_column(file_input)
        return HttpResponse(json.dumps(result), content_type="application/json")
    except (KeyError, ValueError, IndexError) as e:
        # print(e)
        return HttpResponse(json.dumps({"status": -1, "message": "Invalid File"}), content_type="application/json")


def download_output(request):
    '''
        downloads output file 
    '''
    time_id = request.GET["id"] if "id" in request.GET else ""
    with open(OUTPUT_FILEPATH.format(timestamp=time_id), 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + OUTPUT_FILEPATH.format(timestamp=time_id)
            return response



