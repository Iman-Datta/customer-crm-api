from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from app_customer.models import Customer
from app_customer.serializers import CustomerSerializer

class RegisterCustomerView(APIView):
    def post (self, request: Request):
        name = request.data.get("name")
        address = request.data.get('address')
        department = request.data.get('department')

        if not all([name,address, department]):
            return Response({'error' : 'All fields are required.'}, status=400)
        else:
            customer_created: Customer = Customer.objects.create(name=name, address=address, department=department)
            customer_created.save()

            response_data = {
                'message' : 'Customer created successfully',
                'customer' : {
                    'name': customer_created.name,
                    'department': customer_created.department
                }
            }

            return Response(response_data, status=201)
        
class DisplayCustomerView(APIView):
    def get (self, request: Request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data, status=200)