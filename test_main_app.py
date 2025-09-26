import asyncio
import sys
import os

# Add the backend directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

try:
    from app.main import app
    print('Main app imported successfully')
    print(f'Number of routes: {len(app.routes)}')
    
    # Check if the advanced analysis routes are included
    advanced_routes = [route for route in app.routes if route.path.startswith('/api/v1/advanced')]
    print(f'Number of advanced analysis routes: {len(advanced_routes)}')
    for route in advanced_routes:
        print(f'  {route.path} - {route.name}')
        
except Exception as e:
    print(f'Error importing main app: {e}')
    import traceback
    traceback.print_exc()