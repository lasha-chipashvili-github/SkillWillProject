# from django.contrib.auth import authenticate, login, logout
# from rest_framework import status
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response
#
# @api_view(['POST'])
# @permission_classes([AllowAny])
# def api_login(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#     user = authenticate(request, username=username, password=password)
#
#     if user is not None:
#         login(request, user)
#         return Response({'detail': 'Login successful'}, status=status.HTTP_200_OK)
#     else:
#         return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
#
# @api_view(['POST'])
# def api_logout(request):
#     logout(request)
#     return Response({'detail': 'Logout successful'}, status=status.HTTP_200_OK)
