from django.shortcuts import render
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import EventSerializer, ClubAttendeeSerializer
from .models import Event as EventModel
from .models import ClubAttendee as ClubAttendeeModel
import json
from rest_framework.generics import RetrieveAPIView
# Create your views here.


class Events(generics.GenericAPIView):
    serializer_class = EventSerializer()

    def get(self, request):
        event = EventModel.objects.all()
        self.serializer_class = EventSerializer(event, many=True)
        print(self.serializer_class.data)
        # if serializer_class.is_valid():
        return Response(data=self.serializer_class.data, status=status.HTTP_200_OK)

    def post(self, request):
        print(request.query_params['venue'])
        self.serializer_class = EventSerializer(data=request.data)

        if self.serializer_class.is_valid():
            self.serializer_class.save()
            return Response(data=self.serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(data=self.serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     return Response(data=serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
        # serializer_class = json.dumps(EventSerializer())
        # print(serializer_class)
        # print(request)
        # return Response(data={serializer_class}, status=status.HTTP_200_OK)

    # def post(self,request):


class EventDetailView(generics.GenericAPIView):
    serializer_class = EventSerializer()
    event_model = EventModel()

    def get(self, request, pk):
        self.pk = pk
        self.event_model = EventModel.objects.get(pk=self.pk)
        self.serializer_class = EventSerializer(data=self.event_model)
        print(self.serializer_class)
        if self.serializer_class.is_valid():
            return Response(data=self.serializer_class.data, status=status.HTTP_200_OK)
        return Response(data=self.serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        self.request_data = request.data
        serializer_class = EventSerializer(data=self.request_data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(data=serializer_class.data, status=status.HTTP_201_CREATED)


class ClubAttendeeView(generics.GenericAPIView):
    serializer_class = ClubAttendeeSerializer()
    lookup_field = 'pk'

    def get(self, request, pk):
        self.pk = pk
        self.attendee = ClubAttendeeModel.objects.get(pk=self.pk)        
        try:
            self.serializer_class = ClubAttendeeSerializer(self.attendee)
            return Response(data=self.serializer_class.data, status=status.HTTP_200_OK)
        except:
            return Response(data=self.serializer_class.errors,
                            status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer_class = ClubAttendeeSerializer(data=request.data)
        print(serializer_class.is_valid())
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(data=serializer_class.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        self.attendee = ClubAttendeeModel.objects.get(pk=pk)
        self.serializer_class = ClubAttendeeSerializer(
            self.attendee, request.data)

        if self.attendee:
            if self.serializer_class.is_valid():
                self.serializer_class.save()
                return Response(data=self.serializer_class.data, status=status.HTTP_200_OK)
            else:
                return Response(data=self.serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data=self.serializer_class.errors, status=status.HTTP_404_NOT_FOUND)



