from django.http import JsonResponse

SUCCESS = 0
ERROR = 99
VALIDATION_ERROR = 1


class BaseService:
    def json_response(self, body, code=0):
        message = ""
        if code == SUCCESS:
            message = "Transaccion completada con exito"
        if code == ERROR:
            message = "Transaction not was processed"
        if code == VALIDATION_ERROR:
            message = "Los datos enviados son incorrectos"
        return JsonResponse({"code": SUCCESS,
                             "message": message,
                             "response": body})
