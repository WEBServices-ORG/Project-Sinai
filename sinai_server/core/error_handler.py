from fastapi import Request
from fastapi.responses import JSONResponse

async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={
        "error": True,
        "message": "Internal server error",
        "code": "internal_server_error"
    })

def register_error_handlers(app):
    app.add_exception_handler(Exception, global_exception_handler)
