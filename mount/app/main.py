from fastapi import FastAPI

from app.exceptions import ExceptionHandlerMiddleware
from .router import api_router_v1

app_description = """
This API enables users to browse, book, and manage concert tickets seamlessly.  
Key features include:  
- **User Authentication & Authorization** (Signup, Login, JWT-based security)  
- **Event Listings** (View concerts, artists, and venues)  
- **Ticket Booking & Payment** (Reserve and purchase tickets)  
- **Order Management** (View booking history, cancel tickets)  
- **Admin Controls** (Manage events, pricing, availability)  

Built with **FastAPI** for high performance and scalability.  

"""

app = FastAPI(
    title="Concert Ticket Booking System API 🎟️🎶", description=app_description
)


app.include_router(api_router_v1)


app.add_middleware(ExceptionHandlerMiddleware)

@app.get("/", tags=["Health"])
async def health_check():
    """
    Checks System health
    """
    return {"health": "ok"}
