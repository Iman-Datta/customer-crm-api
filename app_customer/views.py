from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

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