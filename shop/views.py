from django.shortcuts import render

def home(request):
    # Дані, які ми передаємо на головну сторінку через контекст
    context = {
        'title': 'Головна сторінка ФК Стохід',
        'description': 'Вітаємо у офіційному фан-шопі нашого клубу!',
        'features': ['Оригінальна форма', 'Швидка доставка', 'Знижки для фанатів']
    }
    return render(request, 'index.html', context)

def catalog(request):
    # Дані для сторінки каталогу
    context = {
        'title': 'Каталог товарів',
        'items': [
            {'name': 'Ігрова футболка', 'price': '1200 грн'},
            {'name': 'Шарф вболівальника', 'price': '350 грн'},
            {'name': 'Кепка з логотипом', 'price': '450 грн'}
        ]
    }
    return render(request, 'catalog.html', context)