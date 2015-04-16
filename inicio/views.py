from django.views.generic import TemplateView


class ViewInicio(TemplateView):
	template_name = "inicio/inicio.html"

	def get_context_data(self, **kwargs):
		context = super(ViewInicio, self).get_context_data(**kwargs)
		context['pagina_inicio'] = True
		return context


class ViewEstres(TemplateView):
	template_name = "inicio/estres.html"


class ViewAtencion(TemplateView):
	template_name = "inicio/atencion_internalizada.html"


class ViewDeportes(TemplateView):
	template_name = "inicio/deportes.html"
