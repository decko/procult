# -*- coding: utf-8 -*-

from import_export import resources, fields
from .models import Proposal


class ProposalResource(resources.ModelResource):
    """
    Resource do modelo de Propostas para
    exportar nos formatos desejados
    """
    numero = fields.Field()
    pasta_proposta = fields.Field()
    artista = fields.Field()
    documento = fields.Field()
    projeto = fields.Field()
    criado_em = fields.Field()
    enviado_em = fields.Field()

    class Meta:
        model = Proposal
        fields = ("numero", "pasta_proposta", "artista", "documento", "projeto",
                  "criado_em", "enviado_em",)
        export_order = ("numero", "pasta_proposta", "artista","projeto",
                        "documento", "criado_em", "enviado_em",)
        exclude = ("id", "number", "ente", "title",
                   "status", "created_at", "sended_at", "updated_at",)

    def get_queryset(self):
        return Proposal.objects.filter(status=Proposal.STATUS_CHOICES.sended)

    def dehydrate_numero(self, proposal):
        return proposal.id

    def dehydrate_pasta_proposta(self, proposal):
        return proposal.number

    def dehydrate_artista(self, proposal):
        return proposal.ente.user.name

    def dehydrate_documento(self, proposal):
        return proposal.ente.cpf or proposal.ente.cnpj

    def dehydrate_projeto(self, proposal):
        return proposal.title

    def dehydrate_criado_em(self, proposal):
        return proposal.created_at.astimezone().strftime("%d/%m/%Y %H:%M:%S")

    def dehydrate_enviado_em(self, proposal):
        return proposal.sended_at.astimezone().strftime("%d/%m/%Y %H:%M:%S")
