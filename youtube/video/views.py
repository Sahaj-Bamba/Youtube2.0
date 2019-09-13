import os

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.encoding import smart_str
from django.views.static import serve

from .models import video
from .forms import videoForm


def play(request):

    return render(request,'video/play.html',{})


def test(request):

    return render(request, 'video/demo.html', {})

def upload(request):
    # lastvideo = video.objects.last()

    # videofile = lastvideo.videofile

    form = videoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context = { 'form': form}

    return render(request, 'video/upload.html', context)


def download(request):
    filepath = '/home/sahaj-bamba/Desktop/webster/Video-Sharing-Portal/youtube/media/videos/videoplayback.mp4'
    response = HttpResponse(content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filepath)
    response['X-Sendfile'] = smart_str(filepath)
    return response


            # serve(request, os.path.basename(filepath), os.path.dirname(filepath))













#
# def send_file(request):
#     """
#     Send a file through Django without loading the whole file into
#     memory at once. The FileWrapper will turn the file object into an
#     iterator for chunks of 8KB.
#     """
#     filename = "videos/videoplayback.mp4"          # Select your file here.
#     wrapper = FileWrapper(file(filename))
#     response = HttpResponse(wrapper, content_type='text/plain')
#     response['Content-Length'] = os.path.getsize(filename)
#     return response
#
#
# def send_zipfile(request):
#     """
#     Create a ZIP file on disk and transmit it in chunks of 8KB,
#     without loading the whole file into memory. A similar approach can
#     be used for large dynamic PDF files.
#     """
#     temp = tempfile.TemporaryFile()
#     archive = zipfile.ZipFile(temp, 'w', zipfile.ZIP_DEFLATED)
#     for index in range(10):
#         filename = __file__ # Select your files here.
#         archive.write(filename, 'file%d.txt' % index)
#     archive.close()
#     wrapper = FileWrapper(temp)
#     response = HttpResponse(wrapper, content_type='application/zip')
#     response['Content-Disposition'] = 'attachment; filename=test.zip'
#     response['Content-Length'] = temp.tell()
#     temp.seek(0)
#     return response
