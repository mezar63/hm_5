import time
from pathlib import Path


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)

        execution_time = time.time() - start_time
        with open(
            f"{Path(__file__).resolve().parent.parent.parent}/log.txt",
            "a",
            encoding="utf-8",
        ) as txt_file:
            txt_file.write(
                f"path: {request.path}, method: {request.method}, execution_time: {execution_time}\n"
            )

        return response
