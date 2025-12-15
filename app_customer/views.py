from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import CustomerSerializer
from .models import Customer

@api_view(['POST'])
def register_customer(request: Request) -> Response:
    name = request.data.get('name')
    address = request.data.get('address')
    department = request.data.get('department')

    if not all([name, address, department]):
        return Response({'error': 'All fields are required'}, status=400)
    else:
        customer = Customer.objects.create(name=name, address=address, department=department)

        response_data = {
            'message': 'Customer created successfully',
            'customer': {
                'id': customer.id,
                'name': customer.name,
                'department': customer.department
            }
        }
        return Response(response_data, status=201)
    
@api_view(['GET'])
def display_customers(request: Request) -> Response:
    if request.method == 'GET':
        customer: Customer = Customer.objects.all()
        serializer: CustomerSerializer = CustomerSerializer(customer, many=True)
        return Response (serializer.data, status=200)

@api_view(['PATCH'])
def update_patch_customer(request: Request, pk):
    try:
        customer: Customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response({
            'error' : 'Customer doesnot exist'
        }, status=404)
    
    serializer: CustomerSerializer = CustomerSerializer(customer, data = request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    else:
        return Response(serializer.errors, status=400)