"""TD Studio direct mode: boc CORS quanh app goc de trinh duyet goi thang cau, khong qua Worker.
Chay bang: uvicorn cors_app:app — lifespan duoc chuyen nguyen cho app goc nen startup/shutdown giu nguyen."""
from app import app as _app


class _CorsMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope.get("type") == "http" and scope.get("method") == "OPTIONS":
            headers = [
                (b"access-control-allow-origin", b"*"),
                (b"access-control-allow-methods", b"*"),
                (b"access-control-allow-headers", b"*"),
                (b"access-control-max-age", b"86400"),
            ]
            await send({"type": "http.response.start", "status": 204, "headers": headers})
            await send({"type": "http.response.body", "body": b""})
            return

        async def _send(message):
            if message["type"] == "http.response.start":
                message["headers"] = list(message.get("headers", [])) + [
                    (b"access-control-allow-origin", b"*")
                ]
            await send(message)

        await self.app(scope, receive, _send)


app = _CorsMiddleware(_app)
