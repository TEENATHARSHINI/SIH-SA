import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def check_user():
    # MongoDB connection
    MONGODB_URI = "mongodb+srv://vijeth:2006@wtlab.9b3zqxr.mongodb.net/sentiment_analysis?retryWrites=true&w=majority"
    MONGODB_DB = "sentiment_analysis"
    
    client = AsyncIOMotorClient(MONGODB_URI)
    
    try:
        # Test the connection
        await client.admin.command('ping')
        print("Successfully connected to MongoDB!")
        
        db = client[MONGODB_DB]
        
        # Check if users collection exists
        collections = await db.list_collection_names()
        print(f"Available collections: {collections}")
        
        if "users" not in collections:
            print("Users collection does not exist!")
            return
        
        # Check all users in the database
        cursor = db.users.find({})
        users = await cursor.to_list(length=100)
        
        print(f"\nFound {len(users)} users in the database:")
        for user in users:
            print(f"- Email: {user.get('email')}")
            print(f"  Username: {user.get('username')}")
            print(f"  Role: {user.get('role')}")
            print(f"  Active: {user.get('is_active')}")
            print(f"  Hashed Password: {user.get('hashed_password')[:20]}...")
            print()
        
        # Check specific user
        user = await db.users.find_one({"email": "admin@example.com"})
        if user:
            print(f"Found admin user:")
            print(f"- Email: {user.get('email')}")
            print(f"- Username: {user.get('username')}")
            print(f"- Role: {user.get('role')}")
            print(f"- Active: {user.get('is_active')}")
        else:
            print("Admin user not found!")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(check_user())