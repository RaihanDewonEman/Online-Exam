from django.shortcuts import render

# Create your views here.

def mathExam1(request):
    if not request.user.is_authenticated:
        return render(request, 'account/home.html',{'name': 'Home page','error':'Please login first!'})
    else:
        if  request.method == 'POST':
            countPoint = 0

            if request.POST['question1'] == 'D':
                countPoint += 1
            if request.POST['question2'] == 'C':
                countPoint += 1
            return render(request, 'examquestion/mathexam1.html',{'name': 'Math Question', 'countPoint': countPoint})
        
        else:
            return render(request, 'examquestion/mathexam1.html',{'name': 'Math Question'})


def mathExamIndex(request):
    if not request.user.is_authenticated:
        return render(request, 'account/home.html',{'name': 'Home page','error':'Please login first!'})
    else:
        return render(request, 'examquestion/mathexamindex.html',{'name': 'Index page'})