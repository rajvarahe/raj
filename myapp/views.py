from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.db.models import Q
from .models import *
# Create your views here.

class QuestionTwo(APIView):
    valid_samples=55
    def post(self,request):
        try:
            self.valid_samples=request.data.get('sample')

            return Response(
                
               {'value':self.valid_samples,
                   'msg':'updated'} )
        except:
            return Response({
                'error': 'update failed'
            })
        
        
        
    def get(self,request):
        return Response({
            'valid_samples':self.valid_samples
        }
        )
        

@api_view(['GET'])
def question_one(request,state_abb,election_cycle,election_round,ac_no):
    filter=SurveyDescDimensionCapi.objects.filter(
        state_abb=state_abb,
        election_cycle=election_cycle,
        election_round=election_round,
        cons_no=ac_no
    ).values_list('sd_dm_pk',flat=True)
    
    capi_id=CapiFact.objects.filter(
        sd_dm_fk__in=filter
    ).values_list('capi_pk', flat=True)
    
    total_samples=len(capi_id)
    
    filter2=V1RejectionSectionCapi.objects.filter(
        capi_fk__in=capi_id,
        v1_rejection=True
    ).values_list('capi_fk',flat=True)
    valid_capi=len(filter2)
    
    filter3=AuditSectionCapi.objects.filter(
        Q(capi_fk__in=filter2)
        &
        ~Q(remark='')
    )
    
    filter4 = V1RejectionSectionCapi.objects.filter(
        capi_fk__in=capi_id,
        v1_rejection=False
    ).values_list('capi_fk',flat=True)
    
    filter5= AuditSectionCapi.objects.filter(
        capi_fk__in=filter2,
        remark='rejected'
    ).values_list('capi_fk',flat=True)
    
    audited_sample=len(filter3)
    v1_rejected_samples=len(filter4)
    v2_rejected_samples=len(filter5)
    
    
    return Response(
        {
            'total sample':total_samples,
            'audited_samples':audited_sample,
            'valid_samples':valid_capi,
            'v1_rejection':v1_rejected_samples,
            'v2_rejection':v2_rejected_samples,
        }
    )