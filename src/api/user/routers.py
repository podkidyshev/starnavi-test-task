from rest_framework.routers import Route, DynamicRoute, SimpleRouter


class UserRouter(SimpleRouter):
    """
    A router for user api routes
    """
    routes = [
        Route(
            url=r'^{prefix}$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            detail=False,
            initkwargs={'suffix': 'Detail'}
        ),
        DynamicRoute(
            url=r'^{prefix}/{url_path}$',
            name='{basename}-{url_name}',
            detail=False,
            initkwargs={}
        )
    ]
