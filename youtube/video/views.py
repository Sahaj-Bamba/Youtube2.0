import os

from MySQLdb import connections
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.views.static import serve

from .forms import videoForm, videoData
from .models import video, tag, videoOrg, playlist



def testbase(request):

    # print("khdvjjn")

    return render(request,'video/testbase.html',{})


def play(request):
    x = request.GET.copy()
    vid = x.get('v')
    vorg = (video.objects.get(id=vid))
    vfile = vorg.org.videofile
    context = {'videofile': vfile , 'MEDIA_URL': "/media/"}
    return render(request,'video/play.html',context)


@csrf_exempt
def add_comment(request):
    print("hsdbngvjbnjkbdsnjsdbn")
    if request.method == 'POST':
        print("hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
        print(request.POST)
    print("dieeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
    pass
    # data = ""
    # return render(request, 'video/test2.html', {'data':data})

    data = {
        'data':1,
        'cons':2,
        'message':"caskhbj"
    }

    return JsonResponse(data)

def comment(request):

    print("khdvjjn")

    return render(request,'video/comment.html',{})


def test(request):
    # data = ""
    #print(os.getcwd())
    #os.chdir(os.getcwd()+"/media/videos")
    # os.system("./media/videos/abc.sh 32.mp4")
    # # os.system("mkdir hi")
    # # os.system("hello > hi.txt")
    # f = open('media/video/ax.txt', 'r')
    # file_content = f.read()
    # data = file_content
    # f.close()

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
            os.system("bash youtube/media/video/abc.sh "+str(z.id2)+" ");
            f = open('youtube/media/video/ax.txt', 'r')
            file_content = f.read()
            f.close()
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


#   required data name description
@csrf_exempt
def createPlaylist(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('name')
        des = request.POST.get('description')
        x = playlist.objects.filter(name=name).filter(owner=request.user)
        if len(x) == 0:
            y = playlist()
            y.name = name
            y.description = des
            y.owner = request.user
            y.save()
            data = {
                'response': 0,
                'message': "Playlist has "+y.name+" been successfully created"
            }
        data = {
            'response': 1,
            'message': "There was an error , you have already created a playlist by that name."
        }

        return JsonResponse(data)

    return render(request, 'video/unauthorised.html', {})


#   required data playlistid videoid
@csrf_exempt
def addToPlaylist(request):
    if request.method == 'POST':
        print(request.POST)
        playlistid = request.POST.get('playlistid')
        videoid = request.POST.get('videoid')
        vid = video.objects.get(id=videoid)
        ply = playlist.objects.filter(id=playlistid)
        ply.videos.add(vid)
        data = {
            'response': 0,
            'message': "Video "+vid.name+" has been successfully added to "+ply.name
        }
        return JsonResponse(data)

    return render(request, 'video/unauthorised.html', {})


#   required data
@csrf_exempt
def viewAllPlaylist(request):
    if request.method == 'POST':
        print(request.POST)
        ply = playlist.objects.filter(owner=request.user)

        playlists = []
        ids = []

        for i in ply:
            playlists.append(i.name)
            id.append(i.id)

        data = {
            'response': 0,
            'ids': ids,
            'playlists': playlists
        }

        if len(ply) == 0:
            data = {
                'response': 1,
                'message': "No playlist belong to you"
            }

        return JsonResponse(data)

    return render(request, 'video/unauthorised.html', {})


#   required data videoid
@csrf_exempt
def liked(request):
    if request.method == 'POST':
        print(request.POST)
        videoid = request.POST.get('videoid')
        vid = video.objects.get(id=videoid)
        flag = 0
        for i in vid.likes.all():

            # check if current user exist in it and update flag
            # flag = 1 if present
            pass

        if flag == 0:
            vid.like += 1
            vid.likes.add(request.user)
            vid.save()
            data = {
                'response': flag,
                'message': "done"
            }
        else:
            data = {
                'response': flag,
                'message': "already exist"
            }

        return JsonResponse(data)

    return render(request, 'video/unauthorised.html', {})

#   required data videoid
@csrf_exempt
def report(request):
    if request.method == 'POST':
        print(request.POST)
        videoid = request.POST.get('videoid')
        vid = video.objects.get(id=videoid)
        flag = 0
        for i in vid.reports.all():

            # check if current user exist in it and update flag
            # flag = 1 if present
            pass

        if flag == 0:
            vid.report += 1
            vid.reports.add(request.user)
            vid.save()
            data = {
                'response': flag,
                'message': "done"
            }
        else:
            data = {
                'response': flag,
                'message': "already exist"
            }

        return JsonResponse(data)

    return render(request, 'video/unauthorised.html', {})


#   required data videoid
@csrf_exempt
def dislike(request):
    if request.method == 'POST':
        print(request.POST)
        videoid = request.POST.get('videoid')
        vid = video.objects.get(id=videoid)
        flag = 0
        for i in vid.dislikes.all():

            # check if current user exist in it and update flag
            # flag = 1 if present
            pass

        if flag == 0:
            vid.report += 1
            vid.dislike.add(request.user)
            vid.save()
            data = {
                'response': flag,
                'message': "done"
            }
        else:
            data = {
                'response': flag,
                'message': "already exist"
            }

        return JsonResponse(data)

    return render(request, 'video/unauthorised.html', {})








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
