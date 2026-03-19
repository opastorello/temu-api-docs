# Skill: Temu Partner API

## Visão Geral

A Temu Partner API permite que sellers e desenvolvedores integrem suas plataformas com o marketplace Temu para gerenciar produtos, pedidos, logística, pós-venda, promoções e anúncios de forma programática.

**Base URL:** `https://openapi-b-global.temu.com/openapi/router`
**Método:** Todas as chamadas são `POST` com corpo JSON.

---

## Autenticação

### Parâmetros obrigatórios em toda requisição

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `app_key` | String | Chave da aplicação (obtida no Seller Center) |
| `access_token` | String | Token de acesso OAuth do seller |
| `timestamp` | Long | Unix timestamp em milissegundos |
| `sign` | String | Assinatura MD5 da requisição |

### Fluxo de autorização

1. Seller acessa a URL de autorização e concede permissão
2. Sistema recebe `code` via callback
3. Chamar `bg.open.accesstoken.create` com o `code` para obter `access_token` e `refresh_token`
4. Usar `access_token` em todas as chamadas subsequentes
5. Renovar token com `bg.open.accesstoken.info.get` antes de expirar

### Geração de assinatura

```python
import hashlib, time, json

def sign(params: dict, app_secret: str) -> str:
    # Ordena e concatena todos os parâmetros (exceto sign)
    sorted_params = sorted(params.items())
    param_str = ''.join(f"{k}{v}" for k, v in sorted_params)
    full_str = app_secret + param_str + app_secret
    return hashlib.md5(full_str.encode('utf-8')).hexdigest().upper()
```

---

## Domínios e Capacidades

### 1. Autorização (`api-reference/authorization/`)
- Obter e renovar access tokens
- Consultar tags e permissões da loja

**Endpoints-chave:**
- `bg.open.accesstoken.create` — obter token pelo code OAuth
- `bg.open.accesstoken.info.get` — consultar/renovar token existente
- `temu.local.mall.tags.get` — obter tags e configurações da loja

---

### 2. Gestão de Produtos (`api-reference/product/`)
Criação, atualização, listagem e gerenciamento completo do catálogo.

**Fluxo para criar produto:**
1. `bg.local.goods.cats.get` — obter categoria
2. `bg.local.goods.template.get` — obter template de atributos da categoria
3. `bg.local.goods.spec.id.get` — gerar IDs de variações (se customizadas)
4. `bg.local.goods.image.upload` — fazer upload das imagens
5. `temu.local.goods.illegal.vocabulary.check` — validar nome/descrição
6. `bg.local.goods.compliance.property.check` — validar atributos de compliance
7. `bg.local.goods.add` ou `temu.local.goods.v2.add` — criar produto

**Endpoints-chave:**
- `bg.local.goods.add` — criar produto (estrutura padrão)
- `temu.local.goods.v2.add` — criar produto (estrutura v2, recomendado)
- `bg.local.goods.update` — atualizar produto completo
- `bg.local.goods.partial.update` — atualizar campos específicos
- `bg.local.goods.list.query` — listar produtos com filtros
- `bg.local.goods.stock.edit` — atualizar estoque
- `bg.local.goods.sale.status.set` — ativar/desativar produto

**Categorias especiais:**
- Apparel (`catType=0`): imagem SKU 3:4, ≥1340×1785px
- Non-Apparel (`catType=1`): imagem SKU 1:1, ≥800×800px
- Livros: ISBN obrigatório (`barCodeType=3`)
- DVD/CD: Studio/Manufacturer obrigatório

---

### 3. Pedidos (`api-reference/order/`)

**Endpoints-chave:**
- `bg.order.list.v2.get` — listar pedidos (filtros: status, data, etc.)
- `bg.order.detail.v2.get` — detalhes completos de um pedido
- `bg.order.shippinginfo.v2.get` — endereço de entrega (criptografado)
- `bg.order.decryptshippinginfo.get` — endereço descriptografado
- `bg.order.unshipped.package.get` — pacotes aguardando envio
- `bg.order.amount.query` / `temu.order.amount.v2.query` — valores financeiros

**Cancelamentos:**
- `temu.order.cancel.appeal.apply` — solicitar cancelamento
- `temu.order.cancel.outofstock.apply` — cancelar por falta de estoque

---

### 4. Logística e Envio (`api-reference/shipping/`)

**Fluxo de fulfillment:**
1. `bg.order.unshipped.package.get` — buscar pedidos para despachar
2. `bg.logistics.companies.get` — listar transportadoras disponíveis
3. `bg.logistics.shipment.create` — criar envio com código de rastreio
4. `bg.logistics.shipment.v2.confirm` — confirmar o envio
5. `temu.track.trackinginfo.get` — consultar rastreamento

**Coleta agendada:**
- `temu.logistics.shipment.pickup.reservation.create` — agendar coleta
- `temu.logistics.shipment.pickup.reservation.cancel` — cancelar coleta

---

### 5. Devoluções e Pós-venda (`api-reference/returns/`)

**Endpoints-chave:**
- `bg.aftersales.aftersales.list.get` — listar ocorrências pós-venda
- `temu.aftersales.parentaftersales.detail.get` — detalhes da ocorrência
- `temu.aftersales.refund.issue` — emitir reembolso
- `temu.aftersales.returnlabel.prepare.get` — preparar etiqueta de devolução
- `temu.aftersales.upload.returnlabel` — upload da etiqueta

---

### 6. Promoções (`api-reference/promotions/`)

**Endpoints-chave:**
- `bg.promotion.activity.query` — listar promoções disponíveis
- `bg.promotion.activity.candidate.goods.query` — produtos elegíveis
- `bg.promotion.activity.goods.enroll` — inscrever produto em promoção
- `bg.promotion.activity.goods.update` — atualizar participação

---

### 7. Anúncios / Ads (`api-reference/ads/`)

Baseado em Search & Recommendation (temu.searchrec).

**Endpoints-chave:**
- `temu.searchrec.ad.create` — criar campanha
- `temu.searchrec.ad.modify` — modificar campanha
- `temu.searchrec.ad.reports.mall.query` — relatório agregado da loja
- `temu.searchrec.ad.reports.goods.query` — relatório por produto
- `temu.searchrec.ad.roas.pred` — previsão de ROAS

---

### 8. Compliance (`api-reference/compliance/`)

Para produtos que exigem certificações ou documentos regulatórios.

**Endpoints-chave:**
- `bg.compliance.metadata.get` — metadados de requisitos
- `bg.arbok.open.cert.queryNeedUploadItems` — listar itens pendentes
- `bg.arbok.open.cert.uploadProductCert` — enviar certificado
- `bg.arbok.open.upload.uploadFile` — upload genérico de arquivo
- `bg.local.compliance.goods.list.query` — listar produtos com requisitos de compliance

---

### 9. Outros (`api-reference/other/`)

Endpoints miscelâneos que não se encaixam nas categorias principais.

**Endpoints-chave:**
- `temu.local.order.verification.upload` — upload de documentos para verificação de pedidos

---

### 11. Warehouse Cooperativo (`api-reference/warehouse/`)

Para sellers que usam armazéns cooperativos Temu.

- `bg.cooperativewarehouse.provider.list` — listar provedores
- `bg.cooperativewarehouse.fulfill.submit` — submeter ordem de fulfillment
- `bg.cooperativewarehouse.fulfill.query` — consultar status

---

### 12. Webhooks (`api-reference/webhook/`)

- `bg.tmc.message.update` — endpoint para receber notificações de eventos

**Eventos disponíveis:** criação de pedido, mudança de status, pós-venda, estoque crítico, etc.
Ver `api-integration-guide/the-event-of-webhook.md` para lista completa de eventos e payloads.

---

## Erros Comuns

| Código | Significado | Solução |
|---|---|---|
| `110020001` | Access token inválido | Renovar token com `bg.open.accesstoken.info.get` |
| `110020002` | Access token expirado | Renovar token antes da expiração |
| `100000020` | Forbidden for Visitor | Verificar autenticação/cookies |
| `40001` | Parâmetro obrigatório ausente | Verificar payload completo |
| `40002` | Assinatura inválida | Verificar geração do sign (MD5, não SHA256) |
| `40003` | Timestamp inválido ou expirado | Usar Unix timestamp em milissegundos |
| `40004` | App key inválida | Verificar app_key no Seller Center |
| `50001` | Rate limit atingido | Exponential backoff; ver `developer-guide/14-rate-limiting-rules.md` |
| `60001` | Produto não encontrado | Verificar goods_id |
| `60002` | SKU não encontrado | Verificar sku_id |
| `70001` | Pedido não encontrado | Verificar order_sn |
| `80001` | Operação não permitida neste estado | Verificar status atual do recurso |

---

## Rate Limiting

- Limite padrão: varia por endpoint (ver `developer-guide/14-rate-limiting-rules.md`)
- Quando atingido: resposta com código `50001`
- Estratégia recomendada: exponential backoff com retry

---

## Sites Suportados

A API suporta múltiplos sites Temu. Alguns campos e regras variam por site (ver `api-integration-guide/28-product-differences-site-currency-volume.md`). O site é determinado pelo `access_token` do seller.

---

## Documentação Completa

```
temu-api-docs/
├── developer-guide/       → Setup, autenticação, assinatura, exemplos
├── api-integration-guide/ → Guias por domínio com fluxos completos
└── api-reference/         → Spec completo de cada endpoint (params, erros, exemplos)
```

Manter atualizado: `python update_docs.py`
