import sys
import os

# Add the backend directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

try:
    # Import the main app
    from app.main import app
    
    print('Main app imported successfully')
    print(f'Total number of routes: {len(app.routes)}')
    
    # Check if the advanced analysis routes are included
    advanced_routes = [route for route in app.routes if '/api/v1/advanced' in route.path]
    print(f'Number of advanced analysis routes: {len(advanced_routes)}')
    
    # Print all routes
    print('\nAll routes:')
    for route in app.routes:
        print(f'  {route.path} - {route.name}')
        
    # Print advanced analysis routes specifically
    print('\nAdvanced analysis routes:')
    for route in advanced_routes:
        print(f'  {route.path} - {route.name}')
        
except Exception as e:
    print(f'Error importing main app: {e}')
    import traceback
    traceback.print_exc()