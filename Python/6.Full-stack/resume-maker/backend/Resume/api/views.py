from rest_framework.response import Response
from . models import ClinetData
from . serilaizers import ClientDataSerializer
from rest_framework.views import APIView
from rest_framework import status
class Resume(APIView):
    def post(self,request,formate=None):
        serializer=ClientDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'True','candidates':serializer.data},status=status.HTTP_201_CREATED)
        return Response({'status':'False','Error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    def get(self,request,formate=None):
        data=ClinetData.objects.all()
        serilaizer=ClientDataSerializer(data,many=True)
        return Response({'status':'True','candidates':serilaizer.data},status=status.HTTP_200_OK)
