from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Review

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Review

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name') or "Anônimo"
        reviewText = request.POST.get('reviewText')
        stars = request.POST.get('stars')

        if not reviewText or not stars:
            messages.error(request, 'Por favor, preencha a avaliação e a nota.')
            return redirect('app:home')

        try:
            stars = int(stars)
            if stars not in range(1, 6):
                raise ValueError("A nota deve ser entre 1 e 5 estrelas.")
            
            Review.objects.create(
                name=name,
                reviewText=reviewText,
                stars=stars
            )
            messages.success(request, 'Avaliação enviada com sucesso!')
        except ValueError as ve:
            messages.error(request, f'Erro: {str(ve)}')
        except Exception as e:
            messages.error(request, 'Erro ao enviar a avaliação. Tente novamente.')
            print(f"Erro detalhado: {str(e)}")
        return redirect('home')

    return render(request, 'pages/index.html')

def reviews(request):
    reviews = Review.objects.all().order_by('-date')
    return render(request, 'pages/reviews.html', {'reviews': reviews})