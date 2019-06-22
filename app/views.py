from django.http import Http404, HttpRequest
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Banks, Branches
from .serializers import BankSerializer, BranchSerializer


class BranchList(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BranchSerializer
    paginate_by = 10
    paginate_by_param = 'page_size'
    max_paginate_by = 100

    def get_queryset(self):
        r = self.request.query_params
        return Branches.objects.filter(
            city__iexact = r.get('branch', ''),
            bank = Banks.objects.filter(
                name__iexact = r.get('bank', '')
            ).first()
        ).all()

class Ifsc(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, ifsc=''):
        b = Branches.objects.filter(ifsc__iexact=ifsc).first()
        serializer = BranchSerializer(b)
        return Response(serializer.data)
