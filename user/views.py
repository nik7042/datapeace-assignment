from django.shortcuts import get_object_or_404
from django.db import connection
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer


class UserDetailView(APIView):
    """
    Handles retrieving, updating, and deleting a single user by ID.
    Allowed methods: GET, PUT, DELETE.
    """
    http_method_names = ['get', 'put', 'delete']

    def get_user(self, id):
        return get_object_or_404(User, id=id)

    def get(self, request, id):
        """Retrieve a user by ID."""
        user = self.get_user(id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        """Update user data by ID."""
        user = self.get_user(id)
        serializer = UserSerializer(instance=user, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Record updated successfully",
                "status_code": status.HTTP_200_OK
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        """Delete a user by ID."""
        user = self.get_user(id)
        user.delete()
        return Response({
            "message": "Record deleted successfully",
            "status_code": status.HTTP_200_OK
        }, status=status.HTTP_200_OK)


class UserListCreateView(APIView):
    """
    Handles listing users with filters, pagination, sorting and creating new users.
    Allowed methods: GET, POST.
    """
    http_method_names = ['get', 'post']

    def get(self, request):
        """
        Retrieve a paginated and optionally filtered list of users.
        Supports pagination, search by name, and sorting.
        """
        try:
            page = int(request.GET.get('page', 1))
            limit = int(request.GET.get('limit', 5))
            name = request.GET.get('name', '').strip()
            sort_field = request.GET.get('sort', '').strip()

            # Determine sort order
            order = "DESC" if sort_field.startswith('-') else "ASC"
            sort_column = sort_field.lstrip('-') or 'id'

            offset = (page - 1) * limit
            search_clause = f"AND (first_name ILIKE '%%{name}%%' OR last_name ILIKE '%%{name}%%')" if name else ""
            order_clause = f"ORDER BY {sort_column} {order}"

            query = f"""
                WITH ordered_users AS (
                    SELECT *, ROW_NUMBER() OVER ({order_clause}) AS row_num
                    FROM user_user
                    WHERE 1=1 {search_clause}
                )
                SELECT id, first_name, last_name, company_name, city, state, zip, email, age
                FROM ordered_users
                WHERE row_num BETWEEN {offset + 1} AND {offset + limit}
                {order_clause};
            """

            with connection.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                if not rows:
                    return JsonResponse([], safe=False, status=status.HTTP_200_OK)

                columns = [col[0] for col in cursor.description]
                result = [dict(zip(columns, row)) for row in rows]

            return JsonResponse(result, safe=False, status=status.HTTP_200_OK)

        except ValueError:
            return Response({"error": "Invalid pagination parameters"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        """
        Create a new user if it doesn't already exist.
        """
        serializer = UserSerializer(data=request.data)

        if User.objects.filter(**request.data).exists():
            return Response({"error": "This user data already exists"}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Record created successfully",
                "status_code": status.HTTP_201_CREATED
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
