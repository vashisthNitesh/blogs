from rest_framework.response import Response
from blog_app.api.serializers import BlogSerializer
from blog_app.models import BlogModel
from rest_framework import status
from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.mixins import LoginRequiredMixin



class BlogAPIView(LoginRequiredMixin,APIView):
    """
    A APIView to perform CRUD operation on Blog Model
    """

    def get_object(self):
        try:
            blog = BlogModel.objects.get(user = self.request.user)
            if blog.user == self.request.user:
                return blog
            else:
                raise Http404
        except BlogModel.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = BlogSerializer(data)
        else:
            data = BlogModel.objects.filter(user=self.request.user).order_by("-created_at")
            serializer = BlogSerializer(data, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = request.data
        serializer = BlogSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save(user=self.request.user)

        return Response(
            {
                "message": "Blog Created Successfully",
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )

    def put(self, request, pk=None, format=None):
        blog_update = self.get_object(pk)
        serializer = BlogSerializer(
            instance=blog_update, data=request.data, partial=True
        )

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(
            {
                "message": "Blog Updated Successfully",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def delete(self, request, pk, format=None):
        blog_delete = self.get_object(pk)

        blog_delete.delete()

        return Response(
            {"message": "Blog Deleted Successfully"}, status=status.HTTP_200_OK
        )
