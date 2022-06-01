import json
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from posts.models import Post

from posts.api.serializers import PostSerializer

# MANERA CON ACCIONES
# @api_view(['GET'])
# def getPosts(request):
#     posts = Post.objects.all()
#     serializer = PostSerializer(posts, many=True)
#     return Response(status=status.HTTP_200_OK, data=serializer.data)

# MANERA CON CLASE API VIEW
# @api_view(['POST'])
# def storePost(request):
#     serializer = PostSerializer(data=json.loads(request.body))
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(status=status.HTTP_200_OK, data=serializer.data)


# class PostApiView(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(status=status.HTTP_200_OK, data=serializer.data)

#     def post(self, request):
#         serializer = PostSerializer(data=json.loads(request.body))
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_200_OK, data=serializer.data)

# MANERA CON VIEWSET
class PostViewSet(ViewSet):
    def list(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, pk: int):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist as e:
            return Response(status=status.HTTP_404_NOT_FOUND, data='Post not found')

        post = PostSerializer(post)
        return Response(status=status.HTTP_200_OK, data=post.data)

    def create(self, request):
        serializer = PostSerializer(data=json.loads(request.body))
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)
