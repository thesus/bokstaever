from django.http import JsonResponse, HttpResponse
from django.core import serializers

import json

class AjaxSerializeListMixin:
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        if request.is_ajax():
            objects = response.context_data['object_list']
            data = {}
            data['fields'] = []
            if objects:
                for instance in objects:
                    model = {}
                    for field in self.fields:
                        model[field] = getattr(instance, field)
                    data['fields'].append(model)
                data['pagination'] = self.pagination_infos(
                    response.context_data['page_obj'],
                    response.context_data['paginator']
                )
                return JsonResponse(data, content_type='application/json')
            else:
                return JsonResponse({})
        else:
            return response

    def pagination_infos(self, page_obj, paginator):
        data = {}
        data['previous_page'] = page_obj.previous_page_number() if page_obj.has_previous() else None
        data['next_page'] = page_obj.next_page_number() if page_obj.has_next() else None
        data['current'] = page_obj.number
        data['count'] = paginator.num_pages
        return data

class AjaxSerializeMixin:
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        if request.is_ajax():
            if self.object:
                data = serializers.serialize(
                    'json',
                    [self.object],
                    fields=self.fields
                )
                return HttpResponse(data, content_type='application/json')
            else:
                return JsonResponse({})
        else:
            return response


class AjaxResponseMixin(AjaxSerializeMixin):
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        if self.request.content_type == 'application/json':
            data = json.loads(
                self.request.body.decode('utf-8')
            )
            kwargs['data'] = data

        return kwargs

    def form_invalid(self, form):
        return JsonResponse(form.errors, status=400)

    def form_valid(self, form):
        super().form_valid(form)
        return JsonResponse({
            'pk': self.object.pk if hasattr(self, 'object') else form.pk
        })
