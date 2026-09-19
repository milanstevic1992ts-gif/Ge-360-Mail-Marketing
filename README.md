# GE360 Mail Marketing

Core/orchestratore self-hosted per lead, CRM, campagne, inbox e opportunità commerciali.

## Obiettivo

GE360 resta il punto centrale. Prospex, Twenty, Mautic e OpenCRM sono motori esterni integrati tramite adapter/API: non comunicano direttamente tra loro e non diventano la fonte unica dei dati.

## Roadmap

### v0.1 - Core
- [x] Repository madre
- [ ] FastAPI orchestrator
- [ ] Modello dati GE360 comune
- [ ] Adapter standardizzati
- [ ] Docker Compose di sviluppo
- [ ] Health check / doctor
- [ ] Configurazione .env

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

## Stato

Bootstrap v0.1 in corso.
