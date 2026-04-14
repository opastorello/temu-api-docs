# Temu Partner API Docs

> Documentação da [Temu Partner API](https://partner.temu.com/documentation) em markdown — atualizada automaticamente todo dia via GitHub Actions.

[![CI](https://github.com/opastorello/temu-api-docs/actions/workflows/update-docs.yml/badge.svg)](https://github.com/opastorello/temu-api-docs/actions/workflows/update-docs.yml) <!-- badge:files -->![285 arquivos](https://img.shields.io/badge/arquivos-285-blue)<!-- /badge --> <!-- badge:date -->![2026-04-14](https://img.shields.io/badge/atualizado-2026--04--14-green)<!-- /badge -->

**Base URL:** `https://openapi-b-global.temu.com/openapi/router` · **Método:** `POST` · **Auth:** `app_key` + `access_token` + `timestamp` + `sign` (MD5)

---

## Estrutura

| Diretório | Arquivos | Descrição |
|---|---|---|
| `developer-guide/` | <!-- count:developer-guide -->22<!-- /count --> | Setup, autenticação, exemplos |
| `api-integration-guide/` | <!-- count:api-integration-guide -->128<!-- /count --> | Guias de integração por domínio |
| `api-reference/authorization/` | <!-- count:authorization -->7<!-- /count --> | OAuth e tokens de acesso |
| `api-reference/product/` | <!-- count:product -->54<!-- /count --> | Catálogo de produtos |
| `api-reference/order/` | <!-- count:order -->13<!-- /count --> | Pedidos |
| `api-reference/shipping/` | <!-- count:shipping -->19<!-- /count --> | Logística e envio |
| `api-reference/returns/` | <!-- count:returns -->12<!-- /count --> | Devoluções e pós-venda |
| `api-reference/promotions/` | <!-- count:promotions -->6<!-- /count --> | Promoções |
| `api-reference/compliance/` | <!-- count:compliance -->7<!-- /count --> | Certificações e compliance |
| `api-reference/ads/` | <!-- count:ads -->8<!-- /count --> | Anúncios (Search & Rec) |
| `api-reference/warehouse/` | <!-- count:warehouse -->5<!-- /count --> | Armazém cooperativo |
| `api-reference/flash/` | <!-- count:flash -->2<!-- /count --> | Flash e reconhecimento de imagem |
| `api-reference/webhook/` | <!-- count:webhook -->1<!-- /count --> | Webhooks |
| `api-reference/other/` | <!-- count:other -->1<!-- /count --> | Outros endpoints |

---

## Developer Guide

| Arquivo | Conteúdo |
|---|---|
| `01-registration-overview.md` | Visão geral do registro |
| `02-developer-registration.md` | Registro de desenvolvedor |
| `03-how-to-choose-registration-platform.md` | Escolha da plataforma |
| `04-create-your-first-app.md` | Criar primeira aplicação |
| `05-self-developed-application-for-sellers.md` | App para sellers |
| `06-complete-partner-profile.md` | Perfil de parceiro |
| `07-seller-authorization-guide.md` | Autorização do seller |
| `08-publish-your-app-to-app-store.md` | Publicar no App Store |
| `09-update-ip-address-or-support-site.md` | Atualizar IP/site |
| `11-endpoints-and-request-method.md` | Endpoints e métodos HTTP |
| `12-common-parameters.md` | Parâmetros comuns |
| `13-signature-method-for-api-request.md` | Assinatura de requisições (MD5) |
| `14-rate-limiting-rules.md` | Rate limiting |
| `15-common-error-codes.md` | Códigos de erro comuns |
| `16-make-your-calls-with-postman.md` | Guia Postman |
| `17-temu-open-api-request-example-python.md` | Exemplo Python |
| `18-compliance-and-security-questionnaires.md` | Compliance e segurança |
| `19-partner-support.md` | Suporte ao parceiro |

---

## API Integration Guide

### Setup

| Arquivo | Conteúdo |
|---|---|
| `01-seller-authorization-guide.md` | Fluxo OAuth do seller |
| `02-endpoints-and-request-method.md` | Endpoints globais |
| `03-common-parameters.md` | Parâmetros comuns |
| `04-signature-method.md` | Como assinar requisições |
| `05-python-example.md` | Exemplo completo Python |
| `06-postman-guide.md` | Configurar Postman |
| `07-rate-limiting-rules.md` | Limites de chamadas |
| `08-common-error-codes.md` | Erros e soluções |

### Produto

| Arquivo | Conteúdo |
|---|---|
| `17-product-basic-introduction.md` | Introdução ao catálogo |
| `18-add-products-guide.md` | Criar produtos (v1) |
| `19-add-products-guide-v2.md` | Criar produtos (v2) |
| `20-parent-child-attribute-guide.md` | Atributos pai-filho |
| `22-product-attributes.md` | Atributos de produto |
| `23-product-listing-instructions.md` | Instruções de listagem |
| `24-product-materials-upload.md` | Upload de imagens/vídeos |
| `25-product-update-guide.md` | Atualizar produtos |
| `26-product-listing-and-delisting-guide.md` | Ativar/desativar listagem |
| `27-inventory-management-guide.md` | Gestão de estoque |
| `28-product-differences-site-currency-volume.md` | Diferenças por site |
| `29-product-vehicles-models.md` | Produtos veículos |
| `30-common-issues-during-product-publishing.md` | Problemas comuns |
| `31-deal-with-second-hand-products.md` | Produtos usados |

### Pedidos, Preços e Fulfillment

| Arquivo | Conteúdo |
|---|---|
| `32-price-management-guide.md` | Gestão de preços |
| `33-guide-of-price.md` | Guia de precificação |
| `34-order-guide.md` | Guia de pedidos |
| `35-order-retrieve-and-management.md` | Consultar e gerenciar pedidos |
| `36-guide-of-order-amount-query.md` | Consultar valores de pedido |
| `37-order-fulfillment-guide.md` | Fulfillment de pedidos |
| `38-split-and-ship-a-package-examples.md` | Split shipment |
| `39-integration-guide-placing-outbound-orders.md` | Outbound orders |
| `40-temu-logistics-tracking-api-documentation.md` | Rastreamento logístico |

### Outros

| Arquivo | Conteúdo |
|---|---|
| `41-return-and-refund-guide.md` | Devoluções e reembolsos |
| `42-promotion-activities-api-overview.md` | API de promoções |
| `43-ads-introduction.md` | Introdução a anúncios |
| `44-the-event-of-webhook.md` | Eventos de webhook |

---

## API Reference

### Authorization

| Endpoint | Descrição |
|---|---|
| `bg.open.accesstoken.create` | Obter Access Token via OAuth |
| `bg.open.accesstoken.info.get` | Consultar / renovar token |
| `temu.local.mall.tags.get` | Obter tags e configurações da loja |

### Product (<!-- count:product -->54<!-- /count --> endpoints)

| Endpoint | Descrição |
|---|---|
| `bg.local.goods.add` | Criar produto |
| `temu.local.goods.v2.add` | Criar produto v2 (recomendado) |
| `bg.local.goods.update` | Atualizar produto |
| `bg.local.goods.partial.update` | Atualização parcial |
| `temu.local.goods.delete` | Deletar produto |
| `bg.local.goods.detail.query` | Detalhes do produto |
| `bg.local.goods.list.query` | Listar produtos |
| `temu.local.goods.list.retrieve` | Listar produtos (v2) |
| `temu.local.sku.list.retrieve` | Listar SKUs |
| `bg.local.goods.sku.list.query` | Consultar SKUs |
| `bg.local.goods.sku.list.price.query` | Preços de SKUs |
| `bg.local.goods.stock.edit` | Editar estoque |
| `temu.local.goods.sku.stock.query` | Consultar estoque |
| `bg.local.goods.sale.status.set` | Ativar/desativar venda |
| `bg.local.goods.publish.status.get` | Status de publicação |
| `temu.local.goods.pre.sale.status.edit` | Status pré-venda |
| `bg.local.goods.cats.get` | Listar categorias |
| `bg.local.goods.template.get` | Template de atributos |
| `bg.local.goods.spec.id.get` | Gerar IDs de variação |
| `bg.local.goods.size.element.get` | Tabela de tamanhos |
| `bg.local.goods.image.upload` | Upload de imagem |
| `bg.local.goods.gallery.signature.get` | Assinatura para upload |
| `bg.local.goods.out.sn.check` | Verificar código externo |
| `bg.local.goods.sku.out.sn.check` | Verificar código SKU |
| `bg.local.goods.out.sn.set` | Definir código externo |
| `bg.local.goods.sku.out.sn.set` | Definir código SKU |
| `bg.local.goods.tax.code.get` | Obter código fiscal |
| `bg.local.goods.category.recommend` | Recomendar categoria |
| `bg.local.goods.category.check` | Verificar categoria |
| `bg.local.goods.priceorder.query` | Consultar order de preço |
| `bg.local.goods.priceorder.change.sku.price` | Alterar preço SKU |
| `temu.local.goods.baseprice.recommend` | Preço base recomendado |
| `temu.local.goods.recommendedprice.query` | Preço recomendado |
| `temu.local.product.attributes.get` | Atributos do produto |
| `temu.local.product.variation.get` | Variações do produto |
| `temu.local.goods.spec.info.get` | Info de especificações |
| `bg.local.goods.property.get` | Propriedades |
| `bg.local.goods.property.relations` | Relações de propriedades |
| `bg.local.goods.property.relations.level.template` | Template por nível |
| `bg.local.goods.property.relations.template` | Template de relações |
| `temu.local.goods.brand.trademark.V2.get` | Marcas registradas |
| `temu.local.goods.sku.net.content.unit.query` | Unidades de conteúdo |
| `temu.local.goods.illegal.vocabulary.check` | Verificar vocabulário |
| `bg.local.goods.compliance.property.check` | Verificar compliance |
| `bg.local.goods.compliance.rules.get` | Regras de compliance |
| `bg.local.goods.compliance.extra.template.get` | Template extra compliance |
| `bg.local.goods.compliance.info.fill.list.query` | Preencher compliance |
| `bg.local.goods.compliance.edit` | Editar compliance |
| `bg.goods.compliancelabel.get` | Labels de compliance |
| `bg.local.compliance.goods.list.query` | Listar produtos compliance |
| `bg.local.goods.videocoverimage.get` | Capa de vídeo |

### Order (<!-- count:order -->13<!-- /count --> endpoints)

| Endpoint | Descrição |
|---|---|
| `bg.order.list.v2.get` | Listar pedidos |
| `bg.order.detail.v2.get` | Detalhes do pedido |
| `bg.order.shippinginfo.v2.get` | Info de envio (criptografado) |
| `bg.order.decryptshippinginfo.get` | Descriptografar endereço |
| `bg.order.unshipped.package.get` | Pacotes aguardando envio |
| `bg.order.combinedshipment.list.get` | Envios combinados |
| `bg.order.customization.get` | Personalizações do pedido |
| `bg.order.amount.query` | Valores do pedido |
| `temu.order.amount.v2.query` | Valores v2 |
| `temu.order.cancel.appeal.apply` | Solicitar cancelamento |
| `temu.order.cancel.appeal.result.get` | Resultado de cancelamento |
| `temu.order.cancel.outofstock.apply` | Cancelar por falta de estoque |
| `temu.order.cancel.outofstock.result.get` | Resultado do cancelamento |

### Shipping (<!-- count:shipping -->19<!-- /count --> endpoints)

| Endpoint | Descrição |
|---|---|
| `bg.freight.template.list.query` | Templates de frete |
| `bg.logistics.companies.get` | Transportadoras disponíveis |
| `bg.logistics.warehouse.list.get` | Armazéns |
| `bg.logistics.shippingservices.get` | Serviços de envio |
| `bg.logistics.shipment.create` | Criar envio |
| `bg.logistics.shipment.v2.get` | Consultar envio |
| `bg.logistics.shipment.v2.confirm` | Confirmar envio |
| `bg.logistics.shipment.sub.confirm` | Confirmar sub-envio |
| `bg.logistics.shipment.update` | Atualizar envio |
| `bg.logistics.shipment.shippingtype.update` | Alterar tipo de envio |
| `bg.logistics.shipment.result.get` | Resultado do envio |
| `bg.logistics.shipment.document.get` | Documento de envio |
| `bg.logistics.shipped.package.confirm` | Confirmar pacote enviado |
| `temu.logistics.shiplogisticstype.get` | Tipos de logística |
| `temu.logistics.label.list.get` | Etiquetas de envio |
| `temu.logistics.shipment.pickup.reservation.create` | Agendar coleta |
| `temu.logistics.shipment.pickup.reservation.cancel` | Cancelar coleta |
| `temu.logistics.shipment.pickup.reservation.result.get` | Resultado da coleta |
| `temu.track.trackinginfo.get` | Rastreamento |

### Returns / After-sales (<!-- count:returns -->12<!-- /count --> endpoints)

| Endpoint | Descrição |
|---|---|
| `bg.aftersales.aftersales.list.get` | Listar pós-venda |
| `bg.aftersales.parentaftersales.list.get` | Listar pós-venda pai |
| `temu.aftersales.parentaftersales.detail.get` | Detalhes pós-venda |
| `bg.aftersales.parentreturnorder.get` | Ordem de devolução |
| `bg.aftersales.cancel.list.get` | Listar cancelamentos |
| `temu.aftersales.refund.issue` | Emitir reembolso |
| `temu.aftersales.carrier.get` | Transportadora pós-venda |
| `temu.aftersales.returnaddress.get` | Endereço de devolução |
| `temu.aftersales.returnlabel.prepare.get` | Preparar etiqueta de devolução |
| `temu.aftersales.upload.returnlabel` | Upload etiqueta devolução |
| `temu.aftersales.signature.get` | Assinatura pós-venda |

### Promotions (<!-- count:promotions -->6<!-- /count --> endpoints)

| Endpoint | Descrição |
|---|---|
| `bg.promotion.activity.query` | Consultar promoções |
| `bg.promotion.activity.candidate.goods.query` | Produtos candidatos |
| `bg.promotion.activity.goods.query` | Produtos em promoção |
| `bg.promotion.activity.goods.enroll` | Inscrever produto |
| `bg.promotion.activity.goods.update` | Atualizar produto em promoção |
| `bg.promotion.activity.goods.operation.query` | Histórico de operações |

### Compliance (<!-- count:compliance -->7<!-- /count --> endpoints)

| Endpoint | Descrição |
|---|---|
| `bg.compliance.metadata.get` | Metadados de compliance |
| `bg.compliance.edit` | Editar compliance |
| `bg.arbok.open.cert.queryNeedUploadItems` | Itens pendentes de certificação |
| `bg.arbok.open.cert.uploadProductCert` | Upload de certificado |
| `bg.arbok.open.upload.uploadFile` | Upload de arquivo |
| `bg.arbok.open.product.cert.query` | Consultar certificados |
| `bg.local.compliance.goods.list.query` | Listar produtos com requisitos de compliance |

### Ads (<!-- count:ads -->8<!-- /count --> endpoints)

| Endpoint | Descrição |
|---|---|
| `temu.searchrec.ad.create` | Criar campanha |
| `temu.searchrec.ad.modify` | Modificar campanha |
| `temu.searchrec.ad.detail.query` | Detalhes da campanha |
| `temu.searchrec.ad.log.query` | Logs de anúncio |
| `temu.searchrec.ad.roas.pred` | Previsão de ROAS |
| `temu.searchrec.ad.reports.mall.query` | Relatório agregado da loja |
| `temu.searchrec.ad.reports.goods.query` | Relatório por produto |
| `temu.searchrec.ad.goods.create.query` | Produtos para anúncio |

### Warehouse (<!-- count:warehouse -->5<!-- /count --> endpoints)

| Endpoint | Descrição |
|---|---|
| `bg.cooperativewarehouse.provider.list` | Listar provedores |
| `bg.cooperativewarehouse.token.authorization` | Autorização de token |
| `bg.cooperativewarehouse.fulfill.submit` | Submeter fulfillment |
| `bg.cooperativewarehouse.fulfill.cancel` | Cancelar fulfillment |
| `bg.cooperativewarehouse.fulfill.query` | Consultar fulfillment |

### Flash (<!-- count:flash -->2<!-- /count --> endpoints)

| Endpoint | Descrição |
|---|---|
| `bg.flash.open.upload.recognize` | Reconhecimento de imagem |
| `bg.flash.open.upload.real.image` | Upload imagem real |

### Webhook (<!-- count:webhook -->1<!-- /count --> endpoint)

| Endpoint | Descrição |
|---|---|
| `bg.tmc.message.update` | Receber notificações de eventos |

Ver `api-integration-guide/the-event-of-webhook.md` para lista completa de eventos e payloads.

### Other (<!-- count:other -->1<!-- /count --> endpoint)

| Endpoint | Descrição |
|---|---|
| `temu.local.order.verification.upload` | Upload de documentos para verificação de pedidos |

---

## Manutenção

```bash
# Atualizar tudo
python update_docs.py

# Ver o que mudaria sem salvar
python update_docs.py --dry-run

# Só endpoints de API
python update_docs.py --section apis

# Só guias
python update_docs.py --section guides
```

O CI roda automaticamente todo dia às **06:00 UTC**. Para rodar manualmente: [Actions → Update Temu Docs → Run workflow](https://github.com/opastorello/temu-api-docs/actions/workflows/update-docs.yml).
