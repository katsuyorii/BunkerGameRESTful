def get_random_serializer_data(model, serializer):
    ''' Method to get random serialized value from database '''
    random_item = model.objects.order_by('?').first()
    serializer_data = serializer(random_item).data

    return serializer_data


def get_random_serializer_seq_data(model, serializer):
    ''' Method to get random serialized 3 values from database '''
    random_item = model.objects.order_by('?')[:3]
    serializer_data = serializer(random_item, many=True).data

    return serializer_data