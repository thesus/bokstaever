from django.http import JsonResponse, HttpResponse
from django.core import serializers

import json

class AjaxSerializeListMixin:
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        if request.is_ajax():
            print(response.context_data)
            objects = response.context_data['object_list']
            if objects:
                data = serializers.serialize(
                    'json',
                    list(objects),
                    fields=self.fields
                )
                print(dir(objects))
                print(data)
                print(dir(response.context_data['page_obj']))
                return HttpResponse(data, content_type='application/json')
            else:
                return JsonResponse({})
        else:
            return response

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
