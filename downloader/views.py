from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from mimetypes import guess_type
import subprocess
import os

def index(request):
    data = {}
    response = HttpResponse()

    if request.method == "POST":
        data["download_url"] = request.POST.get("download_url")
        file_path = "/tmp/1.mp3"
        command = '/usr/bin/youtube2mp3 "{0}" "{1}"'.format(data["download_url"], file_path)
        print("Command: " + command)
        subprocess.call(command, shell=True)

        with open(file_path, "rb") as f:
            response = HttpResponse(f.read(), content_type=guess_type(file_path))
            response['Content-Length'] = os.path.getsize(file_path)
            response['Content-Disposition'] = "attachment; filename=1.mp3"
            print("File length: " + str(os.path.getsize(file_path)))
            print(response)

    else:
        template = loader.get_template("index.html")
        response = HttpResponse(template.render(data, request))

    return response
