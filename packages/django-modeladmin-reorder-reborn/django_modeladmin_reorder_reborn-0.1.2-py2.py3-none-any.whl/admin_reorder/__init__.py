import math
from itertools import chain

from django.contrib.admin import AdminSite
from django.conf import settings

REST_KEY = "__rest__"


def _build_order_config():
    order_config = {}
    order_counter = 0
    for order_item in settings.ADMIN_REORDER:
        app_name = order_item['app']
        app_order_config = order_config.get(app_name, None)
        if not app_order_config:
            app_order_config = {
                'order': order_counter,
                'config': [],
            }
            order_counter += 1
        app_order_config['config'].append(order_item)
        order_config[app_name] = app_order_config

    return order_config


def _order_app_subsets(app, order_config):
    app_config = order_config.get(app['app_label'], None)
    if not app_config:
        return [app]

    used_models = chain.from_iterable(map(
        lambda subset: subset.get('models', []),
        app_config['config']
    ))
    unused_models = set(map(
        lambda model: model['object_name'],
        app['models']
    )).difference(used_models)

    app_subsets = []
    # has_rest_subset = False
    for subset_config in app_config['config']:
        app_subset = app.copy()
        app_subset['name'] = subset_config.get('label', )
        models = subset_config.get('models', None)
        if models:
            app_subset_models = []
            if isinstance(models, (list, tuple)):
                app_subset_models = []
                for object_name in subset_config['models']:
                    model = next(filter(
                        lambda model: model['object_name'] == object_name,
                        app_subset['models']
                    ), None)
                    if not model:
                        raise Exception(f'Model "{object_name}" not found in "{app_subset["app_label"]}" app.')
                    app_subset_models.append(model)
            elif models == REST_KEY:
                app_subset_models = filter(
                    lambda model: model['object_name'] in unused_models,
                    app_subset['models']
                )
                # has_rest_subset = True
            app_subset['models'] = list(app_subset_models)

        app_subsets.append(app_subset)

    # if unused_models and not has_rest_subset:
    #     rest_subset = app.copy()
    #     rest_subset['models'] = list(filter(
    #         lambda model: model['object_name'] in unused_models,
    #         rest_subset['models']
    #     ))
    #     app_subsets.append(rest_subset)

    return app_subsets


def _get_app_order(app, order_config):
    app_name = app['app_label']
    app_config = order_config.get(app_name, None)
    return app_config['order'] if app_config else math.inf


def _build_new_order(app_list):
    order_config = _build_order_config()
    ordered_apps_list = sorted(
        app_list,
        key=lambda app: _get_app_order(app, order_config),
    )
    app_subsets_list = list(map(
        lambda app: _order_app_subsets(app, order_config),
        ordered_apps_list,
    ))

    return chain.from_iterable(app_subsets_list)


class ReorderingAdminSite(AdminSite):
    def get_app_list(self, request):
        app_list = list(self._build_app_dict(request).values())
        return _build_new_order(app_list)
