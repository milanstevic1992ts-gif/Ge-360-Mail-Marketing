# GE360 Mail Marketing

Core/orchestratore self-hosted per lead, CRM, campagne, inbox e opportunità commerciali.

## Obiettivo

GE360 resta il punto centrale. Prospex, Twenty, Mautic e OpenCRM sono motori esterni integrati tramite adapter/API: non comunicano direttamente tra loro e non diventano la fonte unica dei dati.

## Avvio sviluppo

Requisiti: Docker + Docker Compose plugin.

```bash
cp .env.example .env
docker compose up -d --build
```

Oppure:

```bash
make dev
```

Controlli:

```bash
docker compose ps
bash scripts/doctor.sh
```

Core API: `http://127.0.0.1:8789`  
Swagger: `http://127.0.0.1:8789/docs`

## API v0.1

- `GET /api/health` - salute core/database e configurazione motori
- `GET /api/engines` - registry dei motori e capability
- `POST /api/contacts` - crea contatto GE360
- `GET /api/contacts` - lista/filtra contatti
- `GET /api/contacts/{ge360_id}` - dettaglio contatto
- `GET /api/contacts/dedupe/candidates` - possibili duplicati, senza merge automatico

## Sicurezza configurazione

Non committare mai il file `.env`. Le chiavi API restano solo nell'ambiente locale/server.

## Roadmap

### v0.1 - Core
- [x] Repository madre
- [x] FastAPI orchestrator
- [x] Modello dati GE360 comune
- [x] Adapter standardizzati
- [x] Docker Compose di sviluppo
- [x] Health check / doctor
- [x] Configurazione .env
- [x] Deduplica candidati
- [x] Audit base
- [x] Test automatici
- [x] CI verde

### v0.2 - Twenty + Prospex
- [ ] Twenty come CRM operativo
- [ ] Prospex per discovery/enrichment
- [ ] Deduplica e mapping external IDs
- [ ] Sync contatti bidirezionale controllata

### v0.3 - Mautic
- [ ] Segmenti
- [ ] Campagne
- [ ] Eventi email e webhook
- [ ] Suppression list e audit

### v0.4 - OpenCRM + Jarvis
- [ ] AI commerciale
- [ ] Inbox/opportunità
- [ ] Comandi Jarvis
- [ ] Workflow assistiti con approvazione umana

### v0.5 - Debian package
- [ ] installer .deb
- [ ] systemd
- [ ] backup/restore/update/doctor
- [ ] GitHub Actions release

## Principio architetturale

```
Prospex ─┐
Twenty  ─┼──> GE360 Core <──> PostgreSQL
Mautic  ─┤
OpenCRM ─┘
```

Ogni record possiede un `ge360_id` stabile e può avere uno o più `external_ids`.

Consulta anche `docs/ARCHITECTURE.md` e `docs/ROADMAP.md`.
