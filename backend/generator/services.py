def get_random_serializer_data(model, serializer):
    ''' Method to get random serialized value from database '''
    random_item = model.objects.order_by('?').first()
    serializer_data = serializer(random_item).data

    return serializer_data