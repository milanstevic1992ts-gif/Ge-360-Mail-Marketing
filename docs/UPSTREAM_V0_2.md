# Upstream verification - v0.2

Data verifica: 2026-09-19

## Versioni verificate

- Prospex repository: `asiifdev/business-leads-ai-automation`
  - commit verificato: `5b3e260d3291a201c61240387cbcfd84979476c1`
- Twenty repository: `twentyhq/twenty`
  - commit verificato: `91e4caa66ca135da9ce8ddcc2042b468a1c10b6b`

## Twenty - verificato

Fonte: documentazione ufficiale nel repository Twenty.

- Core REST API: `/rest/`
- GraphQL API: `/graphql/`
- People endpoint documentato: `/rest/people`
- Self-hosted base URL: `https://{your-domain}/`
- autenticazione API key: `Authorization: Bearer YOUR_API_KEY`
- API generate dallo schema del workspace
- batch fino a 60 record per richiesta
- limite documentato: 100 richieste/minuto

### Decisione GE360

Il primo adapter Twenty userà REST e partirà in modalità read-only prima del push:
1. health/config check;
2. GET people;
3. normalizzazione verso il modello GE360;
4. solo dopo test reali, creazione/update People.

Non assumere campi custom: vanno letti/verificati sul workspace effettivo.

## Prospex - verificato

Fonte: README e backend corrente del repository Prospex.

Endpoint documentati:
- `GET /api/health`
- `GET /api/leads`
- `GET/POST /api/campaigns`
- `POST /api/scraper/campaigns/:id/start`
- `PATCH /api/leads/:id/crm`
- endpoint export e analytics

### Autenticazione: attenzione

Nel codice corrente:
- `apps/api/src/auth/api-key.guard.ts` accetta header che iniziano con `Authorization: ApiKey ...`;
- il controller `apps/api/src/leads/leads.controller.ts` usa invece `JwtGuard`;
- la guida utente contiene anche un riferimento a API key come Bearer token.

Quindi l'autenticazione macchina-a-macchina per `/api/leads` non viene considerata ancora risolta.

### Decisione GE360

Non implementare un adapter Prospex autenticato finché non viene verificato uno dei seguenti:
1. API key realmente accettata dal controller leads della versione installata;
2. endpoint di service auth dedicato;
3. JWT ottenibile in modo stabile per integrazione server-to-server.

Nessun workaround basato su credenziali hardcoded nel repository.

## Ordine di implementazione v0.2

1. Twenty read-only adapter
2. mapping Twenty Person -> GE360 Contact
3. sync idempotente + external identity
4. verifica auth Prospex sull'istanza che installeremo
5. Prospex pull leads
6. Prospex -> GE360 -> Twenty
