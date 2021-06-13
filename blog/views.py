from django.shortcuts import render
from datetime import date
# Create your views here.
posts=[
    {
        "slug":"hike-in-the-mountains1",
        "img":"1.jpg",
        "author":"Amjad",
        "date":date(2021,3,6),
        "title":"mountain hiking",
        "excerpt":"SDSDASDDA  hgfdedg hgfe       jdjdjdjdjjdjdjdjdj djdjdjdjjdjjdjdjjdj",
        "content":""" gggggggggggggggggggggggggggg
        ggggggggggggggggggggggggg
        ttttttttttttttttttttttttttt
         """

    },
    {
        "slug":"hike-in-the-mountains2",
        "img":"2.jpg",
        "author":"Amjad",
        "date":date(2021,3,6),
        "title":"mountain hiking",
        "excerpt":"SDSDASDDA  hgfdedg hgfe       jdjdjdjdjjdjdjdjdj djdjdjdjjdjjdjdjjdj",
        "content":""" gggggggggggggggggggggggggggg
        ggggggggggggggggggggggggg
        ttttttttttttttttttttttttttt
         """

    },
    {
        "slug":"hike-in-the-mountains3",
        "img":"3.jpg",
        "author":"Amjad",
        "date":date(2021,3,6),
        "title":"mountain hiking",
        "excerpt":"SDSDASDDA  hgfdedg hgfe       jdjdjdjdjjdjdjdjdj djdjdjdjjdjjdjdjjdj",
        "content":""" gggggggggggggggggggggggggggg
        ggggggggggggggggggggggggg
        ttttttttttttttttttttttttttt
         """

    }
]
def get_date(post_item):
    return post_item['date']
def index(request):
    sorted_post=sorted(posts,key=get_date)

    latest_posts=sorted_post[-3:]
    return render(request,"blog/index.html",{"posts":latest_posts})
    


def post(request):
    return render(request,"blog/posts.html",{"posts":posts})

def post_detail(request,slug):
    #found_item=next(post_item for post_item in posts if post_item[slug]==slug)
    return render(request,"blog/post-detail.html",{"post":posts[0]})