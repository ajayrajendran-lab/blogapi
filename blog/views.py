from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from blog.models import Post
from blog.serializers import UserCreationSerializer,PostSerializer,CommentSerializer
from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
from rest_framework import authentication,permissions

# Create your views here.
class UserCreateView(CreateAPIView):
    serializer_class=UserCreationSerializer

class PostListCreateView(ListAPIView,CreateAPIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    serializer_class=PostSerializer

    queryset=Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostRetrieveUpdateDestroyView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    serializer_class=PostSerializer
    queryset=Post.objects.all()

    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message":"deleted"})

class CommentCreateView(CreateAPIView):

    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    serializer_class=CommentSerializer


    def perform_create(self, serializer):
        id=self.kwargs.get("pk")
        post_instance=get_object_or_404(Post,id=id)
        serializer.save(post_object=post_instance,owner=self.request.user)