from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from mimetypes import guess_type
import subprocess

def index(request):
    data = {}
    template = loader.get_template("index.html")
    response = HttpResponse(template.render(data, request))

    if request.method == "POST":
        data["download_url"] = request.POST.get("download_url")
        file_path = "/tmp/1.mp3"
        command = '/usr/bin/youtube2mp3 "{0}" "{1}"'.format(data["download_url"], file_path)
        subprocess.call(command, shell=True)

        with open(file_path, "rb") as f:
            response = HttpResponse(f, content_type='application/force-download')
            response['Content-Length'] = len(response.content)
            response['Content-Disposition'] = 'attachment; filename=1.mp3'

    return response
