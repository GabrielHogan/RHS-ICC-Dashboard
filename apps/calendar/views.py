

class EventListView(APIView):

    def get(self, request):
        events = Event.objects.all()

        serializer = EventSerializer(events, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = EventSerializer(request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)