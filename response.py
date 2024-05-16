from fastapi.responses import JSONResponse

class AppResponse(JSONResponse):
    def __init__(self, message: str, status_code: int, data=None):
        content = {"message": message}
        if data:
            content.update(data)
        
        super().__init__(content=content, status_code=status_code)