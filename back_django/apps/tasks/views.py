import json
from django.http import JsonResponse, HttpResponse
from .models import Task
from django.views.decorators.csrf import csrf_exempt


def get_request():
    last_100_tasks = list(Task.objects.values()[:100])
    
    return JsonResponse({'data': last_100_tasks})
    
def post_request(body):
    try:
        # Проверяем наличие обязательных полей в словаре body
        required_fields = ['title', 'description', 'date_start', 'date_end', 'date_time']
        for field in required_fields:
            if field not in body:
                raise KeyError(field)

        # Проверяем наличие необязательного поля 'checked'
        checked = body.get('checked', False)

        # Создаем новый объект Task
        new_task = Task(
            title=body['title'],
            description=body['description'],
            checked=checked,
            date_start=body['date_start'],
            date_end=body['date_end'],
            date_time=body['date_time'],
        )
        new_task.save()
        
        return HttpResponse(new_task.id)
    except KeyError as e:
        return JsonResponse({'error': f'Missing required field: {e}'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
# Create your views here.
@csrf_exempt
def api(request):
    if request.method == "GET":
        return get_request()
    elif request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        
        return post_request(body)
        
