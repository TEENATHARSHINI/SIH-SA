try:
    from backend.app.routers import advanced_analysis
    print('Advanced analysis router imported successfully')
    print(f'Router prefix: {advanced_analysis.router.prefix}')
    print(f'Number of routes: {len(advanced_analysis.router.routes)}')
    for route in advanced_analysis.router.routes:
        print(f'  {route.path} - {route.name}')
except Exception as e:
    print(f'Error importing advanced analysis router: {e}')
    import traceback
    traceback.print_exc()