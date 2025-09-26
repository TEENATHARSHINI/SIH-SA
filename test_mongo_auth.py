import asyncio
import sys
import os

# Add the backend directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from backend.app.core.mongo_auth import authenticate_user

async def test_auth():
    print("Testing MongoDB authentication...")
    
    # Test admin user
    user = await authenticate_user("admin@example.com", "secret")
    if user:
        print(f"Admin authentication successful!")
        print(f"User ID: {user.id}")
        print(f"Email: {user.email}")
        print(f"Username: {user.username}")
        print(f"Role: {user.role}")
    else:
        print("Admin authentication failed!")
    
    # Test demo user
    user = await authenticate_user("demo@econsult.gov", "demo123")
    if user:
        print(f"Demo authentication successful!")
        print(f"User ID: {user.id}")
        print(f"Email: {user.email}")
        print(f"Username: {user.username}")
        print(f"Role: {user.role}")
    else:
        print("Demo authentication failed!")

if __name__ == "__main__":
    asyncio.run(test_auth())