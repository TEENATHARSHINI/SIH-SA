import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from passlib.context import CryptContext

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against a hash."""
    return pwd_context.verify(plain_password, hashed_password)

async def test_authentication():
    # MongoDB connection
    MONGODB_URI = "mongodb+srv://vijeth:2006@wtlab.9b3zqxr.mongodb.net/sentiment_analysis?retryWrites=true&w=majority"
    MONGODB_DB = "sentiment_analysis"
    
    client = AsyncIOMotorClient(MONGODB_URI)
    
    try:
        # Test the connection
        await client.admin.command('ping')
        print("Successfully connected to MongoDB!")
        
        db = client[MONGODB_DB]
        
        # Test admin user authentication
        user = await db.users.find_one({"email": "admin@example.com"})
        if user and verify_password("secret", user["hashed_password"]):
            print("Admin user authentication successful!")
            print(f"User role: {user.get('role', 'N/A')}")
        else:
            print("Admin user authentication failed!")
        
        # Test demo user authentication
        user = await db.users.find_one({"email": "demo@econsult.gov"})
        if user and verify_password("demo123", user["hashed_password"]):
            print("Demo user authentication successful!")
            print(f"User role: {user.get('role', 'N/A')}")
        else:
            print("Demo user authentication failed!")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(test_authentication())