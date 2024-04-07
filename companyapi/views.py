# from django.http import HttpResponse, JsonResponse


# def home_page(request):
#     print("home page requested")
#     friends=['aman','ravi','uttam']
#     return JsonResponse (friends)


from django.http import JsonResponse

def home_page(request):
    print("home page requested")
    friends = ['aman', 'ravi', 'uttam']
    return JsonResponse({'friends': friends})
