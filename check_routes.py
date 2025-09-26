try:
    from backend.app import main
    print('Main app imported successfully')
    routes = [route.path for route in main.app.routes]
    print(f'Number of routes: {len(routes)}')
    print('Routes:')
    for route in routes:
        print(f'  {route}')
except Exception as e:
    print(f'Error importing main app: {e}')
    import traceback
    traceback.print_exc()