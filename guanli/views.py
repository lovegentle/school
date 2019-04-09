from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django import forms
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from guanli.models import Hello,Li,Wen,type1,type2,type3
from guanli.forms import SearchForm

def index(request):
   context = {
      'searchForm': SearchForm(),
   }
   return render(request, 'ss/index.html', context)


def book_search(request):
   search_by = request.GET.get('search_by', '大学学历')
   books = []
   current_path = request.get_full_path()

   keyword = request.GET.get('keyword', u'_学院列表')

   if keyword == u'_学院列表':
      books = Hello.objects.all()
   else:
      if search_by == u'大学学历':
         keyword = request.GET.get('keyword', None)
         books = Hello.objects.filter(nature__contains=keyword).order_by('-name')[0:50]
      elif search_by == u'大学名称':
         keyword = request.GET.get('keyword', None)
         books = Hello.objects.filter(name__contains=keyword).order_by('-name')[0:50]

   paginator = Paginator(books, 5)
   page = request.GET.get('page', 1)

   try:
      books = paginator.page(page)
   except PageNotAnInteger:
      books = paginator.page(1)
   except EmptyPage:
      books = paginator.page(paginator.num_pages)

   # ugly solution for &page=2&page=3&page=4
   if '&page' in current_path:
      current_path = current_path.split('&page')[0]



   context = {
      'books': books,
      'search_by': search_by,
      'keyword': keyword,
      'current_path': current_path,
      'searchForm': SearchForm(),
   }
   return render(request, 'ss/search.html', context)


def about(request):
   return render(request, 'ss/about.html')


def book_detail(request):
   name = request.GET.get('name', None)
   print(name)
   if not name:
      return HttpResponse('there is no such an ISBN')
   try:
      hello = Hello.objects.get(pk=name)
   except Hello.DoesNotExist:
      return HttpResponse('there is no such an ISBN')

   li=Li.objects.all()
   readerInfo={}
   helloInfo={}
   for r in li:
      if(r.id==name):
         readerInfo[r.low]=r.low
         helloInfo[r.year]=r.year

   helloAmountData = [helloInfo[x] for x in helloInfo]
   readerAmountData = [readerInfo[x] for x in readerInfo]

   wen = Wen.objects.all()
   wenInfo = {}
   nihaoInfo = {}
   for r in wen:
      if(r.id==name):
         wenInfo[r.low] = r.low
         nihaoInfo[r.year] = r.year

   wenAmountData = [wenInfo[x] for x in wenInfo]
   nihaoAmountData = [nihaoInfo[x] for x in nihaoInfo]

   one=type1.objects.all()
   type1Info={}
   score1Info={}
   for r in one:
      if(r.id==name):
         type1Info[r.type]=r.type
         score1Info[r.type]=r.score

   type1AmountData=[type1Info[x] for x in type1Info]
   #print(type1AmountData)
   score1AmountData=[score1Info[x] for x in score1Info]
   #print(score1AmountData)

   two= type2.objects.all()
   type2Info = {}
   score2Info = {}
   for r in two:
      if (r.id == name):
         type2Info[r.type] = r.type
         score2Info[r.type] = r.score

   type2AmountData = [type2Info[x] for x in type2Info]
   score2AmountData = [score2Info[x] for x in score2Info]


   three = type3.objects.all()
   type3Info = {}
   score3Info = {}
   for r in three:
      if (r.id == name):
         type3Info[r.type] = r.type
         score3Info[r.type] = r.score

   type3AmountData = [type3Info[x] for x in type3Info]
   score3AmountData = [score3Info[x] for x in score3Info]
   #print(score3AmountData)



   context = {

      'hello': hello,
      'wenAmountData': wenAmountData,
      'nihaoAmountData': nihaoAmountData,
      'readerAmountData': readerAmountData,
      'helloAmountData': helloAmountData,
      'type1AmountData':type1AmountData,
      'score1AmountData':score1AmountData,
      'type2AmountData':type2AmountData,
      'score2AmountData': score2AmountData,
      'type3AmountData': type3AmountData,
      'score3AmountData': score3AmountData
   }
   return render(request, 'ss/book_detail.html',context)


def statistics(request):
   hello=Hello.objects.all()
   helloInfo={}
   for r in hello:
      if r.type not in helloInfo:
         helloInfo[r.type]=1
      else:
         helloInfo[r.type]+=1
   #print(helloInfo)
   hiInfo = {}
   for r in hello:
      if r.nature not in hiInfo:
         hiInfo[r.nature]=1
      else:
         hiInfo[r.nature]+=1
   #print(hiInfo)
   helloAmountData = [helloInfo[x] for x in helloInfo]
   #print(helloAmountData)
   hiAmountData = [hiInfo[x] for x in hiInfo]


   context={
      'helloAmountData':helloAmountData,
      'hiAmountData':hiAmountData

   }
   return render(request, 'ss/statistics.html', context)

