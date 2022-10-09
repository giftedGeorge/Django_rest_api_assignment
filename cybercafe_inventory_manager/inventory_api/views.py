from requests import delete
from rest_framework.views import APIView
from inventory_api.models import Computer, Mouse
from inventory_api.serializer import ComputerSerializer, MouseSerializer
from rest_framework.response import Response
from rest_framework import status


#for the computer entity
class List_Computer(APIView):
    def get(self, request):
        computers = Computer.objects.all()
        serializer = ComputerSerializer(computers, many=True)
        return Response(serializer.data)

class Create_Computer(APIView):
    def post(self, request):
        serializer = ComputerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Edit_Computer(APIView):
    def get_computer_by_pk(self, pk):
        try:
            return Computer.objects.get(pk=pk)
        except:
            return Response({'Error!': 'Computer with such id does not exist'}, status=status.HTTP_404_NOT_FOUND )

    def get(self, request, pk):
        computer = self.get_computer_by_pk(pk)
        serializer = ComputerSerializer(computer)
        return Response(serializer.data)

    def put(self, request, pk):
        computer = self.get_computer_by_pk(pk)
        serializer = ComputerSerializer(computer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        computer = self.get_computer_by_pk(pk)
        computer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#for the mouse entity
class List_Mouse(APIView):
    def get(self, request):
        mouse = Mouse.objects.all()
        serializer = MouseSerializer(mouse, many=True)
        return Response(serializer.data)

class Create_Mouse(APIView):
    def post(self, request):
        serializer = MouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Edit_Mouse(APIView):
    def get_mouse_by_pk(self, pk):
        try:
            return Mouse.objects.get(pk=pk)
        except:
            return Response({'Error!': 'Mouse with such id does not exist'}, status=status.HTTP_404_NOT_FOUND )

    def get(self, request, pk):
        mouse = self.get_mouse_by_pk(pk)
        serializer = MouseSerializer(mouse)
        return Response(serializer.data)

    def put(self, request, pk):
        mouse = self.get_mouse_by_pk(pk)
        serializer = MouseSerializer(mouse, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        mouse = self.get_mouse_by_pk(pk)
        mouse.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)