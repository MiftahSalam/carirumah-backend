
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,

)
from rest_framework import status

from .models import Rumah, Agent
from .serializers import RumahSerializer, DeveloperSerializer, AgentSerializer, BriefRumahSerializer

# Create your views here.
@api_view(['GET'])
def property_search(request):
    q_text = request.GET.get('query_text')
    qs_addr = Rumah.objects.filter(address__contains=q_text)
    qs_prop_name = Rumah.objects.filter(property_name__contains=q_text)
    qs_all = qs_addr | qs_prop_name

    # print("property_search qs result by address",qs_addr)
    # print("property_search qs result by property_name",qs_prop_name)
    # print("property_search qs result all",qs_all)
    print("property_search qs result all",qs_all.count())

    serializer = BriefRumahSerializer(qs_all, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def property_list(request):
    qs = Rumah.objects.all()
    paginator = Paginator(qs,5)
    page = request.GET.get('page')
    print("property list -> request page ",page)

    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        print("property list -> PageNotAnInteger")
        qs = paginator.page(1)
    except EmptyPage:
        print("property list -> EmptyPage")
        if request.is_ajax():
            print("property list -> EmptyPage ajax")
            return Response({},status=status.HTTP_204_NO_CONTENT)
            
    serializer = BriefRumahSerializer(qs,many=True, context={'request':request})
    return Response(serializer.data)

@api_view(['GET'])
def property_detail(request,id):
    rumah = Rumah.objects.get(id=id)
    serializer = RumahSerializer(rumah)
    return Response(serializer.data)

@api_view(['POST','GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def property_create(request):
    if 'developer' in request.data.keys():
        developer_serializer = DeveloperSerializer(data=request.data['developer'])
        if developer_serializer.is_valid():
            print("developer_serializer valid")
            developer_serializer.save()

        request.data['developer'] = developer_serializer.data['name']
        print(request.data['developer'])

    print('init rumahserializer...')
    rumah_serializer = RumahSerializer(data=request.data)
    print('validating rumahserializer...')
    if rumah_serializer.is_valid(raise_exception=True):
        rumah_serializer.save()
        return Response(rumah_serializer.data, status=status.HTTP_201_CREATED)
    return Response({}, status=status.HTTP_400_BAD_REQUEST)
