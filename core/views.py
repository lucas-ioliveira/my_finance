from django.shortcuts import render
from django.views.generic import TemplateView


class DashViews(TemplateView):
    template_name = 'dash.html'

    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     # Coletando contexto existente
    #     context = super(IndexViews, self).get_context_data(**kwargs)
    #     # Adicionando contexto
    #     context['servicos'] = Servico.objects.all()
    #     context['funcionarios'] = Funcionario.objects.all()
    #     context['recursos'] = Recurso.objects.all()
    #     return context