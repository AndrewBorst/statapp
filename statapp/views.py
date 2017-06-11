from django.http import HttpResponse

def dcv_validation(request):
    return HttpResponse(open('/opt/statapp/statapp/static/28DEBB2B1A4DBCD4063E02EDE09592EB.txt').read())
    