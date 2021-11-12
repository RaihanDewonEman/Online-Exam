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
            if request.POST['question3'] == 'D':
                countPoint += 1
            if request.POST['question4'] == 'C':
                countPoint += 1
            if request.POST['question5'] == 'D':
                countPoint += 1
            if request.POST['question6'] == 'C':
                countPoint += 1
            if request.POST['question7'] == 'D':
                countPoint += 1
            if request.POST['question8'] == 'C':
                countPoint += 1
            if request.POST['question9'] == 'D':
                countPoint += 1
            if request.POST['question10'] == 'C':
                countPoint += 1
            return render(request, 'examquestion/mathexam1.html',{'name': 'Math Question', 'countPoint': countPoint})
        
        else:
            return render(request, 'examquestion/mathexam1.html',{'name': 'Math Question'})

def banglaExam1(request):
    if not request.user.is_authenticated:
        return render(request, 'account/home.html', {'name': 'Home page','error':'Please login first!'})
    else:
        if  request.method == 'POST':
            countPoint = 0

            if request.POST['question1'] == 'A':
                countPoint += 1
            if request.POST['question2'] == 'C':
                countPoint += 1
            if request.POST['question3'] == 'C':
                countPoint += 1
            if request.POST['question4'] == 'C':
                countPoint += 1
            if request.POST['question5'] == 'C':
                countPoint += 1
            if request.POST['question6'] == 'C':
                countPoint += 1
            if request.POST['question7'] == 'C':
                countPoint += 1
            if request.POST['question8'] == 'C':
                countPoint += 1
            if request.POST['question9'] == 'C':
                countPoint += 1
            if request.POST['question10'] == 'C':
                countPoint += 1
            if request.POST['question11'] == 'C':
                countPoint += 1
            if request.POST['question12'] == 'C':
                countPoint += 1
            if request.POST['question13'] == 'C':
                countPoint += 1
            if request.POST['question14'] == 'C':
                countPoint += 1
            if request.POST['question15'] == 'C':
                countPoint += 1
            return render(request, 'examquestion/banglaexam1.html',{'name': 'Bangla Question', 'countPoint': countPoint})
        
        else:
            return render(request, 'examquestion/banglaexam1.html',{'name': 'Bangla Question'})


def mathExamIndex(request):
    if not request.user.is_authenticated:
        return render(request, 'account/home.html',{'name': 'Home page','error':'Please login first!'})
    else:
        return render(request, 'examquestion/mathexamindex.html',{'name': 'Index page'})

def banglaExamIndex(request):
    if not request.user.is_authenticated:
        return render(request, 'account/home.html',{'name': 'Home page','error':'Please login first!'})
    else:
        return render(request, 'examquestion/banglaexamindex.html',{'name': 'Index page'})