from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from app.models import Puzzle
from app.forms import PuzzleForm

# Create your views here.

# Создать новый элемент каталога
def createpuzzle(request):
    # создание формы с указанными параметрами
    if request.method == 'POST':
        form = PuzzleForm(request.POST, request.FILES)

        # сохраняем в бд и возвращаемся обратно на страницу администрирования
        if form.is_valid():            
            newPuzzle = form.save(commit=False)  
            newPuzzle.save()
            return HttpResponseRedirect('/album_admin')

    # пустая форма
    form = PuzzleForm()
    return render(request, "app/upload.html", {'form' : form})


# редактирование элемента каталога
def editpuzzle(request, puzzleNumber):

    # получаем по первичному ключу элемент
    puzzle = Puzzle.objects.get(PK_Puzzle = puzzleNumber)

    if request.method == 'POST':
        # создание формы с указанными параметрами
        form = PuzzleForm(request.POST, request.FILES)

        # если форма заполнена корректно
        if form.is_valid():

            # записываем в поля
            puzzle.PK_Manufacturer = form.cleaned_data["PK_Manufacturer"]
            puzzle.name = form.cleaned_data["name"]
            puzzle.PK_Category = form.cleaned_data["PK_Category"]
            puzzle.number_of_details = form.cleaned_data["number_of_details"]
            puzzle.age = form.cleaned_data["age"]
            puzzle.ifalldetails = form.cleaned_data["ifalldetails"]
            puzzle.description = form.cleaned_data["description"]
            puzzle.imagepath = form.cleaned_data["imagepath"]
            
            # сохраняем
            puzzle.save()
            return HttpResponseRedirect('/album_admin')

    #создание формы с заполнением полей данными модели
    form = PuzzleForm(instance=puzzle)
    return render(request, "app/upload.html", {'form' : form, 'pk' : puzzle.PK_Puzzle})


# главная страница
def index(request):
	return render(request, 'app/index.html')

# альбом
def album(request):
	puzzles = Puzzle.objects.all()
	return render(request, 'app/album.html', {"puzzles" : puzzles})

# администрирование каталога
def album_admin(request):
	puzzles = Puzzle.objects.all() 
	return render(request, 'app/album_admin.html', {"puzzles" : puzzles})

# подробная информация об элементе альбома
def puzzleinfo(request, puzzleNumber):
    thisPuzzle = Puzzle.objects.get(PK_Puzzle=puzzleNumber)
    return render(request, "app/product.html", {"thisPuzzle" : thisPuzzle})

# Удаление элемента альбома
def deletepuzzle(request, puzzleNumber):
    currentPuzzle = Puzzle.objects.get(PK_Puzzle=puzzleNumber)
    currentPuzzle.delete()
    return HttpResponseRedirect('/album_admin')
