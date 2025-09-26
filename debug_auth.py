import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def debug_auth():
    # MongoDB connection
    MONGODB_URI = "mongodb+srv://vijeth:2006@wtlab.9b3zqxr.mongodb.net/sentiment_analysis?retryWrites=true&w=majority"
    MONGODB_DB = "sentiment_analysis"
    
    client = AsyncIOMotorClient(MONGODB_URI)
    
    try:
        # Test the connection
        await client.admin.command('ping')
        print("Successfully connected to MongoDB!")
        
        db = client[MONGODB_DB]
        
        # Check the admin user
        user_data = await db.users.find_one({"email": "admin@example.com"})
        if user_data:
            print("Found admin user:")
            print(f"  Email: {user_data.get('email')}")
            print(f"  Username: {user_data.get('username')}")
            print(f"  Full name: {user_data.get('full_name')}")
            print(f"  Role: {user_data.get('role')}")
            print(f"  Hashed password: {user_data.get('hashed_password')}")
            
            # Try to authenticate with the password
            from passlib.context import CryptContext
            pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
            
            password = "secret"
            hashed_password = user_data.get('hashed_password', '')
            
            print(f"\nVerifying password '{password}' against hash...")
            try:
                result = pwd_context.verify(password, hashed_password)
                print(f"Password verification result: {result}")
            except Exception as e:
                print(f"Error verifying password: {e}")
        else:
            print("Admin user not found!")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(debug_auth())