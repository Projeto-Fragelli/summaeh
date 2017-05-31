from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from .validators import youtube_url_normalizer
from .models import *
from .forms import VideoForm


@login_required
def add_video(request):
    ctx = {}

    if request.method == 'GET':
        ctx['form'] = VideoForm()
    else:
        ctx['form'] = form = VideoForm(request.POST)

        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.link = youtube_url_normalizer(video.link)
            video.save()
            return redirect('videos:list')

    return render(request, 'videos/add_video.html', ctx)


@login_required
def list_videos(request):
    AMOUNT_PER_PAGE = 3

    videos_list = Video.objects.all()

    paginator = Paginator(videos_list, AMOUNT_PER_PAGE)  # Quantidade de vídeo por página

    page = request.GET.get('page')
    try:
        videos = paginator.page(page)
    except PageNotAnInteger:
        # Se a página não for um inteiro, vai para a primeira página
        videos = paginator.page(1)
    except EmptyPage:
        # Se a página estiver fora do alcance vai para a última página existente
        videos = paginator.page(paginator.num_pages)

    return render(request, 'videos/list_videos.html', {'videos_list': videos})


@login_required
def detail_video(request, id_video):
    video = Video.objects.get(id=id_video)
    comments = Comment.objects.filter(video=id_video,user=request.user)
    likes = video.num_likes
    dislikes = video.num_dislikes

    information = {
        'video': video,
        'comments_list': comments,
        'likes_amount': likes,
        'dislikes_amount': dislikes,
    }

    return render(request, 'videos/detail_video.html', information)