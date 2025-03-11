from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer
from rest_framework.pagination import PageNumberPagination
# 🎯 **Secure Student API with JWT Authentication**
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])  # 🛡️ JWT Authentication Required
def student_list(request):
    if request.method == 'GET':  # ✅ Read All Students
        students = Student.objects.all().order_by('id')  # Data Order करें
        paginator = PageNumberPagination()
        paginator.page_size = 2  # प्रति पेज 5 Items

        result_page = paginator.paginate_queryset(students, request)
        serializer = StudentSerializer(result_page, many=True)
        
        return paginator.get_paginated_response(serializer.data)
    
    elif request.method == 'POST':  # ✅ Create Student
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])  # 🛡️ JWT Authentication Required
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':  # ✅ Read One Student
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    elif request.method == 'PUT':  # ✅ Update Student
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':  # ✅ Delete Student
        student.delete()
        return Response({'message': 'Student deleted'}, status=status.HTTP_204_NO_CONTENT)


from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password)
    return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
