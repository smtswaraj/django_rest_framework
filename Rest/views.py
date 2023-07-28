from rest_framework import authentication, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TodoSerializer,TimingTodoSerializer
from .models import Todo,TimingTodo
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action
# Create your views here.

@api_view(['GET','POST','PATCH'])
def home(request):
    if request.method == "GET":
        return Response({
            'status':200,
            'message':'yes! Django rest framework is working!',
            'methode_calling': 'You called GET methode'
        })
    elif request.method == "POST":
        return Response({
            'status':200,
            'message':'yes! Django rest framework is working!',
            'methode_calling': 'You called POST methode'
        })
    if request.method == "PATCH":
        return Response({
            'status':200,
            'message':'yes! Django rest framework is working!',
            'methode_calling': 'You called PATCH methode'
        })
@api_view(['GET'])
def get_todo(request):
    todo_objects = Todo.objects.all()
    serializer = TodoSerializer(todo_objects, many = True)
    return Response({
            'status':True,
            'message':'Todo fetched',
            'data':serializer.data
        })




@api_view(['POST'])
def post_todo(request):
    try:
        data = request.data
        serializer = TodoSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({
            'status':True,
            'message':'Success data',
            'data':serializer.data
        })
        # print(data)




        return Response({
            'status':False,
            'message':'invalid data',
            'data':serializer.errors
        })

    except Exception as e:
        print(e)
        return Response({
            'status':False,
            'message':'Something went wrong'
        })
    # TodoSerializer

@api_view(['PATCH'])
def patch_todo(request):
    try:
        data = request.data
        if not data.get('uid'):

            return Response({
                'status':False,
                'message':'uid is required',
                'data': {}
            })
        obj = Todo.objects.get(uid = data.get('uid'))  
        serializer = TodoSerializer(obj, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({
                'status':True,
                'message':'Success data',
                'data':serializer.data
                 })
        
        return Response({
            'status':False,
            'message':'invalid data',
            'data':serializer.errors
        })


    except Exception as e:
        print(e)
        return Response({
            'status':False,
            'message':'Invalid uid',
            'data': {}

        })
    

class TodoView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    def get(self, request):
        print(request.user)
        todo_objs = Todo.objects.filter(user = request.user)
        serializer = TodoSerializer(todo_objs, many = True)
        return Response({
            'status':200,
            'message':'You called GET methode',
            'data': serializer.data 
        })

    def post(self, request):
        data = request.data
        return Response({
            'status':200,
            'message':'You called POST methode'
        })

    def put(self, request):

        return Response({
            'status':200,
            'message':'You called PUT methode'
        })
    def patch(self, request):

        return Response({
            'status':200,
            'message':'You called PATCH methode'
        })


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    @action(detail=False, methods=['get'])
    def get_timing_todo(self, request):
        objs = TimingTodo.objects.all()
        serializer = TimingTodoSerializer(objs, many = True)
        return Response({
                        'status':True,
                        'message':'Timing todo fetched',
                        'data': serializer.data
                    })



    @action(detail=False, methods=['post'])
    def add_date_to_todo(self , request):
        try:
           data = request.data
           serializer = TimingTodoSerializer(data = data)
           if serializer.is_valid():
                serializer.save()
                return Response({
                        'status':True,
                        'message':'success data',
                        'data': serializer.data
                    })
           return Response({
                'status':False,
                'message':'success data',
                'data': serializer.errors
            })


        except Exception as e:
            print(e)
            return Response({
                'status':False,
                'message':'Something went wrong'
            })