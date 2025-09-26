import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from passlib.context import CryptContext
from datetime import datetime

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    """Generate a password hash."""
    return pwd_context.hash(password)

async def fix_user():
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
        
        # Fix the admin user
        user = await db.users.find_one({"email": "admin@example.com"})
        if user:
            print(f"Found admin user with ID: {user.get('_id')}")
            
            # Update the user with correct structure
            update_data = {
                "$set": {
                    "username": "admin",
                    "full_name": "Administrator",
                    "role": "admin",
                    "is_verified": True,
                    "updated_at": datetime.utcnow()
                }
            }
            
            result = await db.users.update_one(
                {"_id": user["_id"]},
                update_data
            )
            
            print(f"Updated {result.modified_count} user document")
            
            # Verify the update
            updated_user = await db.users.find_one({"_id": user["_id"]})
            print(f"Updated user:")
            print(f"- Email: {updated_user.get('email')}")
            print(f"- Username: {updated_user.get('username')}")
            print(f"- Full Name: {updated_user.get('full_name')}")
            print(f"- Role: {updated_user.get('role')}")
            print(f"- Active: {updated_user.get('is_active')}")
            print(f"- Verified: {updated_user.get('is_verified')}")
        else:
            print("Admin user not found!")
            
        # Create or fix the demo user
        demo_user = await db.users.find_one({"email": "demo@econsult.gov"})
        if not demo_user:
            print("Creating demo user...")
            
            demo_doc = {
                "email": "demo@econsult.gov",
                "username": "demo",
                "full_name": "Demo User",
                "hashed_password": get_password_hash("demo123"),
                "role": "staff",
                "is_active": True,
                "is_verified": True,
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            }
            
            result = await db.users.insert_one(demo_doc)
            print(f"Created demo user with ID: {result.inserted_id}")
        else:
            print("Demo user already exists")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(fix_user())