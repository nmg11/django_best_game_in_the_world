from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

pool_of_users = {'admin':'admin123'}
current_user = ''

#отзывы
reviews_dict = {}
def reverse(request):
    # добавление отзывов
    text_in_area = request.GET['message'].strip()
    print(text_in_area)
    global current_user, reviews_dict
    if current_user == '':
        return render('reviews.html', {'user_not_exist': True})
    else:
        reviews_dict[current_user] = text_in_area
        all_data = {'user_name': current_user, 'all_review': reviews_dict}
        return render(request, 'reviews.html', context=all_data)

def reviews(request):
    #страница отзывов
    global reviews_dict
    all_data = {'user_name': current_user, 'all_review': reviews_dict}
    return render(request, 'reviews.html', context=all_data)

def main(request):
    # главное меню (регистрация)
    return render(request, 'main.html', {'user_alredy_exists': False,
                                             'user_name': current_user})

def login_check(request):
    # вход в профиль \ начало игры
    login_new_user = request.GET['name_user_login']
    login_new_user.strip()
    password_new_user = request.GET['password_user_login']
    password_new_user.strip()
    global current_user
    if login_new_user not in pool_of_users:
        return render(request, 'login.html', {'user_alredy_exists': True})
    else:
        pool_of_users[login_new_user] = password_new_user
        current_user = login_new_user
        return render(request, 'start_game.html', {'user_name': current_user})

text_for_quest = ['Значит так, {{ user_name_noob }}',
                  'Что? Думал это косяк в коде? Конечно нет',
                  'Теперь мне нужно растянуть твоё задание подольше, '
                  'пока я завариваю себе кофе']
time_to_going_later = False
def first_quest(request):
    # первый квест после регистрации
    global text_for_quest,time_to_going_later
    if time_to_going_later == False:
        try:
            current_text_for_quest = text_for_quest[ 0 ]
            text_for_quest.remove(text_for_quest[ 0 ])
        except IndexError:
            time_to_going_later = True
            current_text_for_quest = 'А вот это серьёзно. В курсе, что ты сейчас словил IndexError?' \
                                     ' Так зайди в исходник и посмотри. ' \
                                     'Но кофе оказался достаточно крепким, так что пока что я тебя прощаю. ' \
                                     'На твоё счастье, я хороший тимлид и специально поставил обработчик исключений, ' \
                                     'чтобы ты не вылетел сразу по неопытности. \n' \
                                     'Давай, нажмёшь ещё раз на эту кнопку? Она уже не та, что прежде. Нажмёшь и тоже изменишься';
        finally:
            all_data = {'user_name': current_user, 'text': current_text_for_quest, 'time_to_going_later': time_to_going_later}
            return render(request, 'first_quest.html', context=all_data)
    else:
        return render(request, '2.html')

def login(request):
    # переход на страницу логина
    return render(request, 'login.html', {'user_name': current_user})

def registration_check(request):
    #проверка существования пользователя
    login_new_user = request.GET[ 'name_user_registration' ]
    login_new_user.strip()
    password_new_user = request.GET[ 'password_user_registration' ]
    password_new_user.strip()
    if login_new_user in pool_of_users:
        return render(request, 'main.html', {'user_alredy_exists': True})
    else:
        pool_of_users[ login_new_user ] = password_new_user
        return render(request, 'login.html')

def profile_user(request):
    #профиль пользователя
    global current_user, pool_of_users
    if current_user in pool_of_users:
        current_password = pool_of_users[current_user]
    else:
        current_password = ''
    return render(request, 'profile_user.html', {'user_name': current_user,
                                                 'user_password': current_password})

def quit_profile(request):
    #выход их профиля
    global current_user
    current_user = ''
    return redirect('/')

def start_game(request):
    return render(request, 'start_game.html', {'user_name': current_user})

def quest_number_two(request):
    # переход ко второму квесту
    return render(request, '2.html')

def end_game(request):
    return render(request, 'end_game.html')

def exactly_the_end(request):
    return render(request, 'exactly_the_end.html')

def last_warning(request):
    #последняя попытка
    return render(request, 'last_warning.html')

def happy_end(request):
    #конец игры (счастливый)
    return render(request, 'happy_end.html')

