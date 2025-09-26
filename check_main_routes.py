import sys
import os

# Add the backend directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

try:
    from app.main import app
    print('Main app imported successfully')
    print(f'Number of routes: {len(app.routes)}')
    print('Routes:')
    for route in app.routes:
        print(f'  {route.path} - {route.name}')
except Exception as e:
    print(f'Error importing main app: {e}')
    import traceback
    traceback.print_exc()