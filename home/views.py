from django.shortcuts import render
from django.utils import timezone
from .models import Question, Answer
from django.core.paginator import Paginator


from home.serializers import QuestionSerializer, AnswerSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404 




class question_create(APIView):
    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    



class question_list(APIView):
    def post(self, request):
        questions = Question.objects.all()            
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)
    



class QA_list(APIView):
    oQuestions = []
    oAnswer = []
    aqList = []
    
    def post(self, request):
        questions = Question.objects.all()
        answers = Answer.objects.all()
        for question in questions:
            if question.answer_set.all():
                self.aqList.append(question)
                for answer in answers:
                    if question.answer_set.get() == answer:
                        self.aqList.append(answer)
                qaOserializer = AnswerSerializer(self.aqList, many=True)
        return Response(qaOserializer.data)