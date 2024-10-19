from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, response
from rest_framework.decorators import api_view
from tutorial.quickstart.serializers import GroupSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
class StarWarsViewSet(viewsets.ViewSet):
    def list(self, request):
        return response.Response({"message": "Luke i am your father 1"})

    def create(self, request):
        data = request.data
        return response.Response({"message": "You posted data!", "data": data})

    def put(self, request):
        data = request.data
        return response.Response({"message": "You put data!", "data": data})


# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
@api_view(["GET", "POST"])
def star_wars(request):
    if request.method == "GET":
        data = {"message": "Luke i am your father"}
        return response.Response(data)
    if request.method == "POST":
        body = request.body
        data = {"message": body}
        return response.Response(data)


@api_view(["PUT"])
def star_wars_put(request):
    body = request.body
    data = {"message": body}
    return response.Response(data)
