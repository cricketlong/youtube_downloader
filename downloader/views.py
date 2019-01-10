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
        data["filename"] = request.POST.get("filename")
        file_path = "/tmp/1.mp3"
        command = '/usr/bin/youtube2mp3 "{0}" "{1}"'.format(data["download_url"], file_path)
        subprocess.call(command, shell=True)

        with open(file_path, "w+") as f:
            response = HttpResponse(f, content_type='application/force-download')
            response['Content-Length'] = len(response.content)
            custom_filename = "1"
            if len(data['filename']) > 0:
                custom_filename = data['filename']
            response['Content-Disposition'] = 'attachment; filename={0}.mp3'.format(custom_filename)

    return response
