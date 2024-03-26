import json
from django.http import JsonResponse, HttpResponse
from .models import Task
from django.views.decorators.csrf import csrf_exempt


def get_all_request():
    last_100_tasks = list(Task.objects.values()[:100])
    
    return JsonResponse({'data': last_100_tasks})

def get_by_id_request(task_id):
    task = list(Task.objects.filter(id = task_id).values())[0]
    
    return JsonResponse({"data": task})
    
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
    
def patch_request(body, task_id):
    task = Task.objects.get(id = task_id)
    try:

        # Проверяем наличие необязательного поля 'checked'
        checked = body.get('checked', task.checked)
        title = body.get('title', task.title)
        description = body.get('description', task.description)
        date_start = body.get('date_start', task.date_start)
        date_end = body.get('date_end', task.date_end)
        date_time = body.get('date_time', task.date_time)

        # Создаем новый объект Task
        
        task.title=title
        task.description=description
        task.checked=checked
        task.date_start=date_start
        task.date_end=date_end
        task.date_time=date_time
        
        task.save()
        
        task_json = list(Task.objects.filter(id=task.id).values())[0]
    
        return JsonResponse({'data': task_json})
    except KeyError as e:
        return JsonResponse({'error': f'Missing required field: {e}'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# Create your views here.
@csrf_exempt
def api(request):
    if request.method == "GET":
        return get_all_request()
    elif request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        
        return post_request(body)
    
@csrf_exempt
def task_by_id(request, task_id):
    if request.method == "PATCH":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        
        return patch_request(body, task_id)
    elif request.method == "DELETE":
        task = Task.objects.get(id=task_id).delete()
        
        return HttpResponse(task_id)
    elif request.method == "GET":
        return get_by_id_request(task_id)