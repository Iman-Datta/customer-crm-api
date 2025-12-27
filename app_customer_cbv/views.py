from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from app_customer.models import Customer
from app_customer.serializers import CustomerSerializer
from rest_framework import status

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
    
class UpdateCustomerPatchView(APIView):
    def patch(self, request: Request, pk):
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response({'error':'Customet doesnot exist'}, status=400)
        
        serializer = CustomerSerializer(customer, data = request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

class DeleteCustomerView(APIView):
    def delete(self, request: Request):
        id = request.data.get('id')
        if not id:
            return Response({'error' : 'id not found'}, status=400)
        try:
            customer = Customer.objects.get(pk=id)
            customer.delete()
            return Response({'message' : 'Customer deleted successfully'}, status=200)
        except Customer.DoesNotExist: # Dirived class
            return Response({'error' : 'Customer not found'}, status=404)
        except Exception as e: # Base class
            return Response({'error' : str(e)}, status=500)

class DeleteCustomerViewUrl(APIView):
        def delete (self,pk):
            try:
                customer = Customer.objects.get(pk=pk)
                customer.delete()
                return Response({"message": "Customer deleted successfully"},status=204)
            except Customer.DoesNotExist:
                return Response({"error": "Customer does not exist"},status=404)
            except Exception as e:
                return Response({"error": str(e)},status=500)

class UpdateCustomerPutView(APIView):
    def put(self, request: Request, pk):
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response(
                {'error': 'Customer does not exist'},
                status=status.HTTP_404_NOT_FOUND
            )

        # PUT = full update (partial=False by default)
        serializer = CustomerSerializer(
            customer,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )