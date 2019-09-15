import os

from MySQLdb import connections
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.encoding import smart_str
from django.views.static import serve

from .forms import videoForm, videoData
from .models import video, tag, videoOrg


def play(request):
    x = request.GET.copy()
    vid = x.get('v')
    vorg = (video.objects.get(id=vid))
    vfile = vorg.org.videofile
    context = {'videofile': vfile , 'MEDIA_URL': "/media/"}
    return render(request,'video/play.html',context)


def test(request):

    x = videoOrg.objects.last()
    # x.v
    # cursor = connections["youtube2"].cursor()
    # cursor.execute("select videofile from video_videoorg where id2 = "+x.id2)
    # res = dictfetchall(cursor)
    # serve(request, os.path.basename(filepath), os.path.dirname(filepath))

    return render(request, 'video/test2.html', {})


def upload(request):
    form = videoForm(request.POST or None, request.FILES or None)
    form2 = videoData(request.POST or None)
    errors = ""
    if request.method == 'POST':
        x = form
        data = request.POST.copy()
        if x.is_valid():
            # vid = x.get_videofile()
            # print(x.fields['videofile'].name)
            x.save()
            z = videoOrg.objects.last()
            os.system("mv youtube/media/\"" + z.videofile.name + "\" youtube/media/videos/" + str(z.id2) + ".mp4")

            z.videofile.name = "videos/" + str(z.id2) + ".mp4"
            z.save()
            form2.save()
            y = video.objects.last()
            print("diii")
            print(data.get('field_name'))
            i=0
            while True :
                if 'field_name['+str(i)+']' in data:
                    if len(data.get('field_name['+str(i)+']')) <= 0 :
                        i += 1
                        continue
                        pass
                    if len(tag.objects.filter(name=data.get('field_name['+str(i)+']'))) > 0:
                        tmp = tag.objects.get(name=data.get('field_name['+str(i)+']'));
                    else:
                        tmp = tag()
                        tmp.name = data.get('field_name['+str(i)+']')
                        tmp.save()
                    y.tags.add(tmp)
                    i += 1
                    pass
                else:
                    break
                    pass
                pass
            y.owner = request.user
            y.org = z
            y.save()
        print(x)
        print(data)
        return render(request, 'video/test2.html', {'data':data})

    context = {'form': form, 'form2': form2}
    return render(request, 'video/upload.html', context)


def download(request):
    x = request.GET.copy()
    vid = x.get('v')
    vorg = (video.objects.get(id=vid))
    vfile = vorg.org.videofile
    response = HttpResponse(content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(vfile)
    response['X-Sendfile'] = smart_str(vfile)
    return response















#


# os.mkdir("hi")

# if form.is_valid():
#     form.save()
#     print(form2.name)
#     print(form2.description)
#     # form2.name =
#     form2.save()
#     # print(form['videofile'].value())
#     # print(form['id'].value())
#     # x = form.auto_id
#     # print("Jin")
#     # print(x)
#     # temp = video.objects.get(name=form['name'].value())
#
#     # form.save()
#
# # if form2.is_valid():


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
