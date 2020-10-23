def get_x_request_id(context) -> str:
    for metadata in context.invocation_metadata():
        if metadata.key == "x-request-id": return metadata.value